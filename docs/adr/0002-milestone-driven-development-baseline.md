# ADR 0002 — Milestone-driven development baseline

**Status:** Accepted by product owner in SG-03A  
**Date:** 2026-11-24  
**Scope:** Internal development constraints, roadmap progression, and feasibility assessment

## Context

The SG-01 discovery materials described a one-month solo feasibility hypothesis. The SG-03 independent requirements review concluded that the approved P0 gate was not realistic under that assumed window, estimated 20 working days, and recommended extending the window or reducing the first gate. The SG-02 product baseline already approves 54 requirements across P0, P1, and P2, with criterion-level acceptance requirements and an MVP gate.

The product owner decided that the Codex Build Challenge is external submission context only. Its duration must not set internal product requirements, feature priorities, implementation scope, or engineering acceptance criteria.

## Decision

Use a milestone-driven, quality-first development lifecycle. Advance when the milestone's deliverables and acceptance criteria are complete and validated. Assess feasibility using technical complexity, dependencies, security, correctness, and maintainability. Do not estimate developer working hours or FTE, set calendar-based development targets, or remove or demote an approved capability solely because of development duration.

Preserve the eight lifecycle stages (Understand, Specify, Plan, Design, Implement, Verify, Review, Automate), all approved P0, P1, and P2 capabilities, the SG-02 product decisions, model selection strategy, and mandatory evidence tracking protocol. Runtime execution timeouts, performance requirements, resource limits, and security-related timing controls remain in force.

## SG-03 finding disposition

- The schedule-based portion of SG-03's critical feasibility finding is **superseded by this product-owner-authorized decision**. The assumed one-month window, working-day calculation, request for a fixed delivery window, and suggested duration-based scope reduction no longer apply to the active baseline.
- The critical finding's technical concern remains open: the P0 gate has substantial cross-component work and dependencies across two framework families, intake, traceability, persistence, isolated execution, AI consent/redaction, export, and security. SG-03A makes no claim that implementation is technically feasible or that the risks are resolved. M3 must resolve or explicitly disposition technical blockers with design decisions and acceptance evidence.
- All other SG-03 findings remain open for SG-03B remediation: P0 fixture/MVP-gate mismatch for broken-save behavior; security acceptance boundaries; objective/generalizable test outcomes; AI consent and provider/redaction failure coverage; requirement identity rules; import and runner failure boundaries; and unsupported-scope/sign-off semantics.
- The original [SG-03 independent requirements review](../../codex-evidence/review/SG-03-requirements-review.md) is preserved unchanged as historical evidence.

## Consequences

- The roadmap is gated by deliverables and validated acceptance evidence, with existing priorities preserved: P0 MVP, then four P1 capabilities, then the P2 Surgical Repair Engine.
- The active feasibility notes describe technical complexity, dependencies, and unresolved blockers without estimating development duration.
- No changes are made to the normative PRD, requirements catalog, test plan, SG-02 product decisions, or acceptance thresholds. No product code is authorized or implemented by this decision.
- SG-03B remains the next review-remediation task; this decision does not authorize starting SG-03B or the Design stage.

## Alternatives considered

- Keep the one-month target and narrow P0: rejected because it would let challenge duration drive product scope and change approved requirements.
- Keep all approved scope but set a longer fixed calendar schedule: rejected because the product owner selected deliverable-based progression rather than a replacement time constraint.
- Make no active-baseline update: rejected because the obsolete hypothesis and SG-03 schedule recommendation would continue to read as current constraints.

## Sources

- [GOALS.md](../../GOALS.md)
- [Milestone plan](../../PLANS.md)
- [SG-01 research and feasibility considerations](../RESEARCH.md)
- [SG-02 PRD](../PRD.md), [requirements catalog](../REQUIREMENTS.yaml), and [test plan](../TEST_PLAN.md)
- [SG-03 independent requirements review](../../codex-evidence/review/SG-03-requirements-review.md)
- SG-03A review evidence: [SG-03A.md](../../codex-evidence/review/SG-03A.md)
