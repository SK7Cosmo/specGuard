"""Validate the Codex usage ledger and generate deterministic Markdown and JSON reports."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "codex-evidence" / "models" / "MODEL_USAGE.csv"
DEFAULT_REGISTRY = ROOT / "codex-evidence" / "models" / "LIFECYCLE_REGISTRY.yaml"
DEFAULT_REPORT = ROOT / "codex-evidence" / "models" / "MODEL_REPORT.md"
DEFAULT_METRICS = ROOT / "codex-evidence" / "models" / "MODEL_METRICS.json"
REQUIRED_COLUMNS = {
    "date", "lifecycle_phase", "phase_id", "activity_type", "execution_mode", "record_origin",
    "task_id", "execution_id", "session_id", "model", "reasoning_effort", "completion_status",
    "escalation", "escalation_outcome", "duration_seconds", "input_tokens", "output_tokens",
    "resource_usage", "resource_usage_source",
}
LEDGER_COLUMNS = [
    "date", "lifecycle_phase", "phase_id", "activity_type", "execution_mode", "record_origin",
    "task_id", "execution_id", "session_id", "task_scope", "model", "reasoning_effort",
    "selection_rationale", "starting_git_commit", "completion_status", "escalation", "escalation_outcome",
    "validation_results", "duration_seconds", "input_tokens", "output_tokens", "resource_usage",
    "resource_usage_source", "notes",
]
STATUSES = {"complete", "partial", "blocked", "in_progress", "cancelled"}
MEASUREMENTS = ("duration_seconds", "input_tokens", "output_tokens", "resource_usage")


def available(value: str | None) -> bool:
    return bool(value and value.strip() and value.strip().casefold() not in {"n/a", "na", "unavailable"})


def load_registry(path: Path | str = DEFAULT_REGISTRY) -> dict:
    registry = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    phases = registry.get("phases", [])
    if len(phases) != 8:
        raise ValueError(f"Lifecycle registry must define exactly 8 phases; found {len(phases)}")
    expected_ids = [f"P{i:02}" for i in range(1, 9)]
    if [phase.get("phase_id") for phase in phases] != expected_ids:
        raise ValueError("Lifecycle phases must be ordered P01 through P08")
    expected = [
        ("understand", "Understand"), ("plan", "Plan"), ("design", "Design"), ("build", "Build"),
        ("test", "Test"), ("debug_improve", "Debug & Improve"), ("deploy", "Deploy"), ("automate", "Automate"),
    ]
    if [(p.get("lifecycle_phase"), p.get("display_name")) for p in phases] != expected:
        raise ValueError("Lifecycle registry phase values and display names must match the canonical eight-phase convention")
    names = [phase.get("lifecycle_phase") for phase in phases]
    if len(set(names)) != 8:
        raise ValueError("Lifecycle phase values must be unique")
    if len(registry.get("task_mappings", {})) != len(set(registry.get("task_mappings", {}))):
        raise ValueError("Duplicate task mappings")
    phase_by_id = {p["phase_id"]: p for p in phases}
    for task, phase_id in registry.get("task_mappings", {}).items():
        if phase_id not in phase_by_id:
            raise ValueError(f"Task mapping {task} references unknown phase ID {phase_id!r}")
    return registry


def normalize_records(csv_path: Path | str, registry_path: Path | str = DEFAULT_REGISTRY) -> list[dict[str, str]]:
    """Deterministically migrate legacy lifecycle labels and add structured metadata."""
    registry = load_registry(registry_path)
    phases = {p["phase_id"]: p for p in registry["phases"]}
    mappings = registry["task_mappings"]
    with Path(csv_path).open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Usage CSV has no header")
        rows = []
        for line_number, source in enumerate(reader, 2):
            if None in source or any(value is None for value in source.values()):
                raise ValueError(f"CSV row {line_number}: malformed field count")
            rows.append(dict(source))
    for row in rows:
        task = (row.get("task_id") or "").strip()
        if task not in mappings:
            raise ValueError(f"Task {task or '<missing>'}: no lifecycle mapping in registry")
        phase_id = mappings[task]
        row["phase_id"] = phase_id
        row["lifecycle_phase"] = phases[phase_id]["lifecycle_phase"]
        row["activity_type"] = classify_activity(task, row)
        row["execution_mode"] = classify_mode(row)
        row["record_origin"] = "retrospective" if "HIST-RETRO" in row.get("execution_id", "") else "contemporaneous"
    return rows


def migrate_csv(csv_path: Path | str = DEFAULT_CSV, registry_path: Path | str = DEFAULT_REGISTRY) -> None:
    """Rewrite a ledger in canonical field order; repeat runs produce identical bytes."""
    path = Path(csv_path)
    rows = normalize_records(path, registry_path)
    validate_records(rows, load_registry(registry_path))
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LEDGER_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def classify_activity(task: str, row: dict[str, str]) -> str:
    if task == "SG-00": return "initialization"
    if task == "SG-01": return "research"
    if task == "SG-00B": return "automation"
    if task == "SG-05A-META": return "metadata_maintenance"
    if task.startswith("SG-02"): return "specification"
    if task.startswith("SG-03"): return "review"
    if task.startswith("SG-04"): return "architecture"
    if task.startswith("SG-05"):
        return "testing" if task in {"SG-05J", "SG-05K"} else "implementation"
    return "unavailable"


def classify_mode(row: dict[str, str]) -> str:
    notes = (row.get("notes") or "").casefold()
    rationale = (row.get("selection_rationale") or "").casefold()
    for value in ("plan mode", "default mode", "agent mode"):
        if value in notes or value in rationale:
            return value.removesuffix(" mode")
    return "unavailable"


def validate_records(rows: list[dict[str, str]], registry: dict) -> None:
    phases = {p["phase_id"]: p for p in registry["phases"]}
    mappings = registry["task_mappings"]
    vocab = registry["vocabularies"]
    errors: list[str] = []
    seen: set[str] = set()
    required_ids = ("task_id", "execution_id", "lifecycle_phase", "phase_id", "activity_type", "execution_mode", "record_origin")
    for i, row in enumerate(rows, 2):
        label = f"row {i}"
        for key in required_ids:
            if not (row.get(key) or "").strip(): errors.append(f"{label}: required {key} is missing")
        task, execution = row.get("task_id", "").strip(), row.get("execution_id", "").strip()
        if execution:
            if execution in seen: errors.append(f"{label}: duplicate execution_id {execution!r}")
            seen.add(execution)
        phase_id, phase = row.get("phase_id", "").strip(), row.get("lifecycle_phase", "").strip()
        if phase not in {p["lifecycle_phase"] for p in registry["phases"]}:
            errors.append(f"{label}: unknown lifecycle_phase {phase!r}")
        if phase_id not in phases: errors.append(f"{label}: invalid phase_id {phase_id!r}")
        elif phases[phase_id]["lifecycle_phase"] != phase:
            errors.append(f"{label}: phase_id {phase_id} does not match lifecycle_phase {phase!r}")
        if task not in mappings: errors.append(f"{label}: task {task!r} is not registered")
        elif mappings[task] != phase_id: errors.append(f"{label}: task {task} maps to {mappings[task]}, not {phase_id}")
        for field in ("activity_type", "execution_mode", "record_origin"):
            if row.get(field) not in vocab[field]: errors.append(f"{label}: unsupported {field} {row.get(field)!r}")
        status = (row.get("completion_status") or "").strip().casefold()
        if status not in STATUSES: errors.append(f"{label}: invalid completion_status {status!r}")
        for field in MEASUREMENTS:
            value = row.get(field, "")
            if available(value):
                try: numeric = float(value)
                except (TypeError, ValueError):
                    errors.append(f"{label}: {field} must be a non-negative number or explicitly unavailable")
                    continue
                if not math.isfinite(numeric) or numeric < 0:
                    errors.append(f"{label}: {field} must be a finite non-negative number")
    if errors:
        raise ValueError("Usage ledger validation failed:\n- " + "\n- ".join(errors))


def read_ledger(csv_path: Path | str = DEFAULT_CSV, registry_path: Path | str = DEFAULT_REGISTRY) -> tuple[list[dict[str, str]], dict]:
    registry = load_registry(registry_path)
    with Path(csv_path).open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle, strict=True)
        headers = reader.fieldnames or []
        missing = REQUIRED_COLUMNS - set(headers)
        if missing: raise ValueError("CSV is missing required columns: " + ", ".join(sorted(missing)))
        rows = []
        for line_number, source in enumerate(reader, 2):
            if None in source or any(value is None for value in source.values()):
                raise ValueError(f"CSV row {line_number}: malformed field count")
            if all(not (value or "").strip() for value in source.values()):
                continue
            rows.append(dict(source))
    validate_records(rows, registry)
    return rows, registry


def number(value: str | None) -> float | None:
    if not available(value): return None
    parsed = float(value.strip())
    return parsed if math.isfinite(parsed) and parsed >= 0 else None


def _distribution(values: list[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items(), key=lambda pair: pair[0].casefold()))


def build_metrics(rows: list[dict[str, str]], registry: dict) -> dict:
    phases = registry["phases"]
    order = [p["lifecycle_phase"] for p in phases]
    phase_rows = {name: [r for r in rows if r["lifecycle_phase"] == name] for name in order}
    model_values = [(r.get("model") or "").strip() or "unavailable" for r in rows]
    effort_values = [(r.get("reasoning_effort") or "").strip() or "unavailable" for r in rows]
    def matrix(field: str) -> dict[str, dict[str, int]]:
        columns = sorted({(r.get(field) or "").strip() or "unavailable" for r in rows}, key=str.casefold)
        return {phase: {col: sum(1 for r in phase_rows[phase] if ((r.get(field) or "").strip() or "unavailable") == col) for col in columns}
                for phase in order}
    sessions = {r["session_id"].strip() for r in rows if available(r.get("session_id"))}
    resources = {}
    for field in MEASUREMENTS:
        present = [(r[field], r) for r in rows if number(r.get(field)) is not None]
        resources[field] = {"available_count": len(present), "missing_count": len(rows)-len(present),
                            "total": sum(number(v) for v, _ in present) if present else None,
                            "values": [number(v) for v, _ in present]}
    return {
        "scope": "Codex development model evidence; execution count is not token usage, cost, or computational consumption",
        "recorded_execution_count": len(rows), "distinct_task_count": len({r["task_id"] for r in rows}),
        "known_platform_session_count": len(sessions), "missing_session_id_count": sum(not available(r.get("session_id")) for r in rows),
        "lifecycle_progression_status": "unavailable: execution records do not establish milestone completion",
        "phases": [{"phase_id": p["phase_id"], "lifecycle_phase": p["lifecycle_phase"], "display_name": p["display_name"],
                    "recorded_execution_count": len(phase_rows[p["lifecycle_phase"]]), "progression_status": "unavailable"} for p in phases],
        "model_distribution": _distribution(model_values), "reasoning_effort_distribution": _distribution(effort_values),
        "phase_by_model": matrix("model"), "phase_by_reasoning_effort": matrix("reasoning_effort"),
        "activity_type_distribution": _distribution([r["activity_type"] for r in rows]),
        "execution_mode_distribution": _distribution([r["execution_mode"] for r in rows]),
        "completion_status_distribution": _distribution([r["completion_status"].casefold() for r in rows]),
        "escalation": {"known_count": sum(r.get("escalation", "").casefold() in {"yes", "true", "1", "no", "false", "0"} for r in rows),
                       "missing_count": sum(not available(r.get("escalation")) for r in rows),
                       "escalated_count": sum(r.get("escalation", "").casefold() in {"yes", "true", "1"} for r in rows),
                       "outcome_distribution": _distribution([r.get("escalation_outcome", "").strip() or "unavailable" for r in rows
                                                              if r.get("escalation", "").casefold() in {"yes", "true", "1"}])},
        "resources": resources,
        "timeline": [{"date": r["date"], "phase_id": r["phase_id"], "lifecycle_phase": r["lifecycle_phase"],
                      "task_id": r["task_id"], "execution_id": r["execution_id"], "session_id_known": available(r.get("session_id")),
                      "model": (r.get("model") or "").strip() or "unavailable", "reasoning_effort": (r.get("reasoning_effort") or "").strip() or "unavailable",
                      "activity_type": r["activity_type"], "execution_mode": r["execution_mode"],
                      "record_origin": r["record_origin"], "completion_status": r["completion_status"].casefold()}
                     for r in sorted(rows, key=lambda r: (r["date"], r["execution_id"]))],
        "retrospective_record_count": sum(r["record_origin"] == "retrospective" for r in rows),
        "contemporaneous_record_count": sum(r["record_origin"] == "contemporaneous" for r in rows),
        "metadata_completeness": {field: {"available_count": sum(available(r.get(field)) for r in rows),
                                          "missing_count": sum(not available(r.get(field)) for r in rows)}
                                  for field in ("phase_id", "activity_type", "record_origin", "session_id", "model", "reasoning_effort", "execution_mode", "completion_status", "duration_seconds", "input_tokens", "output_tokens", "resource_usage")},
    }


def build_report(metrics: dict) -> str:
    lines = ["# Codex development model usage report", "", "This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.",
             "Execution counts are record counts; they do not represent token usage, monetary cost, or computational consumption.", "",
             "## Recorded activity", "", "| Measure | Count |", "|---|---:|",
             f"| Recorded executions | {metrics['recorded_execution_count']} |", f"| Distinct tasks | {metrics['distinct_task_count']} |",
             f"| Known platform sessions | {metrics['known_platform_session_count']} |", f"| Missing session IDs | {metrics['missing_session_id_count']} |",
             f"| Retrospective records | {metrics['retrospective_record_count']} |", "",
             "Lifecycle progression status is unavailable from execution counts and is not inferred.", "",
             "## Lifecycle phases", "", "| Phase | ID | Recorded executions | Progression status |", "|---|---|---:|---|"]
    for p in metrics["phases"]: lines.append(f"| {p['display_name']} | {p['phase_id']} | {p['recorded_execution_count']} | unavailable |")
    sections = (("Model distribution", "model_distribution"), ("Reasoning effort distribution", "reasoning_effort_distribution"),
                ("Activity type distribution", "activity_type_distribution"), ("Execution mode distribution", "execution_mode_distribution"),
                ("Completion status distribution", "completion_status_distribution"))
    for title, key in sections:
        lines += ["", f"## {title}", "", "| Value | Count |", "|---|---:|"]
        for value, count in metrics[key].items(): lines.append(f"| {value} | {count} |")
    for title, key in (("Phase by model", "phase_by_model"), ("Phase by reasoning effort", "phase_by_reasoning_effort")):
        matrix = metrics[key]; columns = sorted({c for row in matrix.values() for c in row}, key=str.casefold)
        lines += ["", f"## {title}", "", "| Phase | " + " | ".join(columns) + " |", "|---|" + "---:|"*len(columns)]
        for phase, vals in matrix.items(): lines.append("| " + phase + " | " + " | ".join(str(vals.get(c, 0)) for c in columns) + " |")
    esc = metrics["escalation"]
    lines += ["", "## Escalations", "", f"Known escalation values: {esc['known_count']}; escalated: {esc['escalated_count']}; unavailable: {esc['missing_count']}.", "",
              "## Resource measurements", "", "| Measure | Available | Missing | Total |", "|---|---:|---:|---:|"]
    for field, values in metrics["resources"].items(): lines.append(f"| {field} | {values['available_count']} | {values['missing_count']} | {values['total'] if values['total'] is not None else 'N/A'} |")
    lines += ["", "## Timeline records", "", "Chronological execution records are available as structured entries in `MODEL_METRICS.json`; sensitive request content and raw notes are excluded.", ""]
    return "\n".join(lines)


def generate_report(csv_path: Path | str = DEFAULT_CSV, registry_path: Path | str = DEFAULT_REGISTRY) -> str:
    rows, registry = read_ledger(csv_path, registry_path)
    return build_report(build_metrics(rows, registry))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_METRICS)
    args = parser.parse_args()
    rows, registry = read_ledger(args.input, args.registry)
    metrics = build_metrics(rows, registry)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build_report(metrics), encoding="utf-8", newline="\n")
    args.json_output.write_text(json.dumps(metrics, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__": main()
