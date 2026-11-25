"""Migration for an explicitly designated, local, synthetic development database."""

import sqlite3

APPLICATION_ID = 0x53474744  # SGGD
SCHEMA_VERSION = 1


def _inspect(connection: sqlite3.Connection) -> int:
    (app_id,) = connection.execute("PRAGMA application_id").fetchone()
    (version,) = connection.execute("PRAGMA user_version").fetchone()
    occupied = connection.execute("SELECT 1 FROM sqlite_schema LIMIT 1").fetchone()
    if occupied or (app_id, version) not in ((0, 0), (APPLICATION_ID, SCHEMA_VERSION)):
        raise ValueError("Unrecognized foundation schema")
    return version


def migrate(connection: sqlite3.Connection) -> None:
    """Claim an empty database or reopen v1. Runtime session state is memory-only."""
    if connection.in_transaction:
        raise ValueError("Migration requires its own transaction")
    _inspect(connection)
    connection.execute("PRAGMA foreign_keys=ON")
    (mode,) = connection.execute("PRAGMA journal_mode=WAL").fetchone()
    if mode != "wal":
        raise ValueError("Migration requires a file-backed WAL database")
    connection.execute("BEGIN IMMEDIATE")
    try:
        if _inspect(connection) == 0:
            connection.execute(f"PRAGMA application_id={APPLICATION_ID}")
            connection.execute(f"PRAGMA user_version={SCHEMA_VERSION}")
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
