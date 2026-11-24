# Milestone plan

This plan is a framework, not a claim that any milestone has been completed. Keep each milestone bounded, reviewable, and tied to evidence.

| Milestone | Lifecycle stage(s) | Intended outcome | Status |
|---|---|---|---|
| M0: Initialize repository | Understand, Plan | Establish project guidance, goals, plans, and evidence framework | In progress |
| M1: Understand the problem | Understand | Capture users, context, assumptions, risks, and source evidence | Complete: SG-01 evidence recorded; initial user and target confirmed; technical decisions deferred to Specify/Design |
| M2: Define requirements | Specify | Establish authorized, traceable functional and quality requirements | Complete. SG-02 baseline and documentation checks recorded in [Specify evidence](codex-evidence/specify/SG-02.md). |
| M3: Plan and design | Plan, Design | Resolve technical decisions and dependencies; define architecture, threat model, runner contract and limits, controlled fixture, and acceptance evidence for the approved baseline | Not started |
| M4: Implement the approved P0 capability set | Implement | Implement approved P0 behavior in reviewable increments, using test-first development for critical paths | Not started |
| M5: Verify and review the P0 gate | Verify, Review | Validate all 39 P0 requirements and the end-to-end gate against approved acceptance criteria; record security, quality, and unresolved risks | Not started |
| M6: Automate repeatable checks | Automate | Automate approved deterministic checks and evidence capture, with repeatability demonstrated by evidence | Not started |
| M7: Deliver approved P1 capabilities | Implement, Verify, Review, Automate | Implement and validate all four approved P1 features against their existing requirements and acceptance cases | Not started; follows MVP gate |
| M8: Deliver approved P2 capability | Implement, Verify, Review, Automate | Implement and validate Surgical Repair Engine against its existing requirements and acceptance cases | Not started; follows P1 milestone |

Progression is deliverable- and evidence-driven, with no calendar target or developer-hour estimate. A milestone advances when its documented deliverables satisfy its acceptance criteria and review gate. Record scope changes and obtain authorization before changing requirements. Preserve the eight lifecycle stages; milestones may span stages.

## SG-02 product baseline

- M2 defines the [PRD](docs/PRD.md), [requirements catalog](docs/REQUIREMENTS.yaml), [verification policy](docs/VERIFICATION_POLICY.md), and [acceptance test plan](docs/TEST_PLAN.md).
- The approved MVP is a local web audit of one Git snapshot against its original specification. It covers Python/FastAPI and React/Next.js, all five mandatory features, test report import, approved isolated test execution, and optional remote AI trace suggestions with per-audit consent. See the [audit operating boundary decision](docs/adr/0001-audit-operating-boundary.md).
- M3 resolves architecture, security boundaries, runner and resource limits, and controlled fixture design against all approved P0 obligations. Technical blockers are recorded and resolved or explicitly dispositioned before dependent implementation proceeds.
- M4 implements the approved P0 capability set. M5 verifies all 39 P0 requirements and the end-to-end gate before claiming MVP completion. M6 makes approved deterministic checks and evidence capture repeatable.
- M7 delivers the four approved P1 features after the MVP gate. M8 delivers the approved P2 Surgical Repair Engine. No approved capability is removed or demoted because of development duration; existing P0/P1/P2 order is preserved.
- SG-03B owns remediation and disposition of all SG-03 review findings other than the superseded schedule-based portion of the critical feasibility finding. Technical feasibility concerns in that finding remain open for M3; see [decision 0002](docs/adr/0002-milestone-driven-development-baseline.md).
