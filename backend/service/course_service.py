"""
课程服务层 — 课程相关业务逻辑 + 分页
"""
from sqlalchemy.orm import Session
from utils.exceptions import BusinessException, ERR_NOT_FOUND, ERR_CONFLICT
from utils.logging import get_logger
import crud.course_crud as crud

logger = get_logger(__name__)


class CourseService:
    """课程业务逻辑"""

    @staticmethod
    def list_subjects(db: Session) -> list:
        """获取学科大类列表"""
        subjects = crud.get_subjects(db)
        return [
            {"id": s.id, "key": s.key, "name": s.name, "desc": s.desc}
            for s in subjects
        ]

    @staticmethod
    def list_courses(
        db: Session,
        category: str | None = None,
        subject: str | None = None,
        hot: bool | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> dict:
        """
        获取课程列表（分页）
        返回 { "list": [...], "page_info": {...} }
        """
        courses, total = crud.get_courses_paginated(
            db, category=category, subject=subject, hot=hot,
            page=page, page_size=page_size,
        )
        total_pages = max(1, (total + page_size - 1) // page_size)

        return {
            "list": [
                {
                    "id": c.id,
                    "subject": c.subject,
                    "category": c.category,
                    "name": c.name,
                    "desc": c.desc,
                    "teacher": c.teacher,
                    "students": c.students,
                    "rating": c.rating,
                    "price": c.price,
                    "hot": c.hot,
                    "duration": c.duration,
                    "lessons": c.lessons,
                    "is_active": c.is_active,
                    "created_at": c.created_at.isoformat() if c.created_at else None,
                }
                for c in courses
            ],
            "page_info": {
                "page": page,
                "page_size": page_size,
                "total": total,
                "total_pages": total_pages,
            },
        }

    @staticmethod
    def get_course_detail(db: Session, course_id: int) -> dict:
        """获取课程详情"""
        course = crud.get_course_by_id(db, course_id)
        if not course:
            raise BusinessException(code=ERR_NOT_FOUND, message="课程不存在")
        return {
            "id": course.id,
            "subject": course.subject,
            "category": course.category,
            "name": course.name,
            "desc": course.desc,
            "teacher": course.teacher,
            "students": course.students,
            "rating": course.rating,
            "price": course.price,
            "hot": course.hot,
            "duration": course.duration,
            "lessons": course.lessons,
            "is_active": course.is_active,
            "created_at": course.created_at.isoformat() if course.created_at else None,
        }

    @staticmethod
    def enroll_course(db: Session, user_id: int, course_id: int) -> dict:
        """
        报名课程（需登录）
        返回报名记录
        """
        # 检查是否已报名
        enrolled = crud.get_enrollment(db, user_id, course_id)
        if enrolled:
            return {
                "id": enrolled.id,
                "user_id": enrolled.user_id,
                "course_id": enrolled.course_id,
                "enrolled_at": enrolled.enrolled_at.isoformat() if enrolled.enrolled_at else None,
            }

        enrollment = crud.enroll_course(db, user_id=user_id, course_id=course_id)
        if not enrollment:
            raise BusinessException(code=ERR_NOT_FOUND, message="课程不存在")

        logger.info("用户 %s 报名课程 %s", user_id, course_id)

        return {
            "id": enrollment.id,
            "user_id": enrollment.user_id,
            "course_id": enrollment.course_id,
            "enrolled_at": enrollment.enrolled_at.isoformat() if enrollment.enrolled_at else None,
        }