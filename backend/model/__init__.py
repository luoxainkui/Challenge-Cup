from core.database import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimestampMixin:
    """时间戳混入 — 自动管理 created_at / updated_at"""
    created_at = Column(DateTime(timezone=True), server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")


from model.user_model import User
from model.course_model import Course, Subject, Enrollment
from model.quiz_model import Question, QuizPaper, QuizRecord, MistakeBook

__all__ = [
    "Base",
    "TimestampMixin",
    "User",
    "Course",
    "Subject",
    "Enrollment",
    "Question",
    "QuizPaper",
    "QuizRecord",
    "MistakeBook",
]