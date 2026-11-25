# SG-04 Design Closure — SG-04D

## Recommendation and approval boundary

**Implementation readiness: NOT READY.** This report records the SG-04C remediation and the final M3 Design closure package for product-owner review. The approved product and requirements baseline is retained; the architecture below is a recommended design baseline pending product-owner approval. All D01–D12 progression gates remain **OPEN**. No implementation-stage condition is closed, no requirements or acceptance criteria changed, and SG-05 has not started.

Product-owner approval is requested for the design package and for the unresolved decisions listed below. Approval of the package alone will not close a condition or authorize SG-05. Dependent M4 work remains blocked until each applicable designated gate has been satisfied with reviewed controlled evidence.

## Execution record

- Lifecycle phase / milestone / task: Design / M3 / SG-04D.
- Execution ID: `SG-04D-20261124-01`.
- Session ID: N/A (not exposed); execution mode: Default.
- Client date / timezone: 2026-11-24 / Asia/Calcutta.
- Execution began and model metadata was confirmed on 2026-11-24; closure evidence was finalized on 2026-11-25 / Asia/Calcutta.
- Actual model / reasoning effort: GPT-6 Luna / High; developer-confirmed for this execution.
- Selection rationale: GPT-6 Luna / High is the strategy's moderately complex cross-document design and evidence choice; confirmed by the developer for SG-04D.
- Starting Git commit: `81ff5ff03d1b5ee859f23ed6eb38306df64483d9`.
- Starting worktree: pre-existing modified/untracked SG-04A/SG-04B/SG-04C design, review, tracking, and experiment artifacts; preserved as inputs. No commit, push, or deployment.
- Duration, token counts, cost, and resource measurements: N/A; not observable.
- Authorization: User requested SG-04D remediation, evidence, condition reconciliation, closure report, and stop for product-owner approval. No SG-05 authorization.
- Human intervention: Developer confirmed GPT-6 Luna / High after the required metadata request. No other decision was made on the unresolved product-owner questions.

## Recommended architecture baseline for approval

Retain the approved local-audit product boundary and eight lifecycle stages. The recommended design keeps an independent deterministic verification core; bounded, non-executing repository/spec/report adapters; human-controlled link, rule, evidence, and baseline decisions; immutable audit/baseline/revision identities; a separately approved and isolated runner; optional consent-bound AI proposals; and local persistence/export with integrity and provenance checks.

The SG-04D design contracts clarify intake before all persistence sinks, staged versus activated specification changes, complete evidence admissibility, criterion-token matching, typed rules/cases, durable runner-attempt recovery, scoped idempotency, same-audit/baseline identity, and proposal-only AI. The unsupported-only verdict wording now follows the normative Verification Policy: repository coverage and criterion evidence are independent decisions, with insufficient unsupported-dependent evidence remaining unresolved and notice references retained.

The architecture remains a proposal. In particular, D08 session bootstrap/topology, D09 supported isolation backend and limits, D10 provider endpoint/transport policy, and D11 storage mechanics require product-owner disposition and controlled evidence. The package does not impose a new product capability, change AI from optional, or relax any approved feature or priority.

## Design deliverables

