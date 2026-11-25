# SG-04A Proposed Local API Contracts

**Status:** Design contract for product-owner review; endpoint names and transport details remain proposals. No API implementation or compatibility promise exists. D06, D08, D10 and D11 remain open.

## Contract conventions

- Base path: `/api/v1`; JSON responses use UTF-8 and explicit schema versions for exports and persisted records.
- All protected reads and mutations require validated local authority/session proof and the Host/Origin rules in the verification policy. State-changing requests require same-origin proof and an idempotency key when replay could duplicate work.
- IDs in a body must resolve within the path audit and active baseline. Unknown enum/schema values, duplicate keys/IDs, path escapes and illegal state transitions are rejected.
- Input size, nesting, count, execution and response limits are selected under M3. A rejected input is atomic: no partial baseline/evidence becomes active.
- Errors never echo untrusted source, rejected secrets, provider credentials, test output or stack traces. Safe identifiers, rule/limit codes and correlation IDs may be returned.

## Endpoint proposal

| Method/path | Request intent | Success result | Important validation/failure |
|---|---|---|---|
| `POST /api/v1/audits` | Create draft using local repository selection and full commit ID | Audit ID and draft state | Resolve commit and required objects before activation; no fetch or source mutation |
| `POST /api/v1/audits/{auditId}/specification` | Submit Markdown/YAML bytes | Accepted digest, format, requirement/criterion IDs and source locations | Secret inspection before persistence; detected covered secret or incomplete inspection returns sanitized reject and requires resubmission; never returns rejected bytes |
| `POST /api/v1/audits/{auditId}/index` | Build static index for pinned baseline | Index version, supported artifacts and coverage notices | No application import/run; bounded and repeatable for the same baseline/version |
| `GET /api/v1/audits/{auditId}` | Read audit summary and active baseline | Explicit state, revision, coverage, progress and summary counts | Authority proof before protected data disclosure |
| `GET /api/v1/audits/{auditId}/requirements` | Read requirements, criteria, links and verdicts | Paged/filterable records with provenance and unresolved reasons | State fields distinguish candidate/inferred/confirmed and verified/failed/unresolved |
| `POST /api/v1/audits/{auditId}/links/{linkId}/review` | Review candidate link | Updated review state and reviewer attribution | Allowed transition and rationale validation; AI candidate remains unconfirmed until action |
| `POST /api/v1/audits/{auditId}/cases/{caseId}/approve` | Approve edited case and expected outcome | Approved case revision with reviewer | Criterion revision and explicit declared outcome required; cannot auto-execute |
| `POST /api/v1/audits/{auditId}/reports` | Import JUnit XML | Report evidence ID and case outcome inventory | Enforce byte/depth limits and reject external retrieval/entity expansion atomically |
| `POST /api/v1/audits/{auditId}/runner-approvals` | Approve exact executable, args, baseline and runner policy for one attempt | Approval ID and binding digest | Reviewable exact invocation; proof lifetime/consumption governed by D03/D09 |
| `POST /api/v1/audits/{auditId}/runs` | Consume approval and request one run | Operation ID; later operation result | Recheck exact binding; fail closed if runner unavailable/setup/teardown uncertain; no host fallback |
| `POST /api/v1/audits/{auditId}/ai-preview` | Build exact sanitized proposal request | Exact displayable payload bytes, digest and full endpoint | Withhold content if redaction/validation cannot establish safe output |
| `POST /api/v1/audits/{auditId}/ai-approvals` | Record per-audit consent for preview | Approval binding digest and state | Bind audit, payload bytes and endpoint; new values require fresh approval |
| `POST /api/v1/audits/{auditId}/ai-suggestions` | Dispatch currently approved request | Operation ID and validated inferred suggestions | Recheck consent and binding; no redirects; bound response; validate every ID/path/location; never promote verdict |
| `GET /api/v1/audits/{auditId}/operations/{operationId}` | Inspect asynchronous operation | State, safe failure, linked outputs | Sanitized diagnostics; preserve previous evidence |
| `GET /api/v1/audits/{auditId}/export?format=json&version=1` | Export audit snapshot | Versioned JSON document | Exclude rejected source, unreviewed model payloads and unsafe content; stable scope notice references |

## Example response shapes

Accepted specification:

```json
{
  "audit_id": "aud_…",
  "baseline_revision_id": "base_…",
  "state": "accepted",
  "specification": {
    "format": "yaml-v1",
    "sha256": "…",
    "source_bytes_preserved": true,
    "requirement_count": 1,
    "criterion_count": 1
  }
}
```

Sanitized rejection (no source value or excerpt):

```json
{
  "error": {
    "code": "SPEC_SECRET_DETECTED",
    "safe_message": "Remove covered sensitive material and submit the specification again.",
    "retryable": false,
    "operation_id": "op_…",
    "rule_or_limit": "configured-secret-class",
    "correlation_id": "…"
  }
}
```

Criterion result:

