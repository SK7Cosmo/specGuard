# SG-04A Proposed Architecture Deliverables

**Review status:** Documentation plan executed; architecture package submitted for product-owner approval. No technology decision or validation gate is represented as approved or complete by this register.

| Deliverable | Proposed location | Status / purpose |
|---|---|---|
| System architecture and design narrative | [SG-04A-system-architecture.md](SG-04A-system-architecture.md) | Documented for review; covers containers, components, lifecycle, traceability, evidence, verdicts, risks and sequence |
| System context/container/component diagrams | `SG-04A-system-architecture.md` Mermaid diagrams | Documented as logical diagrams; trust-boundary implementation remains subject to proof |
| Verification lifecycle sequence diagram | `SG-04A-system-architecture.md` Mermaid sequence | Documented; includes fail-closed specification intake and separately approved operations |
| Requirement/criterion architecture traceability | [SG-04A-architecture-traceability.csv](SG-04A-architecture-traceability.csv) | 68 criterion rows cover all 54 requirements; rows cite design sections, existing test-plan cases, applicable gates and unrun validation status |
| Mandatory condition decision/proof matrix | [SG-04A-condition-matrix.md](SG-04A-condition-matrix.md) and [authoritative register](../adr/SG-03D-m3-mandatory-conditions.md) | Design coverage/status recorded for all 12; every condition remains OPEN and prospective capability restrictions are recorded; role owners are proposed, not assigned |
| Logical data model and artifact lifecycle | [SG-04A-data-model.md](SG-04A-data-model.md) | Logical records/relationships documented; storage format and D11 validation remain open |
| API contracts | [SG-04A-api-contracts.md](SG-04A-api-contracts.md) | Proposed `/api/v1` resources, validation and safe errors documented; transport/status details remain review items |
| Frontend information architecture | `SG-04A-system-architecture.md`, section 11 | Documented; P1 visual flow remains assigned to M7 |
| Security boundary and failure design | [SG-04A-security-design.md](SG-04A-security-design.md) | Assets, boundaries and failure controls documented; no security feasibility proof claimed |
| ADR: architecture boundaries and evidence authority | [SG-04A-architecture-boundaries.md](../adr/SG-04A-architecture-boundaries.md) | Proposed, not accepted; records module/evidence boundary and rejects unsafe alternatives |
| ADR: Git and parser choices/limits | `docs/adr/` (future decision record) | Deferred until controlled options and D06 evidence; no library selected |
| ADR: source index and analyzer approach | `docs/adr/` (future decision record) | Deferred until D02/D07 evidence; no analyzer feasibility claimed |
| ADR: local session and browser authority | `docs/adr/` (future decision record) | Deferred until D08 proof |
| ADR: runner platform/backend/recovery | `docs/adr/` (future decision record) | Deferred until D03/D09 evidence; no platform selected |
| ADR: provider transport/redaction | `docs/adr/` (future decision record) | Deferred until D10 evidence; existing SG-03D policy remains controlling |
| ADR: persistence/revision/export format | `docs/adr/` (future decision record) | Deferred until D11 evidence; logical model does not select storage |
| ADR: integrated fixture repository and harness | `docs/adr/` (future decision record) | Deferred until D12 evidence; fixtures and independent oracles not selected or run |
| Secret policy decision | [SG-03D-secret-handling-decision.md](../adr/SG-03D-secret-handling-decision.md) | Existing accepted product-owner decision; SG-04A preserves it, while D01/D10 proofs remain open |
| Incremental implementation sequence | `SG-04A-system-architecture.md`, section 15; [PLANS.md](../../PLANS.md) | Proposal preserves M3→M4→M5→M6→M7→M8 order and all approved P0/P1/P2 scope; no schedule estimate |

## Approval boundary

This SG-04A text records the original Design-package approval boundary. SG-04R authorizes a prospective component-level progression policy: relevant approved design contracts permit implementation to begin, while each mandatory condition remains open until its controlled evidence is recorded and reviewed. Applicable conditions gate capability activation, not unrelated implementation. Approval of the lifecycle change does not approve each proposed technology choice or close a condition; any requirement or priority change still requires a separate explicit product-owner decision. See ADR SG-04R and its roadmap for current progression.

