import os
import urllib.parse

from dotenv import load_dotenv
from redis import Redis

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

PRODUCTION = os.environ.get("PYTHON_ENV", "production") == "production"


# Redis configuration

REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")


# Session configuration

SESSION_CONFIG = {
    "SESSION_COOKIE_NAME": "sessionid",
    "SESSION_COOKIE_PATH": "/",
    "SESSION_COOKIE_HTTPONLY": True,
    "SESSION_COOKIE_SECURE": PRODUCTION,
    "SESSION_TYPE": "redis",
    "SESSION_REDIS": Redis(host="redis", password=REDIS_PASSWORD, port=6379),
    "SESSION_USE_SIGNER": True,
}


# Discord configuration

DISCORD_CLIENT_ID = os.environ.get("DISCORD_CLIENT_ID")

DISCORD_CLIENT_SECRET = os.environ.get("DISCORD_CLIENT_SECRET")

DISCORD_API_ENDPOINT = urllib.parse.urlparse("https://discord.com/api/v10")

DISCORD_AUTH_ENDPOINT = urllib.parse.urlparse("https://discord.com/oauth2/authorize")

DISCORD_OAUTH_SCOPES = [
    "identify",
    "email",
    "connections",
    "guilds",
    "guilds.join",
    "guilds.members.read",
    "messages.read",
    "rpc",
    "rpc.notifications.read",
    "rpc.voice.read",
    "rpc.voice.write",
    "rpc.activities.write",
]
