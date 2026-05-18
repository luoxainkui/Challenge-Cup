"""
认证 API — 路由层（薄层，只负责参数解析和调用 Service）
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schema.user_schema import UserRegister, UserLogin
from schema.common import ApiResponse
from service.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["认证"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """注册 → 返回 { code, message, data: { access_token, user } }"""
    result = AuthService.register(
        db,
        username=data.username,
        email=data.email,
        password=data.password,
        phone=data.phone,
    )
    return ApiResponse.ok(data=result, message="注册成功")


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    """登录 → 返回 { code, message, data: { access_token, user } }"""
    result = AuthService.login(db, username=data.username, password=data.password)
    return ApiResponse.ok(data=result, message="登录成功")