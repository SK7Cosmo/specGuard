# Evidence index

This index maps lifecycle stages to their evidence locations. Add links to concrete artifacts as work occurs; keep planned evidence distinct from completed evidence.

| Stage | Evidence directory | Current state |
|---|---|---|
| Understand | [understand/](understand/) | Completed: [SG-01 desk research and discovery record](understand/SG-01.md); initial user and first target confirmed; technical decisions deferred to Specify/Design |
| Specify | [specify/](specify/) | Completed: [SG-02 requirements baseline and documentation validation](specify/SG-02.md); SG-03D secret-handling policy and criteria documented in the review closure |
| Plan | [plan/](plan/) | Framework initialized; milestone plan and [SG-00 initialization record](plan/SG-00.md) |
| Design | [design/](design/) | SG-04A architecture package, SG-04B feasibility evidence, and [SG-04D design closure](design/SG-04D-closure.md) with [bounded contract-check evidence](design/SG-04D-feasibility.md) and [document/traceability check results](design/SG-04D-document-check-results.json); remediation recorded; all D01–D12 remain OPEN; NOT READY for implementation pending product-owner approval |
| Implement | [implement/](implement/) | Framework initialized; no functionality claimed |
| Verify | [verify/](verify/) | [SG-00B report generator tests](verify/SG-00B-tests.md): 10 tests passed |
| Review | [review/](review/) | [SG-03 independent requirements review](review/SG-03-requirements-review.md), [SG-03A development-constraint revision](review/SG-03A.md) and [ADR 0002](../docs/adr/0002-milestone-driven-development-baseline.md), [SG-03B requirements remediation](review/SG-03B.md) with the [M3 Design decision register](../docs/adr/SG-03B-design-decision-register.md), [SG-03C independent re-review](review/SG-03C.md), [SG-03D conditional closure](review/SG-03D.md), and [SG-04C independent architecture/security review](review/SG-04C.md): NOT READY FOR IMPLEMENTATION; 14 findings; all D01–D12 OPEN; product-owner approval pending |
| Automate | [automate/](automate/) | [SG-00B model tracking and report automation](automate/SG-00B.md) |

## Model tracking

Codex development usage is recorded in [models/MODEL_USAGE.csv](models/MODEL_USAGE.csv). The generated aggregate is [models/MODEL_REPORT.md](models/MODEL_REPORT.md). SG-03B and SG-03C each have separate developer-confirmed planning and execution records. SG-03 is reconciled in a retrospective row; unrecovered fields remain unavailable. SG-03D records the developer-confirmed Luna / High / Default metadata. SG-04A has separate draft and documentation-closure execution records; session IDs and unobserved measurements remain unavailable. Runtime LLM usage is outside this tracking dataset.

SG-04C records developer-confirmed GPT-6.2 Sol / High, current input fingerprints, a 68-criterion independent assessment, reproduced synthetic results and concrete counterexamples. Its [review record](review/SG-04C.md) distinguishes observations from proposed verification and retains unavailable measurements as N/A. SG-04D records developer-confirmed GPT-6 Luna / High and its own execution/check evidence in the design closure report; session and usage measurements remain N/A when unobserved.

The product owner confirmed the canonical model names: `Sol` means `GPT-6.2 Sol`, and `Luna` means `GPT-6 Luna`. Use these full names in model metadata; unavailable historical models remain unavailable. The [SG-04C metadata correction](review/SG-04C-model-metadata.md) records the alias normalization and report regeneration.

## Evidence entry guidance

For each artifact, record its title, stage, date, source or command, scope, result, limitations, and links to requirement or milestone IDs where relevant. Preserve original inputs and outputs when appropriate, and never fabricate evidence.
