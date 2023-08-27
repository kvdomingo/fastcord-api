from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastcord.enums import ChannelType

from .base import BaseModel


class Channel(BaseModel):
    __tablename__ = "channel"
    __table_args__ = (
        UniqueConstraint(
            "name", "type", "guild_id", name="unique_channel_names_types_per_guild"
        ),
    )

    name: Mapped[str] = mapped_column(String(32))
    type: Mapped[ChannelType] = mapped_column(default=ChannelType.TEXT)
    guild_id: Mapped[str] = mapped_column(ForeignKey("guild.id"))
    guild: Mapped["Guild"] = relationship(back_populates="channels")
    messages: Mapped[list["Message"]] = relationship(back_populates="channel")
    channel_group_id: Mapped[str] = mapped_column(ForeignKey("channel_group.id"))
    channel_group: Mapped["ChannelGroup"] = relationship(back_populates="channels")
