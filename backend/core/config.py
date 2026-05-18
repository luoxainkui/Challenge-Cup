from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 应用
    APP_NAME: str = "Challenge Cup Backend"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # 数据库 - 支持 SQLite（开发）/ PostgreSQL（生产）
    DATABASE_URL: str = "sqlite:///./challenge_cup.db"

    # JWT 安全
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # 服务
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()