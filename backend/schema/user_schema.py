from pydantic import BaseModel, EmailStr, field_validator
import re


class UserRegister(BaseModel):
    """注册请求"""
    username: str
    email: EmailStr
    password: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        v = v.strip()
        if not (1 <= len(v) <= 10):
            raise ValueError("用户名长度需在 1-10 个字符之间")
        if re.match(r"^\d+$", v):
            raise ValueError("用户名不能为纯数字")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("密码长度至少 6 个字符")
        return v


class UserLogin(BaseModel):
    """登录请求 — 使用邮箱"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """用户信息响应（不返回密码）"""
    id: int
    username: str
    email: str
    is_active: bool

    model_config = {"from_attributes": True}


class Token(BaseModel):
    """JWT Token 响应"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse