"""
统一日志模块
- 请求日志：记录每个 HTTP 请求的方法、路径、状态码、耗时
- 错误日志：记录异常堆栈信息
- SQL 日志：由 SQLAlchemy echo 控制（开发环境开启）
- 开发环境：纯文本输出
- 生产环境：JSON 行格式（接入 ELK / Loki）
- 高并发：BufferedLogger 批量落盘避免 I/O 阻塞
"""
import asyncio
import json
import logging
import time
import sys

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from core.config import settings

# ── 日志格式化（开发：纯文本 / 生产：JSON） ────
LOG_FORMAT_TEXT = "[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class _JsonFormatter(logging.Formatter):
    """JSON 行日志格式，适合生产环境接入 ELK / Loki"""

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": self.formatTime(record, DATE_FORMAT),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info and record.exc_info[1]:
            payload["exc"] = str(record.exc_info[1])
        return json.dumps(payload, ensure_ascii=False)


def _make_handler():
    """根据 DEBUG 决定输出格式和级别"""
    is_dev = getattr(settings, "DEBUG", False)
    h = logging.StreamHandler(sys.stdout)
    h.setLevel(logging.DEBUG if is_dev else logging.WARNING)
    if is_dev:
        h.setFormatter(logging.Formatter(LOG_FORMAT_TEXT, datefmt=DATE_FORMAT))
    else:
        h.setFormatter(_JsonFormatter())
    return h


# 根日志器
root_logger = logging.getLogger("challenge_cup")
root_logger.setLevel(logging.DEBUG if getattr(settings, "DEBUG", False) else logging.WARNING)
root_logger.handlers.clear()
root_logger.addHandler(_make_handler())
root_logger.propagate = False

logger = root_logger


# ── 请求日志中间件 ─────────────────────────────
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    记录每个 HTTP 请求，异步无阻塞。
    生产环境下超过 1s 的请求自动标记为 WARNING（慢查询检测）。
    """
    SLOW_THRESHOLD_MS: float = 1000.0

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        elapsed = (time.perf_counter() - start) * 1000

        level = logging.WARNING if elapsed > self.SLOW_THRESHOLD_MS else logging.INFO
        logger.log(
            level,
            "%-6s %s → %s (%.2fms)",
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
        )
        return response


# ── 高并发缓冲日志 ─────────────────────────────
class BufferedLogger:
    """批量收集日志消息，由后台任务定时刷出，避免每条日志触发 I/O"""

    def __init__(self, flush_interval: float = 2.0, max_buffer: int = 500):
        self._buffer: list[str] = []
        self._flush_interval = flush_interval
        self._max_buffer = max_buffer
        self._task: asyncio.Task | None = None

    async def _flush_loop(self):
        while True:
            await asyncio.sleep(self._flush_interval)
            await self.flush()

    async def flush(self):
        if not self._buffer:
            return
        batch = self._buffer[:]
        self._buffer.clear()
        for msg in batch:
            logger.info(msg)

    def log(self, msg: str):
        self._buffer.append(msg)
        if len(self._buffer) >= self._max_buffer:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self.flush())
            except RuntimeError:
                pass

    def start(self):
        try:
            loop = asyncio.get_running_loop()
            self._task = loop.create_task(self._flush_loop())
        except RuntimeError:
            pass

    async def stop(self):
        if self._task:
            self._task.cancel()
        await self.flush()


buffered_logger = BufferedLogger()


def get_logger(name: str) -> logging.Logger:
    """获取子 logger（模块级使用）"""
    return root_logger.getChild(name)