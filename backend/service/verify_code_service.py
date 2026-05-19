"""
验证码服务 — 邮件真实发送 + 终端打印兜底
"""
import random
import time
import logging

from utils.email import send_verify_code_email

logger = logging.getLogger(__name__)

# 内存存储：{ "email": {"code": "123456", "expire_at": 1234567890, "last_send": 1234567890 } }
_store: dict[str, dict] = {}

# 验证码有效期（秒）
CODE_EXPIRE_SECONDS = 300  # 5 分钟
# 发送间隔（秒）
CODE_INTERVAL_SECONDS = 60  # 1 分钟内不允许重复发送


def generate_code() -> str:
    """生成 6 位数字验证码"""
    return str(random.randint(100000, 999999))


async def send_code(email: str) -> str:
    """
    生成验证码并通过 QQ 邮箱发送。
    同时打印到终端作为调试兜底。
    """
    now = time.time()

    # 检查是否在发送间隔内
    if email in _store:
        last_send = _store[email].get("last_send", 0)
        if now - last_send < CODE_INTERVAL_SECONDS:
            remaining = int(CODE_INTERVAL_SECONDS - (now - last_send))
            raise ValueError(f"请 {remaining} 秒后再试")

    code = generate_code()
    expire_at = now + CODE_EXPIRE_SECONDS

    _store[email] = {
        "code": code,
        "expire_at": expire_at,
        "last_send": now,
    }

    # 打印到终端（开发阶段兜底）
    log_msg = (
        "\n" + "=" * 50 + "\n"
        f"  📧 验证码已生成\n"
        f"  邮箱: {email}\n"
        f"  验证码: {code}\n"
        f"  有效期: {CODE_EXPIRE_SECONDS} 秒\n"
        + "=" * 50 + "\n"
    )
    logger.info(log_msg)
    print(log_msg)

    # 真实发送邮件
    try:
        await send_verify_code_email(email, code)
    except Exception as e:
        logger.error("邮件发送失败: %s —— 请使用终端打印的验证码", str(e))
        print(f"⚠️ 邮件发送失败: {e}\n请使用上方终端打印的验证码")

    return code


def verify_code(email: str, code: str) -> bool:
    """验证验证码是否正确且未过期"""
    entry = _store.get(email)
    if not entry:
        return False

    now = time.time()
    if now > entry["expire_at"]:
        del _store[email]
        return False

    if entry["code"] != code:
        return False

    # 验证成功后删除，防止重复使用
    del _store[email]
    return True


def cleanup_expired():
    """清理过期验证码（可定时调用）"""
    now = time.time()
    expired = [k for k, v in _store.items() if now > v["expire_at"]]
    for k in expired:
        del _store[k]