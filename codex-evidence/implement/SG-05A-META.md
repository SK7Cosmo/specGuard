# Phase 04 | BUILD | SG-05A-META | Lifecycle and Model Evidence Standardization

- **Task:** SG-05A-META, bounded evidence maintenance under SG-05A.
- **Date:** 2026-11-25 (Asia/Calcutta).
- **Execution:** `SG-05A-META-20261125-01`.
- **Session:** `01a2118b-ca45-7a71-bb06-f1afa3ffb4c6` (`CODEX_SESSION_ID`).
- **Starting commit:** `4bed4560b8990d11df5a618ef59238829223317a`.
- **Model / effort:** GPT-6 Luna / Medium, developer-confirmed for this session.
- **Execution mode:** Default.
- **Activity / origin:** metadata_maintenance / contemporaneous.
- **Duration, token counts, resource use:** unavailable; not inferred.

## Baseline and decisions

The starting ledger contained 20 records, 16 distinct task IDs, and 20 unique execution IDs. The recorded model distribution was GPT-6 Luna 10, GPT-6.2 Sol 8, GPT-6.2 Astra 1, unavailable 1. Before appending this task, normalized phases were Understand 3, Plan 8, Design 8, Build 1, and zero for Test, Debug & Improve, Deploy, and Automate.

Existing phase labels placed SG-00 and SG-00B in Plan/Automate, placed SG-02 in Specify and SG-03 tasks in Review, and used the noncanonical string `Phase 04 BUILD` for SG-05A. The approved historical mappings correct these to P01, P02 and P04 respectively. The approved roadmap maps SG-05J to Test and SG-05K/SG-05N to Automate; SG-05L/M remain Build. Evidence directories and filenames were not renamed.

`LIFECYCLE_REGISTRY.yaml` defines exactly eight ordered phases, historical mappings, current SG-05A-META mapping, roadmap-backed future mappings, and controlled vocabularies. `MODEL_USAGE.csv` now carries `phase_id`, `activity_type`, `execution_mode`, and `record_origin`. Original IDs, task IDs, sessions, models, efforts, dates, statuses, escalation fields, validation text, notes, commit references and measurements were retained. Unknown execution modes and session IDs remain explicitly unavailable. SG-03's historical retro row is distinguished by `record_origin=retrospective`; it was not duplicated.

The report generator validates all rows before generating Markdown and structured JSON. It emits the canonical eight-phase order including zero-count phases, numeric metrics, model/effort matrices, distributions, resource availability, and a timeline without request content, raw notes, credentials or local paths. Execution totals are not presented as consumption, cost or lifecycle completion.

## Files changed for this execution

- `AGENTS.md`, `PLANS.md`, `codex-evidence/automate/SG-00B.md`
- `codex-evidence/models/LIFECYCLE_REGISTRY.yaml`, `MODEL_USAGE.csv`, `MODEL_REPORT.md`, `MODEL_METRICS.json`
- `scripts/generate_model_report.py`, `tests/test_generate_model_report.py`
- `codex-evidence/EVIDENCE_INDEX.md`
- This evidence record.

## Commands and observed results

- `python -B -m unittest tests.test_generate_model_report -v` — 14 passed.
- `.venv\Scripts\python.exe -B -m unittest discover -s tests -v` with permitted loopback — 33 tests ran; 32 passed and the browser test skipped because `SPECGUARD_TEST_BROWSER` was not configured.
- `python -B -m scripts.generate_model_report` — passed; generated Markdown and JSON.
- `git diff --check` — passed after final evidence/index updates; Git emitted only configured LF-to-CRLF notices.

Migration unit coverage verifies repeat-run byte identity and preservation of factual metadata. The generator rejects invalid phase values and IDs, mapping mismatches, duplicate execution IDs, missing identifiers, unsupported vocabulary, invalid statuses, malformed CSV rows and malformed measurements. Explicit unavailable and unrecognized historical model/effort values are retained without guessing.

## Limits and status

Execution modes cannot be recovered for some historical tasks and remain `unavailable`; session IDs, durations and resource measurements were unavailable in the source ledger and remain so. The one browser test was skipped in the complete regression run because no approved browser executable was configured for this run. This task changed lifecycle and evidence tooling only. It did not change application behavior, approved requirements, D01–D12 statuses, or SG-05A completion status. No commit, push or deployment occurred.
