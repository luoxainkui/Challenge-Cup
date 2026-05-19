import json
import os

from sqlalchemy.orm import Session
from sqlalchemy import and_
from model.quiz_model import Question, QuizPaper, QuizRecord, MistakeBook


# ── 题库 ────────────────────────────────────────

def get_questions(
    db: Session,
    subject: str | None = None,
    type: str | None = None,
    point_id: str | None = None,
    difficulty: int | None = None,
    page: int = 1,
    page_size: int = 20,
):
    """获取题目列表（分页），支持按学科/题型/考点/难度筛选"""
    q = db.query(Question).filter(Question.is_active == True)
    if subject:
        q = q.filter(Question.subject == subject)
    if type:
        q = q.filter(Question.type == type)
    if point_id:
        q = q.filter(Question.point_id == point_id)
    if difficulty:
        q = q.filter(Question.difficulty == difficulty)

    total = q.count()
    offset = (page - 1) * page_size
    items = q.order_by(Question.id).offset(offset).limit(page_size).all()
    return items, total


def get_question_by_id(db: Session, question_id: int):
    """获取单道题目"""
    return db.query(Question).filter(Question.id == question_id, Question.is_active == True).first()


def get_question_ids_by_point(db: Session, point_id: str):
    """获取某考点下所有题目ID"""
    return [q.id for q in db.query(Question.id).filter(
        Question.point_id == point_id,
        Question.is_active == True,
    ).all()]


# ── 试卷 ────────────────────────────────────────

def get_papers(db: Session, paper_type: str | None = None):
    """获取试卷列表"""
    q = db.query(QuizPaper).filter(QuizPaper.is_active == True)
    if paper_type:
        q = q.filter(QuizPaper.type == paper_type)
    return q.order_by(QuizPaper.id).all()


def get_paper_by_id(db: Session, paper_id: int):
    """获取单份试卷"""
    return db.query(QuizPaper).filter(QuizPaper.id == paper_id, QuizPaper.is_active == True).first()


# ── 答题记录 ────────────────────────────────────

