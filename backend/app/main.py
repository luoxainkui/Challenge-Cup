from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from core.database import engine, Base, SessionLocal
from api.common_api import router as common_router
from api.auth_api import router as auth_router
from api.course_api import router as course_router
from utils.logging import RequestLoggingMiddleware
from utils.exceptions import register_exception_handlers

# 注册所有模型，确保 create_all 能发现
import model.user_model  # noqa: F401
import model.course_model  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时：自动建表（生产环境建议用 Alembic 迁移）
    Base.metadata.create_all(bind=engine)

    # 初始化种子数据
    db = SessionLocal()
    try:
        import crud.course_crud as course_crud
        course_crud.seed_subjects(db)
        course_crud.seed_courses(db)
    finally:
        db.close()

    yield
    # 关闭时：释放引擎连接池
    engine.dispose()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan,
)

# ── 请求日志中间件 ──
app.add_middleware(RequestLoggingMiddleware)

# ── CORS 中间件 ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── 注册全局异常处理器 ──
register_exception_handlers(app)

# ── 注册路由 ──
app.include_router(common_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(course_router, prefix="/api")


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running"}