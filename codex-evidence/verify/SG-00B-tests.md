# SG-00B verification evidence

- **Task:** SG-00B — Automated model report generator
- **Lifecycle phase:** Verify
- **Date:** 2026-11-24 (client date)
- **Execution record:** `SG-00B-20261124-01` in `../models/MODEL_USAGE.csv`

## Verification performed

Command: `python -m unittest discover -s tests -v`

Result: **10 tests passed**. Coverage includes empty CSV, a single model, multiple models in one session, missing measurements, malformed rows, duplicate execution IDs, model and phase aggregation, repeatable output, escalation statistics, and unavailable escalation values.

Command: `python -m scripts.generate_model_report`

Result: report generated from the current CSV. Tests assert report content and exact repeatability for fixed input.

## Limitations

These tests cover the report generator and its supported CSV shape. They do not verify application functionality or SpecGuard runtime LLM behavior.