- [System architecture](../../docs/architecture/SG-04A-system-architecture.md): added SG-04D contracts and corrected unsupported-only verdict interpretation.
- [Logical data model](../../docs/architecture/SG-04A-data-model.md): added audit/baseline scoped identities, staged change records, evidence assessments, typed rules/cases, provider proposals, and durable runner attempts; accepted external specifications are no longer modeled as repository-only artifacts.
- [API contracts](../../docs/architecture/SG-04A-api-contracts.md): specified staged intake, clarification/change decisions, manual links, rule/case review, assertion relevance, dismissal, reopen/export, and authority/provider constraints.
- [Security design](../../docs/architecture/SG-04A-security-design.md): specified receive-to-discard boundary, bounded parser obligations, session proof rules, and accurate review/security evidence limits.
- [Architecture-boundaries ADR](../../docs/adr/SG-04A-architecture-boundaries.md): added the SG-04D normative-policy reconciliation and open-decision status; remains proposed, not accepted.
- [Requirement/design traceability](../../docs/architecture/SG-04A-architecture-traceability.csv): retained all 68 criterion rows and added SG-04C finding IDs, SG-04D remediation references, and open-validation status.
- [Mandatory condition register](../../docs/adr/SG-03D-m3-mandatory-conditions.md): added a finding-specific SG-04D disposition for every D01–D12 gate while keeping all statuses OPEN.
- [Feasibility evidence](SG-04D-feasibility.md) and [machine-readable results](SG-04D-contract-check-results.json): record the limited synthetic contract check and its limitations.
- [Document/traceability check](SG-04D-document-check-results.json) and reproducible [closure validator](../../experiments/sg04d/verify_document_closure.py): check the unchanged baseline, all 68 mappings, 14 finding records, 12 OPEN gates, and feasibility-result provenance.

## Findings remediation register

The independent SG-04C report remains unchanged as historical review evidence. “Addressed” below means the design/documentation defect was corrected or made explicit; it does not claim that its controlled feasibility gate passed.

| Finding | Root cause | SG-04D remediation | Verification result and status |
|---|---|---|---|
| F01 — Critical: gates/readiness | Matrix coverage and synthetic PASS counts were at risk of being mistaken for integrated feasibility or gate closure. | Kept M3 open; mapped every finding to conditions and preserved the rule that only designated reviewed evidence closes a gate. | All 12 conditions remain OPEN; readiness NOT READY. Open blocker. |
| F02 — High: local session | Bootstrap authority, deployment origin, proof transport, lifetime, and revocation had no selected contract. | Specified deny-before-disclosure behavior and required bootstrap properties; left topology and mechanism for product-owner disposition. | D08 request matrix not run; owner decision and feasibility remain open. |
| F03 — High: secret-safe intake | Design stopped at an application buffer and did not cover framework spooling, parser ambiguity, or derived-data sinks. | Specified receive-to-discard ordering, sink exclusions, duplicate rejection, bounded parser classes, exact accepted bytes, and inert rendering obligations. | No real ingress, parser, sink, storage, or browser observation; D01/D04/D06/D10 open. |
| F04 — High: runner | No backend, numeric limits, durable attempt binding, or crash/recovery state model. | Added atomic consume-before-launch states, invocation/environment identity, concurrency rejection, service-wide uncertainty block, and fresh-approval recovery. | No backend selected or runner launched; D03/D09 open. |
| F05 — High: persistence | Logical entities lacked transaction ordering, scoped idempotency, integrity-on-read, and restart reconciliation. | Added canonical payload binding, changed-input conflict, staged artifact publication, atomic active-baseline transition, and startup reconciliation contract. | No store or fault injection; D03/D11 open. |
| F06 — High: evidence admissibility | Synthetic importer flags and claimed assertion IDs acted as the verdict oracle. | Separated source outcome, inspected assertion/observation, reviewer rationale, integrity, freshness, completeness, and admissibility; retained rejected provenance. | SG-04D matrix checks reject unrelated, AI, and conflicting inputs; no actual importer/reviewer/store tested; D05/D11 open. |
| F07 — High: unsupported verdict | Architecture text conflicted with the normative policy by allowing unsupported repository scope to suppress independent criterion evidence. | Corrected system architecture and proposed ADR: coverage and admissible criterion evidence are independent; insufficiency stays unresolved with notices. | 18 synthetic combinations across coverage/evidence matched expectations; no product evaluator/UI/export run; D05/D07/D12 open. |
| F08 — High: case generation | No typed rule schema, joint-bound semantics, declared failure outcome, or independent expected-case oracle. | Added a typed rule/case revision contract, exact bounds/domain requirements, conflict and stale-revision rejection, explicit outcomes, and review-before-execution. | Design contract only; no generator/oracle matrix run; D02 open. |
| F09 — Medium: matching/analyzer | Proof matcher omitted complete criterion IDs and did not define syntax-aware two-stack behavior. | Defined full-token boundaries, criterion-prefix suppression, both-stack syntax-aware analysis, positive/negative controls, and baseline-bound locations. | 6 inert ID cases passed, including suffix and identifier decoys; no Python/React/Next.js indexer run; D07 open. |
| F10 — Medium: weak experiments | Some named checks were constant flags, non-observing fixtures, or sequenced so the asserted defect could not be detected. | Added an independent expected-outcome matrix and a deliberately defective unsupported-only mutant sensitivity control; recorded the initial matcher failure and correction. | Defective verdict mutant was detected; 6 token and 18 admissibility cases pass. Historical SG-04B results remain unchanged; D01–D04/D06–D07/D12 still open. |
| F11 — High: provider boundary | Proposal schema, taint, endpoint/transport policy, exact serialization, and dispatch/revocation ordering were unspecified. | Added a strict proposal-only schema/authority boundary and exact-preview consent contract; explicitly left endpoint policy for owner decision. | No provider call or traffic capture; D10 open. |
| F12 — High: workflow contracts | API/data model omitted approved manual, clarification, semantic-change, dismissal, rule-edit, and relevance workflows. | Added scoped records, request/transition contracts, stale-write checks, and staged-to-active baseline transition semantics. | Contract review only; no round-trip or full P0/MVP design dry run; D05/D11/D12 open. |
| F13 — Medium: P1/P2 design | Matrix names reserved features without feature-specific design contracts. | Explicitly retained these as M7/M8 design deliverables; preserved all P1/P2 requirements and acceptance criteria. | No P1/P2 contract work or scope reduction; defer to their existing stages; SG-04 remains P0-blocked by other gates. |
| F14 — Medium: proof provenance | Historical result files lacked self-contained harness/input/version/invocation provenance. | Added a required provenance envelope for future proofs and generated SG-04D results containing harness/fixture hashes, runtime, invocation, commit, and limits. | Current SG-04D check is reproducible; historical SG-04B metadata cannot be recovered and remains unavailable. |

