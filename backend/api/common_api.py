"""
通用 API — 健康检查等
"""
from fastapi import APIRouter
from schema.common import ApiResponse

router = APIRouter()


@router.get("/hello")
def hello():
    return ApiResponse.ok(data={"hello": "world"})