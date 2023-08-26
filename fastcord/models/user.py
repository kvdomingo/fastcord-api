from datetime import datetime
from enum import Enum
from random import randint
from typing import Optional, Self

from sqlalchemy import Column, ForeignKey, Integer, String, Table, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .base import Base, generate_uuid


def generate_discriminator():
    return randint(0, 9999)


class AvailabilityStatus(Enum):
    ONLINE = "ONLINE"
    DO_NOT_DISTURB = "DO_NOT_DISTURB"
    IDLE = "IDLE"
    OFFLINE = "OFFLINE"


friendship_association_table = Table(
    "friendship_association_table",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("friend_id", ForeignKey("user.id"), primary_key=True),
    UniqueConstraint("user_id", "friend_id", name="unique_friendship"),
)


class User(Base):
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint(
            "username", "discriminator", name="unique_username_discriminator"
        ),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=generate_uuid, index=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now(), index=True)
    name: Mapped[Optional[str]] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(256), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(32))
    discriminator: Mapped[int] = mapped_column(
        Integer, nullable=False, default=generate_discriminator
    )
    avatar: Mapped[Optional[str]] = mapped_column(String)
    friends: Mapped[list[Self]] = relationship(
        "User",
        secondary=friendship_association_table,
        primaryjoin=id == friendship_association_table.c.user_id,
        secondaryjoin=id == friendship_association_table.c.friend_id,
    )
    messages: Mapped[list["Message"]] = relationship(back_populates="author")
    availability_status: Mapped[AvailabilityStatus] = mapped_column(
        default=AvailabilityStatus.OFFLINE
    )
    status_message: Mapped[Optional[str]] = mapped_column(String(32))
    status_emoji_id: Mapped[Optional[str]] = mapped_column(ForeignKey("emoji.id"))

    def __repr__(self):
        return f"User <{str(self)}>"

    def __str__(self):
        return f"{self.username}#{self.discriminator:04}"
