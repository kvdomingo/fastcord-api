from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Response
from pydantic import UUID4
from sqlalchemy import text

from fastcord.db import engine
from fastcord.schemas import Guild

router = APIRouter(prefix="/guild")


@router.get("")
async def list_guilds() -> list[Guild]:
    async with engine.connect() as conn:
        cursor = await conn.execute(text('SELECT * FROM "guild"'))
        results = [Guild(**row) for row in cursor.mappings()]
    return results


@router.get("/{id}")
async def get_guild(id: UUID4) -> Guild:
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text('SELECT * FROM "guild" WHERE "id" = :id'),
            {"id": str(id)},
        )
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=f"Guild with id {id} not found"
            )
        result = Guild(**row._asdict())
    return result


@router.post("")
async def create_guild(guild: Guild) -> Guild:
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text(
                """
                INSERT INTO "guild" ("name", "avatar", "banner")
                VALUES (:name, :avatar, :banner)
                RETURNING *
                """
            ),
            {**guild.model_dump(), "id": str(id)},
        )
        row = cursor.fetchone()
        result = Guild(**row._asdict())
    return result


@router.put("/{id}")
async def update_guild(id: UUID4, guild: Guild) -> Guild:
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text(
                """
                UPDATE "guild"
                SET "name" = :name,
                    "avatar" = :avatar,
                    "banner" = :banner
                WHERE "id" = :id
                RETURNING *
                """
            ),
            {**guild.model_dump(), "id": str(id)},
        )
        row = cursor.fetchone()
        result = Guild(**row._asdict())
    return result


@router.delete("/{id}")
async def delete_guild(id: UUID4):
    async with engine.connect() as conn:
        cursor = await conn.execute(
            text('DELETE FROM "guild" WHERE "id" = :id RETURNING "id"'),
            {"id": str(id)},
        )
        id = cursor.fetchone()
        if id is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail=f"Guild with id {id} not found"
            )
    return Response(status_code=HTTPStatus.NO_CONTENT)
