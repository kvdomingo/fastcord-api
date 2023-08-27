from fastapi import APIRouter
from sqlalchemy import text

from fastcord.db import engine
from fastcord.schemas import Channel

router = APIRouter(prefix="/channel")


@router.get("")
async def list_channels() -> list[Channel]:
    async with engine.connect() as conn:
        cursor = await conn.execute(text('SELECT * FROM "channel"'))
        results = [Channel(**row) for row in cursor.mappings()]
    return results
