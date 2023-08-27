from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class ChannelGroup(BaseModel):
    __tablename__ = "channel_group"
    __table_args__ = (
        UniqueConstraint(
            "name", "guild_id", name="unique_channel_group_names_per_guild"
        ),
    )

    name: Mapped[str] = mapped_column(String(32))
    order: Mapped[int] = mapped_column(Integer(), autoincrement=True)
    guild_id: Mapped[str] = mapped_column(ForeignKey("guild.id"))
    guild: Mapped["Guild"] = relationship(back_populates="channels")
    channels: Mapped[list["Channel"]] = relationship(back_populates="channel_group")
