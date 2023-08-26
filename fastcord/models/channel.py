from datetime import datetime

from sqlalchemy import ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastcord.enums import ChannelType

from .base import Base, generate_uuid


class Channel(Base):
    __tablename__ = "channel"
    __table_args__ = (
        UniqueConstraint(
            "name", "type", "guild_id", name="unique_channel_names_types_per_guild"
        ),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid, index=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    name: Mapped[str] = mapped_column(String(32))
    type: Mapped[ChannelType] = mapped_column(String(5))
    guild_id: Mapped[str] = mapped_column(ForeignKey("guild.id"))
    guild: Mapped["Guild"] = relationship(back_populates="channels")
    messages: Mapped[list["Message"]] = relationship(back_populates="channel")
