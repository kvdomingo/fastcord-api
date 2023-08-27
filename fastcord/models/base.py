from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        primary_key=True, server_default=func.gen_random_uuid(), index=True
    )
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
