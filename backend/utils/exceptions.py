"""
统一异常模块 — 自定义业务异常 + 全局异常处理器

使用方式：
    raise BusinessException(code=404, message="课程不存在")
    raise BusinessException(code=409, message="用户名已存在")
"""
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.logging import get_logger

logger = get_logger(__name__)

# ── 业务错误码常量 ──────────────────────────────────
ERR_OK = 0
ERR_BAD_REQUEST = 400
ERR_UNAUTHORIZED = 401
ERR_FORBIDDEN = 403
ERR_NOT_FOUND = 404
ERR_CONFLICT = 409
ERR_VALIDATION = 422
ERR_INTERNAL = 500


class BusinessException(Exception):
    """业务异常，包含错误码和消息"""

    def __init__(self, code: int = ERR_INTERNAL, message: str = "服务器内部错误"):
        self.code = code
        self.message = message
        super().__init__(message)


# ── 全局异常处理器 ──────────────────────────────────

async def business_exception_handler(request: Request, exc: BusinessException):
    logger.warning("业务异常 [%s] %s: %s", exc.code, request.url.path, exc.message)
    return JSONResponse(
        status_code=exc.code if exc.code < 500 else 200,
        content={"code": exc.code, "message": exc.message, "data": None},
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning("HTTP 异常 [%s] %s: %s", exc.status_code, request.url.path, exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "message": str(exc.detail), "data": None},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """pydantic 参数校验失败 → 422"""
    errors = exc.errors()
    messages = []
    for err in errors:
        field = " → ".join(str(loc) for loc in err["loc"] if loc != "body") or "参数"
        messages.append(f"{field}: {err['msg']}")
    detail = "; ".join(messages)
    logger.warning("参数校验失败 %s: %s", request.url.path, detail)
    return JSONResponse(
        status_code=422,
        content={"code": ERR_VALIDATION, "message": detail, "data": None},
    )


async def unhandled_exception_handler(request: Request, exc: Exception):
    """未知异常兜底 → 500"""
    logger.exception("未捕获异常 %s: %s", request.url.path, str(exc))
    return JSONResponse(
        status_code=500,
        content={"code": ERR_INTERNAL, "message": "服务器内部错误", "data": None},
    )


# ── 注册到 FastAPI app ───────────────────────────────

def register_exception_handlers(app):
    """将全局异常处理器注册到 FastAPI 应用"""
    from utils.exceptions import BusinessException
    from fastapi.exceptions import RequestValidationError
    from starlette.exceptions import HTTPException as StarletteHTTPException

    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
    logger.info("全局异常处理器已注册")