## Requirements and acceptance criteria coverage

The normative baseline remains **54 requirements**: 39 P0, 12 P1, and 3 P2; **68 acceptance criteria**: 53 P0, 12 P1, and 3 P2. All 68 criteria retain an exact test-plan case and an architecture row. The traceability CSV now links each criterion to its SG-04C finding(s), SG-04D contract reference, applicable gate status, and design-validation status. SG-04D did not alter the catalog, verification policy, or test-plan expected outcomes.

SG-04C's independent structural observation remains: 85 source paths resolve and requirement dependencies are acyclic. These are source/structure checks, not product acceptance. No criterion or MVP scenario is claimed passed. The 53 P0 cases and MVP-01–MVP-05 still need the D12 independent oracle dry run before M4 integration; actual acceptance remains M5 work.

## Feasibility results

### SG-04D bounded design-contract check

Command: `python -B experiments/sg04d/verify_design_contracts.py`.

- First attempt failed on the deliberately malformed string `SG-R001-AC010`: the draft matcher incorrectly emitted the requirement prefix. The boundary rule was tightened and the exact same check rerun.
- Final result: **PASS**; six exact-token/boundary fixtures and 18 coverage × admissibility cases matched the independent expected table. A deliberately defective blanket-unsupported verdict mutant disagreed with the relevant-pass oracle and was detected.
- Evidence records Python/runtime, command, starting commit, fixture count, harness SHA-256 and fixture SHA-256 in the JSON result.
- Scope is limited to inert synthetic strings and records and the design-contract functions in the SG-04D review harness. It does not execute SpecGuard application code or establish parser, browser, provider, persistence, runner, or integrated feasibility. It does not close D05, D07, or D12.

### Prior SG-04B feasibility evidence retained

