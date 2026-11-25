# Repository guidance

- Title sessions using the [eight-phase convention](PLANS.md#development-phases). Preserve historical evidence paths.
- Keep work bounded to an approved milestone and preserve the requirements in `GOALS.md`.
- Prefer deterministic checks before LLM judgment; use evidence for verification and TDD for critical behavior.
- Treat untrusted code as unsafe. Do not execute it outside an isolated, controlled environment.
- Record only work, evidence, model usage, and measurements that actually occurred.
- Do not change requirements without authorization. Do not commit, push, or deploy without approval.
- Keep project plans in `PLANS.md`, decisions in `docs/adr/`, and stage evidence in `codex-evidence/`.
- For model selection and recording, follow `codex-evidence/models/MODEL_STRATEGY.md` and its adjacent templates.
- Before each development task, identify its lifecycle phase, task ID, and session ID; record the actual model, reasoning effort, selection rationale, and starting Git commit when available. Use `N/A` for unavailable measurements; do not infer them.
- Resolve each task's phase through `codex-evidence/models/LIFECYCLE_REGISTRY.yaml` and the approved roadmap; register new task mappings before writing usage records. Lifecycle phase is roadmap position, not activity type.
- Record `phase_id`, canonical `lifecycle_phase`, `activity_type`, `execution_mode`, and `record_origin` for every usage entry. Use only the registry vocabularies and explicitly mark unknown historical metadata unavailable.
- Before declaring a development task complete, append or update its unique execution record in `codex-evidence/models/MODEL_USAGE.csv`; record decisions, changed files, commands, actual test results, limitations, and human interventions in the matching `codex-evidence/<phase>/` directory; update `EVIDENCE_INDEX.md`; regenerate `MODEL_REPORT.md`; and state which evidence files changed. Keep separate usage records when model or reasoning effort changes and document why.
- Validate the ledger with `python -m scripts.generate_model_report`, regenerate both model reports, and run the applicable report-generator tests before closing the task. The generator rejects invalid rows rather than omitting them.
- If essential model metadata is unavailable, request developer confirmation. Never fabricate models, token use, costs, duration, tests, or execution evidence. Keep Codex development usage separate from SpecGuard runtime LLM usage.
- Change `MODEL_STRATEGY.md` only when the strategy changes, and `MODEL_EXPERIMENTS.md` only when conducting a controlled experiment.
- Add task-specific guidance only when a directory has distinct needs; keep this file concise.
