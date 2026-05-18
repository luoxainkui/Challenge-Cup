"""
统一日志模块
- 请求日志：记录每个 HTTP 请求的方法、路径、状态码、耗时
- 错误日志：记录异常堆栈信息
- SQL 日志：由 SQLAlchemy echo 控制（开发环境开启）
"""
import logging
import time
import sys
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.config import settings

# ── 日志格式化 ──────────────────────────────────
LOG_FORMAT = (
    "[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s"
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 控制台输出
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

# 根日志器
root_logger = logging.getLogger("challenge_cup")
root_logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
root_logger.handlers.clear()
root_logger.addHandler(console_handler)
root_logger.propagate = False

logger = root_logger


# ── 请求日志中间件 ─────────────────────────────
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """记录每个 HTTP 请求的方法、路径、状态码、耗时"""

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed = (time.perf_counter() - start) * 1000  # ms
        logger.info(
            "%s %s → %s (%.2fms)",
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
        )
        return response


def get_logger(name: str) -> logging.Logger:
    """获取子 logger（模块级使用）"""
    return root_logger.getChild(name)