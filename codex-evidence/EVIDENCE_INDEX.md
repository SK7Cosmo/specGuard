# Evidence index

This index maps lifecycle stages to their evidence locations. Add links to concrete artifacts as work occurs; keep planned evidence distinct from completed evidence.

| Stage | Evidence directory | Current state |
|---|---|---|
| Understand | [understand/](understand/) | Completed: [SG-01 desk research and discovery record](understand/SG-01.md); initial user and first target confirmed; technical decisions deferred to Specify/Design |
| Specify | [specify/](specify/) | Completed: [SG-02 requirements baseline and documentation validation](specify/SG-02.md); SG-03D secret-handling policy and criteria documented in the review closure |
| Plan | [plan/](plan/) | Framework initialized; milestone plan and [SG-00 initialization record](plan/SG-00.md) |
| Design | [design/](design/) | SG-04A through SG-04E evidence preserved. [SG-04R lifecycle restructuring](design/SG-04R.md), [lifecycle ADR](../docs/adr/SG-04R-lifecycle-restructuring.md), [implementation decisions](../docs/adr/SG-04R-implementation-decisions.md), and [consolidated roadmap](../docs/design/SG-04R-implementation-roadmap.md) define prospective component-level activation. D01–D12 remain OPEN. |
| Implement | [implement/](implement/) | [Phase 04 BUILD, SG-05A Foundation and Local Authority](implement/SG-05A.md); [SG-05A-META lifecycle, model evidence, and Vercel readiness](implement/SG-05A-META.md); [Vercel deployment readiness ADR](../docs/adr/SG-05A-vercel-readiness.md) |
| Verify | [verify/](verify/) | [SG-00B report generator tests](verify/SG-00B-tests.md): 10 tests passed |
| Review | [review/](review/) | [SG-03 independent requirements review](review/SG-03-requirements-review.md), [SG-03A development-constraint revision](review/SG-03A.md) and [ADR 0002](../docs/adr/0002-milestone-driven-development-baseline.md), [SG-03B requirements remediation](review/SG-03B.md) with the [M3 Design decision register](../docs/adr/SG-03B-design-decision-register.md), [SG-03C independent re-review](review/SG-03C.md), [SG-03D conditional closure](review/SG-03D.md), and [SG-04C independent architecture/security review](review/SG-04C.md): NOT READY FOR IMPLEMENTATION; 14 findings; all D01–D12 OPEN; product-owner approval pending |
| Automate | [automate/](automate/) | [SG-00B model tracking and report automation](automate/SG-00B.md) |

## Model tracking

Codex development usage is recorded in [models/MODEL_USAGE.csv](models/MODEL_USAGE.csv). The generated aggregate is [models/MODEL_REPORT.md](models/MODEL_REPORT.md). SG-03B and SG-03C each have separate developer-confirmed planning and execution records. SG-03 is reconciled in a retrospective row; unrecovered fields remain unavailable. SG-03D records the developer-confirmed Luna / High / Default metadata. SG-04A has separate draft and documentation-closure execution records; session IDs and unobserved measurements remain unavailable. Runtime LLM usage is outside this tracking dataset.

SG-04C records developer-confirmed GPT-6.2 Sol / High, current input fingerprints, a 68-criterion independent assessment, reproduced synthetic results and concrete counterexamples. Its [review record](review/SG-04C.md) distinguishes observations from proposed verification and retains unavailable measurements as N/A. SG-04D records developer-confirmed GPT-6 Luna / High and its own execution/check evidence in the design closure report; session and usage measurements remain N/A when unobserved.

The product owner confirmed the canonical model names: `Sol` means `GPT-6.2 Sol`, and `Luna` means `GPT-6 Luna`. Use these full names in model metadata; unavailable historical models remain unavailable. The [SG-04C metadata correction](review/SG-04C-model-metadata.md) records the alias normalization and report regeneration.

The [lifecycle registry](models/LIFECYCLE_REGISTRY.yaml) is authoritative for phase IDs, machine-readable lifecycle values, task mappings, and structured-field vocabularies. The validated ledger generates [MODEL_REPORT.md](models/MODEL_REPORT.md) and [MODEL_METRICS.json](models/MODEL_METRICS.json). The SG-05A-META [BUILD evidence](implement/SG-05A-META.md) records the verified baseline, normalization and current execution metadata.

The SG-05A-META Vercel readiness addendum records the local/hosted deployment profiles and official platform documentation checked. `python -m scripts.generate_model_report` also emits `frontend/public/analytics/model-metrics.json`, a schema-versioned sanitized static asset intended for a future frontend-only Vercel project. No dashboard or deployment is claimed.

SG-04E records developer-confirmed GPT-6.2 Sol / High and the observed Codex session ID. Its [Design evidence](design/SG-04E.md) records the documentation checks and unobserved usage measurements.

SG-04R records developer-confirmed GPT-6 Luna / High, the observed Codex session ID, and the starting Git commit. Its [Design evidence](design/SG-04R.md) and [model usage record](models/MODEL_USAGE.csv) record actual commands and validation scope; unavailable duration/token/resource measurements remain N/A.

## Evidence entry guidance

For each artifact, record its title, stage, date, source or command, scope, result, limitations, and links to requirement or milestone IDs where relevant. Preserve original inputs and outputs when appropriate, and never fabricate evidence.

SG-05A records developer-confirmed GPT-6.2 Astra / High and the observed session ID. Its [BUILD record](implement/SG-05A.md) links the controlled HTTP, UI, migration and regression evidence.
