from sqlalchemy.orm import Session
from model.user_model import User
from core.security import hash_password, verify_password


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_phone(db: Session, phone: str) -> User | None:
    return db.query(User).filter(User.phone == phone).first()


def create_user(db: Session, username: str, email: str, password: str, phone: str | None = None) -> User:
    """
    创建用户：密码 bcrypt 哈希后入库。
    唯一性检查由 API 层在调用前完成。
    """
    user = User(
        username=username,
        email=email,
        phone=phone,
        hashed_password=hash_password(password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """
    认证用户：查找用户名 -> 验证密码 -> 返回用户或 None
    """
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user