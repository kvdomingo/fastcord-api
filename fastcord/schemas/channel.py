from pydantic import UUID4, Field, conint, constr

from fastcord.enums import ChannelType

from .base import BaseSchema


class Channel(BaseSchema):
    name: constr(min_length=3, max_length=32)
    order: conint(ge=1)
    type: ChannelType = Field(default=ChannelType.TEXT)
    guild_id: UUID4
    channel_group_id: UUID4