```json
{
  "criterion_id": "SG-R001-AC01",
  "semantic_revision": 1,
  "verdict": "unresolved",
  "reason_codes": ["NO_ADMISSIBLE_ASSERTION", "UNSUPPORTED_SCOPE"],
  "evidence_ids": [],
  "scope_notice_ids": ["scope_…"]
}
```

The examples are illustrative contract shapes, not a selected public API or generated runtime output.

## Error semantics

| HTTP class (proposed) | Meaning | Required behavior |
|---|---|---|
| 400 | Invalid syntax/schema, duplicate key/ID, malformed request | Reject atomically; identify safe field/rule |
| 403 | Local authority/session/origin proof failed | Reject before protected disclosure or state change |
| 404 | Unknown audit-scoped object | Do not reveal objects from another audit |
| 409 | Baseline changed, approval binding stale/consumed, illegal transition | Preserve prior state; require fresh review/approval where appropriate |
| 413 | Configured input/response size exceeded | Withhold/stop affected input; no partial persisted result |
| 422 | Well-formed but unsupported/semantically invalid input | Return sanitized reason and supported scope; no false verification |
| 500/503 | Internal/dependency unavailable | Safe generic diagnostic, correlation ID, preserve prior audit state |

Exact status-code mapping, pagination, authentication-proof transport, content streaming and operation polling cadence remain unresolved. M3 proofs D06, D08, D10 and D11 govern these boundaries. Error behavior must remain fail-closed regardless of status code.

## SG-04D workflow contract completion (proposed)

The following behavioral operations are required by the approved workflow even if endpoint names or transport shape later change. Every write uses an audit-scoped idempotency key, canonical request digest, expected object revision, and validated same-audit/baseline references. Reusing a key with different bytes returns conflict. A stale revision or illegal transition makes no partial change.

| Operation | Request fields | Result and transition |
|---|---|---|
| Stage specification candidate | source bytes, source kind, parent baseline, client operation ID | Secret inspection precedes parsing or persistence; accepted candidate is staged and cannot become active; rejected bytes are discarded. |
| Classify clarification/change | candidate ID, per-criterion classification, source spans, rationale, expected baseline revision | Records clarification or semantic-change proposals. Replacement/split/retirement require explicit target relationships. |
| Decide and activate candidate | candidate ID, reviewer decision, rationale, expected active baseline revision | Reject preserves current active baseline. Approval atomically activates a new immutable baseline and records lineage; no cross-baseline ID reuse. |
| Create or decide trace link | criterion revision, target artifact/test identity, origin, decision, rationale, expected link revision | Supports manual link creation and confirm/reject/dismiss/edit. A stale concurrent edit conflicts. |
| Edit/approve rule and case | typed rule family, criterion revision, fields/domains/bounds/states/outcomes; or case revision and reviewer decision | Reject incomplete/contradictory rules. Draft generation is deterministic; case review is separate from execution approval. |
| Map imported assertion | evidence ID, assertion/test identity, criterion/case revision, inspected assertion summary, relevance decision, rationale | Original report outcome/provenance is immutable. Reviewer mapping alone cannot override integrity, freshness, completeness or contradictory evidence checks. |
| Dismiss finding | finding ID, expected revision, reviewer, rationale | Persists a review decision without changing requirement verdict or deleting the original finding. |
| Reopen/export audit | audit and baseline identity, export format version | Revalidates stored artifact digests and evidence applicability before serving verdicts or export; preserves historical revisions. |

State transition summary:

```text
Active baseline -> staged candidate -> [rejected | approved + atomically activated successor]
Trace candidate -> [confirmed | rejected | dismissed | edited] (review decision retained)
Rule revision -> generated draft case -> [rejected | approved] -> separately approved runner attempt
Imported report -> parsed immutable result -> inspected assertion -> reviewer relevance decision -> evaluator
Runner approval -> consumed attempt -> [complete | incomplete | cleanup blocked] -> verified recovery + fresh approval
```

The complete request schemas, persistence ordering and conflict semantics must be exercised in the D11 and D12 design dry run. Route contracts do not authorize implementation and do not close those gates.

## Authority and transport decisions still open

Protected operations require proof before body disclosure or mutation. Originless mutations, including proof establishment, are rejected. A same-origin deployment topology, loopback host/port allowlist (including IPv4/IPv6), bootstrap possession mechanism, proof transport/storage/lifetime/revocation, and restart semantics require product-owner disposition and the D08 request matrix. No secret or bearer proof is placed in URL or persistent browser storage in this proposal; the concrete safe bootstrap mechanism remains unselected.

Provider requests carry only the exact previewed serialized bytes and full destination bound to current consent. Redirects are refused and a revocation linearization check occurs immediately before dispatch. The proposal response schema is versioned and has no action/evidence/verdict fields; every string is untrusted. Endpoint/address/TLS/proxy/credential rules, body/timeout limits and response streaming policy remain open for D10 and product-owner disposition. The API does not create a new mandatory provider or change optional AI consent.

