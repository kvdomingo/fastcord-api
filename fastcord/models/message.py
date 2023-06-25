from datetime import datetime

import mongoengine

from .base import Base


class Message(Base):
    created = mongoengine.DateTimeField(required=True, default=datetime.utcnow)
    modified = mongoengine.DateTimeField(required=True, default=datetime.utcnow)
    content = mongoengine.StringField(required=True, min_length=1, max_length=2048)
    author = mongoengine.LazyReferenceField("User")
