"""Operator entry point for a disposable, synthetic session check."""

import argparse
import sys

from .app import EXPORT
from .local import LocalAddress
from .server import bind_listener, make_server


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--local-check",
        required=True,
        action="store_true",
        help="start the controlled session-only fixture",
    )
    parser.add_argument(
        "--port", type=int, default=0, help="loopback port (0 selects a free port)"
    )
    args = parser.parse_args()
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        parser.exit(2, "An interactive local terminal is required.\n")
    if not (EXPORT / "index.html").is_file() or not (EXPORT / "_next/static").is_dir():
        parser.exit(2, "Build the local frontend before starting.\n")
    try:
        with bind_listener(args.port) as listener:
            origin = LocalAddress(listener.getsockname()[1]).origin

            def display(code: str):
                print(f"Open {origin}/\nOne-time terminal code: {code}", flush=True)

            server = make_server(listener, display)
            server.run(sockets=[listener])
            return 0 if server.started else 1
    except (ValueError, OSError):
        parser.exit(2, "Local listener unavailable.\n")


if __name__ == "__main__":
    raise SystemExit(main())
