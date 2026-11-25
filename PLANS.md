# Milestone plan

This plan is a framework, not a claim that any milestone has been completed. Keep each milestone bounded, reviewable, and tied to evidence.

| Milestone | Lifecycle stage(s) | Intended outcome | Status |
|---|---|---|---|
| M0: Initialize repository | Understand, Plan | Establish project guidance, goals, plans, and evidence framework | In progress |
| M1: Understand the problem | Understand | Capture users, context, assumptions, risks, and source evidence | Complete: SG-01 evidence recorded; initial user and target confirmed; technical decisions deferred to Specify/Design |
| M2: Define requirements | Specify | Establish authorized, traceable functional and quality requirements | Complete. SG-02 baseline and documentation checks recorded in [Specify evidence](codex-evidence/specify/SG-02.md). |
| M3: Plan and design | Plan, Design | Maintain approved design contracts and produce reviewed evidence for applicable D01–D12 capability activation gates | In progress: SG-04A through SG-04E evidence is preserved. SG-04R restructures prospective progression; D01–D12 remain OPEN and are validated alongside implementation. See the [lifecycle ADR](docs/adr/SG-04R-lifecycle-restructuring.md) and [roadmap](docs/design/SG-04R-implementation-roadmap.md). |
| M4: Implement the approved P0 capability set | Implement | Implement approved P0 behavior in reviewable increments, using TDD and independent expected outcomes for critical controls | SG-05A foundation implemented for controlled checks. D08 review pending. Each capability remains disabled until its applicable gate passes. |
| M5: Verify and review the P0 gate | Verify, Review | Validate all 53 criteria across the 39 P0 requirements and all five MVP scenarios; record security, quality, and unresolved risks | Not started; no P0 completion claim until all criteria, scenarios, and applicable mandatory gates pass. |
| M6: Automate repeatable checks | Automate | Automate approved deterministic checks and evidence capture, with repeatability demonstrated by evidence | Not started |
| M7: Deliver approved P1 capabilities | Implement, Verify, Review, Automate | Implement and validate all four approved P1 features and all 12 P1 criteria against existing requirements and acceptance cases | Not started; follows MVP gate |
| M8: Deliver approved P2 capability | Implement, Verify, Review, Automate | Implement and validate Surgical Repair Engine against all three existing P2 criteria and acceptance cases | Not started; follows P1 milestone |

Progression is deliverable- and evidence-driven, with no calendar target or developer-hour estimate. A milestone advances when its documented deliverables satisfy its acceptance criteria and review gate. Record scope changes and obtain authorization before changing requirements. Milestones may span phases.

## Development phases

Use `Phase NN | STAGE | SESSION-ID | Session Title` for new sessions. Phase numbers and session identifiers are independent. Existing evidence directories retain their historical names. The authoritative phase IDs, machine-readable values, task mappings and controlled metadata vocabularies are in [LIFECYCLE_REGISTRY.yaml](codex-evidence/models/LIFECYCLE_REGISTRY.yaml). Register a new task mapping from its approved roadmap phase before adding its ledger execution record. Lifecycle phase is the task's roadmap position, not its activity type. Verification, security testing and remediation may occur during BUILD as well as dedicated later phases.

| Phase | Stage | Purpose and session classification |
|---|---|---|
| 01 | UNDERSTAND | Initialization and discovery (SG-00, SG-00B, SG-01) |
| 02 | PLAN | Requirements, acceptance and verification planning (SG-02 and SG-03 series) |
| 03 | DESIGN | Architecture and implementation planning (SG-04 series, including SG-04R) |
| 04 | BUILD | Production implementation, integration and TDD (SG-05 series) |
| 05 | TEST | Independent verification, acceptance and security validation |
| 06 | DEBUG & IMPROVE | Remediation, optimization and hardening |
| 07 | DEPLOY | Packaging, deployment and release readiness |
| 08 | AUTOMATE | CI/CD, regression automation and operational workflows |

The model usage ledger stores the canonical lowercase values `understand`, `plan`, `design`, `build`, `test`, `debug_improve`, `deploy`, and `automate`, paired with `P01` through `P08` in order. The validated ledger produces both `codex-evidence/models/MODEL_REPORT.md` and `codex-evidence/models/MODEL_METRICS.json`; execution totals do not establish lifecycle or milestone completion.

SG-04F0–F8 and SG-04G were proposals only. The SG-05 work packages retain the verification, review and automation activities assigned by the roadmap.

## SG-02 product baseline

- M2 defines the [PRD](docs/PRD.md), [requirements catalog](docs/REQUIREMENTS.yaml), [verification policy](docs/VERIFICATION_POLICY.md), and [acceptance test plan](docs/TEST_PLAN.md).
- The approved MVP is a local web audit of one Git snapshot against its original specification. It covers Python/FastAPI and React/Next.js, all five mandatory features, test report import, approved isolated test execution, and optional remote AI trace suggestions with per-audit consent. See the [audit operating boundary decision](docs/adr/0001-audit-operating-boundary.md).
- M3 maintains the architecture and produces controlled evidence for D01–D12. Under SG-04R, an open condition blocks only activation of capabilities that depend on it; it does not block unrelated implementation.
- M4 implements the approved P0 capability set in the order in the [SG-04R roadmap](docs/design/SG-04R-implementation-roadmap.md), with security controls from the first change. M5 verifies all 53 criteria across the 39 P0 requirements and all five MVP scenarios before any MVP completion claim. M6 makes approved deterministic checks and evidence capture repeatable.
- M7 delivers the four approved P1 features after the MVP gate. M8 delivers the approved P2 Surgical Repair Engine. No approved capability is removed or demoted because of development duration; existing P0/P1/P2 order is preserved.
- The [SG-03B remediation report](codex-evidence/review/SG-03B.md) records the disposition of all eight findings. [ADR 0002](docs/adr/0002-milestone-driven-development-baseline.md) supersedes the schedule-based part of F01. [ADR SG-04R](docs/adr/SG-04R-lifecycle-restructuring.md) supersedes the collective pre-implementation gate rule; all original gate evidence and requirements remain authoritative.

## M3 and M4 progression

| Task | Status | Progression |
|---|---|---|
| SG-04E | Corrective Design planning recorded in the [remediation plan](docs/design/SG-04E-gate-remediation-plan.md) and [stage evidence](codex-evidence/design/SG-04E.md). | Preserved as historical planning; its proposed F0–F8 validation sequence is not the active roadmap. |
| SG-04R | Lifecycle restructuring, implementation decisions, roadmap and document validation recorded in [Design evidence](codex-evidence/design/SG-04R.md). | Restructuring authorized. The owner subsequently assigned Foundation and Local Authority to SG-05A. |
| SG-05A | Phase 04 BUILD, Foundation and Local Authority. Controlled implementation and verification recorded in [BUILD evidence](codex-evidence/implement/SG-05A.md). | PARTIAL pending independent D08 review. Next roadmap ID is SG-05C. |
