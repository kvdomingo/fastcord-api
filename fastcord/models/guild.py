import mongoengine

from .base import Base


class Guild(Base):
    name = mongoengine.StringField(required=True, min_length=3, max_length=64)
    avatar = mongoengine.URLField()
    banner = mongoengine.URLField()
