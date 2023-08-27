import asyncio

import yaml
from sqlalchemy import text

from fastcord.db import engine
from fastcord.settings import get_settings

settings = get_settings()


async def main():
    with open(settings.BASE_DIR / "fixtures" / "test-data.yml", "r") as f:
        fixtures = yaml.safe_load(f)

    async with engine.connect() as conn:
        for fixture in fixtures:
            fields = dict(id=fixture["id"], **fixture["fields"])
            columns = ", ".join(map(lambda k: f'"{k}"', fields.keys()))
            values = ", ".join(map(lambda v: f"'{v}'", fields.values()))
            await conn.execute(
                text(
                    f'INSERT INTO "{fixture["table"]}" ({columns}) VALUES ({values}) ON CONFLICT (id) DO NOTHING'
                )
            )
        await conn.commit()


if __name__ == "__main__":
    asyncio.run(main())
