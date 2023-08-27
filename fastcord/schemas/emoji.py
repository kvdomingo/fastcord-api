from pydantic import UUID4, AnyHttpUrl, constr

from .base import BaseSchema


class Emoji(BaseSchema):
    name: constr(min_length=1, max_length=32)
    source: AnyHttpUrl
    guild_id: UUID4
