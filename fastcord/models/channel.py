from enum import Enum

import mongoengine

from .base import Base


class ChannelType(Enum):
    TEXT = "TEXT"
    VOICE = "VOICE"
    FORUM = "FORUM"
    FORUM_POST = "FORUM_POST"


class Channel(Base):
    name = mongoengine.StringField(required=True, min_length=3, max_length=32)
    type = mongoengine.StringField(
        required=True, min_length=4, max_length=10, default=ChannelType.TEXT
    )
    guild = mongoengine.LazyReferenceField("Guild")
    forum = mongoengine.LazyReferenceField("Channel")
