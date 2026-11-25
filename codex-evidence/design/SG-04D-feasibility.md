# SG-04D Bounded Design-Contract Feasibility Evidence

## Execution and provenance

- Phase/task/execution: Design / SG-04D / `SG-04D-20261124-01`.
- Starting Git commit: `81ff5ff03d1b5ee859f23ed6eb38306df64483d9`; the worktree already contained uncommitted SG-04A/B/C review inputs.
- Command: `python -B experiments/sg04d/verify_design_contracts.py`.
- Runtime observed: Python 3.12.7 on Windows 11 (`10.0.26200-SP0`).
- Harness SHA-256: `e125023a2444ec9f766f439d06bed8a338a4cd95a5848fa79121ceeec796a5db`.
- Canonical synthetic fixture SHA-256: `e97f4945ab2e1a0351735b164969a0568c70cc67167658da5e2586a56e3a8419`.
- Machine-readable output: [SG-04D contract-check results](SG-04D-contract-check-results.json).
- No product code, dependency, network service, browser, provider, runner, or repository test workload was executed.

## Hypotheses and expected observations

1. Criterion identifiers are recognized only as complete tokens; criterion IDs are not double-counted as a requirement prefix, and suffix/identifier decoys are not accepted.
2. Repository coverage is independent from criterion evidence. Sufficient admissible evidence keeps its ordinary pass/fail outcome even under unsupported repository coverage, while coverage notices remain visible.
3. Missing, conflicting, unrelated, or AI-origin evidence cannot verify a criterion.
4. A deliberately defective blanket rule that forces every unsupported-only verdict to unresolved is detected by the independent relevant-pass expected outcome.

## Actual observations

The first run failed on `SG-R001-AC010`: the draft matcher rejected the malformed criterion but then accepted the `SG-R001` prefix. The requirement-token boundary was tightened to suppress a requirement candidate followed by an `-AC` criterion suffix. The identical command was rerun after that correction.

The corrected run passed:

- 6 token-boundary fixtures, including exact criterion/requirement IDs, underscore and prefix decoys, punctuation, and malformed criterion suffix.
- 18 verdict cases across supported/partial/unsupported coverage and no evidence, relevant pass/fail, conflict, unrelated green result, and AI claim.
- The blanket unsupported-only mutant was detected because it disagreed with the specified relevant-pass result.
- Coverage notices were retained for partial and unsupported analysis in every matrix row.

Expected and actual values are retained in the machine-readable output. The harness and fixture fingerprints identify the bytes used in this run. No independent model adjudication was used; expected results are explicit in the inert fixture table.

## Feasibility conclusion and limitations

The observations support feasibility of the **design contracts for exact catalog-token recognition and separation of coverage status from evidence admissibility** in this bounded synthetic harness. They do not validate the SG-04A product implementation because none exists in the executed path. They do not demonstrate assertion quality, reviewer behavior, persistence, UI/export consistency, framework indexing, parser safety, session security, runner isolation, provider controls, or integrated MVP workflow.

This evidence partially addresses review findings F06/F07/F09/F10 at design-contract level. It does not close D05, D07, or D12; all twelve mandatory conditions remain OPEN. Further controlled evidence remains necessary as stated in the [SG-04D closure report](SG-04D-closure.md) and authoritative [SG-03D condition register](../../docs/adr/SG-03D-m3-mandatory-conditions.md).
