"""
异步数据库模块（asyncpg + SQLAlchemy 2.0 async）
- 连接池大小：20 + overflow 10，适合高并发
- 自动重连 (pool_pre_ping)
- 长查询超时 30s
- 连接池耗尽自动降级提示
"""
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from core.config import settings

# ── 异步引擎 ────────────────────────────────────
DATABASE_URL = settings.DATABASE_URL

# 兼容旧配置中的 sqlite:/// → 自动转为 aiosqlite
# 兼容 postgresql:// → 自动转为 postgresql+asyncpg://
if DATABASE_URL.startswith("sqlite"):
    # SQLite → aiosqlite
    if not DATABASE_URL.startswith("sqlite+aiosqlite"):
        DATABASE_URL = DATABASE_URL.replace("sqlite:///", "sqlite+aiosqlite:///", 1)
elif DATABASE_URL.startswith("postgresql"):
    # PostgreSQL → asyncpg
    if "asyncpg" not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)

_is_sqlite = "sqlite" in DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    pool_size=20 if not _is_sqlite else 1,
    max_overflow=10 if not _is_sqlite else 0,
    pool_pre_ping=not _is_sqlite,
    pool_recycle=3600,
    echo=settings.DEBUG,
    connect_args={
        "timeout": 30,           # 连接超时 30s
        "command_timeout": 60,   # 查询超时 60s（asyncpg）
        "server_settings": {"application_name": "challenge_cup"},
    } if not _is_sqlite else {"check_same_thread": False},
)

# ── 异步会话工厂 ───────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# ── 基类 ───────────────────────────────────────
Base = declarative_base()


# ── 依赖注入（异步版） ──────────────────────────
async def get_db() -> AsyncSession:  # type: ignore[return]
    """
    FastAPI 异步依赖注入。
    用法：
        @app.get("/items")
        async def list_items(db: AsyncSession = Depends(get_db)):
            ...
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()