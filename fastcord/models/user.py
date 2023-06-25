import mongoengine

from .base import Base


class User(Base):
    name = mongoengine.StringField(required=True, min_length=3, max_length=64)
    email = mongoengine.EmailField(required=True)
    username = mongoengine.StringField(required=True, min_length=3, max_length=32)
    discriminator = mongoengine.IntField(required=True, min_value=0, max_value=9999)
    avatar = mongoengine.URLField()
    friends = mongoengine.ListField(
        mongoengine.LazyReferenceField("User"), default=list
    )
