from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Guild(BaseModel):
    __tablename__ = "guild"

    name: Mapped[str] = mapped_column(String(64))
    avatar: Mapped[Optional[str]] = mapped_column(String)
    banner: Mapped[Optional[str]] = mapped_column(String)
    channels: Mapped[list["Channel"]] = relationship(back_populates="guild")
    emojis: Mapped[list["Emojis"]] = relationship(back_populates="guild")