def record_answer(db: Session, user_id: int, question_id: int, user_answer: list | None, is_correct: bool, paper_id: int | None = None):
    """记录一次答题"""
    record = QuizRecord(
        user_id=user_id,
        question_id=question_id,
        paper_id=paper_id,
        user_answer=user_answer,
        is_correct=is_correct,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_user_records(
    db: Session,
    user_id: int,
    paper_id: int | None = None,
    page: int = 1,
    page_size: int = 20,
):
    """获取用户答题记录"""
    q = db.query(QuizRecord).filter(QuizRecord.user_id == user_id)
    if paper_id is not None:
        q = q.filter(QuizRecord.paper_id == paper_id)

    total = q.count()
    offset = (page - 1) * page_size
    items = q.order_by(QuizRecord.created_at.desc()).offset(offset).limit(page_size).all()
    return items, total


def get_quiz_stats(db: Session, user_id: int):
    """获取用户答题统计"""
    total = db.query(QuizRecord).filter(QuizRecord.user_id == user_id).count()
    correct = db.query(QuizRecord).filter(QuizRecord.user_id == user_id, QuizRecord.is_correct == True).count()
    return {
        "total": total,
        "correct": correct,
        "wrong": total - correct,
        "accuracy": round(correct / total * 100, 1) if total > 0 else 0,
    }


# ── 错题本 ──────────────────────────────────────

def get_mistake_by_user_and_question(db: Session, user_id: int, question_id: int):
    """查询用户某题的错题记录"""
    return db.query(MistakeBook).filter(
        MistakeBook.user_id == user_id,
        MistakeBook.question_id == question_id,
    ).first()


def record_wrong(db: Session, user_id: int, question_id: int):
    """记录答错（新增或增加错误计数）"""
    mistake = get_mistake_by_user_and_question(db, user_id, question_id)
    if mistake:
        mistake.wrong_count = (mistake.wrong_count or 0) + 1
        from datetime import datetime, timezone
        mistake.last_wrong_at = datetime.now(timezone.utc)
    else:
        from datetime import datetime, timezone
        mistake = MistakeBook(
            user_id=user_id,
            question_id=question_id,
            wrong_count=1,
            correct_count=0,
            last_wrong_at=datetime.now(timezone.utc),
        )
        db.add(mistake)
    db.commit()
    db.refresh(mistake)
    return mistake


def record_correct(db: Session, user_id: int, question_id: int, auto_remove_threshold: int = 3):
    """记录答对（增加正确计数，达到阈值则自动移除）"""
    mistake = get_mistake_by_user_and_question(db, user_id, question_id)
    if not mistake:
        return None
    mistake.correct_count = (mistake.correct_count or 0) + 1
    if mistake.correct_count >= auto_remove_threshold:
        db.delete(mistake)
        db.commit()
        return None
    db.commit()
    db.refresh(mistake)
    return mistake


def get_mistake_list(db: Session, user_id: int, subject: str | None = None, page: int = 1, page_size: int = 20):
    """获取用户错题列表（分页），支持按学科筛选"""
    q = db.query(MistakeBook).filter(MistakeBook.user_id == user_id)
    if subject:
        q = q.join(Question, MistakeBook.question_id == Question.id).filter(Question.subject == subject)

    total = q.count()
    offset = (page - 1) * page_size
    items = q.order_by(MistakeBook.last_wrong_at.desc()).offset(offset).limit(page_size).all()
    return items, total


def remove_mistake(db: Session, user_id: int, question_id: int):
    """手动移除错题"""
    mistake = get_mistake_by_user_and_question(db, user_id, question_id)
    if mistake:
        db.delete(mistake)
        db.commit()
        return True
    return False


def clear_all_mistakes(db: Session, user_id: int):
    """清空所有错题"""
    db.query(MistakeBook).filter(MistakeBook.user_id == user_id).delete()
    db.commit()


def get_mistake_stats(db: Session, user_id: int):
    """错题本统计信息"""
    mistakes = db.query(MistakeBook).filter(MistakeBook.user_id == user_id).all()
    total_questions = db.query(Question).filter(Question.is_active == True).count()

    # 按考点分布
    point_map = {}
    # 按科目分布
    subject_map = {}
    # 按题型分布
    type_map = {}

    for m in mistakes:
        q = m.question
        if not q:
            continue
        point_map[q.point_id] = point_map.get(q.point_id, 0) + 1
        subject_map[q.subject] = subject_map.get(q.subject, 0) + 1
        type_map[q.type] = type_map.get(q.type, 0) + 1

    return {
        "total_mistakes": len(mistakes),
        "total_questions": total_questions,
        "mistake_rate": round(len(mistakes) / total_questions * 100, 1) if total_questions > 0 else 0,
        "point_distribution": [{"point_id": k, "count": v} for k, v in sorted(point_map.items(), key=lambda x: -x[1])],
        "subject_distribution": [{"subject": k, "count": v} for k, v in sorted(subject_map.items(), key=lambda x: -x[1])],
        "type_distribution": [{"type": k, "count": v} for k, v in sorted(type_map.items(), key=lambda x: -x[1])],
    }


# ── 种子数据（从 JSON 文件加载）──────────────────

def _load_seed_data():
    """加载种子 JSON 文件"""
    seed_path = os.path.join(os.path.dirname(__file__), "..", "seed_data", "quiz_data.json")
    seed_path = os.path.normpath(seed_path)
    with open(seed_path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_questions(db: Session):
    """从 JSON 文件初始化种子题目（幂等）"""
    existing = db.query(Question).first()
    if existing:
        return

    data = _load_seed_data()
    for q in data.get("questions", []):
        db.add(Question(**q))
    db.commit()


def seed_papers(db: Session):
    """从 JSON 文件初始化种子试卷（幂等）"""
    existing = db.query(QuizPaper).first()
    if existing:
        return

    data = _load_seed_data()
    for p in data.get("papers", []):
        db.add(QuizPaper(**p))
    db.commit()
