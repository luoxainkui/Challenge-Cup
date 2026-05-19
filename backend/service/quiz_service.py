"""
答题服务层 — 题目/试卷/答题/错题本业务逻辑
"""
from sqlalchemy.orm import Session
from utils.exceptions import BusinessException, ERR_NOT_FOUND, ERR_CONFLICT
from utils.logging import get_logger
import crud.quiz_crud as crud

logger = get_logger(__name__)

QUESTION_TYPES = {"single": "单选题", "multi": "多选题", "truefalse": "判断题", "fill": "填空题"}
QUIZ_SUBJECTS = [
    {"name": "大学英语", "icon": "EN", "color": "#2a6eff"},
    {"name": "高等数学", "icon": "数", "color": "#ff6b35"},
    {"name": "大学语文", "icon": "语", "color": "#9c27b0"},
    {"name": "政治", "icon": "政", "color": "#e74c3c"},
    {"name": "管理学", "icon": "管", "color": "#4caf50"},
    {"name": "会计学", "icon": "会", "color": "#008888"},
    {"name": "计算机", "icon": "计", "color": "#ff9800"},
    {"name": "经济学", "icon": "经", "color": "#607d8b"},
]

EXAM_POINTS = {
    "vocab": {"name": "词汇与语法", "subject": "大学英语"},
    "reading": {"name": "阅读理解", "subject": "大学英语"},
    "writing": {"name": "写作与翻译", "subject": "大学英语"},
    "function": {"name": "函数与极限", "subject": "高等数学"},
    "derivative": {"name": "导数与微分", "subject": "高等数学"},
    "integral": {"name": "积分及应用", "subject": "高等数学"},
    "classical": {"name": "文言文阅读", "subject": "大学语文"},
    "poetry": {"name": "诗词鉴赏", "subject": "大学语文"},
    "philosophy": {"name": "马克思主义哲学", "subject": "政治"},
    "socialism": {"name": "中国特色社会主义", "subject": "政治"},
    "management": {"name": "管理概述与决策", "subject": "管理学"},
    "organization": {"name": "组织设计与文化", "subject": "管理学"},
    "accounting": {"name": "会计基础与凭证", "subject": "会计学"},
    "finance": {"name": "财务报表编制", "subject": "会计学"},
    "office": {"name": "Office办公应用", "subject": "计算机"},
    "network": {"name": "网络与安全基础", "subject": "计算机"},
    "demand": {"name": "需求与供给理论", "subject": "经济学"},
    "macro": {"name": "宏观经济学基础", "subject": "经济学"},
}


def _question_to_dict(q) -> dict:
    """题目模型 → 字典"""
    return {
        "id": q.id,
        "subject": q.subject,
        "point_id": q.point_id,
        "type": q.type,
        "difficulty": q.difficulty,
        "stem": q.stem,
        "options": q.options,
        "answer": q.answer,
        "analysis": q.analysis,
        "created_at": q.created_at.isoformat() if q.created_at else None,
    }


def _question_to_list_item(q) -> dict:
    """题目模型 → 列表项字典（不含答案和解析）"""
    return {
        "id": q.id,
        "subject": q.subject,
        "point_id": q.point_id,
        "type": q.type,
        "difficulty": q.difficulty,
        "stem": q.stem,
        "options": q.options,
        "created_at": q.created_at.isoformat() if q.created_at else None,
    }


