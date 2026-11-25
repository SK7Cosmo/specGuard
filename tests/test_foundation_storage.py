"""D11 migration-only oracle. Each database is an isolated synthetic fixture."""

import sqlite3
import tempfile
import unittest
from pathlib import Path

from specguard.storage import migrate


class MigrationTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "foundation.sqlite3"

    def connect(self):
        connection = sqlite3.connect(self.path)
        self.addCleanup(connection.close)
        return connection

    def test_empty_reopen_and_repeat(self):
        db = self.connect()
        migrate(db)
        self.assertEqual(db.execute("PRAGMA foreign_keys").fetchone(), (1,))
        self.assertEqual(db.execute("PRAGMA journal_mode").fetchone(), ("wal",))
        migrate(db)
        db.close()
        reopened = self.connect()
        migrate(reopened)
        self.assertEqual(reopened.execute("PRAGMA user_version").fetchone(), (1,))
        self.assertEqual(
            reopened.execute(
                "SELECT name FROM sqlite_schema WHERE type='table'"
            ).fetchall(),
            [],
        )
        self.assertNotEqual(reopened.execute("PRAGMA application_id").fetchone(), (0,))

    def test_unknown_database_and_future_schema_preserved(self):
        db = self.connect()
        db.execute("CREATE TABLE unrelated (id INTEGER PRIMARY KEY)")
        with self.assertRaises(ValueError):
            migrate(db)
        self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (0,))
        self.assertEqual(db.execute("PRAGMA journal_mode").fetchone(), ("delete",))
        db.execute("DROP TABLE unrelated")
        migrate(db)
        db.execute("PRAGMA user_version=2")
        with self.assertRaises(ValueError):
            migrate(db)
        self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (2,))

    def test_version_write_failure_rolls_back_and_retry_succeeds(self):
        db = self.connect()

        def deny_version(action, key, value, *_):
            if (
                action == sqlite3.SQLITE_PRAGMA
                and key == "user_version"
                and value is not None
            ):
                return sqlite3.SQLITE_DENY
            return sqlite3.SQLITE_OK

        db.set_authorizer(deny_version)
        with self.assertRaises(sqlite3.DatabaseError):
            migrate(db)
        self.assertFalse(db.in_transaction)
        self.assertEqual(db.execute("PRAGMA application_id").fetchone(), (0,))
        self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (0,))
        db.set_authorizer(None)
        migrate(db)
        self.assertEqual(db.execute("PRAGMA user_version").fetchone(), (1,))
