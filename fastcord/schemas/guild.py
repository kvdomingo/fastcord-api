from datetime import datetime
from typing import Optional

from pydantic import UUID4, AnyHttpUrl, BaseModel, ConfigDict, constr


class Guild(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    created: datetime
    name: constr(min_length=3, max_length=64)
    avatar: Optional[AnyHttpUrl]
    banner: Optional[AnyHttpUrl]
