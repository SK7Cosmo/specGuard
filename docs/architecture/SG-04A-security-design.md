# SG-04A Security Design

**Status:** Design baseline for product-owner approval; threat controls are proposed and unvalidated. The product-owner secret policy in [SG-03D ADR](../adr/SG-03D-secret-handling-decision.md) remains authoritative. No security condition is closed by this document.

## Assets and security objectives

| Asset | Objective |
|---|---|
| Developer host, credentials and source repository | Read only the selected commit; never expose host credentials or write to the source; do not execute repository code outside approved isolation |
| Rejected specification content | Never persist or expose covered secret values in storage, logs, caches, exports, session evidence or remote payloads; fail closed on incomplete inspection |
| Accepted specification | Preserve exact accepted bytes and digest; restrict access to the local authorized audit |
| Audit and verification evidence | Preserve provenance, integrity and baseline applicability; distinguish observations from inference and unresolved evidence |
| Runner environment | Execute only exact approved invocation once, in bounded disposable isolation; prevent network/credential/source-write escape and block after uncertain teardown |
| Remote AI payload and provider credentials | Send only exact sanitized, consent-bound payload to displayed endpoint; keep provider authentication material out of excerpts/evidence |
| Local browser session | Reject disallowed Host/Origin or absent/invalid/expired/revoked proof before protected disclosure or mutation |

## Trust boundaries

1. Browser ↔ loopback FastAPI process: local authority, session proof, Host/Origin validation and safe UI rendering.
2. FastAPI workflow ↔ Git/spec/report adapters: untrusted inputs, snapshot scoping, byte/depth limits and atomic validation.
3. Verification core ↔ source artifacts: read-only static data; no imports or application execution.
4. Host controller ↔ disposable runner: single-use command binding, nonprivileged isolation, resource enforcement, process termination and teardown verification.
5. Local process ↔ remote provider: explicit per-audit exact payload/endpoint consent, redaction, bounded response and redirect refusal.
6. Persistent store ↔ UI/export: integrity check, untrusted inert rendering, secret-safe diagnostics, revision and freshness rules.

## Threat handling

| Threat | Primary design control | Fail-closed response | Proof gate |
|---|---|---|---|
| Malicious/missing Git object, path escape, symlink or submodule | Full commit pin; object/path allowlist; no fetch; normalized in-tree paths | Reject before baseline activation; source and earlier audit unchanged | D06 |
| Hostile or oversized Markdown/YAML/XML | Bounded parsers; duplicate/unsafe construct rejection; no external retrieval | Reject atomically with safe rule/limit diagnostic | D01, D06 |
| Covered secret in incoming spec | Mandatory detector before persistence/downstream path; retain only exact bytes after successful inspection | Reject and discard transient input; require sanitized resubmission; safe diagnostic only | D01 |
| Hostile stored/imported markup or text | Escape as inert content; no active HTML/navigation/action; output encoding at every sink | Withhold unsafe rendering/export preview | D04 |
| Misleading or unrelated test report | Preserve original result/provenance; map baseline, test identity, assertion, criterion and relevance | Report remains inspectable but cannot support unrelated criterion | D05 |
| Local browser-origin abuse | Loopback bind; exact Host/port; authorized UI session proof; same-origin mutations; reject originless mutation | Deny before data disclosure/state change | D08 |
| Malicious repository tests or resource exhaustion | Exact one-attempt approval; disposable nonprivileged runner; no network/host credentials/writable source; resource limits | Block if setup absent; incomplete on overruns; never run on host | D03, D09 |
| Runner teardown uncertainty or orphan process | Verify process tree and environment removal; persist blocked state across restart | Block later execution until recovery proof and fresh approval | D03, D09 |
| Secret in imported output or outbound excerpt | Redact before persistence, preview, logs, export and provider transmission; withhold on validation failure | Sanitized reason; preserve prior evidence/verdict; no unsafe output | D10 |
| Provider consent race, payload/endpoint mutation or redirect | Bind consent to audit+exact bytes+full endpoint; recheck at dispatch; disable redirects | No request if binding differs; redirect target receives none; no suggestion adoption on failure | D10 |
| Corrupted or stale artifact | Digest verification; baseline/semantic revision binding; retained history | Exclude altered/stale evidence from current verdict; show reason | D11 |

