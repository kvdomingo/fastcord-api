from datetime import datetime

from sqlalchemy import ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, generate_uuid


class Emoji(Base):
    __tablename__ = "emoji"
    __table_args__ = (
        UniqueConstraint("name", "guild_id", name="unique_emoji_names_per_guild"),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid, index=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    name: Mapped[str] = mapped_column(String(16))
    source: Mapped[str] = mapped_column(String)
    guild_id: Mapped[str] = mapped_column(ForeignKey("guild.id"))
    guild: Mapped["Guild"] = relationship(back_populates="emojis")
