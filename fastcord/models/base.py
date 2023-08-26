from uuid import uuid4

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


def generate_uuid():
    return str(uuid4())
