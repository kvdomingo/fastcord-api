from datetime import datetime
from typing import Optional

from pydantic import UUID4, AnyHttpUrl, BaseModel, constr


class Guild(BaseModel):
    id: UUID4
    created: datetime
    name: constr(min_length=3, max_length=64)
    avatar: Optional[AnyHttpUrl]
    banner: Optional[AnyHttpUrl]
