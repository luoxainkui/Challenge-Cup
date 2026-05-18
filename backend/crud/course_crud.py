from sqlalchemy.orm import Session
from model.course_model import Course, Subject, Enrollment


def get_subjects(db: Session):
    """获取所有启用的学科大类"""
    return db.query(Subject).filter(Subject.is_active == True).all()


def seed_subjects(db: Session):
    """初始化种子学科数据（幂等）"""
    seed_data = [
        {"key": "yuwen", "name": "语文", "desc": "文言文 · 现代文阅读 · 写作"},
        {"key": "shuxue", "name": "数学", "desc": "函数 · 微积分 · 线性代数"},
        {"key": "yingyu", "name": "英语", "desc": "词汇 · 语法 · 阅读 · 写作"},
        {"key": "zhuanyeke", "name": "专业课", "desc": "管理 · 会计 · 计算机 · 经济"},
    ]
    for item in seed_data:
        if not db.query(Subject).filter(Subject.key == item["key"]).first():
            db.add(Subject(**item))
    db.commit()


def seed_courses(db: Session):
    """初始化种子课程数据（幂等），匹配前端 constants/courses.js 的 COURSES 数组"""
    existing = db.query(Course).first()
    if existing:
        return

    courses_data = [
        {"subject": "大学英语", "category": "公共课", "name": "专升本大学英语精讲班",
         "desc": "从词汇到写作，系统性提升英语综合能力，紧扣广西专升本英语考纲",
         "teacher": "张雪峰教授", "students": 3256, "rating": 4.9, "price": 299,
         "hot": True, "duration": "12周", "lessons": 48},
        {"subject": "高等数学", "category": "公共课", "name": "专升本高等数学强化班",
         "desc": "聚焦必考知识点，精讲精练，帮助零基础学员快速突破数学难关",
         "teacher": "李明博士", "students": 2187, "rating": 4.8, "price": 359,
         "hot": True, "duration": "10周", "lessons": 40},
        {"subject": "管理学", "category": "专业课", "name": "管理学原理精讲精练",
         "desc": "结合广西专升本管理学考纲，深入浅出讲解管理理论与实践案例",
         "teacher": "王红副教授", "students": 1876, "rating": 4.7, "price": 259,
         "hot": False, "duration": "8周", "lessons": 32},
        {"subject": "大学语文", "category": "公共课", "name": "专升本大学语文基础班",
         "desc": "从文言文到现代文阅读，全面提升语文素养与应试技巧",
         "teacher": "刘芳教授", "students": 1567, "rating": 4.8, "price": 199,
         "hot": False, "duration": "10周", "lessons": 36},
        {"subject": "会计学", "category": "专业课", "name": "会计学基础与实务",
         "desc": "理论联系实际，掌握会计核心技能，轻松应对专业考试",
         "teacher": "陈强讲师", "students": 1342, "rating": 4.6, "price": 279,
         "hot": False, "duration": "8周", "lessons": 30},
        {"subject": "计算机", "category": "专业课", "name": "计算机应用基础速成班",
         "desc": "零基础入门，涵盖Office操作与计算机基础理论，快速提分",
         "teacher": "赵敏博士", "students": 2103, "rating": 4.7, "price": 239,
         "hot": False, "duration": "6周", "lessons": 24},
        {"subject": "政治", "category": "公共课", "name": "专升本政治理论精讲班",
         "desc": "紧扣时事热点，系统梳理政治理论考点，助力高分突破",
         "teacher": "周华教授", "students": 2890, "rating": 4.9, "price": 269,
         "hot": True, "duration": "8周", "lessons": 32},
        {"subject": "经济学", "category": "专业课", "name": "经济学原理与实务",
         "desc": "宏观微观经济学核心知识详解，配合同步习题巩固提升",
         "teacher": "吴芳博士", "students": 987, "rating": 4.5, "price": 289,
         "hot": False, "duration": "10周", "lessons": 36},
    ]

    for c in courses_data:
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
