# SpecGuard verification policy

## Evidence and provenance

Judge each acceptance criterion against its explicitly stated expected outcome. Establish the Git commit, exact specification digest, applicable criteria and revisions, and analyzer configuration before assessing evidence. Determine the expected behavior from the original specification and reviewer-approved clarifications before using implementation or test output as evidence.

| Provenance | What it represents | How it may be used |
|---|---|---|
| Observed | A SpecGuard static check, controlled runner result, direct inspection, or recorded demonstration | Can support a verdict when the method fits the criterion, the baseline matches, and the observation directly exercises or inspects the obligation. |
| Imported | A developer-supplied report with separately recorded provenance | Can support a verdict after the reviewer confirms its baseline, test identity, criterion mapping and relevance. Preserve the original reported outcome and imported provenance. |
| Inferred | A suggested trace link, AI output, or ghost heuristic | Use to direct investigation. Confirmation can establish a link, while the behavior requires its own evidence. |
| Reviewer-confirmed | A human decision on a link, interpretation, test oracle, or evidence association | Establishes what the reviewer accepted and why. A direct manual observation supports a verdict only with a recorded setup, action, observation, and baseline. |

Start with deterministic analysis and exact identifiers. Record the method, criterion ID, original expectation, code and test references, baseline, result, and limitations. For tests also capture invocation, runner identity, enforced limits, start and finish times, exit status and sanitized output references. Unsupported proof is evidence that does not substantiate its associated acceptance criterion. A passing suite without a matching assertion is one example. Keep the reported result and provenance for inspection and exclude it from support for that criterion. A Vault digest checks artifact integrity against the recorded digest. It provides no independent attestation of the original report or protection against someone who can rewrite the entire local Vault.

## Criterion verdicts

| Verdict | Rule |
|---|---|
| Verified | Current, intact, admissible evidence directly supports the expected outcome and there is no unresolved conflicting evidence. |
| Failed | Current admissible evidence directly demonstrates a mismatch with the expected outcome, with no unresolved contradiction. |
| Unresolved | Evidence is absent, stale, skipped, blocked, incomplete, altered, insufficient, or contradictory, the criterion needs clarification, or the criterion depends on unsupported artifacts and lacks sufficient independent supported evidence. Retain the reason and prior evidence for review. |

Track operation outcomes separately from criterion verdicts. For example, a nonzero exit caused by setup failure leaves the criterion unresolved. An observed assertion failure for an unrelated test has no effect on that criterion. A confirmed trace link establishes a relationship. For a requirement with several criteria, treat it as verified only when every criterion is verified and expose each criterion’s actual state. Superseded requirements retain their evidence under their original baseline.

