"""
答题 API — 题目/试卷/答题/错题本
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
from schema.common import ApiResponse
from schema.quiz_schema import SubmitAnswerRequest
from service.quiz_service import QuizService

router = APIRouter(prefix="/quiz", tags=["答题·Quiz"])


# ── 选题页面 ────────────────────────────────────

@router.get("/subjects")
def list_subjects(db: Session = Depends(get_db)):
    """获取刷题学科列表（含题目数量）"""
    return ApiResponse.ok(data=QuizService.get_subjects(db))


@router.get("/questions")
def list_questions(
    subject: str | None = Query(None, description="按学科筛选"),
    type: str | None = Query(None, description="按题型筛选"),
    point_id: str | None = Query(None, description="按考点筛选"),
    difficulty: int | None = Query(None, description="按难度筛选 1-3"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    db: Session = Depends(get_db),
):
    """获取题目列表（分页，不含答案和解析）"""
    data = QuizService.list_questions(db, subject=subject, type=type, point_id=point_id,
                                      difficulty=difficulty, page=page, page_size=page_size)
    return ApiResponse.ok(data=data)


@router.get("/questions/{question_id}")
def get_question_detail(
    question_id: int,
    db: Session = Depends(get_db),
):
    """获取题目详情（含答案和解析，用于回顾）"""
    return ApiResponse.ok(data=QuizService.get_question_detail(db, question_id))


# ── 试卷 ────────────────────────────────────────

@router.get("/papers")
def list_papers(
    type: str | None = Query(None, description="mock|real"),
    db: Session = Depends(get_db),
):
    """获取试卷列表"""
    return ApiResponse.ok(data=QuizService.get_papers(db, paper_type=type))


# ── 答题 ────────────────────────────────────────

@router.post("/answer")
def submit_answer(
    submit_data: SubmitAnswerRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """提交单题答案并获取判题结果（需登录）"""
    result = QuizService.submit_answer(
        db,
        user_id=current_user.id,
        question_id=submit_data.question_id,
        user_answer=submit_data.user_answer,
        paper_id=submit_data.paper_id,
    )
    return ApiResponse.ok(data=result)


@router.get("/stats")
def get_quiz_stats(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """获取用户答题统计（需登录）"""
    return ApiResponse.ok(data=QuizService.get_quiz_stats(db, current_user.id))


# ── 错题本 ───────────────────────────────────────

@router.get("/mistakes")
def list_mistakes(
    subject: str | None = Query(None, description="按学科筛选"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """获取用户错题列表（需登录）"""
    data = QuizService.list_mistakes(db, current_user.id, subject=subject, page=page, page_size=page_size)
    return ApiResponse.ok(data=data)


@router.get("/mistakes/stats")
def get_mistake_stats(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """获取错题本统计（需登录）"""
    return ApiResponse.ok(data=QuizService.get_mistake_stats(db, current_user.id))


@router.delete("/mistakes/{question_id}")
def remove_mistake(
    question_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """手动移除某道错题（需登录）"""
    QuizService.remove_mistake(db, current_user.id, question_id)
    return ApiResponse.ok(message="已移除")


@router.delete("/mistakes")
def clear_all_mistakes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """清空所有错题（需登录）"""
    QuizService.clear_all_mistakes(db, current_user.id)
    return ApiResponse.ok(message="错题本已清空")
