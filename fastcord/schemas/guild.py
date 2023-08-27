from typing import Optional

from pydantic import AnyHttpUrl, Field, constr

from .base import BaseSchema


class Guild(BaseSchema):
    name: constr(min_length=3, max_length=64)
    avatar: Optional[AnyHttpUrl] = Field(default=None)
    banner: Optional[AnyHttpUrl] = Field(default=None)
