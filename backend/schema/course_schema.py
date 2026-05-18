from pydantic import BaseModel
from datetime import datetime


class SubjectOut(BaseModel):
    """学科大类"""
    id: int
    key: str
    name: str
    desc: str | None = None

    model_config = {"from_attributes": True}


class CourseBase(BaseModel):
    """课程基础字段"""
    subject: str
    category: str
    name: str
    desc: str | None = None
    teacher: str | None = None
    rating: float = 0.0
    price: int = 0
    hot: bool = False
    duration: str | None = None
    lessons: int = 0


class CourseOut(CourseBase):
    """课程响应"""
    id: int
    students: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class EnrollmentOut(BaseModel):
    """报名记录响应"""
    id: int
    user_id: int
    course_id: int
    enrolled_at: datetime

    model_config = {"from_attributes": True}