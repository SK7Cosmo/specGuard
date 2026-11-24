# SpecGuard verification policy

## Evidence and provenance

Judge each acceptance criterion against its explicitly stated expected outcome. Establish the Git commit, exact specification digest, applicable criteria and revisions, and analyzer configuration before assessing evidence. Determine the expected behavior from the original specification and reviewer-approved clarifications before using implementation or test output as evidence.

| Provenance | What it represents | How it may be used |
|---|---|---|
| Observed | A SpecGuard static check, controlled runner result, direct inspection, or recorded demonstration | Can support a verdict when the method fits the criterion, the baseline matches, and the observation directly exercises or inspects the obligation. |
| Imported | A developer-supplied report with separately recorded provenance | Can support a verdict after the reviewer confirms its baseline, test identity, criterion mapping and relevance. Preserve the original reported outcome and imported provenance. |
| Inferred | A suggested trace link, AI output, or ghost heuristic | Use to direct investigation. Confirmation can establish a link, while the behavior requires its own evidence. |
| Reviewer-confirmed | A human decision on a link, interpretation, test oracle, or evidence association | Establishes what the reviewer accepted and why. A direct manual observation supports a verdict only with a recorded setup, action, observation, and baseline. |

Start with deterministic analysis and exact identifiers. Record the method, criterion ID, original expectation, code and test references, baseline, result, and limitations. For tests also capture invocation, runner identity, enforced limits, start and finish times, exit status and sanitized output references. A passing suite without a matching assertion is insufficient proof. A Vault digest checks artifact integrity against the recorded digest. It provides no independent attestation of the original report or protection against someone who can rewrite the entire local Vault.

## Criterion verdicts

| Verdict | Rule |
|---|---|
| Verified | Current, intact, admissible evidence directly supports the expected outcome and there is no unresolved conflicting evidence. |
| Failed | Current admissible evidence directly demonstrates a mismatch with the expected outcome, with no unresolved contradiction. |
| Unresolved | Evidence is absent, stale, skipped, blocked, incomplete, altered, insufficient, or contradictory, or the criterion needs clarification. Retain the reason and prior evidence for review. |

Track operation outcomes separately from criterion verdicts. For example, a nonzero exit caused by setup failure leaves the criterion unresolved. An observed assertion failure for an unrelated test has no effect on that criterion. A confirmed trace link establishes a relationship. For a requirement with several criteria, treat it as verified only when every criterion is verified and expose each criterion’s actual state. Superseded requirements retain their evidence under their original baseline.

## Verification methods

| Method | Minimum evidence |
|---|---|
| Inspection | Reviewed artifact, scope, applicable criterion, and specific observation. |
| Static analysis | Pinned inputs and analyzer version or rule configuration, matching locations, and observed findings. |
| Automated test | Independent expected outcome, fixture and test IDs, exact invocation or imported report, and outcome. |
| Manual demonstration | Repeatable setup and steps, observed behavior, baseline, reviewer, and captured evidence. |

Keep generated cases in draft until a reviewer approves the expected outcome. Start with controlled product behavior cases such as numeric boundaries, invalid field values, state transitions and timeouts. Generated cases do not execute automatically. Use synthetic records and a controlled fixture for SG-02 acceptance design.

## Security and failure handling

- Bind the interface to loopback, validate Host and Origin, and require local session proof for state changes. Treat source, imported documents, returned model data, and test output as untrusted data. Parse reports without external references and render stored text safely. Keep the audit read-only with respect to the selected source.
- Approve the exact executable, arguments and snapshot for one attempted run. Start only in an approved disposable, non-privileged environment with blocked network, no host credentials, and no writable source mount. Enforce wall-time, CPU, memory, process, and output limits. Tear down the environment after an attempt. A missing runner, failed isolation check, or resource limit violation yields a blocked or incomplete check, with earlier audit work preserved.
- Redact secret values before storage in logs or exports and before any remote payload is approved. Exclude credentials and unrelated environment data from test runs and remote requests. If safe redaction or payload validation fails, withhold the affected output and record the reason.
- Keep remote AI disabled by default. Display the exact sanitized excerpts and destination for per-audit consent. A changed payload or destination invalidates prior consent. Withhold requests if approval is declined or unavailable. On provider failure preserve prior results and offer deterministic and reviewer-supplied linking. Validate suggestion IDs and paths against the audit snapshot and require review.
- Reject invalid inputs with a location or affected field and a reason. Keep the active baseline on failed import. Mark unsupported components out of coverage. Preserve completed steps when a later step fails. Retrying a failed step must not duplicate already recorded evidence.
- Treat drift as a prompt to reassess the affected evidence. Preserve links and evidence from the earlier baseline so the reviewer can see why a verdict changed.

Use the [requirements catalog](REQUIREMENTS.yaml) for individual obligations and the [test plan](TEST_PLAN.md) for acceptance oracles.
