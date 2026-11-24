# SG-03D Requirements Sign-off and Conditional Closure

## Verdict

**READY FOR DESIGN WITH MANDATORY DESIGN GATES**

The product-owner policy choice is recorded and its requirements, acceptance case, and verification policy agree. The SG-03C conditions are carried into an M3 register with source findings, affected IDs, deliverables, evidence, dependent components, gates and open status. The historical SG-03 model record is reconciled retrospectively; model, effort, execution mode and platform session ID remain unavailable because the preserved review and available historical artifacts do not establish them.

This verdict establishes requirements readiness to enter Design subject to the listed gates. It does not establish technical feasibility, security adequacy, or product acceptance. No product code was implemented, no Design proof was run, and SG-04 was not started.

## Product-owner decision

SG-03C C1 is resolved by the [specification secret-handling decision](../../docs/adr/SG-03D-secret-handling-decision.md): inspect before persistence; reject detected covered secrets and fail closed on mandatory inspection failure; give only safe diagnostics; require sanitization and resubmission; prevent rejected values entering storage, logs, caches, exports, session evidence or remote AI payloads; retain exact source bytes only for successfully accepted specifications; do not silently redact and accept or encrypt and retain a rejected original; scope detection claims to documented supported classes.

Affected normative material: [PRD](../../docs/PRD.md), [requirements catalog SG-R004-AC01–AC02](../../docs/REQUIREMENTS.yaml), [test plan](../../docs/TEST_PLAN.md), and [verification policy](../../docs/VERIFICATION_POLICY.md). Existing requirement and criterion IDs remain intact. SG-R004-AC01 was clarified to apply to accepted source, and one additive P0 criterion, SG-R004-AC02, was added for rejection and resubmission.

## Mandatory M3 conditions

The [M3 condition register](../../docs/adr/SG-03D-m3-mandatory-conditions.md) records 12 mandatory open gates. It carries forward objective observations for rule generation, single-use runner approvals, safe rendering, imported-evidence relevance, all seven technical decision areas, and the approved secret-handling policy across intake, evidence storage and source view. Each gate names its source finding, affected requirement and criterion IDs, Design deliverable, required validation, dependent components and the implementation progression point.

No condition is marked resolved. Dependent M4 implementation is prohibited until its applicable gate is satisfied. The [existing M3 decision register](../../docs/adr/SG-03B-design-decision-register.md) now includes the secret-safe intake and source-view proof.

## Baseline preservation and counts

- 54 requirements: 39 P0, 12 P1 and 3 P2. All approved features, priorities, MVP scenarios and the eight lifecycle stages remain.
- 68 acceptance criteria: 53 P0, 12 P1 and 3 P2, mapped one-to-one to 68 test-plan rows.
- 85 catalog source references; dependencies remain valid and acyclic.
- No calendar-driven development restriction, working-hour estimate, or duration-based scope reduction was introduced. ADR 0002 remains in force.
- The original [SG-03 independent review](SG-03-requirements-review.md) is preserved unchanged.

## Historical SG-03 model evidence

The original report was inspected together with the available repository evidence and model ledger. The original report records its phase, task, date and starting commit but does not identify the actual model, reasoning effort, execution mode or platform session ID. No independent historical source established those fields. A row labeled `SG-03-HIST-RETRO-01` was added to the ledger with each unavailable value explicit; it is retrospective and does not amend the original review. The model report was regenerated from the resulting ledger.

## SG-03D execution record

| Field | Recorded value |
|---|---|
| Lifecycle phase and task | Specify/Plan closure, SG-03D |
| Unique execution ID | `SG-03D-20261124-01` |
| Platform session ID | Unavailable |
| Date and timezone | 2026-11-24, Asia/Calcutta |
| Execution mode | Default |
| Starting Git commit | `957c138c4720c9783c47b23aa9ffc19dc44d29e6` |
| Actual model and reasoning effort | Luna / High, developer confirmed |
| Selection rationale | Luna High matches the MODEL_STRATEGY guidance for moderately complex cross-document analysis and requirements closure. |
| Duration, token counts and resource usage | N/A; not observed |

## Validation results

| Check | Actual result |
|---|---|
| `python -B -m unittest discover -s tests -v` | Passed: all 10 existing evidence-tool/report-generator tests. These are not product acceptance tests. |
| `python -B -m scripts.generate_model_report` | Passed: regenerated the report from 11 unique valid ledger executions, including the retrospective SG-03 row and SG-03D. |
| Documentation validator using PyYAML and Markdown parsing | Passed after aligning the catalog and case expected text: 54 requirements, 68 criteria, 39 P0 requirements, 53 P0 criteria, 68 exact ID/method/expected-result test mappings, 85 source references, valid dependency order, and 200 local Markdown links across 42 Markdown files. |
| `git -c core.safecrlf=false diff --check HEAD` | Passed. |

The documentation validator checks catalog structure and duplicate keys, criterion-to-test mappings, source paths and fragments, dependency acyclicity and priority, and local Markdown paths and heading references. It does not assess runtime behavior or product acceptance. The first parity pass caught an SG-R004-AC02 expected-text mismatch; the catalog and case were aligned before the passing run.

## Changed files

- `docs/PRD.md`
- `docs/REQUIREMENTS.yaml`
- `docs/TEST_PLAN.md`
- `docs/VERIFICATION_POLICY.md`
- `docs/adr/SG-03B-design-decision-register.md`
- `docs/adr/SG-03D-secret-handling-decision.md`
- `docs/adr/SG-03D-m3-mandatory-conditions.md`
- `docs/adr/README.md`
- `PLANS.md`
- `codex-evidence/review/SG-03D.md`
- `codex-evidence/models/MODEL_USAGE.csv`
- `codex-evidence/models/MODEL_REPORT.md`
- `codex-evidence/EVIDENCE_INDEX.md`

No product code or test files changed. No product acceptance tests or Design feasibility proofs were run. The requested evidence report presents the results for developer approval; it does not authorize automatic progression to SG-04.

