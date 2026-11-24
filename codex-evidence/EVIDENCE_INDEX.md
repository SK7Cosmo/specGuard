# Evidence index

This index maps lifecycle stages to their evidence locations. Add links to concrete artifacts as work occurs; keep planned evidence distinct from completed evidence.

| Stage | Evidence directory | Current state |
|---|---|---|
| Understand | [understand/](understand/) | Completed: [SG-01 desk research and discovery record](understand/SG-01.md); initial user and first target confirmed; technical decisions deferred to Specify/Design |
| Specify | [specify/](specify/) | Completed: [SG-02 requirements baseline and documentation validation](specify/SG-02.md) |
| Plan | [plan/](plan/) | Framework initialized; milestone plan and [SG-00 initialization record](plan/SG-00.md) |
| Design | [design/](design/) | Framework initialized; no design evidence recorded |
| Implement | [implement/](implement/) | Framework initialized; no functionality claimed |
| Verify | [verify/](verify/) | [SG-00B report generator tests](verify/SG-00B-tests.md): 10 tests passed |
| Review | [review/](review/) | [SG-03 independent PRD, requirements, and test-plan review](review/SG-03-requirements-review.md) (preserved); [SG-03A development-constraint revision evidence](review/SG-03A.md) and [decision 0002](../docs/adr/0002-milestone-driven-development-baseline.md) |
| Automate | [automate/](automate/) | [SG-00B model tracking and report automation](automate/SG-00B.md) |

## Model tracking

Codex development usage is recorded in [models/MODEL_USAGE.csv](models/MODEL_USAGE.csv). The generated aggregate is [models/MODEL_REPORT.md](models/MODEL_REPORT.md). Developer-confirmed model and effort metadata for SG-00, SG-00B, SG-01, and SG-02 is recorded. Unavailable measurements remain `N/A`. Runtime LLM usage is outside this tracking dataset.

## Evidence entry guidance

For each artifact, record its title, stage, date, source or command, scope, result, limitations, and links to requirement or milestone IDs where relevant. Preserve original inputs and outputs when appropriate, and never fabricate evidence.
