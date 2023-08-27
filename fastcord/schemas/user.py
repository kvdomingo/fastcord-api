from typing import Optional

from pydantic import UUID4, AnyHttpUrl, EmailStr, Field, conint, constr

from fastcord.enums import AvailabilityStatus
from fastcord.models import generate_discriminator

from .base import BaseSchema


class User(BaseSchema):
    name: Optional[constr(min_length=1, max_length=64)] = Field(default=None)
    email: EmailStr
    username: constr(min_length=1, max_length=32)
    discriminator: conint(ge=0, le=9999) = Field(default_factory=generate_discriminator)
    avatar: Optional[AnyHttpUrl] = Field(default=None)
    availability_status: AvailabilityStatus
    status_message: Optional[constr(min_length=1, max_length=32)] = Field(default=None)
    status_emoji_id: Optional[UUID4] = Field(default=None)
