from datetime import datetime

from pydantic import UUID4, BaseModel, ConfigDict, constr


class Channel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created: datetime
    name: constr(min_length=3, max_length=32)
    guild_id: UUID4
