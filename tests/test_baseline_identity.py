"""SG-04A §17 scopes identity by audit, baseline, object and revision."""

import unittest
from dataclasses import FrozenInstanceError

from specguard.domain import RevisionRef


class IdentityTests(unittest.TestCase):
    def test_reference_is_immutable_and_scoped(self):
        ref = RevisionRef("audit", "base", "obj", 1)
        self.assertEqual(ref, RevisionRef("audit", "base", "obj", 1))
        for other in [
            ("other", "base", "obj", 1),
            ("audit", "next", "obj", 1),
            ("audit", "base", "other", 1),
            ("audit", "base", "obj", 2),
        ]:
            self.assertNotEqual(ref, RevisionRef(*other))
        with self.assertRaises(FrozenInstanceError):
            ref.revision = 2

    def test_incomplete_identity_is_rejected(self):
        for incomplete in [
            ("", "base", "obj", 1),
            ("audit", "", "obj", 1),
            ("audit", "base", " ", 1),
            ("audit", "base", "obj", None),
        ]:
            with self.assertRaises(ValueError):
                RevisionRef(*incomplete)
