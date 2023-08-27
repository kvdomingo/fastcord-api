from sqlalchemy.ext.asyncio import create_async_engine

from fastcord.settings import get_settings

settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL, echo=settings.PYTHON_ENV == "development"
)
