from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SubmitAnswerRequest(BaseModel):
    """提交单题答案请求"""
    question_id: int = Field(..., description="题目ID")
    user_answer: list = Field(..., description="用户答案索引数组")
    paper_id: Optional[int] = Field(None, description="试卷ID（章节练习则为空）")


class SubmitAnswerResponse(BaseModel):
    """提交单题答案响应"""
    is_correct: bool
    correct_answer: list
    analysis: Optional[str] = None


class QuestionOut(BaseModel):
    """题目出参"""
    id: int
    subject: str
    point_id: str
    type: str
    difficulty: int
    stem: str
    options: Optional[list] = None
    answer: Optional[list] = None  # 仅在已提交/回顾时返回
    analysis: Optional[str] = None  # 仅在已提交/回顾时返回
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class QuestionListItem(QuestionOut):
    """题目列表项（不含答案和解析）"""
    answer: None = None
    analysis: None = None


class QuizPaperOut(BaseModel):
    """试卷出参"""
    id: int
    name: str
    type: str
    subject: Optional[str] = None
    duration: int
    total_questions: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class QuizStatsOut(BaseModel):
    """答题统计"""
    total: int
    correct: int
    wrong: int
    accuracy: float


class MistakeItemOut(BaseModel):
    """错题项"""
    id: int
    question_id: int
    stem: str
    subject: str
    point_id: str
    type: str
    options: Optional[list] = None
    answer: list
    analysis: Optional[str] = None
    wrong_count: int
    correct_count: int
    last_wrong_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MistakeStatsOut(BaseModel):
    """错题统计"""
    total_mistakes: int
    total_questions: int
    mistake_rate: float
    point_distribution: list
    subject_distribution: list
    type_distribution: list