SG-04B recorded 12 synthetic PASS results, but SG-04C independently found five counterexamples/weak checks and confirmed no real service, browser, runner, provider or store was exercised. D08 (session), D09 (backend), and D11 (persistence) lacked prerequisites; D12 only counted mappings. SG-04D preserves those historical results and limitations and does not re-label them as gate evidence. No universal infeasibility finding is made; missing tools in the prior environment do not prove host impossibility.

## Security review results

SG-04C remains the independent security and architecture review: 1 Critical, 9 High, 4 Medium findings; no production exploit or deployed vulnerability was observed or claimed. SG-04D corrected the design-policy conflict and strengthened contracts for receive paths, parser boundaries, reviewer evidence, authority, runner recovery, and provider taint. The SG-04D work did not perform a penetration test, execute untrusted application code, launch a runner, contact a provider, or inspect a real persistence implementation. Security feasibility remains open at the designated gates.

## Conditions register reconciliation

All conditions remain **OPEN**. The SG-04D column in the authoritative [SG-03D register](../../docs/adr/SG-03D-m3-mandatory-conditions.md) records remediation and why each gate is not closed. “Design contract clarified” is not equivalent to the required controlled observation.

| Gate | Remediation/reference | Designated closure evidence still required | Dependent M4 status |
|---|---|---|---|
| D01 | F03/F10; intake and sink contract | Covered clean/secret/error Markdown/YAML; actual receive/temp/log/cache/storage/export/provider sinks; byte-exact accepted round trip | Blocked |
| D02 | F08/F09/F10; typed rules/cases | Independent positive/negative, combined-bound, impossible-domain, conflict, failure-outcome and generator oracle matrix | Blocked |
| D03 | F04/F10; runner state contract | Atomic concurrent consumption, replay, changed invocation, setup/crash/restart/recovery observations | Blocked |
| D04 | F03/F10/F11; inert-render contract | Actual React/Next.js hostile content views with browser DOM/navigation/state observations | Blocked |
| D05 | F06/F07/F12; admissibility/verdict contracts | Actual assertion inspection, rationale, relevance controls, integrity/freshness/conflict and UI/reopen/export agreement | Blocked |
| D06 | F03/F09/F10; parser/Git contract | Selected libraries and limits; pinned Git, malformed/oversized/unsafe inputs, no retrieval/path escape, atomic preservation | Blocked |
| D07 | F09/F10; exact-token/analyzer contract | Equivalent Python/FastAPI and React/Next.js fixtures, routing/handler negatives, moved locations, mixed/unsupported scope | Blocked |
| D08 | F02; session contract | Product-owner choice of bootstrap/topology/proof; controlled Host/Origin, originless, expiry/revocation/restart requests before disclosure/mutation | Blocked; owner decision required |
| D09 | F04; durable runner/recovery contract | Product-owner disposition of supported host/backend and numeric limits; benign isolated limits/network/credential/mount/teardown/restart proof | Blocked; feasibility selection required |
| D10 | F03/F11; provider taint/consent contract | Product-owner endpoint/transport policy; exact bytes, redirect refusal, revoke race, bounds, response validation and sanitized failure captures | Blocked; owner decision required |
| D11 | F05/F06/F12; persistence contract | Select store/schema; fault-injected round trips, integrity, stale history, all coverage states, atomicity and idempotent recovery | Blocked |
| D12 | F01/F10/F12/F14; traceability and proof provenance | Pinned fixtures and independent oracles for all 53 P0 criteria and MVP-01–MVP-05, then complete design dry run | Blocked |

## Product-owner decisions and remaining risks

- Accept, reject, or revise the proposed SG-04A architecture boundaries ADR and this SG-04D design baseline.
- Resolve the D08 same-origin topology, bootstrap/local-possession mechanism, proof transport/storage/lifetime, restart and revocation policy.
- Resolve the D09 supported host/backend and numeric resource-limit selection path. Current evidence establishes neither support nor impossibility.
- Resolve the D10 endpoint/address/TLS/proxy/credential policy and exact transport boundary while retaining optional consent-controlled AI.
- Review D01/D06 parser and secret-class/limit selections, and D11 storage/transaction choices, before any dependent implementation.
- Keep P1/P2 feature design deliverables assigned to M7/M8 without dropping, demoting, or altering their approved requirements.
- No scope change is proposed. If the owner requests a requirement or acceptance-criteria change, record it through the approved change process before updating normative documents.

