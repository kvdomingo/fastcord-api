from datetime import datetime

from pydantic import UUID4, BaseModel, constr

from fastcord.enums import ChannelType


class Channel(BaseModel):
    id: UUID4
    created: datetime
    name: constr(min_length=3, max_length=32)
    type: ChannelType
    guild_id: UUID4