class QuizService:
    """答题业务逻辑"""

    @staticmethod
    def list_questions(
        db: Session,
        subject: str | None = None,
        type: str | None = None,
        point_id: str | None = None,
        difficulty: int | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> dict:
        """获取题目列表（分页，不含答案和解析）"""
        items, total = crud.get_questions(
            db, subject=subject, type=type, point_id=point_id,
            difficulty=difficulty, page=page, page_size=page_size,
        )
        total_pages = max(1, (total + page_size - 1) // page_size)
        return {
            "list": [_question_to_list_item(q) for q in items],
            "page_info": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": total_pages,
            },
        }

    @staticmethod
    def get_question_detail(db: Session, question_id: int) -> dict:
        """获取题目详情（包含答案和解析）"""
        q = crud.get_question_by_id(db, question_id)
        if not q:
            raise BusinessException(code=ERR_NOT_FOUND, message="题目不存在")
        return _question_to_dict(q)

    @staticmethod
    def get_subjects(db: Session) -> list:
        """获取刷题学科列表（含题目数量）"""
        # 统计每个学科的题目数
        items, _ = crud.get_questions(db, page=1, page_size=10000)
        subject_counts = {}
        for q in items:
            subject_counts[q.subject] = subject_counts.get(q.subject, 0) + 1

        return [
            {
                "name": s["name"],
                "icon": s["icon"],
                "color": s["color"],
                "count": subject_counts.get(s["name"], 0),
            }
            for s in QUIZ_SUBJECTS
        ]

    @staticmethod
    def get_papers(db: Session, paper_type: str | None = None) -> list:
        """获取试卷列表"""
        papers = crud.get_papers(db, paper_type=paper_type)
        return [
            {
                "id": p.id,
                "name": p.name,
                "type": p.type,
                "subject": p.subject,
                "duration": p.duration,
                "total_questions": p.total_questions,
                "created_at": p.created_at.isoformat() if p.created_at else None,
            }
            for p in papers
        ]

    @staticmethod
    def submit_answer(db: Session, user_id: int, question_id: int, user_answer: list, paper_id: int | None = None) -> dict:
        """提交单题答案并获取判题结果"""
        q = crud.get_question_by_id(db, question_id)
        if not q:
            raise BusinessException(code=ERR_NOT_FOUND, message="题目不存在")

        # 判题
        correct_answer = q.answer or []
        user_sorted = sorted(user_answer) if user_answer else []
        ans_sorted = sorted(correct_answer)
        is_correct = user_sorted == ans_sorted

        # 记录答题
        crud.record_answer(db, user_id=user_id, question_id=question_id,
                           user_answer=user_answer, is_correct=is_correct, paper_id=paper_id)

        # 同步错题本
        if is_correct:
            crud.record_correct(db, user_id, question_id)
        else:
            crud.record_wrong(db, user_id, question_id)

        logger.info("用户 %s 答题 #%d，正确: %s", user_id, question_id, is_correct)

        return {
            "is_correct": is_correct,
            "correct_answer": correct_answer,
            "analysis": q.analysis,
        }

    @staticmethod
    def get_quiz_stats(db: Session, user_id: int) -> dict:
        """获取用户答题统计"""
        return crud.get_quiz_stats(db, user_id)

    # ── 错题本 ──

    @staticmethod
    def list_mistakes(db: Session, user_id: int, subject: str | None = None, page: int = 1, page_size: int = 20) -> dict:
        """获取用户错题列表（分页）"""
        items, total = crud.get_mistake_list(db, user_id, subject=subject, page=page, page_size=page_size)
        total_pages = max(1, (total + page_size - 1) // page_size)

        mistake_items = []
        for m in items:
            q = m.question
            if not q:
                continue
            mistake_items.append({
                "id": m.id,
                "question_id": q.id,
                "stem": q.stem,
                "subject": q.subject,
                "point_id": q.point_id,
                "type": q.type,
                "options": q.options,
                "answer": q.answer,
                "analysis": q.analysis,
                "wrong_count": m.wrong_count,
                "correct_count": m.correct_count,
                "last_wrong_at": m.last_wrong_at.isoformat() if m.last_wrong_at else None,
            })

        return {
            "list": mistake_items,
            "page_info": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": total_pages,
            },
        }

    @staticmethod
    def get_mistake_stats(db: Session, user_id: int) -> dict:
        """获取错题本统计"""
        stats = crud.get_mistake_stats(db, user_id)

        # 丰富考点/科目/题型信息
        enriched_points = []
        for item in stats["point_distribution"]:
            point_info = EXAM_POINTS.get(item["point_id"], {})
            enriched_points.append({
                "point_id": item["point_id"],
                "point_name": point_info.get("name", item["point_id"]),
                "subject": point_info.get("subject", ""),
                "count": item["count"],
            })

        enriched_subjects = []
        for item in stats["subject_distribution"]:
            subject_info = next((s for s in QUIZ_SUBJECTS if s["name"] == item["subject"]), None)
            enriched_subjects.append({
                "subject": item["subject"],
                "count": item["count"],
                "color": subject_info["color"] if subject_info else "#2a6eff",
            })

        enriched_types = []
        for item in stats["type_distribution"]:
            enriched_types.append({
                "type": item["type"],
                "label": QUESTION_TYPES.get(item["type"], item["type"]),
                "count": item["count"],
            })

        return {
            "total_mistakes": stats["total_mistakes"],
            "total_questions": stats["total_questions"],
            "mistake_rate": stats["mistake_rate"],
            "point_distribution": enriched_points,
            "subject_distribution": enriched_subjects,
            "type_distribution": enriched_types,
        }

    @staticmethod
    def remove_mistake(db: Session, user_id: int, question_id: int) -> bool:
        """手动移除错题"""
        if not crud.remove_mistake(db, user_id, question_id):
            raise BusinessException(code=ERR_NOT_FOUND, message="错题记录不存在")
        return True

    @staticmethod
    def clear_all_mistakes(db: Session, user_id: int) -> bool:
        """清空所有错题"""
        crud.clear_all_mistakes(db, user_id)
        return True