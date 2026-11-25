"""Identity shared by baseline-scoped workflow records (SG-04A §17)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class RevisionRef:
    audit_id: str
    baseline_id: str
    object_id: str
    revision: int

    def __post_init__(self):
        for value in (self.audit_id, self.baseline_id, self.object_id):
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Incomplete scoped object identity")
        if type(self.revision) is not int or self.revision < 1:
            raise ValueError("Invalid semantic revision")
