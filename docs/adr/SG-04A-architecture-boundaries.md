# SG-04A Proposed Decision: Architecture Boundaries and Evidence Authority

**Status:** Proposed for product-owner approval; not accepted.  
**Decision owner:** Product owner.  
**Date:** 2026-11-24 (Asia/Calcutta).  
**Scope:** Design baseline only; no application implementation authorization.

## Context

SG-02 approved a local web audit with optional consent-controlled remote AI. SG-03D closed requirements entry to Design while leaving 12 mandatory M3 conditions open. The architecture must retain requirement-to-code-to-test traceability, evidence provenance and calibrated verdicts while preserving local control and fail-closed security boundaries.

## Proposed decision

Adopt a layered local architecture with a FastAPI workflow/API shell, React/Next.js interface, bounded Git/spec/report/runner/provider adapters, local audit/evidence persistence, and an independent Python verification core with deterministic inputs and typed observations. The verification core does not import FastAPI, UI, database, provider or runner-control code. It never executes repository application modules. Human review controls trace-link adoption and case approval. Remote AI remains a proposal-only adapter and cannot create evidence or change verdicts. Runner execution is a separate approval-gated capability. The accepted SG-03D secret-handling decision remains controlling.

## Alternatives considered

1. Put parsing, analysis, persistence, UI orchestration and runner dispatch in one application service. Rejected in this proposal because it couples trust boundaries and makes deterministic behavior harder to review.
2. Let AI or report-level pass status determine requirement verdicts. Rejected because both conflict with approved evidence policy and human-review boundaries.
3. Execute indexed application modules to discover behavior during indexing. Rejected because the selected repository is untrusted and requirements prohibit unsafe execution.

## Consequences

- Deterministic analyzer outputs, imported evidence, human decisions and AI inferences remain distinct record types.
- Unsupported/incomplete/stale/corrupted/conflicting evidence remains unresolved unless the normative verification policy permits a supported verdict.
- The architecture requires baseline/version references and provenance on links, findings, evidence and verdicts.
- Detailed library, persistence, session, runner-platform and provider choices remain separate decisions governed by the M3 conditions.
- This proposal does not close any SG-03D condition, establish feasibility, change requirements, or authorize SG-05.

## Validation and progression status

Architecture documents and criterion mapping are recorded in `docs/architecture/` and `codex-evidence/design/SG-04A-closure.md`. No controlled security, parser, index, runner, provider or persistence proof is claimed. All D01–D12 remain OPEN until the evidence in [the mandatory M3 register](SG-03D-m3-mandatory-conditions.md) is produced and reviewed.

## SG-04D remediation addendum (still proposed)

The SG-04C review found that the unsupported-only verdict wording could override sufficient independent criterion evidence. The architecture interpretation is corrected to follow the normative [Verification Policy](../VERIFICATION_POLICY.md): repository coverage and criterion admissibility are separate; unsupported-dependent insufficiency remains unresolved with notice references; sufficient admissible evidence continues through ordinary pass/fail/conflict rules. No policy or requirement text is changed.

The proposal also makes explicit that imported evidence requires inspected assertions or recorded reviewer observations, evidence from AI remains inadmissible, IDs and transitions are audit/baseline/revision scoped, staged specification changes do not activate until approved, and runner/provider boundaries confer no implicit authority. These are design interpretations of existing requirements and boundaries, not newly approved product capabilities.

The local session bootstrap/topology (D08), runner platform and numeric limits (D09), provider endpoint/transport policy (D10), and persistence technology/transactions (D11) remain unresolved. D01–D12 remain **OPEN**. This addendum remains proposed for product-owner review and does not authorize SG-05.

## SG-04R lifecycle addendum (2026-11-25)

The SG-04R product-owner-authorized lifecycle decision supersedes the collective rule that all applicable D01–D12 empirical gates must close before any M4 implementation. Relevant approved design contracts permit staged implementation. Each OPEN condition restricts activation of dependent capabilities as defined in the authoritative [mandatory conditions register](SG-03D-m3-mandatory-conditions.md); unrelated work may proceed. All D01–D12 remain OPEN until their designated reviewed evidence is recorded. The SG-04R [preferred implementation decisions](SG-04R-implementation-decisions.md) provide recommendations and proposed numeric defaults for owner review; none establish runtime feasibility or close a gate. This addendum does not authorize a product requirement change or capability activation.

