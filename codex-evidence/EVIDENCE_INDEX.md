# Evidence index

This index maps lifecycle stages to their evidence locations. Add links to concrete artifacts as work occurs; keep planned evidence distinct from completed evidence.

| Stage | Evidence directory | Current state |
|---|---|---|
| Understand | [understand/](understand/) | Framework initialized; no discovery evidence recorded |
| Specify | [specify/](specify/) | Framework initialized; no requirements evidence recorded |
| Plan | [plan/](plan/) | Framework initialized; milestone plan and [SG-00 initialization record](plan/SG-00.md) |
| Design | [design/](design/) | Framework initialized; no design evidence recorded |
| Implement | [implement/](implement/) | Framework initialized; no functionality claimed |
| Verify | [verify/](verify/) | [SG-00B report generator tests](verify/SG-00B-tests.md): 10 tests passed |
| Review | [review/](review/) | Framework initialized; no review evidence recorded |
| Automate | [automate/](automate/) | [SG-00B model tracking and report automation](automate/SG-00B.md) |

## Model tracking

Codex development usage is recorded in [models/MODEL_USAGE.csv](models/MODEL_USAGE.csv); the generated aggregate is [models/MODEL_REPORT.md](models/MODEL_REPORT.md). Developer-confirmed model and effort metadata for SG-00 and SG-00B is recorded; measurements not supplied or otherwise unavailable remain `N/A`. Runtime LLM usage is outside this tracking dataset.

## Evidence entry guidance

For each artifact, record its title, stage, date, source or command, scope, result, limitations, and links to requirement or milestone IDs where relevant. Preserve original inputs and outputs when appropriate, and never fabricate evidence.
