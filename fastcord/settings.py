from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PYTHON_ENV: str = "production"
    DATABASE_URL: str
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SENDGRID_API_KEY: str
    CORS_ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings():
    return Settings()
