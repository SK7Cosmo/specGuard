import csv
import json
import tempfile
import unittest
from pathlib import Path

from scripts.generate_model_report import (
    LEDGER_COLUMNS, build_metrics, generate_report, load_registry, migrate_csv,
    normalize_records, read_ledger, validate_records,
)


def row(**overrides):
    result = {field: "N/A" for field in LEDGER_COLUMNS}
    result.update({"date": "2026-11-24", "lifecycle_phase": "build", "phase_id": "P04",
                   "activity_type": "implementation", "execution_mode": "default",
                   "record_origin": "contemporaneous", "task_id": "SG-05A",
                   "execution_id": "SG-05A-01", "session_id": "S-1",
                   "model": "GPT-6 Luna", "reasoning_effort": "Medium",
                   "completion_status": "complete", "escalation": "no",
                   "duration_seconds": "N/A", "input_tokens": "N/A", "output_tokens": "N/A",
                   "resource_usage": "N/A"})
    result.update(overrides)
    return result


class ModelReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.registry_path = Path(__file__).resolve().parents[1] / "codex-evidence/models/LIFECYCLE_REGISTRY.yaml"
        self.registry = load_registry(self.registry_path)

    def csv_file(self, records, columns=LEDGER_COLUMNS):
        path = self.root / "usage.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            writer.writerows(records)
        return path

    def test_all_eight_phases_in_canonical_order_including_zeroes(self):
        records = [row()]
        metrics = build_metrics(records, self.registry)
        self.assertEqual([p["phase_id"] for p in metrics["phases"]], [f"P{i:02}" for i in range(1, 9)])
        self.assertEqual([p["recorded_execution_count"] for p in metrics["phases"]], [0, 0, 0, 1, 0, 0, 0, 0])

    def test_historical_phase_normalization_preserves_facts_and_is_idempotent(self):
        legacy = {key: "N/A" for key in ("date", "lifecycle_phase", "task_id", "execution_id", "session_id", "task_scope", "model", "reasoning_effort", "selection_rationale", "starting_git_commit", "completion_status", "escalation", "escalation_outcome", "validation_results", "duration_seconds", "input_tokens", "output_tokens", "resource_usage", "resource_usage_source", "notes")}
        legacy.update(date="2026-11-24", lifecycle_phase="review", task_id="SG-03A", execution_id="E1", session_id="N/A", model="GPT-6 Luna", reasoning_effort="High", completion_status="complete", notes="Plan mode. Keep exact evidence.")
        path = self.csv_file([legacy], list(legacy))
        original = normalize_records(path, self.registry_path)[0]
        self.assertEqual((original["phase_id"], original["lifecycle_phase"]), ("P02", "plan"))
        self.assertEqual((original["model"], original["reasoning_effort"], original["notes"]), ("GPT-6 Luna", "High", "Plan mode. Keep exact evidence."))
        migrate_csv(path, self.registry_path)
        once = path.read_bytes()
        migrate_csv(path, self.registry_path)
        self.assertEqual(path.read_bytes(), once)

    def test_invalid_phase_and_phase_id_rejected(self):
        for changes in ({"lifecycle_phase": "other"}, {"phase_id": "P03"}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "row 2"):
                validate_records([row(**changes)], self.registry)

    def test_task_phase_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "task SG-05A maps to P04"):
            validate_records([row(lifecycle_phase="plan", phase_id="P02")], self.registry)

    def test_duplicate_execution_id_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate execution_id"):
            validate_records([row(), row(execution_id="SG-05A-01")], self.registry)

    def test_multiple_executions_for_one_task_count_once_as_task(self):
        records = [row(), row(execution_id="SG-05A-02", session_id="S-2")]
        self.assertEqual(build_metrics(records, self.registry)["recorded_execution_count"], 2)
        self.assertEqual(build_metrics(records, self.registry)["distinct_task_count"], 1)

    def test_missing_sessions_and_retrospective_records_are_separate_metadata(self):
        metrics = build_metrics([row(session_id="N/A", record_origin="retrospective")], self.registry)
        self.assertEqual(metrics["known_platform_session_count"], 0)
        self.assertEqual(metrics["missing_session_id_count"], 1)
        self.assertEqual(metrics["retrospective_record_count"], 1)

    def test_unavailable_model_effort_and_measurements_are_valid_and_counted(self):
        metrics = build_metrics([row(model="unavailable", reasoning_effort="unavailable")], self.registry)
        self.assertEqual(metrics["model_distribution"], {"unavailable": 1})
        self.assertEqual(metrics["resources"]["input_tokens"]["missing_count"], 1)

    def test_unrecognized_model_and_effort_are_retained_without_guessing(self):
        record = row(model="Future Model X", reasoning_effort="extreme")
        validate_records([record], self.registry)
        metrics = build_metrics([record], self.registry)
        self.assertEqual(metrics["model_distribution"], {"Future Model X": 1})
        self.assertEqual(metrics["reasoning_effort_distribution"], {"extreme": 1})

    def test_metadata_completeness_and_escalation_outcomes_are_structured(self):
        metrics = build_metrics([row(escalation="yes", escalation_outcome="approved")], self.registry)
        self.assertEqual(metrics["escalation"]["outcome_distribution"], {"approved": 1})
        self.assertEqual(metrics["metadata_completeness"]["activity_type"], {"available_count": 1, "missing_count": 0})

    def test_invalid_vocab_status_measurement_and_identifiers_rejected(self):
        cases = [
            (row(activity_type="guess"), "unsupported activity_type"),
            (row(execution_mode="random"), "unsupported execution_mode"),
            (row(completion_status="done"), "invalid completion_status"),
            (row(duration_seconds="-1"), "finite non-negative"),
            (row(input_tokens="many"), "must be a non-negative number"),
            (row(execution_id=""), "required execution_id"),
        ]
        for record, message in cases:
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                validate_records([record], self.registry)

    def test_deterministic_json_and_phase_order(self):
        records = [row(), row(execution_id="SG-05A-02", activity_type="testing")]
        first = json.dumps(build_metrics(records, self.registry), sort_keys=True, indent=2)
        second = json.dumps(build_metrics(records, self.registry), sort_keys=True, indent=2)
        self.assertEqual(first, second)

    def test_malformed_csv_row_is_rejected(self):
        path = self.csv_file([row()])
        with path.open("a", encoding="utf-8") as handle:
            handle.write("too,few,fields\n")
        with self.assertRaisesRegex(ValueError, "malformed field count"):
            read_ledger(path, self.registry_path)
        with self.assertRaisesRegex(ValueError, "malformed field count"):
            migrate_csv(path, self.registry_path)

    def test_report_distinguishes_executions_tasks_sessions_and_excludes_notes(self):
        records = [row(notes="private request", session_id="S-1"), row(execution_id="E2", session_id="S-1")]
        path = self.csv_file(records)
        report = generate_report(path, self.registry_path)
        self.assertIn("Recorded executions | 2", report)
        self.assertIn("Distinct tasks | 1", report)
        self.assertIn("Known platform sessions | 1", report)
        self.assertNotIn("private request", report)


if __name__ == "__main__":
    unittest.main()
