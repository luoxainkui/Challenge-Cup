"""课程/科目 CRUD"""
import json
import os

from sqlalchemy.orm import Session
from model.course_model import Course, Subject, Enrollment


def _load_seed_data():
    """加载课程种子 JSON 文件"""
    seed_path = os.path.join(os.path.dirname(__file__), "..", "seed_data", "course_data.json")
    seed_path = os.path.normpath(seed_path)
    with open(seed_path, "r", encoding="utf-8") as f:
        return json.load(f)


# ── 学科 ──

def get_subjects(db: Session):
    """获取所有启用的学科大类"""
    return db.query(Subject).filter(Subject.is_active == True).all()


def seed_subjects(db: Session):
    """从 JSON 文件初始化种子学科数据（幂等）"""
    data = _load_seed_data()
    for item in data.get("subjects", []):
        if not db.query(Subject).filter(Subject.key == item["key"]).first():
            db.add(Subject(**item))
    db.commit()


# ── 课程 ──

def seed_courses(db: Session):
    """从 JSON 文件初始化种子课程数据（幂等），匹配前端 constants/courses.js"""
    existing = db.query(Course).first()
    if existing:
        return

    data = _load_seed_data()
    for c in data.get("courses", []):
        db.add(Course(**c))
    db.commit()


def get_courses(db: Session, category: str | None = None, subject: str | None = None, hot: bool | None = None):
    """获取课程列表，支持按分类、学科、热门筛选"""
    q = db.query(Course).filter(Course.is_active == True)
    if category:
        q = q.filter(Course.category == category)
    if subject:
        q = q.filter(Course.subject == subject)
    if hot is not None:
        q = q.filter(Course.hot == hot)
    return q.order_by(Course.id).all()


def get_courses_paginated(
    db: Session,
    category: str | None = None,
    subject: str | None = None,
    hot: bool | None = None,
    page: int = 1,
    page_size: int = 20,
):
    """获取课程列表（分页），返回 (items, total)"""
    q = db.query(Course).filter(Course.is_active == True)
    if category:
        q = q.filter(Course.category == category)
    if subject:
        q = q.filter(Course.subject == subject)
    if hot is not None:
        q = q.filter(Course.hot == hot)

    total = q.count()
    offset = (page - 1) * page_size
    items = q.order_by(Course.id).offset(offset).limit(page_size).all()
    return items, total


def get_course_by_id(db: Session, course_id: int):
    """获取课程详情"""
    return db.query(Course).filter(Course.id == course_id, Course.is_active == True).first()


# ── 报名 ──

def get_enrollment(db: Session, user_id: int, course_id: int):
    """查询用户是否已报名某课程"""
    return db.query(Enrollment).filter(
        Enrollment.user_id == user_id,
        Enrollment.course_id == course_id,
    ).first()


def enroll_course(db: Session, user_id: int, course_id: int):
    """报名课程（自动更新报名人数）"""
    course = get_course_by_id(db, course_id)
    if not course:
        return None

    existing = get_enrollment(db, user_id, course_id)
    if existing:
        return existing

    enrollment = Enrollment(user_id=user_id, course_id=course_id)
    course.students += 1
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment