from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from model import TimestampMixin, Base


class User(TimestampMixin, Base):
    """用户表"""
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    username        = Column(String(50), unique=True, nullable=False, comment="用户名")
    email           = Column(String(100), unique=True, nullable=False, comment="邮箱")
    phone           = Column(String(20), unique=True, nullable=True, comment="手机号")
    hashed_password = Column(String(255), nullable=False, comment="哈希密码")
    is_active       = Column(Boolean, default=True, server_default="1", nullable=False, comment="是否激活")

    enrollments   = relationship("Enrollment", back_populates="user")
    quiz_records  = relationship("QuizRecord", back_populates="user")
    mistake_books = relationship("MistakeBook", back_populates="user")