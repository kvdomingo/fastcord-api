from uuid import uuid4

import mongoengine


class Base(mongoengine.Document):
    id = mongoengine.UUIDField(
        binary=False, default=uuid4, primary_key=True, unique=True
    )
