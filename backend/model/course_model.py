from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime, timezone


class Course(Base):
    """课程模型"""
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    subject = Column(String(50), nullable=False, comment="学科：大学英语/高等数学/管理学等")
    category = Column(String(20), nullable=False, comment="分类：公共课/专业课")
    name = Column(String(200), nullable=False, comment="课程名称")
    desc = Column(Text, nullable=True, comment="课程描述")
    teacher = Column(String(100), nullable=True, comment="授课教师")
    students = Column(Integer, default=0, comment="报名学生数")
    rating = Column(Float, default=0.0, comment="评分")
    price = Column(Integer, default=0, comment="价格（元）")
    hot = Column(Boolean, default=False, comment="是否热门")
    duration = Column(String(20), nullable=True, comment="课程周期")
    lessons = Column(Integer, default=0, comment="课时数")
    is_active = Column(Boolean, default=True, comment="是否上架")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    enrollments = relationship("Enrollment", back_populates="course")


class Subject(Base):
    """学科大类"""
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(String(30), unique=True, nullable=False, comment="唯一标识")
    name = Column(String(50), nullable=False, comment="学科名称")
    desc = Column(Text, nullable=True, comment="一句话描述")
    is_active = Column(Boolean, default=True)


class Enrollment(Base):
    """课程报名记录"""
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, comment="用户ID")
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, comment="课程ID")
    enrolled_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")