## Specification secret-handling sequence

1. Accept bytes into a bounded, nonpersistent intake buffer.
2. Inspect the complete input for configured documented secret classes before parsing that could persist, logging, caching, evidence creation, source view, export or remote request construction.
3. On detected covered secret, detector unavailability/error, or inability to establish a safe result: terminate intake, discard buffer and derived values, return only a sanitized reason, and require sanitized resubmission.
4. Only after a successful inspection and format validation, persist the exact accepted bytes, digest and safe source locations.
5. If output redaction/validation for other evidence cannot establish safety, withhold the affected output and record a sanitized failure.

The configured classes/patterns are bounded; no claim of detecting every possible secret is made. The SG-03D decision forbids silent redaction-and-acceptance and encrypted retention of a rejected original.

## Failure and recovery rules

- Deny protected requests before disclosure or mutation if authority proof is invalid.
- Failed intake, parser or report validation is atomic and does not replace an active baseline or earlier evidence.
- Interrupted, blocked, skipped or over-limit operations are not passing criterion evidence.
- Any uncertain runner setup/teardown blocks additional runs across service restart until documented cleanup verification; subsequent attempts require fresh approval.
- Provider errors, redirects, malformed/oversized responses or invalid references yield visible sanitized failure and no adopted suggestion or verdict promotion.
- Keep earlier evidence, verdicts and audit revisions addressable. Retry with idempotency to avoid duplicate evidence.
- Treat all source, report, test-output and provider text as untrusted at every UI/export sink.

## Residual risk and proof boundary

The product threat model does not claim protection from a compromised developer account, hostile local process able to steal session proof, compromised host, compromised isolation backend or attacks outside configured resource limits. These exclusions and limits require product-owner review. This document is design evidence only; controlled detector, browser-origin, parser, runner, provider and persistence demonstrations remain mandatory under D01–D11.

## SG-04D boundary clarifications

### Intake before persistence

The security boundary begins at the actual HTTP receive path, before framework upload spooling, request-body logging, tracing, temporary files, cache insertion, parser invocation, or error capture. The implementation must use bounded streaming or an equally demonstrated no-persistence receive path; disable or sanitize body capture at middleware/proxy/access-log layers; and discard rejected content and transient buffers on every exit. Detector classes and limits remain those in the accepted secret-handling decision. Detector error or inability to complete inspection fails closed. Accepted source bytes are retained byte-for-byte only after inspection. Derived diagnostics and metadata receive their own covered-secret inspection before persistence or display. D01's sink inspection and byte-exact reopen proof remain mandatory.

Markdown/YAML/JUnit parsers must be schema-directed and bounded by documented byte, depth, alias, node, scalar, entity, and record-count limits. Duplicate IDs/keys are rejected rather than silently overwritten. XML external retrieval and entity expansion are disabled. Git access uses pinned object reads without checkout hooks, filters, fetch, submodule traversal, or repository code. Candidate library and numeric limit selection, including invalid UTF-8 and path-escape behavior, remains open under D06.

### Session proof and state transitions

Origin and Host checks run before protected reads or writes. Originless requests are permitted only for the specifically approved nonmutating read surface; all writes, including session establishment, require origin proof and local possession/session proof. Failure precedes data disclosure and state change. Proof never appears in a URL, referrer, application log, export, or persistent browser storage. The exact bootstrap/transport, topology, lifetimes, restart behavior and revocation remain product-owner decisions under D08; no real request matrix has been observed.

### Findings and current evidence boundary

SG-04C is a design/security review of documentation, proof sketches, and inert counterexamples; it does not report a production exploit. Its observed false assurance cases are confined to synthetic SG-04B expressions. The supported conclusion is that the design and evidence are insufficient for implementation readiness, with the specific gate impact recorded per finding in [SG-04D closure evidence](../../codex-evidence/design/SG-04D-closure.md). No independent penetration test or product security test was performed for SG-04D.

