"""A single interactive possession grant scoped to one application lifespan."""

import hashlib
import hmac
import secrets
import time
from collections.abc import Callable

IDLE_SECONDS = 30 * 60
MAX_SECONDS = 8 * 60 * 60


def digest(proof: bytes) -> bytes:
    return hashlib.sha256(proof).digest()


class Session:
    """Transitions are synchronous on the single Uvicorn event loop."""

    def __init__(self, clock: Callable[[], float] = time.monotonic):
        self.clock = clock
        self.clear()

    def clear(self):
        self.bootstrap_digest: bytes | None = None
        self.session_digest: bytes | None = None
        self.issued = self.last_seen = 0.0

    def begin(self) -> str:
        self.clear()
        code = secrets.token_urlsafe(32)
        self.bootstrap_digest = digest(code.encode("ascii"))
        return code

    def exchange(self, proof: bytes) -> str | None:
        if self.bootstrap_digest is None or not hmac.compare_digest(
            self.bootstrap_digest, digest(proof)
        ):
            return None
        token = secrets.token_urlsafe(32)
        self.bootstrap_digest = None
        self.session_digest = digest(token.encode("ascii"))
        self.issued = self.last_seen = self.clock()
        return token

    def authorize(self, proof: bytes) -> bool:
        if self.session_digest is None:
            return False
        now = self.clock()
        if now - self.issued >= MAX_SECONDS or now - self.last_seen >= IDLE_SECONDS:
            self.clear()
            return False
        if not hmac.compare_digest(self.session_digest, digest(proof)):
            return False
        self.last_seen = now
        return True
