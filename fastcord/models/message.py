from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import Base, generate_uuid


class Message(Base):
    __tablename__ = "message"

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid, index=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    modified: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=func.now()
    )
    content: Mapped[str] = mapped_column(String(2048))
    author_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="messages")
    channel_id: Mapped[str] = mapped_column(ForeignKey("channel.id"))
    channel: Mapped["Channel"] = relationship(back_populates="messages")
