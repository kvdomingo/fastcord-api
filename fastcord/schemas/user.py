from datetime import datetime
from typing import Optional

from pydantic import UUID4, AnyHttpUrl, BaseModel, ConfigDict, EmailStr, conint, constr

from fastcord.enums import AvailabilityStatus


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created: datetime
    name: Optional[constr(min_length=1, max_length=64)]
    email: EmailStr
    username: constr(min_length=1, max_length=32)
    discriminator: conint(ge=0, le=9999)
    avatar: Optional[AnyHttpUrl]
    availability_status: AvailabilityStatus
    status_message: Optional[constr(min_length=1, max_length=32)]
    status_emoji_id: Optional[UUID4]
