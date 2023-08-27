from fastapi import APIRouter
from pydantic import UUID4
from sqlalchemy import text

from fastcord.db import engine
from fastcord.schemas import Channel

router = APIRouter(prefix="/{guild_id}/channel")


@router.get("")
async def list_channels(guild_id: UUID4) -> list[Channel]:
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text(
                'SELECT * FROM "channel" WHERE "guild_id" = :guild_id ORDER BY "order"'
            ),
            {"guild_id": str(guild_id)},
        )
        results = [Channel(**row) for row in cursor.mappings()]
    return results
