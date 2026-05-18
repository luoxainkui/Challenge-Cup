"""
课程 API — 路由层（薄层，只负责参数解析和调用 Service）
"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_user
from schema.common import ApiResponse
from service.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["课程"])


@router.get("/subjects")
def list_subjects(db: Session = Depends(get_db)):
    """获取学科大类列表"""
    result = CourseService.list_subjects(db)
    return ApiResponse.ok(data=result)


@router.get("")
def list_courses(
    category: str | None = Query(None, description="分类筛选：公共课/专业课"),
    subject: str | None = Query(None, description="学科筛选"),
    hot: bool | None = Query(None, description="是否热门"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页数量"),
    db: Session = Depends(get_db),
):
    """获取课程列表（分页）"""
    result = CourseService.list_courses(
        db,
        category=category,
        subject=subject,
        hot=hot,
        page=page,
        page_size=page_size,
    )
    return ApiResponse.ok(data=result)


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    """获取课程详情"""
    result = CourseService.get_course_detail(db, course_id)
    return ApiResponse.ok(data=result)


@router.post("/{course_id}/enroll")
def enroll_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """报名课程（需登录）"""
    result = CourseService.enroll_course(db, user_id=current_user.id, course_id=course_id)
    return ApiResponse.ok(data=result, message="报名成功")