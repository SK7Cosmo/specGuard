# SG-00B evidence: mandatory tracking and report generation

- **Task:** SG-00B — Establish Mandatory Evidence and Model Tracking
- **Lifecycle phase:** Automate
- **Date:** 2026-11-24 (client date)
- **Execution record:** `SG-00B-20261124-01` in `../models/MODEL_USAGE.csv`
- **Session ID:** N/A; not exposed to this task.
- **Starting Git commit:** N/A; repository has no `HEAD` commit.
- **Model / reasoning effort:** GPT-6 Luna / Medium (developer confirmed 2026-11-24); no model or effort switching occurred.
- **Selection rationale:** Bounded documentation, scripting, and routine testing; selected to conserve ChatGPT Plus usage while maintaining sufficient engineering quality.

## Decisions

- Extended `MODEL_USAGE.csv` with task and execution identifiers, phase, session, commit, completion, escalation, validation, duration, token, and resource fields.
- Used unique `execution_id` values to detect and skip duplicate records in reports.
- Kept unavailable measurements as `N/A` and excluded them from numeric aggregates.
- Kept the report explicitly scoped to Codex development usage, separate from runtime LLM usage.
- Used Python standard-library modules only.

## Files changed

`AGENTS.md`, `.gitignore`, `codex-evidence/models/MODEL_USAGE.csv`, `codex-evidence/models/MODEL_REPORT.md`, `codex-evidence/EVIDENCE_INDEX.md`, `codex-evidence/automate/SG-00B.md`, `codex-evidence/verify/SG-00B-tests.md`, `codex-evidence/plan/SG-00.md`, `scripts/__init__.py`, `scripts/generate_model_report.py`, and `tests/test_generate_model_report.py`.

## Commands and results

- `python -m unittest discover -s tests -v` — 10 tests passed.
- `python -m scripts.generate_model_report` — generated the report from the usage CSV.
- `git rev-parse HEAD` — no `HEAD` exists; starting commit is unavailable.

Earlier intermediate runs exposed assertion wording mismatches; assertions were corrected and the final full test run passed. An initial report-generation attempt occurred before the CSV schema was expanded and correctly rejected the old header; the report was subsequently regenerated successfully from the updated schema. Additional reporting logic excludes unavailable escalation values from known escalation rates.

## Limitations and human intervention

The developer confirmed the model and reasoning effort; the existing SG-00B usage record was updated in place, with no duplicate execution record. Session ID, elapsed duration, token counts, and resource usage remain unavailable and are recorded as `N/A`. No controlled model experiment was conducted, so `MODEL_EXPERIMENTS.md` was not changed. No product requirements were changed, and no commit, push, or deployment was performed.

## Current tracking protocol (SG-05A-META)

The canonical lifecycle registry is `../models/LIFECYCLE_REGISTRY.yaml`. It defines P01–P08, the controlled activity, execution-mode and record-origin vocabularies, and task mappings. The ledger now records `phase_id`, `activity_type`, `execution_mode`, and `record_origin`; historical values are populated only from existing notes and evidence. SG-00B's original evidence path and facts remain intact. Its phase was normalized to P01 because the canonical historical mapping places SG-00B in Understand, while this evidence artifact remains under `automate/`.

`python -m scripts.generate_model_report` validates the ledger and generates both `../models/MODEL_REPORT.md` and `../models/MODEL_METRICS.json`. Invalid rows are rejected. The structured report includes every lifecycle phase in registry order, numeric aggregates, matrices and a privacy-limited timeline. Unknown measurements remain unavailable, and execution counts do not represent cost, token consumption or lifecycle completion.

