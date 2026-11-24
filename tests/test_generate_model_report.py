import csv
import tempfile
import unittest
from pathlib import Path

from scripts.generate_model_report import generate_report


FIELDS = [
    "date", "lifecycle_phase", "task_id", "execution_id", "session_id",
    "task_scope", "model", "reasoning_effort", "selection_rationale",
    "starting_git_commit", "completion_status", "escalation",
    "escalation_outcome", "validation_results", "duration_seconds",
    "input_tokens", "output_tokens", "resource_usage", "resource_usage_source",
    "notes",
]


def row(**overrides):
    result = {field: "N/A" for field in FIELDS}
    result.update({"date": "2026-11-24", "lifecycle_phase": "verify",
                   "task_id": "SG-T", "execution_id": "SG-T-01",
                   "session_id": "S-1", "model": "GPT-6 Luna Medium",
                   "reasoning_effort": "Medium", "completion_status": "complete",
                   "escalation": "no", "duration_seconds": "12",
                   "input_tokens": "100", "output_tokens": "25"})
    result.update(overrides)
    return result


class ModelReportTests(unittest.TestCase):
    def render(self, records, malformed_line=None):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        path = Path(temp.name) / "usage.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(records)
            if malformed_line:
                handle.write(malformed_line + "\n")
        return generate_report(path)

    def test_empty_csv(self):
        report = self.render([])
        self.assertIn("Task executions | 0", report)
        self.assertIn("No valid usage records", report)

    def test_valid_single_model_record(self):
        report = self.render([row()])
        self.assertIn("Task executions | 1", report)
        self.assertIn("GPT-6 Luna Medium", report)
        self.assertIn("verify", report)

    def test_multiple_models_within_one_session(self):
        report = self.render([row(), row(execution_id="SG-T-02", model="GPT-6.2 Sol High")])
        self.assertIn("Sessions with available ID | 1", report)
        self.assertIn("GPT-6.2 Sol High", report)
        self.assertIn("Task executions | 2", report)

    def test_missing_optional_measurements(self):
        report = self.render([row(duration_seconds="N/A", input_tokens="", output_tokens="N/A")])
        self.assertIn("Missing duration measurements: **1**", report)
        self.assertIn("missing token measurements: **2**", report)
        self.assertIn("| Duration (seconds) | 0 | N/A | N/A | 1 |", report)

    def test_malformed_records_are_reported_and_skipped(self):
        report = self.render([row()], malformed_line="too,few,columns")
        self.assertIn("Malformed or duplicate rows | 1", report)
        self.assertIn("Task executions | 1", report)

    def test_duplicate_execution_identifiers_are_skipped(self):
        report = self.render([row(), row(model="GPT-6.2 Sol High")])
        self.assertIn("Malformed or duplicate rows | 1", report)
        self.assertIn("Task executions | 1", report)
        self.assertNotIn("GPT-6.2 Sol High", report)

    def test_aggregation_by_model_and_lifecycle_phase(self):
        report = self.render([
            row(),
            row(execution_id="SG-T-02", model="GPT-6.2 Sol High", lifecycle_phase="implement"),
            row(execution_id="SG-T-03", lifecycle_phase="implement", session_id="S-2"),
        ])
        self.assertIn("| verify | 1 |", report)
        self.assertIn("| implement | 2 |", report)
        self.assertIn("| GPT-6 Luna Medium | 2 |", report)

    def test_repeatable_report_generation(self):
        records = [row(), row(execution_id="SG-T-02", model="GPT-6.2 Sol High")]
        self.assertEqual(self.render(records), self.render(records))

    def test_escalation_statistics(self):
        report = self.render([row(escalation="yes", escalation_outcome="resolved")])
        self.assertIn("Escalations among known values | 1 / 1", report)
        self.assertIn("| Escalation outcome: resolved | 1 |", report)

    def test_unavailable_escalation_is_not_counted_as_no(self):
        report = self.render([row(escalation="N/A")])
        self.assertIn("Escalations among known values | 0 / 0", report)
        self.assertIn("Records missing escalation value | 1", report)


if __name__ == "__main__":
    unittest.main()
