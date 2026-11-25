# SG-04R — Development lifecycle restructuring and design decision closure

## Execution record

- **Lifecycle phase / task:** Design / M3 / SG-04R.
- **Execution ID:** `SG-04R-20261125-01`.
- **Session ID:** `01a2110d-bbb3-7912-ab1b-f5be6ae696c4` (observed `CODEX_SESSION_ID`).
- **Execution mode:** Default.
- **Date / timezone:** 2026-11-25 / Asia/Calcutta.
- **Actual model / reasoning effort:** GPT-6 Luna / High, developer-confirmed for this task.
- **Selection rationale:** SG-04R requires cross-document lifecycle, security, requirements and evidence reasoning; GPT-6 Luna / High is the repository's strategy choice for moderately complex analysis, and the developer confirmed the actual model and effort.
- **Starting Git commit:** `4bed4560b8990d11df5a618ef59238829223317a`.
- **Starting worktree:** Already modified `PLANS.md`, evidence index, model report and usage ledger from SG-04E; SG-04E evidence and its remediation plan were untracked inputs. These inputs were preserved and extended where requested.
- **Duration, tokens, cost, resource usage:** N/A; not exposed or measured.
- **Authorization / human intervention:** Product owner requested SG-04R and authorized the lifecycle restructuring. Developer confirmed GPT-6 Luna / High after metadata was requested. No requirements or acceptance criteria were changed.
- **Stop boundary:** SG-04R only. No SG-05 implementation, dependency installation, virtualization provisioning, workload launch, provider request, commit, push or deployment.

## Decisions recorded

- Replaced collective pre-implementation D01–D12 closure with relevant-design-contract entry, component-level verification, and capability activation restrictions. All D01–D12 statuses remain OPEN and historical evidence/findings are retained.
- Preserved 54 requirements, 68 criteria (39 P0 requirements / 53 P0 criteria; 12 P1 requirements / 12 P1 criteria; 3 P2 requirements / 3 P2 criteria), all five MVP scenarios, the approved feature and priority scope, the evidence/verdict policy, and the SG-03D secret-handling decision.
- Recorded preferred FastAPI/React/Next.js, same-origin loopback, session bootstrap/lifetime/revocation/restart, SQLite, read-only pinned Git, bounded Markdown/YAML/JUnit, Python AST/TypeScript Compiler API, exact-decimal rules, Playwright, HTTPX and disposable Linux VM decisions. Numeric limits and runtime settings are proposed defaults only; no technology or capability was installed, provisioned, launched or verified.
- Reconciled SG-04F0, SG-04F1–F8 and SG-04G as not-started historical proposals incorporated where useful into component tasks; retained SG-05A as the historical blocked attempt; identified SG-05B as the next implementation task.
- Applied the approved consistency corrections: hyphen identifier boundaries; impossible field violations are inapplicable without invalidating an otherwise valid rule; SG-R032-AC02 is mapped explicitly to D06 and D12.

## Changed files

- `PLANS.md`
- `docs/adr/SG-03D-m3-mandatory-conditions.md`
- `docs/adr/SG-04R-lifecycle-restructuring.md`
- `docs/adr/SG-04R-implementation-decisions.md`
- `docs/adr/README.md`
- `docs/architecture/SG-04A-system-architecture.md`
- `docs/architecture/SG-04A-condition-matrix.md`
- `docs/architecture/SG-04A-architecture-traceability.csv`
- `docs/architecture/SG-04A-deliverables.md`
- `docs/architecture/README.md`
- `docs/adr/SG-03B-design-decision-register.md`
- `docs/adr/SG-04A-architecture-boundaries.md`
- `docs/design/SG-04R-implementation-roadmap.md`
- `experiments/sg04r/validate_documents.py`
- `codex-evidence/design/SG-04R.md`
- `codex-evidence/design/SG-04R-document-check-results.json`
- `codex-evidence/design/README.md`
- `codex-evidence/EVIDENCE_INDEX.md`
- `codex-evidence/models/MODEL_USAGE.csv`
- `codex-evidence/models/MODEL_REPORT.md` (regenerated)

The PRD, REQUIREMENTS.yaml, VERIFICATION_POLICY.md, TEST_PLAN.md, all prior gate evidence, SG-04C findings, and SG-04E history were not edited.

## Validation

- `python -B experiments/sg04r/validate_documents.py` — **PASS**. Confirmed byte-identical normative documents against starting commit; 54 requirements, 68 criteria and exact case mappings; priority counts 39/53 P0, 12/12 P1, 3/3 P2; all five MVP scenarios; 12 OPEN conditions and 12 activation restrictions; all 68 traceability rows; SG-R032-AC02 mapped to D06 and D12; 13 ordered implementation tasks with no forward/circular dependency; **143 local Markdown links**; and preserved SG-04D closure and evidence hashes.
- `python -B -m scripts.generate_model_report` — generated aggregate from the usage ledger.
- `git diff --check HEAD` — **PASS** after final edits; Git printed only configured LF-to-CRLF working-copy notices.
- No product acceptance suite, runtime feasibility probe, existing unit-test suite, browser, provider, database or runner was run. The document check is not gate-closure or product-acceptance evidence.

Initial validator attempts exposed three issues in the new checker: an incorrect assumption that the 13 catalog feature labels equal the nine product-feature count, task-ID extraction including task titles, and treating ignored SG-04D result JSON as Git-tracked baseline files. The checker was corrected to preserve the complete catalog without imposing that taxonomy assumption, parse IDs correctly, compare the tracked SG-04D closure record to the starting commit, and hash the pre-existing result artifacts. The final run passed.

## Remaining blockers and limitations

- D01–D12 remain OPEN. The proposed technology choices and resource limits are not runtime evidence.
- Disposable Linux VM/host capabilities and permissions, browser availability/launch permission, controlled provider endpoint/egress, package availability, and a writable scratch Git repository remain unverified. These affect only their dependent activation/proof.
- SG-04R validated document structure and traceability, not application behavior or security feasibility. No product acceptance criterion or MVP scenario is claimed passed.

## Evidence index updates

Updated `codex-evidence/EVIDENCE_INDEX.md` and `codex-evidence/design/README.md`. Updated the development model usage ledger and regenerated the model report. No SpecGuard runtime LLM use occurred.
