# ADR SG-04R — Component-level implementation progression

**Status:** Prepared under product-owner authorization and submitted for review; capability activation remains evidence-gated.  
**Decision owner:** Product owner.  
**Date:** 2026-11-25 (Asia/Calcutta).  
**Scope:** Development progression policy only. Product requirements, acceptance outcomes, priorities, and security boundaries are unchanged.

## Context

SG-04E records a blocked SG-05A entry because the prior progression policy required broad M3 validation closure before M4 implementation. The design package contains approved contracts and substantial findings, while some proofs require a live service, browser, database, controlled provider receiver, or disposable Linux isolation environment. A single collective gate delays unrelated work and duplicates engineering in non-production harnesses.

## Decision

Replace the collective pre-implementation closure rule for D01–D12 with staged implementation, component-level verification, and capability activation gates:

1. Begin implementation when the relevant design contracts are approved, even if empirical conditions remain OPEN.
2. Build applicable security controls from the first change. Use TDD with independently authored expected outcomes for critical controls.
3. Keep a sensitive capability disabled or fail it closed until its applicable condition has designated, reviewed evidence. A gate passes only on that evidence.
4. Let unrelated deterministic, manual, evidence-import, and documentation work proceed when an optional runner or another isolated capability is unavailable.
5. Never execute untrusted repository code outside verified disposable isolation. Never transmit to remote AI until redaction, consent, exact-payload, and transport controls pass. Never expose a protected service until local authority controls pass.
6. Do not claim P0 MVP completion until all 53 P0 criteria, all five MVP scenarios, and applicable mandatory gates have passed.
7. Retain isolated feasibility probes only for real environment or architecture uncertainty. Do not create a duplicate non-production application solely to meet sequencing policy.

The authoritative condition register retains D01–D12, all mappings and statuses, the designated closure evidence, and prior SG-04A/SG-04D/SG-04E history. Its SG-04R section defines prospective activation restrictions. All conditions remain OPEN at this decision point.

## Scope preservation

This is not a requirements change. Preserve 54 requirements, 68 criteria (39 P0 requirements / 53 P0 criteria; 12 P1 requirements / 12 P1 criteria; 3 P2 requirements / 3 P2 criteria), five MVP scenarios, nine major product features, D01–D12, evidence/verdict policy, and the accepted SG-03D secret-handling decision. No requirement, criterion, feature, or priority is deleted, demoted, weakened, or rewritten.

## Consequences

- Implementation can proceed in small dependency-ordered work packages while feature activation remains fail-closed.
- Documentation contracts and unit or deterministic checks can be developed without claiming environmental feasibility.
- The roadmap assigns one task per requested implementation session and records the requirements, prerequisites, checks, gates, restrictions, deliverables, and exit conditions.
- P0 acceptance and release claims remain subject to M5 and the original test plan.
- The D09 disposable Linux runner remains a distinct infrastructure-dependent capability; its absence does not prevent non-runner development.

## Related records

- [SG-03D mandatory conditions](SG-03D-m3-mandatory-conditions.md): preserved history and prospective component activation restrictions.
- [SG-04R implementation decisions](SG-04R-implementation-decisions.md): preferred technology and proposed numeric defaults; none are claimed as verified runtime settings.
- [SG-04R implementation roadmap](../design/SG-04R-implementation-roadmap.md): task sequence and acceptance/exit conditions.
- [SG-04R evidence](../../codex-evidence/design/SG-04R.md): actual document and traceability validation.

No SG-05 implementation, dependency installation, virtualization provisioning, workload launch, provider request, commit, push, or deployment is authorized by this ADR.
