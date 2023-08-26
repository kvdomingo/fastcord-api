from datetime import datetime
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import Base, generate_uuid


class Guild(Base):
    __tablename__ = "guild"

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid, index=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    name: Mapped[str] = mapped_column(String(64))
    avatar: Mapped[Optional[str]] = mapped_column(String)
    banner: Mapped[Optional[str]] = mapped_column(String)
    channels: Mapped[list["Channel"]] = relationship(back_populates="guild")
    emojis: Mapped[list["Emojis"]] = relationship(back_populates="guild")
