# SG-03B Requirements Review Remediation

## Execution record

| Field | Planning | Approved documentation execution |
|---|---|---|
| Lifecycle phase | Review | Review |
| Task and execution ID | SG-03B, `SG-03B-20261124-01` | SG-03B, `SG-03B-20261124-02` |
| Platform session ID | N/A | N/A |
| Client date and timezone | 2026-11-24, Asia/Calcutta | 2026-11-24, Asia/Calcutta |
| Execution mode | Plan mode | Default mode |
| Starting Git commit | `957c138c4720c9783c47b23aa9ffc19dc44d29e6` | `957c138c4720c9783c47b23aa9ffc19dc44d29e6` |
| Actual model and reasoning effort | Sol / High, developer confirmed | Sol / High, developer confirmed |
| Selection rationale | Complex requirements remediation, cross-document analysis, threat modeling, objective acceptance and technical dependency assessment. | Retained for precise revisions to approved requirements, security boundaries, objective acceptance and cross-document consistency. |
| Duration, token counts, costs and resource usage | N/A | N/A |

The developer confirmed the P0 browser-origin and unauthorized-request boundary, including the exclusions for developer-account compromise and hostile local processes able to steal session proof. The developer then authorized the presented documentation plan, including the revised criteria and ten additions. Git and PowerShell were used for baseline inspection. Python and PyYAML were used for catalog and documentation validation. Both execution records belong to Codex development usage.

Sources include the [independent SG-03 review](SG-03-requirements-review.md), [SG-03A evidence](SG-03A.md), [ADR 0002](../../docs/adr/0002-milestone-driven-development-baseline.md), and the [SG-02 baseline evidence](../specify/SG-02.md).

## Finding dispositions

| Finding | Disposition and rationale | Acceptance references |
|---|---|---|
| F01 Technical feasibility | The schedule-based portion is superseded by ADR 0002. Technical feasibility remains open for M3. The assessment below maps dependencies and potential blockers while preserving the full P0 gate. | SG-R001–SG-R039, MVP-01–MVP-05 |
| F02 Fixture and MVP gate | The P0 fixture specifies the omitted field, the backend stub and a separate example of unsupported proof. Unsupported proof fails to substantiate the criterion and leaves it unresolved in the fixture. The P1 broken-save flow records a passing visual comparison and a failing save/readback observation separately. | SG-R020-AC01, SG-R029-AC02, SG-R042-AC01, MVP-01 |
| F03 Security acceptance | The verification policy defines the bounded threat model, allowed requests, session proof and safe response to failure. The test plan observes unauthorized access, isolation properties, credential exclusion, enforced limits and cleanup. | SG-R031-AC01, SG-R034-AC01/02, SG-R035-AC01/02, SG-R038-AC01/02 |
| F04 Objective and generalizable acceptance | Supported analyzer signals now have finite rules and positive and negative fixture observations. The structured proposal contract supplies outcome oracles. Classification checks cover the reviewer's decision and rationale. | SG-R006-AC01, SG-R009-AC01, SG-R020-AC01 through SG-R026-AC02 |
| F05 AI consent and provider safety | Per-audit approval binds sanitized payload bytes and endpoint at dispatch. Redirects are prohibited. Redaction, validation and provider failures preserve prior evidence, keep fallback available and prevent unsupported verdict promotion. | SG-R013-AC01/02, SG-R038-AC01/02, SG-R039-AC01/02, MVP-02 |
| F06 Revision identity | Continuing obligations retain stable IDs. Semantic change requires approval, a new revision and stale applicability tracking. Replacement, split and retirement retain historical identities and lineage. | SG-R005-AC01, SG-R007-AC01/02 |
| F07 Import and runner failure boundaries | Added bounded Git, XML, setup, teardown and descendant-cleanup cases. Invalid input and unverified teardown preserve prior evidence. Further runner execution depends on verified recovery. | SG-R015-AC01/02, SG-R032-AC02, SG-R034-AC01/02, SG-R035-AC01/02, SG-R036-AC01, MVP-03 |
| F08 Unsupported coverage and verdicts | Audit coverage and criterion verdicts have separate rules. Supported artifacts in mixed audits remain usable. Unsupported-only diagnostics are exportable. Independent supported proof can determine a criterion verdict. | SG-R008-AC02, SG-R018-AC01/02, MVP-04 |

F02–F08 are remediated at the requirements level. Their product acceptance cases belong to M5 for P0 and M7 for the P1 visual flow. F01 remains open in its technical portion.

## Technical feasibility and dependencies

