"""
认证 API — 路由层（薄层，只负责参数解析和调用 Service）
"""
from pydantic import BaseModel, EmailStr, field_validator
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schema.user_schema import UserRegister, UserLogin
from schema.common import ApiResponse
from service.auth_service import AuthService
from service.verify_code_service import send_code as svc_send_code, verify_code
from utils.exceptions import ERR_BAD_REQUEST, ERR_NOT_FOUND
import crud.user_crud as crud

router = APIRouter(prefix="/auth", tags=["认证"])


class SendCodeRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("密码长度至少6位")
        return v


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """注册 → 返回 { code, message, data: { access_token, user } }"""
    result = AuthService.register(
        db,
        username=data.username,
        email=data.email,
        password=data.password,
    )
    return ApiResponse.ok(data=result, message="注册成功")


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    """登录 → 返回 { code, message, data: { access_token, user } }"""
    result = AuthService.login(db, email=data.email, password=data.password)
    return ApiResponse.ok(data=result, message="登录成功")


@router.post("/send-code")
async def send_code(data: SendCodeRequest):
    """
    发送验证码 — 通过 QQ 邮箱发送到用户邮箱
    同时打印到终端控制台作为调试兜底
    """
    try:
        code = await svc_send_code(data.email)
        return ApiResponse.ok(
            data={"code": code},
            message="验证码已发送到您的邮箱，如未收到请检查垃圾箱或使用终端打印的验证码"
        )
    except ValueError as e:
        return ApiResponse.fail(code=ERR_BAD_REQUEST, message=str(e))


@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    """
    通过邮箱+验证码重置密码
    """
    if not verify_code(data.email, data.code):
        return ApiResponse.fail(code=ERR_BAD_REQUEST, message="验证码错误或已过期")
    ok = crud.update_password_by_email(db, data.email, data.password)
    if not ok:
        return ApiResponse.fail(code=ERR_NOT_FOUND, message="邮箱未注册")
    return ApiResponse.ok(data=None, message="密码重置成功")