from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Emoji(BaseModel):
    __tablename__ = "emoji"
    __table_args__ = (
        UniqueConstraint("name", "guild_id", name="unique_emoji_names_per_guild"),
    )

    name: Mapped[str] = mapped_column(String(16))
    source: Mapped[str] = mapped_column(String)
    guild_id: Mapped[str] = mapped_column(ForeignKey("guild.id"))
    guild: Mapped["Guild"] = relationship(back_populates="emojis")
