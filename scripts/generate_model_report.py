"""Generate a deterministic Markdown summary of Codex development model usage."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "codex-evidence" / "models" / "MODEL_USAGE.csv"
DEFAULT_REPORT = ROOT / "codex-evidence" / "models" / "MODEL_REPORT.md"
REQUIRED_COLUMNS = {"lifecycle_phase", "task_id", "execution_id", "session_id", "model",
                    "reasoning_effort", "completion_status", "escalation", "escalation_outcome",
                    "duration_seconds", "input_tokens", "output_tokens"}


def available(value: str | None) -> bool:
    return bool(value and value.strip() and value.strip().upper() not in {"N/A", "NA", "UNAVAILABLE"})


def number(value: str | None) -> float | None:
    if not available(value):
        return None
    try:
        parsed = float(value.strip())
    except (ValueError, AttributeError):
        return None
    return parsed if parsed >= 0 else None


def fmt_num(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:.2f}".rstrip("0").rstrip(".")


def distribution_table(title: str, counts: Counter[str]) -> list[str]:
    lines = [f"### {title}", "", "| Value | Count | Distribution |", "|---|---:|---|"]
    total = sum(counts.values())
    if not counts:
        lines.append("| N/A | 0 | |")
    for key in sorted(counts, key=lambda item: item.casefold()):
        count = counts[key]
        bar = "█" * (round(20 * count / total) if total else 0)
        lines.append(f"| {key} | {count} | {bar} ({100 * count / total:.1f}%) |" if total else f"| {key} | {count} | |")
    lines.append("")
    return lines


def generate_report(csv_path: Path | str = DEFAULT_CSV) -> str:
    """Read records, skip malformed/duplicate executions, and return stable Markdown."""
    rows: list[dict[str, str]] = []
    malformed = 0
    path = Path(csv_path)
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle, strict=True)
        try:
            headers = next(reader)
        except StopIteration:
            headers = []
        missing_columns = REQUIRED_COLUMNS - set(headers)
        if missing_columns:
            raise ValueError("CSV is missing required columns: " + ", ".join(sorted(missing_columns)))
        seen: set[str] = set()
        for values in reader:
            if not values or all(not value.strip() for value in values):
                continue
            if len(values) != len(headers):
                malformed += 1
                continue
            row = dict(zip(headers, values))
            execution_id = row.get("execution_id", "").strip()
            task_id = row.get("task_id", "").strip()
            if not execution_id or not task_id or execution_id in seen:
                malformed += 1
                continue
            seen.add(execution_id)
            rows.append(row)

    sessions = {r["session_id"].strip() for r in rows if available(r.get("session_id"))}
    missing_sessions = sum(not available(r.get("session_id")) for r in rows)
    models = Counter((r.get("model", "").strip() or "N/A") for r in rows)
    efforts = Counter((r.get("reasoning_effort", "").strip() or "N/A") for r in rows)
    phases: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        phases[row.get("lifecycle_phase", "").strip() or "N/A"][row.get("model", "").strip() or "N/A"] += 1
    phase_counts = Counter((r.get("lifecycle_phase", "").strip() or "N/A") for r in rows)
    completion = Counter((r.get("completion_status", "").strip() or "N/A").casefold() for r in rows)
    known_escalations = [r for r in rows if r.get("escalation", "").strip().casefold() in {"yes", "true", "1", "no", "false", "0"}]
    escalation_rows = [r for r in known_escalations if r.get("escalation", "").strip().casefold() in {"yes", "true", "1"}]
    missing_escalations = len(rows) - len(known_escalations)
    escalation_outcomes = Counter((r.get("escalation_outcome", "").strip() or "N/A") for r in escalation_rows)
    durations = [n for r in rows if (n := number(r.get("duration_seconds"))) is not None]
    input_tokens = [n for r in rows if (n := number(r.get("input_tokens"))) is not None]
    output_tokens = [n for r in rows if (n := number(r.get("output_tokens"))) is not None]
    duration_missing = len(rows) - len(durations)
    token_missing = sum(not available(r.get(k)) for r in rows for k in ("input_tokens", "output_tokens"))

    out = ["# Codex development model usage report", "",
           "This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.", "",
           "## Recorded activity", "",
           "| Measure | Count |", "|---|---:|",
           f"| Sessions with available ID | {len(sessions)} |", f"| Records missing session ID | {missing_sessions} |",
           f"| Task executions | {len(rows)} |",
           f"| Malformed or duplicate rows | {malformed} |", "",
           "Task executions count unique, valid `execution_id` records. Sessions count unique available session IDs. Duplicate execution IDs are skipped.", ""]
    if not rows:
        out += ["No valid usage records are available yet.", ""]
    out += distribution_table("Model usage distribution", models)
    out += distribution_table("Reasoning effort distribution", efforts)
    out += ["### Model usage by lifecycle phase", "", "| Lifecycle phase | Task executions | Models used |", "|---|---:|---|"]
    for phase in sorted(phase_counts, key=str.casefold):
        model_text = ", ".join(f"{name}: {count}" for name, count in sorted(phases[phase].items(), key=lambda item: item[0].casefold()))
        out.append(f"| {phase} | {phase_counts[phase]} | {model_text} |")
    if not phase_counts:
        out.append("| N/A | 0 | |")
    out += ["", "### Task completion", "", "| Status | Count |", "|---|---:|"]
    for status in sorted(completion, key=str.casefold):
        out.append(f"| {status} | {completion[status]} |")
    if not completion:
        out.append("| N/A | 0 |")
    completed = completion.get("complete", 0)
    out += ["", f"Completed: **{completed} / {len(rows)}** task executions.", "",
            "### Escalations", "", "| Measure | Count |", "|---|---:|",
            f"| Escalations among known values | {len(escalation_rows)} / {len(known_escalations)} |",
            f"| Records missing escalation value | {missing_escalations} |"]
    for outcome in sorted(escalation_outcomes, key=str.casefold):
        out.append(f"| Escalation outcome: {outcome} | {escalation_outcomes[outcome]} |")
    out += ["", "### Duration and token statistics", "", "| Measure | Available count | Total | Mean | Missing measurement count |", "|---|---:|---:|---:|---:|"]
    for label, values, missing in (("Duration (seconds)", durations, duration_missing),
                                   ("Input tokens", input_tokens, len(rows) - len(input_tokens)),
                                   ("Output tokens", output_tokens, len(rows) - len(output_tokens))):
        total = sum(values)
        out.append(f"| {label} | {len(values)} | {fmt_num(total) if values else 'N/A'} | {fmt_num(mean(values)) if values else 'N/A'} | {missing} |")
    out += ["", f"Missing duration measurements: **{duration_missing}**; missing token measurements: **{token_missing}** (input and output token fields counted separately).", "",
            "Only numeric, non-negative measurements are aggregated. Blank, `N/A`, unavailable, and invalid measurements are not treated as zero.", ""]
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_CSV, help="Usage CSV path")
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT, help="Markdown report path")
    args = parser.parse_args()
    report = generate_report(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