Use the [coverage contract](PRD.md#coverage-and-export) for repository-level scope and export. A scope notice does not by itself determine a verdict. Evaluate criteria with sufficient independent supported evidence under the ordinary verdict rules, including conflict handling. When the unsupported scope prevents a verdict, associate the unresolved criterion with the applicable scope notice and preserve any other unresolved reasons.

When an approved semantic change alters evidence applicability, retain the older result, links and provenance under the original baseline and mark the affected evidence stale for the new baseline. Reassess the baseline, criterion revision, and admissibility before reusing evidence. A reviewer-selected clarification reason and rationale stay visible while verification is unresolved.

## Verification methods

| Method | Minimum evidence |
|---|---|
| Inspection | Reviewed artifact, scope, applicable criterion, and specific observation. |
| Static analysis | Pinned inputs and analyzer version or rule configuration, matching locations, and observed findings. |
| Automated test | Independent expected outcome, fixture and test IDs, exact invocation or imported report, and outcome. |
| Manual demonstration | Repeatable setup and steps, observed behavior, baseline, reviewer, and captured evidence. |

Generate cases only from the [supported proposal rules](PRD.md#adversarial-case-proposal-rules) that the reviewer has confirmed. Keep generated cases in draft until a reviewer approves the expected outcome. Generated cases do not execute automatically. Use synthetic records and a controlled fixture to verify the generated actions and independently specified outcomes.

## Security and failure handling

### Threat model and local audit access

Protect the audit and host from unauthorized browser-origin requests, untrusted repository content and test workloads, and malformed or oversized provider responses. Treat source, specifications, reports, test output and provider data as untrusted. Render stored text safely and keep the selected source read-only. The threat model excludes compromise of the developer account, hostile local processes that can steal its session proof, a compromised host or isolation backend, and attacks outside the configured resource model. Inputs above configured limits are still rejected or stopped as specified below.

Bind only to loopback. Validate the request Host against the allowed loopback service authority, including its port. Establish session proof through the authorized local UI. Require valid, unexpired, unrevoked proof for protected reads and mutations. Reject disallowed origins and require an allowed same-origin Origin for mutations, including session establishment that changes state. Reject originless mutations. An originless protected read still requires a valid session and an allowed Host. Enforce these checks before releasing protected data or performing a state change. M3 selects the session mechanism, lifetime and invalidation settings against SG-R031-AC01.

### Snapshot and report intake

Resolve only the pinned local Git snapshot. Reject a missing commit or malformed object needed by that snapshot before activation. Reject malformed, oversized or deeply nested reports and any XML declarations that request external retrieval or entity expansion. Keep parsing within configured limits. Identify the failing input, location or field when available, and the violated rule or limit. Failed intake preserves the active baseline and earlier evidence, performs no external retrieval and leaves the source unchanged. Retrying a failed step must not duplicate earlier evidence.

### Approved execution and recovery

Approve the exact executable, arguments and snapshot for one attempted run. Launch it only after verifying an approved disposable, non-privileged environment with blocked network access, no host credentials or unrelated host environment, and no writable source mount. A missing runner or setup failure blocks the command before launch. Host test execution is prohibited. Enforce and record wall-time, CPU, memory, process-count and output limits. An overrun yields an incomplete result, including when output must be truncated.

After an attempt or partially allocated setup, verify teardown of the isolation environment and removal of its resources. Upon timeout, terminate the entire process tree and verify that no descendants remain. Unverified cleanup records a visible failure and marks a launched run incomplete. Block further execution through service restarts until recovery documents verified cleanup. A subsequent run requires fresh invocation approval. Preserve earlier evidence during a failure or recovery.

### Redaction and remote suggestions

For specification intake, inspect the complete incoming source for the configured, documented supported secret classes before any persistence. Reject detected covered secrets and fail closed if mandatory inspection is unavailable, errors, or cannot establish a safe result. Return only a sanitized reason and ask the developer to sanitize and resubmit. Do not persist or retain rejected values in storage, logs, caches, exports, session evidence, or remote AI payloads; do not encrypt and retain the rejected original. Do not silently redact then accept it as the exact source. For successful intake, retain and hash the exact source bytes. Detection is bounded to the documented classes and patterns; it does not establish detection of all possible secrets.

For other evidence and outbound AI excerpts, redact secrets before evidence storage, logs, export, consent preview or provider transmission. Cover representative API token, password and private-key material using synthetic acceptance examples. Keep provider authentication material and unrelated environment data out of excerpts and evidence. This coverage is bounded to configured secret classes. When redaction or validation cannot establish safe output, withhold the affected content and record a sanitized reason.

Remote AI is disabled by default. Display the exact sanitized outbound payload and provider endpoint, including scheme, host, port, path and any query. Bind developer approval to the payload bytes, endpoint and audit. Recheck that binding and current approval at dispatch. Withhold transmission when disabled, denied or revoked, or when the payload bytes, endpoint or audit change without fresh approval. Never follow a provider redirect.

Apply configured timeout and response-size limits. A timeout, error status, redirect, malformed response or oversized body yields a visible failure without adopting suggestions. Validate each suggestion's criterion or requirement ID and its artifact path and location against the pinned index. Reject invalid references with a reason and keep valid suggestions inferred and awaiting review. If no references are valid, report the failure. Provider data cannot promote a verdict. Preserve earlier evidence and verdicts and keep deterministic and manual verification available throughout.

Use the [requirements catalog](REQUIREMENTS.yaml) for individual obligations and the [test plan](TEST_PLAN.md) for acceptance oracles.
