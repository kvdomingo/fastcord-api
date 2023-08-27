from datetime import datetime

from pydantic import UUID4, AnyHttpUrl, BaseModel, ConfigDict, constr


class Emoji(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created: datetime
    name: constr(min_length=1, max_length=32)
    source: AnyHttpUrl
    guild_id: UUID4
