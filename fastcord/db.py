from mongoengine import connect

from fastcord.config import get_settings

settings = get_settings()


connect(settings.DATABASE_URL)
