"""
认证服务层 — 登录/注册业务逻辑编排
"""
from sqlalchemy.orm import Session
from utils.exceptions import BusinessException, ERR_CONFLICT, ERR_UNAUTHORIZED, ERR_BAD_REQUEST, ERR_TOO_MANY_REQUESTS
from utils.logging import get_logger
from core.security import create_access_token
import crud.user_crud as crud
from service.login_rate_limit_service import is_locked, get_locked_remaining, record_fail, reset

logger = get_logger(__name__)


class AuthService:
    """认证业务逻辑"""

    @staticmethod
    def register(db: Session, username: str, email: str, password: str) -> dict:
        """
        注册用户
        返回 { "access_token": str, "user": dict }
        """
        # 唯一性检查
        if crud.get_user_by_username(db, username):
            raise BusinessException(code=ERR_CONFLICT, message="用户名已存在")
        if crud.get_user_by_email(db, email):
            raise BusinessException(code=ERR_CONFLICT, message="邮箱已注册")

        user = crud.create_user(db, username, email, password)
        access_token = create_access_token(data={"sub": str(user.id)})

        logger.info("用户注册成功: id=%s username=%s email=%s", user.id, username, email)

        return {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_active": user.is_active,
            },
        }

    @staticmethod
    def login(db: Session, email: str, password: str) -> dict:
        """
        用户登录（邮箱+密码）
        返回 { "access_token": str, "user": dict }
        """
        if not email or not password:
            raise BusinessException(code=ERR_BAD_REQUEST, message="邮箱和密码不能为空")

        # 检查是否已被锁定
        if is_locked(email):
            remaining = get_locked_remaining(email)
            minutes = remaining // 60
            seconds = remaining % 60
            raise BusinessException(
                code=ERR_TOO_MANY_REQUESTS,
                message=f"登录失败次数过多，请 {minutes} 分 {seconds} 秒后再试",
            )

        user = crud.authenticate_user_by_email(db, email, password)
        if not user:
            # 记录失败次数
            remaining = record_fail(email)
            if remaining > 0:
                raise BusinessException(
                    code=ERR_UNAUTHORIZED,
                    message=f"邮箱或密码错误，还剩 {remaining} 次尝试机会",
                )
            else:
                raise BusinessException(
                    code=ERR_TOO_MANY_REQUESTS,
                    message="登录失败次数过多，请 15 分钟后再试",
                )

        # 登录成功，重置失败计数
        reset(email)

        access_token = create_access_token(data={"sub": str(user.id)})

        logger.info("用户登录成功: id=%s email=%s", user.id, email)

        return {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "is_active": user.is_active,
            },
        }
