"""FastAPI shell for the operator's controlled local session check."""

import time
from collections.abc import Callable
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from starlette.datastructures import Headers, MutableHeaders
from starlette.responses import FileResponse, JSONResponse, Response
from starlette.staticfiles import StaticFiles
from starlette.types import ASGIApp, Receive, Scope, Send

from .local import LOOPBACK, LocalAddress
from .session import Session

SESSION_PATH = "/api/v1/session"
EXPORT = Path(__file__).resolve().parents[1] / "frontend" / "out"
SAFE_HEADERS = {
    "Cache-Control": "no-store",
    "Referrer-Policy": "no-referrer",
    "X-Content-Type-Options": "nosniff",
    "Cross-Origin-Resource-Policy": "same-origin",
    "Content-Security-Policy": "default-src 'none'; script-src 'self'; style-src 'self'; "
    "connect-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'none'",
}


def denied() -> Response:
    return JSONResponse({"error": "access_denied"}, status_code=403)


def cookie_proof(headers: Headers, name: str) -> bytes:
    cookies = headers.getlist("cookie")
    if len(cookies) != 1:
        return b""
    values = []
    for pair in cookies[0].split(";"):
        key, sep, value = pair.strip().partition("=")
        if key == name and sep:
            values.append(value)
    return values[0].encode("latin-1") if len(values) == 1 else b""


class LocalBoundary:
    def __init__(self, app: ASGIApp, address: LocalAddress):
        self.app = app
        self.address = address

    def permits(self, scope: Scope) -> bool:
        method, path = scope["method"], scope["path"]
        headers = Headers(scope=scope)
        origin = headers.getlist("origin")
        peer = scope.get("client")
        if (
            not peer
            or peer[0] != LOOPBACK
            or scope.get("scheme") != "http"
            or tuple(scope.get("server") or ()) != (LOOPBACK, self.address.port)
            or headers.getlist("host") != [self.address.authority]
        ):
            return False
        if origin != [self.address.origin] and (
            origin or method not in ("GET", "HEAD")
        ):
            return False
        if "transfer-encoding" in headers or headers.getlist("content-length") not in (
            [],
            ["0"],
        ):
            return False
        if path == SESSION_PATH:
            return method in ("GET", "POST", "DELETE") and not scope["query_string"]
        return method in ("GET", "HEAD") and (
            path == "/" or path.startswith("/_next/static/")
        )

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        async def send_safe(message):
            if message["type"] == "http.response.start":
                MutableHeaders(scope=message).update(SAFE_HEADERS)
            await send(message)

        if not self.permits(scope):
            await denied()(scope, receive, send_safe)
            return
        await self.app(scope, receive, send_safe)


def create_app(
    address: LocalAddress,
    issue_code: Callable[[str], None],
    *,
    clock: Callable[[], float] = time.monotonic,
) -> FastAPI:
    session = Session(clock)
    cookie_name = f"sg_session_{address.port}"

    @asynccontextmanager
    async def lifespan(app):
        try:
            issue_code(session.begin())
            yield
        finally:
            session.clear()

    app = FastAPI(
        lifespan=lifespan,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        redirect_slashes=False,
    )
    app.add_middleware(LocalBoundary, address=address)

    @app.post(SESSION_PATH)
    async def bootstrap(request: Request):
        codes = request.headers.getlist("x-specguard-bootstrap")
        token = (
            session.exchange(codes[0].encode("latin-1")) if len(codes) == 1 else None
        )
        if token is None:
            return denied()
        response = Response(status_code=204)
        response.set_cookie(
            cookie_name, token, httponly=True, samesite="strict", path="/"
        )
        return response

    @app.get(SESSION_PATH)
    async def status(request: Request):
        if not session.authorize(cookie_proof(request.headers, cookie_name)):
            return denied()
        return {"session": "active"}

    @app.delete(SESSION_PATH)
    async def revoke(request: Request):
        if not session.authorize(cookie_proof(request.headers, cookie_name)):
            return denied()
        session.clear()
        response = Response(status_code=204)
        response.delete_cookie(cookie_name, httponly=True, samesite="strict", path="/")
        return response

    @app.api_route("/", methods=["GET", "HEAD"])
    async def index():
        if not (EXPORT / "index.html").is_file():
            return JSONResponse({"error": "ui_unavailable"}, status_code=503)
        return FileResponse(EXPORT / "index.html")

    assets = EXPORT / "_next" / "static"
    if assets.is_dir():
        app.mount("/_next/static", StaticFiles(directory=assets))
    return app
