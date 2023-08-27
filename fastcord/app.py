from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from fastcord.routes import channel, guild

app = FastAPI(title="Fastcord API")
app.include_router(guild.router)
app.include_router(channel.router)


@app.get("/")
def health_check():
    return PlainTextResponse("ok")
