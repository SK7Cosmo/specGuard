# SG-04C model metadata normalization

- Lifecycle / task / execution: Review / SG-04C / `SG-04C-20261124-02`.
- Client date / timezone: 2026-11-24 / Asia/Calcutta; execution mode: Default.
- Session ID: N/A (not exposed).
- Actual model / effort: GPT-6.2 Sol / High. The existing Sol / High confirmation continues; the user explicitly confirmed that Sol denotes GPT-6.2 Sol and Luna denotes GPT-6 Luna.
- Selection rationale: Continue the confirmed model for a bounded evidence-metadata correction; no model switch or escalation.
- Starting commit: `81ff5ff03d1b5ee859f23ed6eb38306df64483d9`; prior dirty working-tree work preserved.
- Scope: Normalize known model aliases in the CSV and regenerate its report. Preserve unavailable metadata, reasoning effort, historical observations and measurements. No product changes or changes to the independent gate recommendation.
- Human intervention: User explicitly authorized the canonical names and CSV/report update.
- Duration, tokens, cost and resource usage: N/A; not measured.

## Changes and validation

- CSV-aware normalization changed five `Sol` values to `GPT-6.2 Sol` and four `Luna` values to `GPT-6 Luna`. Assertions confirmed all non-model fields in the fifteen existing records were preserved. Already canonical names and the unavailable historical SG-03 model were retained.
- Added the unique execution `SG-04C-20261124-02` for this correction, using the confirmed GPT-6.2 Sol / High metadata. This is another task execution, not a model switch or an inferred session.
- Updated the SG-04C review's current actual-model field to reflect the explicit alias confirmation. Historical quoted model confirmations and review measurements remain historical observations.
- Recorded the canonical-name convention in EVIDENCE_INDEX.md for subsequent metadata recording. MODEL_STRATEGY.md and MODEL_EXPERIMENTS.md were not changed.
- `python -B -m unittest discover -s tests -v`: all ten existing evidence-tool tests passed; no product tests ran.
- `python -B -m scripts.generate_model_report`: completed. Independent CSV/report validation passed: sixteen unique executions, zero malformed/duplicate records, eight GPT-6 Luna records, seven GPT-6.2 Sol records and one unavailable record; generated report matches the CSV exactly.

Evidence files changed: `codex-evidence/models/MODEL_USAGE.csv`, generated `codex-evidence/models/MODEL_REPORT.md`, `codex-evidence/review/SG-04C.md`, this correction record and `codex-evidence/EVIDENCE_INDEX.md`.

This correction implements the user's authorized naming convention. The independent recommendation remains NOT READY FOR IMPLEMENTATION, with no requirements changes, implementation fixes, commit, push or deployment.
