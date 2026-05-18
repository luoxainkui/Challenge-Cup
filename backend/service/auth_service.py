"""
认证服务层 — 登录/注册业务逻辑编排
"""
from sqlalchemy.orm import Session
from utils.exceptions import BusinessException, ERR_CONFLICT, ERR_UNAUTHORIZED, ERR_BAD_REQUEST
from utils.logging import get_logger
from core.security import create_access_token
import crud.user_crud as crud

logger = get_logger(__name__)


class AuthService:
    """认证业务逻辑"""

    @staticmethod
    def register(db: Session, username: str, email: str, password: str, phone: str | None = None) -> dict:
        """
        注册用户
        返回 { "access_token": str, "user": dict }
        """
        # 唯一性检查
        if crud.get_user_by_username(db, username):
            raise BusinessException(code=ERR_CONFLICT, message="用户名已存在")
        if crud.get_user_by_email(db, email):
            raise BusinessException(code=ERR_CONFLICT, message="邮箱已注册")
        if phone and crud.get_user_by_phone(db, phone):
            raise BusinessException(code=ERR_CONFLICT, message="手机号已注册")

        user = crud.create_user(db, username, email, password, phone)
        access_token = create_access_token(data={"sub": str(user.id)})

        logger.info("用户注册成功: id=%s username=%s", user.id, username)

        return {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "is_active": user.is_active,
            },
        }

    @staticmethod
    def login(db: Session, username: str, password: str) -> dict:
        """
        用户登录
        返回 { "access_token": str, "user": dict }
        """
        if not username or not password:
            raise BusinessException(code=ERR_BAD_REQUEST, message="用户名和密码不能为空")

        user = crud.authenticate_user(db, username, password)
        if not user:
            raise BusinessException(code=ERR_UNAUTHORIZED, message="用户名或密码错误")

        access_token = create_access_token(data={"sub": str(user.id)})

        logger.info("用户登录成功: id=%s username=%s", user.id, username)

        return {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "is_active": user.is_active,
            },
        }