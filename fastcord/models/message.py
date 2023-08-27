from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import BaseModel


class Message(BaseModel):
    __tablename__ = "message"

    modified: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=func.now()
    )
    content: Mapped[str] = mapped_column(String(2048))
    author_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="messages")
    channel_id: Mapped[str] = mapped_column(ForeignKey("channel.id"))
    channel: Mapped["Channel"] = relationship(back_populates="messages")