## Implementation work packages (not authorized to start)

1. Complete and review controlled M3 proofs D01–D12, with dependent components blocked until their gates pass.
2. M4 P0 intake, session authority, Git/parser, baseline and persistence foundations after D01/D04/D06/D08/D11.
3. M4 static indexing, trace/finding rules, typed rule/case generation, and manual review after D02/D07/D12.
4. M4 evidence import, relevance, verdict, history and export after D05/D06/D11/D12.
5. M4 runner and optional AI adapter after D03/D09 and D10 respectively; retain fail-closed behavior.
6. M5 verify all 53 P0 criteria across 39 P0 requirements and MVP-01–MVP-05 with actual product evidence.
7. M6 automate repeatable deterministic checks and evidence capture.
8. M7 design, implement, and validate all 12 P1 criteria across their existing features.
9. M8 design, implement, and validate all 3 P2 criteria for Surgical Repair Engine.

This sequence preserves the approved milestone and priority baseline. Items 1–5 are not started as implementation in SG-04D.

## Actual model usage and evidence references

Codex development usage for SG-04D is recorded separately from SpecGuard runtime LLM usage in [MODEL_USAGE.csv](../models/MODEL_USAGE.csv); the generated aggregate is [MODEL_REPORT.md](../models/MODEL_REPORT.md). SG-04D used GPT-6 Luna / High as developer-confirmed. Session ID, duration, token counts, cost, and resource usage were unavailable and recorded as N/A. No runtime model was called.

Evidence files changed for this execution: [SG-04D closure report](SG-04D-closure.md), [feasibility narrative](SG-04D-feasibility.md), [contract results](SG-04D-contract-check-results.json), [document-check results](SG-04D-document-check-results.json), [design evidence index](README.md), [evidence index](../EVIDENCE_INDEX.md), [MODEL_USAGE.csv](../models/MODEL_USAGE.csv), and regenerated [MODEL_REPORT.md](../models/MODEL_REPORT.md). The prior SG-04C review artifacts were preserved. Design and planning artifacts changed: `PLANS.md`; `docs/architecture/README.md`, `SG-04A-system-architecture.md`, `SG-04A-data-model.md`, `SG-04A-api-contracts.md`, `SG-04A-security-design.md`, `SG-04A-architecture-traceability.csv`, and `SG-04A-condition-matrix.md`; `docs/adr/SG-03D-m3-mandatory-conditions.md`, `docs/adr/SG-04A-architecture-boundaries.md`, and `docs/adr/README.md`. Reproducible evidence tooling added: `experiments/sg04d/verify_design_contracts.py` and `verify_document_closure.py`.

## Verification and limitations

- `python -B experiments/sg04d/verify_design_contracts.py`: initial negative-control failure exposed a malformed suffix boundary; corrected run passed 6 token cases and 18 admissibility cases.
- `python -B experiments/sg04d/verify_document_closure.py`: PASS; 54 requirements, 68 criteria and exact case mappings, 68 traceability rows, 12 OPEN gates, 14 findings, and matching recorded harness hash.
- Local Markdown link-path check across 14 changed design/evidence documents: 130 paths checked, 0 missing.
- `git diff --check HEAD`: passed; Git emitted only configured LF-to-CRLF working-copy notices. No product acceptance tests were run.
- No `SG-05` activity, product code, dependency installation, network request, provider call, runner launch, or untrusted application execution occurred.
- The architecture, feasibility, and security conclusions are limited to the written contracts and the controlled inert design checks described above.

**Final recommendation:** accept or return the design package and resolve the listed product-owner decisions. Keep the implementation gate **NOT READY** until all applicable M3 gates have the designated reviewed evidence. Stop here for product-owner approval; SG-05 has not started.
