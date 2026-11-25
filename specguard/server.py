"""One loopback socket, one lifespan, and a fixed diagnostic boundary."""

import socket
import time
from collections.abc import Callable

import uvicorn

from .app import create_app
from .local import LOOPBACK, LocalAddress


def bind_listener(port: int) -> socket.socket:
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError("Invalid local listener port")
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if hasattr(socket, "SO_EXCLUSIVEADDRUSE"):
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        listener.bind((LOOPBACK, port))
        return listener
    except BaseException:
        listener.close()
        raise


def make_server(
    listener: socket.socket,
    issue_code: Callable[[str], None],
    *,
    clock: Callable[[], float] = time.monotonic,
) -> uvicorn.Server:
    host, port = listener.getsockname()
    if host != LOOPBACK:
        raise ValueError("A loopback listener is required")
    app = create_app(LocalAddress(port), issue_code, clock=clock)
    # Protocol exceptions may include request bytes. Suppress transport and access
    # logs at their source, including tracebacks and malformed-request warnings.
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {"discard": {"class": "logging.NullHandler"}},
        "loggers": {
            name: {"handlers": ["discard"], "propagate": False}
            for name in ("uvicorn", "uvicorn.access", "uvicorn.error", "uvicorn.asgi")
        },
    }
    return uvicorn.Server(
        uvicorn.Config(
            app,
            host=host,
            port=port,
            http="h11",
            ws="none",
            proxy_headers=False,
            server_header=False,
            access_log=False,
            log_config=log_config,
            lifespan="on",
        )
    )
