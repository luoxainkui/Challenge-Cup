"""
登录限次服务 — 基于邮箱的登录失败次数限制
- 同一邮箱连续失败 5 次后锁定 15 分钟
- 成功登录后重置失败计数
"""
import time
import threading
import logging

logger = logging.getLogger(__name__)

# ── 内存存储：{ email: { "fail_count": int, "locked_until": float } } ──
_store: dict[str, dict] = {}
_lock = threading.Lock()

# 配置
MAX_FAIL_COUNT = 5            # 最多连续失败次数
LOCK_DURATION_SECONDS = 900   # 锁定时间 15 分钟
CLEANUP_INTERVAL_SECONDS = 600  # 清理过期记录间隔 10 分钟


def record_fail(email: str) -> int:
    """
    记录一次登录失败。
    返回剩余尝试次数（0 表示已被锁定）
    """
    email = email.strip().lower()
    now = time.time()

    with _lock:
        entry = _store.get(email)
        if not entry:
            entry = {"fail_count": 1, "locked_until": 0}
            _store[email] = entry
            return MAX_FAIL_COUNT - 1

        # 检查是否还在锁定期内
        if entry.get("locked_until", 0) > now:
            remaining = int(entry["locked_until"] - now)
            logger.warning("登录锁定中: %s, 剩余 %d 秒", email, remaining)
            return 0  # 已被锁定

        # 累加失败次数
        entry["fail_count"] += 1
        if entry["fail_count"] >= MAX_FAIL_COUNT:
            entry["locked_until"] = now + LOCK_DURATION_SECONDS
            logger.warning("登录已被锁定: %s, 锁定 %d 秒", email, LOCK_DURATION_SECONDS)
            return 0

        return MAX_FAIL_COUNT - entry["fail_count"]


def is_locked(email: str) -> bool:
    """检查邮箱是否处于锁定状态"""
    email = email.strip().lower()
    now = time.time()

    with _lock:
        entry = _store.get(email)
        if not entry:
            return False
        if entry.get("locked_until", 0) > now:
            return True
        return False


def get_locked_remaining(email: str) -> int:
    """获取锁定剩余秒数，未锁定返回 0"""
    email = email.strip().lower()
    now = time.time()

    with _lock:
        entry = _store.get(email)
        if not entry:
            return 0
        if entry.get("locked_until", 0) > now:
            return int(entry["locked_until"] - now)
        return 0


def reset(email: str) -> None:
    """登录成功后重置失败计数"""
    email = email.strip().lower()
    with _lock:
        _store.pop(email, None)
        logger.debug("登录成功，重置失败计数: %s", email)


def cleanup_expired():
    """清理过期的锁定记录"""
    now = time.time()
    with _lock:
        expired = [
            k for k, v in _store.items()
            if v.get("locked_until", 0) > 0 and v["locked_until"] <= now
        ]
        for k in expired:
            del _store[k]
    if expired:
        logger.debug("清理 %d 条过期登录锁定记录", len(expired))