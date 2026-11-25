"""Configured origin of an already-bound IPv4 loopback socket."""

from dataclasses import dataclass

LOOPBACK = "127.0.0.1"


@dataclass(frozen=True)
class LocalAddress:
    port: int

    def __post_init__(self):
        if type(self.port) is not int or not 1 <= self.port <= 65535:
            raise ValueError("Invalid local service port")

    @property
    def authority(self) -> str:
        return f"{LOOPBACK}:{self.port}"

    @property
    def origin(self) -> str:
        return f"http://{self.authority}"
