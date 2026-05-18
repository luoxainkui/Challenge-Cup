"""
统一响应格式 + 分页包装器

所有 API 响应统一为：
{
    "code": 0,          # 0=成功，其他=错误码
    "message": "success",
    "data": { ... }
}
"""
from typing import Any, Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """统一响应格式"""
    code: int = 0
    message: str = "success"
    data: T | None = None

    @classmethod
    def ok(cls, data: Any = None, message: str = "success") -> "ApiResponse":
        """成功响应"""
        return cls(code=0, message=message, data=data)

    @classmethod
    def fail(cls, code: int, message: str, data: Any = None) -> "ApiResponse":
        """失败响应"""
        return cls(code=code, message=message, data=data)


class PageInfo(BaseModel):
    """分页信息"""
    page: int = 1
    page_size: int = 20
    total: int = 0
    total_pages: int = 0


class PageResponse(BaseModel, Generic[T]):
    """分页响应"""
    list: list[T]
    page_info: PageInfo