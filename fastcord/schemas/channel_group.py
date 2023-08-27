from pydantic import UUID4, conint, constr

from .base import BaseSchema


class ChannelGroup(BaseSchema):
    name: constr(min_length=3, max_length=32)
    order: conint(ge=1)
    guild_id: UUID4
