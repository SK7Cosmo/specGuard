# SG-03D Product-owner decision: specification secret handling

**Status:** Accepted for the requirements baseline; Design validation remains open. **Decision owner:** Product owner. **Recorded:** 2026-11-24 (Asia/Calcutta). **Source:** SG-03C condition C1 and finding F03.

## Decision

SpecGuard inspects each incoming Markdown or YAML specification for covered secrets before persistence. It rejects a specification when the configured inspection detects a covered secret or mandatory inspection cannot complete. The user receives a safe, sanitized diagnostic and must sanitize and resubmit.

Rejected secret-bearing source values must not enter persistent storage, logs, caches, exports, session evidence, or remote AI payloads. The system does not silently redact and accept the specification as the exact original source, and does not encrypt and retain the original rejected specification. Successfully accepted specifications retain their exact source bytes and source locations and use the exact bytes for the digest.

Detection is limited to the configured and documented supported classes and patterns. The requirement makes no claim that every possible secret is detectable. Design must identify the supported scope and demonstrate the required boundary behavior before dependent implementation.

## Consequences and verification

This decision resolves the requirements-level policy choice. It does not demonstrate detector coverage, parser safety, persistence isolation, or source-view feasibility. SG-R004-AC02 and its test case define the observable outcome. The mandatory M3 gates are recorded in the [Design conditions register](SG-03D-m3-mandatory-conditions.md).

