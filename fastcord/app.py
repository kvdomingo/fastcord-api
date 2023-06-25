from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from fastcord.routes import guild

app = FastAPI()
app.include_router(guild.router)


@app.get("/")
def health_check():
    return PlainTextResponse("ok")
