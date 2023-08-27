from pydantic import UUID4, Field, constr

from fastcord.enums import ChannelType

from .base import BaseSchema


class Channel(BaseSchema):
    name: constr(min_length=3, max_length=32)
    type: ChannelType = Field(default=ChannelType.TEXT)
    guild_id: UUID4
    channel_group_id: UUID4