| Dependency order | Work and integration complexity | Unresolved technical blocker |
|---|---|---|
| 1. Intake and snapshot identity | Pin one commit and retain exact specification bytes and source locations. Every downstream artifact and verdict depends on this identity. | M3 must demonstrate bounded local reads and safe parser failure before selecting intake libraries. |
| 2. Static index and reviewed requirement revisions | Integrate source and test locations across Python/FastAPI and React/Next.js. Deterministic trace links, ghost rules and structured proposals depend on an indexed snapshot and reviewed criterion identity. | M3 must demonstrate location fidelity, deterministic signals and unsupported diagnostics on both stacks. Static rule coverage is limited to the documented patterns. |
| 3. Vault, verdict and export | Normalize provenance, revision staleness and coverage. JUnit import, the runner, AI suggestions and the UI must preserve pinned evidence and operation state across retries and reopens. | M3 must validate storage and exported coverage contracts with round-trip and failure-state evidence. |
| 4. Local access, runner and optional provider | Protect audit operations and approvals. Isolated execution and provider integration each add separate security and recovery dependencies. | M3 must show authorized local session behavior, enforceable runner limits and verified recovery, and exact-consent provider dispatch with redaction and fallback. Windows with WSL2/Docker is a runner candidate. |
| 5. Integrated workflow and sign-off | Connect the approved operations through the local UI and verify the complete P0 journey. Design of the pinned fixture and independent assertions is shared integration work. | M3 must map the controlled fixture to the full gate. M5 requires observed passing evidence for all 52 P0 criteria and five MVP scenarios. |

The [Design decision register](../../docs/adr/SG-03B-design-decision-register.md) lists unresolved platform and backend, intake and runtime limits, session and transport implementation, storage and export, two-stack indexing and fixture decisions. Each decision has an M3 resolution milestone and specified evidence before dependent M4 work. A failed containment, cleanup or consent proof blocks the corresponding work. Cross-stack indexing, revision representation and UI integration also create implementation complexity. This documentation review did not establish runtime behavior or technical feasibility.

## Requirement and acceptance counts

| Priority | Requirements before and after | Criteria before | Criteria after |
|---|---:|---:|---:|
| P0 | 39 | 42 | 52 |
| P1 | 12 | 12 | 12 |
| P2 | 3 | 3 | 3 |
| Total | 54 | 57 | 67 |

The ten new P0 IDs provide independently mapped checks for replacement, split and retirement (SG-R007-AC02), provider fallback (SG-R013-AC02), coverage export and verdicts (SG-R018-AC02), documented failure proposals (SG-R026-AC02), unsupported proof (SG-R029-AC02), invalid snapshots (SG-R032-AC02), unverified teardown (SG-R034-AC02), descendant termination (SG-R035-AC02), failed redaction (SG-R038-AC02), and redirect handling (SG-R039-AC02). Twenty-three existing criteria were clarified or expanded, including the self-audit import count. The eight stages, ten approved features, requirement and existing criterion IDs, and priority assignments were retained.

## Changed documents and evidence

- The [PRD](../../docs/PRD.md), [requirements catalog](../../docs/REQUIREMENTS.yaml), [test plan](../../docs/TEST_PLAN.md), [verification policy](../../docs/VERIFICATION_POLICY.md), and [failure scenarios](../../docs/FAILURE_SCENARIOS.md) define the approved remediation.
- [Goals](../../GOALS.md) and [research](../../docs/RESEARCH.md) reflect the approved local audit and optional AI direction. The [milestone plan](../../PLANS.md), [ADR index](../../docs/adr/README.md) and [Design decision register](../../docs/adr/SG-03B-design-decision-register.md) record the technical handoff.
- This report, the [evidence index](../EVIDENCE_INDEX.md), the [model usage ledger](../models/MODEL_USAGE.csv), and the regenerated [model report](../models/MODEL_REPORT.md) record the change and the two actual executions.

## Documentation validation

| Check | Observed result |
|---|---|
| `git status --short --branch` and `git rev-parse HEAD` | Both turns started with a clean working tree at the recorded commit. |
| Read-only Python and PyYAML check via stdin | Catalog v1 parsed with duplicate-key rejection. Compared against the starting commit and confirmed 54 retained requirement IDs, 57 retained criterion IDs, 23 revised outcomes and ten approved P0 additions. Priorities, features, types, methods and dependencies were preserved. All 67 case rows matched by ID, priority, method and expected outcome. All five MVP scenarios remained mapped. |
| Source, dependency and Markdown checks via the same validator | All 85 catalog sources and 137 local Markdown links across 37 documents resolved. Dependencies are acyclic and priority-valid. The six baseline research-anchor references for SG-R014–SG-R019 were repaired. The original review, prior evidence, existing ADRs and model strategy files were preserved. |
| Cross-document review | The P1 save flow and all 52 P0 criteria stayed in their approved gates. Fixture outcomes, verdict and coverage semantics, revision lineage, remote-consent rules and runner recovery agree across the normative documents. Progression remains milestone-based. |
| `python -B -m unittest discover -s tests -v` | All ten existing ledger tests passed. |
| `python -B -m scripts.generate_model_report` | Regenerated the report with seven unique execution records, including separate SG-03B planning and documentation records, and zero malformed or duplicate rows. |
| `git diff --check` and explicit whitespace checks for new documents | Passed. Git printed working-copy line-ending notices. |

The planning check identified the six pre-existing source-anchor failures. The first post-edit catalog comparison caught a missing SG-R029-AC02 row. The row was added to the catalog and test plan, and the comparison passed on rerun. No product acceptance tests, untrusted repository code, or Design proofs of concept were run.
