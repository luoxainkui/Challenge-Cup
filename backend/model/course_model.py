from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from model import TimestampMixin, Base


class Course(TimestampMixin, Base):
    """课程主表"""
    __tablename__ = "courses"

    id       = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    subject  = Column(String(50), nullable=False, comment="学科：大学英语/高等数学/管理学等")
    category = Column(String(20), nullable=False, comment="分类：公共课/专业课")
    name     = Column(String(200), nullable=False, comment="课程名称")
    desc     = Column(Text, comment="课程描述")
    teacher  = Column(String(100), comment="授课教师")
    students = Column(Integer, server_default="0", comment="报名学生数")
    rating   = Column(Float, server_default="0", comment="评分")
    price    = Column(Integer, server_default="0", comment="价格（元）")
    hot      = Column(Boolean, server_default="0", comment="是否热门")

    duration  = Column(String(20), comment="课程周期")
    lessons   = Column(Integer, server_default="0", comment="课时数")
    is_active = Column(Boolean, server_default="1", comment="是否上架")

    enrollments = relationship("Enrollment", back_populates="course")


class Subject(Base):
    """学科大类"""
    __tablename__ = "subjects"

    id        = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    key       = Column(String(30), unique=True, nullable=False, comment="唯一标识")
    name      = Column(String(50), nullable=False, comment="学科名称")
    desc      = Column(Text, comment="一句话描述")
    is_active = Column(Boolean, server_default="1", comment="是否启用")


class Enrollment(Base):
    """课程报名记录"""
    __tablename__ = "enrollments"

    id          = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False, comment="用户ID")
    course_id   = Column(Integer, ForeignKey("courses.id"), nullable=False, comment="课程ID")
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now(), comment="报名时间")

    user   = relationship("User", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")