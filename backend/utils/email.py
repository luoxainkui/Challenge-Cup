"""
邮件发送工具 — 基于 aiosmtplib 异步发送验证码邮件
"""
import logging
import ssl
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import aiosmtplib
import certifi

from core.config import settings

logger = logging.getLogger(__name__)

# 验证码邮件 HTML 模板
VERIFY_CODE_TEMPLATE = """\
<div style="max-width:500px;margin:0 auto;padding:40px 30px;\
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;\
background:#f4f6fb;border-radius:16px;text-align:center">
  <div style="font-size:40px;line-height:1;margin-bottom:8px">🏫</div>
  <h2 style="color:#1a202c;margin:0 0 4px;font-size:22px">桂升通</h2>
  <p style="color:#718096;font-size:14px;margin:0 0 24px">升学备考一站式平台</p>
  <div style="background:#fff;border-radius:12px;padding:28px 20px;margin-bottom:20px">
    <p style="color:#4a5568;font-size:15px;margin:0 0 16px">您的验证码是</p>
    <div style="font-size:36px;font-weight:800;color:#2a6eff;letter-spacing:8px;\
                padding:8px 0">{code}</div>
    <p style="color:#a0aec0;font-size:12px;margin:16px 0 0">
      验证码 {expire_minutes} 分钟内有效，请勿泄露给他人
    </p>
  </div>
  <p style="color:#a0aec0;font-size:12px;margin:0">
    如非本人操作，请忽略此邮件
  </p>
</div>"""


async def send_verify_code_email(to_email: str, code: str) -> None:
    """异步发送验证码邮件"""
    html = VERIFY_CODE_TEMPLATE.format(code=code, expire_minutes=5)

    msg = MIMEMultipart("alternative")
    sender_name = settings.SMTP_FROM or "桂升通"
    # RFC 2047 编码中文发件人名称（QQ 邮箱 SMTP 要求）
    msg["From"] = f"{Header(sender_name, 'utf-8').encode()} <{settings.SMTP_USER}>"
    msg["To"] = to_email
    msg["Subject"] = "桂升通 - 邮箱验证码"
    msg.attach(MIMEText(html, "html", "utf-8"))

    tls_context = ssl.create_default_context(cafile=certifi.where())
    await aiosmtplib.send(
        msg,
        hostname=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASSWORD,
        use_tls=settings.SMTP_USE_SSL,
        tls_context=tls_context,
    )
    logger.info("验证码邮件已发送 -> %s", to_email)