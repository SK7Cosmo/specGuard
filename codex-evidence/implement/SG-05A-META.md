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

## Incremental Vercel-readiness execution — 2026-11-27

- **Execution:** `SG-05A-META-20261127-01`, Phase 04 BUILD / P04, activity `architecture`.
- **Session:** `01a2118b-ca45-7a71-bb06-f1afa3ffb4c6` (`CODEX_SESSION_ID`); same session and confirmed GPT-6 Luna / Medium as the prior recorded SG-05A-META execution.
- **Starting commit:** `04950dc4d99c4e1390bb43ecd4d2b596f016c689`.
- **Scope:** Record the owner-required Vercel constraint, assess current architecture against the two deployment profiles, and version/package sanitized metrics as a static frontend build artifact. No product behavior was modified.

### Decisions and architecture observations

Added [SG-05A Vercel deployment readiness](../../docs/adr/SG-05A-vercel-readiness.md) with profile definitions, a per-capability compatibility register, known conflicts, future adjustments, owner-review items, and official documentation references checked on 2026-11-27. Updated AGENTS.md, PLANS.md, and the active SG-04R implementation roadmap to require profile implications, dependencies, local state assumptions, hosted restrictions, and relevant build checks in future task records.

Findings: the frontend is a Next.js 16.4.6 static export, but its current page calls the local `/api/v1/session` endpoint; the Python FastAPI app owns that endpoint and serves the export. FastAPI binds a single IPv4 loopback socket and requires interactive terminal bootstrap. Session and revocation proofs live in process memory. SQLite support is a local, schema-metadata-only migration. `specguard/app.py` resolves the exported UI through a repository-relative path. The pure `RevisionRef` domain value object is a useful framework-independent pattern. No Vercel config or deployment is present.

Compatibility disposition: static sanitized analytics and a future synthetic-only static demo are Vercel-compatible in principle, with environment-specific deployment verification required; the current local UI, loopback authority and current SQLite/session profile remain local-only. Hosted authentication, durable storage, repository access, AI provider use and interactive protected operations require separate architecture/security approval; repository ingestion and isolated execution also require external infrastructure. D01–D12 remain OPEN. The ADR records the conflict between the local-only protection model and public hosted protected access, proposing a separate static, synthetic demo until specific hosted flows receive approval.

### Analytics schema and artifact

`MODEL_METRICS.json` now carries `schema_name=specguard-model-metrics` and numeric `schema_version=1`. Its chronology omits execution IDs and platform session IDs; the existing aggregate session counts remain. The generator writes the exact same sanitized JSON payload to `frontend/public/analytics/model-metrics.json`. Thus a future frontend build can serve the dataset as a static asset without Python at request time, a Vercel Function, or a database. The repository has no CI workflow yet, so the documented regeneration command is available for development and a future CI job but was not wired into CI. No dashboard or chart UI was built.

Official platform sources checked: [Next.js on Vercel](https://vercel.com/docs/frameworks/full-stack/nextjs), [Function runtimes and filesystem support](https://vercel.com/docs/functions/runtimes), [build configuration](https://vercel.com/docs/builds/configure-a-build), and [CDN caching for static files](https://vercel.com/docs/caching/cdn-cache). They establish platform behavior, not SpecGuard deployment compatibility.

### Checks and files changed

- `python -B -m unittest tests.test_generate_model_report -v` — 15 passed.
- `.venv\Scripts\python.exe -B -m unittest discover -s tests -v` with permitted loopback — 34 tests ran; 33 passed, 1 browser test skipped because `SPECGUARD_TEST_BROWSER` was not set.
- `python -B -m scripts.generate_model_report` — passed; regenerated Markdown, canonical JSON, and the static frontend JSON.
- `npm.cmd run build --prefix frontend` — passed with Next.js 16.4.6 and static export. `frontend/out/analytics/model-metrics.json` matched the public source asset, SHA-256 `47676BF629E5C8AE7340A97358E39096C6113F3D293458204B72A4A8A937A738`.
- Public-data assertions — passed: schema name/version, 8 phases, 22 executions, 17 tasks, no current execution/session IDs, and canonical/public JSON byte equality.
- `git diff --check` — passed after final ledger/evidence/report updates; Git emitted only configured line-ending notices.

Files changed by this incremental execution: `AGENTS.md`, `PLANS.md`, `docs/design/SG-04R-implementation-roadmap.md`, `docs/adr/README.md`, new `docs/adr/SG-05A-vercel-readiness.md`, `scripts/generate_model_report.py`, `tests/test_generate_model_report.py`, `codex-evidence/models/MODEL_USAGE.csv`, regenerated `MODEL_REPORT.md` and `MODEL_METRICS.json`, new `frontend/public/analytics/model-metrics.json`, `codex-evidence/EVIDENCE_INDEX.md`, and this evidence file. `frontend/out/` is ignored build output.

No Vercel project or external infrastructure was provisioned. No cloud authentication, public API, hosted persistence, remote repository, runner or provider was enabled. The successful Next.js static export is not a Vercel deployment or deployment-readiness claim. Requirements, product behavior, and mandatory gate statuses were unchanged; no commit, push or deployment occurred.
