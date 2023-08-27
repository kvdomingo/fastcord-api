from datetime import datetime

from pydantic import UUID4, Field, constr

from .base import BaseSchema


class Message(BaseSchema):
    modified: datetime = Field(default_factory=datetime.utcnow)
    content: constr(min_length=1, max_length=2048)
    author_id: UUID4
    channel_id: UUID4
