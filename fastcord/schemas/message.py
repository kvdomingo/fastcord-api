from datetime import datetime

from pydantic import UUID4, BaseModel, ConfigDict, constr


class Message(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created: datetime
    modified: datetime
    content: constr(min_length=1, max_length=2048)
    author_id: UUID4
    channel_id: UUID4
