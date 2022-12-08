import urllib.parse
from hashlib import sha256
from http import HTTPStatus

import requests
from flask import Flask, Response, jsonify, redirect, request, session
from flask_session import Session
from loguru import logger

from .config import (
    DISCORD_API_ENDPOINT,
    DISCORD_AUTH_ENDPOINT,
    DISCORD_CLIENT_ID,
    DISCORD_CLIENT_SECRET,
    DISCORD_OAUTH_SCOPES,
    PRODUCTION,
    SECRET_KEY,
    SESSION_CONFIG,
)

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config.from_mapping(SESSION_CONFIG)
Session(app)


@app.route("/")
def index():
    return Response("ok")


@app.route("/auth")
def auth():
    state = sha256(session.sid.encode()).hexdigest()
    params = {
        "client_id": DISCORD_CLIENT_ID,
        "redirect_uri": "http://fastcord.localhost/callback",
        "response_type": "code",
        "scope": " ".join(DISCORD_OAUTH_SCOPES),
        "state": state,
    }
    pr = DISCORD_AUTH_ENDPOINT
    pr = pr._replace(query="&".join([f"{k}={urllib.parse.quote(v, safe='')}" for k, v in params.items()]))
    session.update(dict(state=state))
    return redirect(pr.geturl())


@app.route("/callback")
def callback():
    local_state = session.get("state")
    returned_state = request.args.get("state")
    if local_state != returned_state:
        res = jsonify({"error": "state mismatch"})
        res.status = HTTPStatus.UNAUTHORIZED
        return res
    if request.args.get("error"):
        res = jsonify({"error": urllib.parse.unquote(request.args.get("error_description"))})
        res.status = HTTPStatus.UNAUTHORIZED
        return res
    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": request.args.get("code"),
        "redirect_uri": "http://fastcord.localhost/callback",
    }
    pr = DISCORD_API_ENDPOINT
    pr = pr._replace(path=f"{pr.path}/oauth2/token")
    res = requests.post(
        pr.geturl(),
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    if not res.ok:
        logger.error(res.text)
        res.raise_for_status()
    data = res.json()
    res = jsonify(data)
    res.set_cookie(
        "access",
        data["access_token"],
        secure=PRODUCTION,
        httponly=True,
        path="/",
        samesite="Strict",
        max_age=data["expires_in"],
    )
    res.set_cookie(
        "refresh",
        data["refresh_token"],
        secure=PRODUCTION,
        httponly=True,
        path="/refresh",
        samesite="Strict",
    )
    return res


@app.route("/refresh")
def refresh():
    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": request.cookies.get("refresh"),
    }
    pr = DISCORD_API_ENDPOINT
    pr = pr._replace(path=f"{pr.path}/oauth2/token")
    res = requests.post(
        pr.geturl(),
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    if not res.ok:
        logger.error(res.text)
        res.raise_for_status()
    data = res.json()
    res = jsonify(data)
    res.set_cookie(
        "access",
        data["access_token"],
        secure=PRODUCTION,
        httponly=True,
        path="/",
        samesite="Strict",
        max_age=data["expires_in"],
    )
    res.set_cookie(
        "refresh",
        data["refresh_token"],
        secure=PRODUCTION,
        httponly=True,
        path="/refresh",
        samesite="Strict",
    )
    return res
