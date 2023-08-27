from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware

from fastcord.routes import guild
from fastcord.settings import get_settings

settings = get_settings()

app = FastAPI(title="Fastcord API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(guild.router)


@app.get("/")
def health_check():
    return PlainTextResponse("ok")
