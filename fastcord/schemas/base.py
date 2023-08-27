from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, ConfigDict, Field


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4 = Field(default_factory=uuid4)
    created: datetime = Field(default_factory=datetime.utcnow)
