from pydantic import UUID4, constr

from .base import BaseSchema


class Channel(BaseSchema):
    name: constr(min_length=3, max_length=32)
    guild_id: UUID4
