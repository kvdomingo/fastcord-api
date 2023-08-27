from fastapi import APIRouter
from pydantic import UUID4
from sqlalchemy import text

from fastcord.db import engine
from fastcord.schemas import ChannelGroup

router = APIRouter(prefix="/{guild_id}/channel-group")


@router.get("")
async def list_channel_groups(guild_id: UUID4) -> list[ChannelGroup]:
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text(
                'SELECT * FROM "channel_group" WHERE "guild_id" = :guild_id ORDER BY "order"'
            ),
            {"guild_id": str(guild_id)},
        )
        results = [ChannelGroup(**row) for row in cursor.mappings()]
    return results
