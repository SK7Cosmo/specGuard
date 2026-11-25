# SG-04A Architecture Design Evidence

## Task record

| Field | Value |
|---|---|
| Lifecycle phase / task | Design / SG-04A |
| Execution ID | `SG-04A-20261124-01` |
| Date / timezone | 2026-11-24 / Asia/Calcutta |
| Execution mode | Default |
| Actual model / reasoning effort | Luna / High; developer confirmed |
| Selection rationale | Used for cross-document architecture synthesis, component-boundary design, risk analysis and full baseline-to-component mapping. |
| Starting Git commit | `81ff5ff03d1b5ee859f23ed6eb38306df64483d9` |
| Platform session ID | Unavailable |
| Duration, tokens, resource usage | N/A; not observed |
| Human intervention | Developer supplied repository instructions and confirmed actual model and effort. Product-owner approval of the resulting design remains pending. |

## Baseline inspection

Read `AGENTS.md`, `GOALS.md`, `PLANS.md`, the PRD and machine-readable requirements catalog, acceptance test plan, verification policy, SG-03 independent review, SG-03D closure, secret-handling ADR, mandatory condition register, existing design decision register, model strategy/ledger/report, evidence index and design evidence conventions, plus discovery/vision/scope documents.

The authoritative baseline matches SG-03D:

- 54 requirements: 39 P0, 12 P1, 3 P2.
- 68 acceptance criteria: 53 P0, 12 P1, 3 P2.
- 68 existing test-plan cases mapped by criterion ID and verification method.
- 12 mandatory M3 conditions, all OPEN.

The `PLANS.md` reference to 53 criteria is explicitly the P0 M5 gate, not the full baseline, so it is consistent with 68 overall criteria. SG-03D says requirements readiness for Design with mandatory gates; it does not establish feasibility or condition closure. The accepted secret decision is preserved without modification.

## Design decisions proposed

- Separate local UI/API orchestration, intake and adapters from a deterministic independent verification core.
- Keep Git snapshots immutable and scoped; static indexing does not import or execute repository code.
- Inspect specification bytes for covered secrets before persistence or downstream handling; reject detected covered secrets and fail closed when inspection cannot establish safety; retain exact bytes only after successful acceptance.
- Treat trace matches, ghost findings and generated cases as reviewable observations; AI suggestions stay inferred and cannot affect verdicts.
- Evaluate evidence per criterion using baseline, assertion relevance, provenance, integrity, freshness, coverage and trust; incomplete/unsupported/stale evidence remains unresolved.
- Keep runner approval single-use and isolated; keep remote AI disabled by default with exact payload/destination consent binding and no redirects.
- Preserve audit revisions and evidence history; failures are atomic/idempotent and do not erase earlier work.
- Preserve the approved milestone sequence and all P0/P1/P2 scope; no schedule-based reduction.

These are proposal statements, not demonstrated feasibility or closed conditions.

## Deliverables prepared

- `docs/architecture/SG-04A-system-architecture.md`: context/container/component diagrams, lifecycle, logical data model, trace model, evidence/verdict behavior, proposed API, frontend information architecture, security, risks and sequence.
- `docs/architecture/SG-04A-architecture-traceability.csv`: 68 criterion rows covering all 54 requirements; each points to proposed component(s), catalog verification method and the existing test-plan case.
- `docs/architecture/SG-04A-condition-matrix.md`: all 12 conditions with proposed decision, required proof, role-level owner and closure gate; all OPEN.
- `docs/architecture/SG-04A-deliverables.md` and `docs/architecture/README.md`: approval boundaries and proposed architecture/diagram/ADR/data/API/security/fixture deliverables.
- `PLANS.md`: M3 marked in progress with the proposal and all 12 gates open.

No application code, dependencies, requirements, acceptance cases, or ADR product decisions were changed. SG-05 was not started.

## Commands and actual validation

- Inspected repository files and Git baseline with PowerShell `Get-Content`, `Get-ChildItem`/`rg --files`, and `git rev-parse HEAD` / `git status --short`.
- Parsed `docs/REQUIREMENTS.yaml` with PyYAML and counted requirement/criterion priorities; result matched 54 requirements and 68 criteria.
- Parsed all criterion IDs in `docs/TEST_PLAN.md` and generated the architecture CSV; result: 68 case IDs mapped across all 54 requirements.
- Ran a structural check of the generated matrix and condition coverage: 68 unique criterion/case rows, all 54 requirement IDs represented, all 12 D01–D12 present and marked OPEN. Two initial inline-check attempts had incorrect checker expressions (case-ID regex escaping, then OPEN-cell formatting); the corrected check passed and found no repository baseline mismatch.
- Ran `git diff --check`; passed.
- Regenerated `codex-evidence/models/MODEL_REPORT.md` with `python -m scripts.generate_model_report` after updating the usage ledger.
- No product acceptance tests, unit tests, security experiments, controlled fixtures, parser proofs, runner proofs, provider proofs, or feasibility demonstrations were run.

## Limitations and gate status

This is an architecture proposal for product-owner review. No library, storage implementation, host runner platform, provider transport or numeric resource limits have been proven feasible. The named role owners are proposals, not assignments. D01–D12 remain OPEN. The design does not authorize dependent M4 implementation, close M3, alter product requirements, or start SG-05.

