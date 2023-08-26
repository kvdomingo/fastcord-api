from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PYTHON_ENV: str = "production"
    DATABASE_URL: PostgresDsn

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
