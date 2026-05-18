from pydantic import BaseModel, EmailStr, field_validator
import re


class UserRegister(BaseModel):
    """注册请求"""
    username: str
    email: EmailStr
    phone: str | None = None
    password: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not (3 <= len(v) <= 50):
            raise ValueError("用户名长度需在 3-50 个字符之间")
        if not re.match(r"^[a-zA-Z0-9_]+$", v):
            raise ValueError("用户名只能包含字母、数字和下划线")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("密码长度至少 6 个字符")
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str | None) -> str | None:
        if v is not None and not re.match(r"^1[3-9]\d{9}$", v):
            raise ValueError("手机号格式不正确")
        return v


class UserLogin(BaseModel):
    """登录请求"""
    username: str
    password: str


class UserResponse(BaseModel):
    """用户信息响应（不返回密码）"""
    id: int
    username: str
    email: str
    phone: str | None = None
    is_active: bool

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """JWT Token 响应"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse