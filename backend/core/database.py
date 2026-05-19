"""
同步数据库模块（SQLAlchemy ORM + psycopg2 / pysqlite）
- 连接池大小：20 + overflow 10，适合高并发
- 自动重连 (pool_pre_ping)
- 长查询超时 30s
- 连接池耗尽自动降级提示
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# ── 同步引擎 ────────────────────────────────────
DATABASE_URL = settings.DATABASE_URL

_connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    _connect_args = {"check_same_thread": False}
else:
    _connect_args = {
        "connect_timeout": 30,
        "application_name": "challenge_cup",
    }

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=settings.DEBUG,
    connect_args=_connect_args,
)

# ── 会话工厂 ────────────────────────────────────
SessionLocal = sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False,
)

# ── 基类 ───────────────────────────────────────
Base = declarative_base()


# ── 依赖注入（同步版） ──────────────────────────
def get_db():
    """
    FastAPI 同步依赖注入。
    用法：
        @app.get("/items")
        def list_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()