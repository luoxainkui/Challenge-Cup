from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from model import TimestampMixin, Base


class Question(TimestampMixin, Base):
    """题库主表"""
    __tablename__ = "questions"

    id         = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    subject    = Column(String(50), nullable=False, comment="所属学科：大学英语/高等数学等")
    point_id   = Column(String(50), nullable=False, comment="考点标识：vocab/reading/function等")
    type       = Column(String(20), nullable=False, comment="题型：single/multi/truefalse/fill")
    difficulty = Column(Integer, server_default="1", comment="难度 1-3")
    stem       = Column(Text, nullable=False, comment="题干")
    options    = Column(JSON, comment="选项列表（单选/多选时有值）")
    answer     = Column(JSON, nullable=False, comment="正确答案索引数组")
    analysis   = Column(Text, comment="解析")
    is_active  = Column(Boolean, server_default="1", comment="是否启用")


class QuizPaper(TimestampMixin, Base):
    """试卷表"""
    __tablename__ = "quiz_papers"

    id              = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    name            = Column(String(100), nullable=False, comment="试卷名称")
    type            = Column(String(20), nullable=False, comment="类型：chapter/mock/real")
    subject         = Column(String(50), comment="所属学科")
    duration        = Column(Integer, server_default="120", comment="考试时长（分钟）")
    total_questions  = Column(Integer, server_default="0", comment="总题数")
    is_active       = Column(Boolean, server_default="1", comment="是否启用")


class QuizRecord(Base):
    """答题记录表"""
    __tablename__ = "quiz_records"

    id          = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False, comment="用户ID")
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False, comment="题目ID")
    paper_id    = Column(Integer, ForeignKey("quiz_papers.id"), nullable=True, comment="试卷ID（无试卷则为章节练习）")
    user_answer = Column(JSON, comment="用户答案索引数组")
    is_correct  = Column(Boolean, comment="是否正确")
    created_at  = Column(DateTime(timezone=True), server_default=func.now(), comment="答题时间")

    question = relationship("Question")
    user     = relationship("User", back_populates="quiz_records")


class MistakeBook(Base):
    """错题本表"""
    __tablename__ = "mistake_books"

    id            = Column(Integer, primary_key=True, autoincrement=True, comment="主键ID")
    user_id       = Column(Integer, ForeignKey("users.id"), nullable=False, comment="用户ID")
    question_id   = Column(Integer, ForeignKey("questions.id"), nullable=False, comment="题目ID")
    wrong_count   = Column(Integer, server_default="1", comment="错误次数")
    correct_count = Column(Integer, server_default="0", comment="正确次数")
    last_wrong_at = Column(DateTime(timezone=True), comment="最后错误时间")
    created_at    = Column(DateTime(timezone=True), server_default=func.now(), comment="收录时间")
    updated_at    = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="更新时间")

    question = relationship("Question")
    user     = relationship("User", back_populates="mistake_books")