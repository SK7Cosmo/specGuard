# SpecGuard product requirements

## Purpose and users

SpecGuard helps a solo developer using coding agents assess an existing repository against its original specification. It shows which criteria have evidence, where that evidence came from, and which gaps still need review. Small-team technical leads and QA practitioners are secondary users. Product owners may consume the findings when making release decisions. The personas and scenario prevalence remain unvalidated.

The machine-readable [requirements catalog](REQUIREMENTS.yaml) is the normative baseline. The [verification policy](VERIFICATION_POLICY.md) governs evidence and verdicts. The [test plan](TEST_PLAN.md) defines independent acceptance cases. Discovery inputs are the [problem statement](PROBLEM_STATEMENT.md), [personas](USER_PERSONAS.md), [research](RESEARCH.md), and [failure scenarios](FAILURE_SCENARIOS.md).

## Approved product scope

- A loopback-only web interface audits one local Git commit and an explicitly selected original specification per run. The MVP supports Python/FastAPI backends and React/Next.js frontends, including a repository containing both. Show supported artifact locations, reviewed and candidate links, criterion verdicts, ghost findings, and requirement-derived tests.
- Collect existing JUnit XML and run developer-approved existing test invocations in disposable isolation. Requirement-derived cases begin as reviewable inputs and expected outcomes. Existing tests are eligible only after exact invocation approval.
- Offer remote AI trace suggestions as an opt-in MVP capability. Show the exact sanitized outbound payload and provider endpoint for per-audit authorization. Revalidate both and the current consent before dispatch. A changed payload or destination requires fresh consent. Provider redirects are prohibited. Deterministic and manual trace workflows remain available without a provider.
- Inspect each incoming specification for covered secrets before persistence. Reject a specification when the configured inspection detects a covered secret or cannot complete. Give a sanitized reason and require developer sanitization and resubmission. Do not silently redact and accept it as the exact original source. Preserve the exact bytes of successfully accepted specifications.
- Export machine-readable audit evidence and allow local inspection of completed audits. The developer owns the decision to accept an interpretation, apply a repair, or release.
- Treat the repository, documents, test reports, and provider responses as untrusted input. Contain repository reads, enforce runner limits, and redact sensitive data before persistence or transmission. See the [verification policy](VERIFICATION_POLICY.md).

## Supported inputs and limits

| Input or output | MVP contract |
|---|---|
| Code snapshot | One committed local Git tree per audit. Resolve and display the full commit ID. Ignore working-tree modifications and untracked content. Refuse path escapes, symlink traversal, and submodule contents. Reject missing commits and malformed objects needed by the selected snapshot without fetching or changing the source. |
| Original specification | UTF-8 Markdown with explicit requirement and criterion sections, or YAML catalog version 1. Inspect for covered secrets before persistence. Reject detected covered secrets or an incomplete mandatory inspection, with a sanitized reason; the developer must sanitize and resubmit. Do not retain rejected source bytes or expose them to logs, caches, exports, session evidence or remote AI payloads. For an accepted specification, retain its exact bytes and source locations and hash the exact imported bytes. Detection is limited to the documented supported classes; no claim is made that all possible secrets are detected. |
| Markdown structure | Use a level-two ATX heading such as `## SG-R001`, a description, and one or more level-three criterion headings such as `### SG-R001-AC01` with explicit expected outcomes. A requirement section may also include a `Priority: P0`, `P1`, or `P2` metadata line. Missing priority is shown as unspecified until the reviewer assigns it. Ignore fenced examples and comments when identifying headings. |
| YAML structure | `schema_version: 1` and a `requirements` sequence. The canonical entry shape and enums are defined below. Treat YAML as plain data. Reject duplicate keys, duplicate identifiers, unsafe tags and unsupported versions. |
| Existing test results | User-selected JUnit XML with test identity and outcome. Accept passing, failing, errored, and skipped outcomes. Reject malformed XML, reports over the byte or nesting limits, and declarations that request external retrieval or entity expansion. Unmapped imported tests may be inspected but cannot establish a criterion verdict. |
| Isolated test invocation | An existing test command represented as an executable plus arguments, bound to the selected snapshot and runner policy. Use a prepared environment with dependencies already present. Each authorization covers one attempt. |
| Audit export | Versioned JSON with the audit baseline, requirement and criterion IDs, verdicts, reasons, trace links, findings, evidence references, and coverage status and notices. Raw secrets and unreviewed model payloads are excluded. |

Set explicit limits on input bytes, parser expansion, execution time, CPU, memory, process count, and captured output. Record the enforced execution limits with the run. Numeric defaults and runner packaging belong to M3 design. Deterministic findings, normalized links and verdicts must be reproducible for the same baseline, analyzer configuration, and evidence inputs. Audit IDs and timestamps can differ.

### Coverage and export

The audit UI and versioned JSON report coverage as `supported` for supported-only repositories, `partial` for mixed repositories, or `unsupported` for unsupported-only repositories. Partial audits continue with the supported artifacts. Unsupported-only audits display an unsupported outcome and allow diagnostic export.

The JSON `coverage` record contains `status` and a `notices` array. Each notice has an `id` stable within the baseline, a snapshot `path` or `component`, and a `reason`. The audit baseline identifies the snapshot for all notices. Retain these notices when reopening an audit. A criterion with unresolved unsupported coverage references the relevant notices in the UI and includes their IDs in `scope_notice_ids` in the export. Coverage notices identify analyzer scope. Apply the [criterion verdict rules](VERIFICATION_POLICY.md#criterion-verdicts) to the actual evidence for each criterion.

### Canonical catalog contract

Each YAML record has an `id`, `feature`, `type`, `description`, `priority`, `acceptance_criteria`, `verification_method`, `sources`, and `depends_on`. Types are `functional`, `non_functional`, and `security`. Priorities are P0, P1, and P2. Criterion records have an `id` and `expected` outcome. Verification methods are `inspection`, `static_analysis`, `automated_test`, and `manual_demonstration`. Source references are paths relative to the catalog with optional heading fragments. Dependencies are IDs in the catalog and form an acyclic graph.

Requirement IDs use `SG-R` and a three-digit sequence. Criteria append `-AC` and a two-digit sequence. Track a semantic revision for each requirement and criterion, starting at 1. Reordering and wording-only edits preserve both the identity and semantic revision. A change to the imported bytes still produces a new specification digest. The reviewer records the classification and rationale for an edit.

A changed threshold or expected outcome within a continuing obligation retains its requirement and criterion IDs and increments the affected semantic revisions. Replacement of a fundamentally different obligation assigns new identities and records its predecessor. A split retires the compound parent and assigns new IDs to the child obligations and criteria, with lineage to the parent and the source criteria where applicable. Retiring an obligation removes it from active verification and preserves its ID, previous revisions, links and evidence. Retired IDs are never reused.

Semantic edits, replacements, splits and retirements require explicit reviewer approval before activation. Pending or declined changes leave the original baseline active. For an approved change, mark evidence whose applicability changed as stale for the new baseline. Keep it addressable under the original baseline and verify applicability before reusing any prior evidence.

### Deterministic analyzer boundary

In the supported snapshot index, exact and case-sensitive references to known requirement or criterion IDs produce trace candidates for the complete identifier. For this rule, a token ends at a character outside letters, digits, underscore and hyphen. A complete criterion ID matches the criterion without generating a separate candidate from its requirement-ID prefix. Record the matching signal and source location. Manual or reviewed AI suggestions can supply links without an exact match.

Ghost candidates carry a rule and source location. The MVP recognizes these patterns in supported artifacts:

- A recognized FastAPI route with a single executable statement of `raise NotImplementedError`, `raise NotImplementedError()`, `pass`, or an ellipsis expression. A docstring does not count as an implementation.
- A React interactive control whose event is attached to an inline or statically resolved local function with an empty block body.
- An indexed route that directly returns literal sample data with an adjacent `specguard:sample` comment on the return or immediately preceding it.

Dynamic handlers, unmarked literals and indirect service returns are outside those rules. Candidates require review and behavioral evidence. For unclear prose, the reviewer can select a reason such as vague, compound or other and record why clarification is needed. The workflow verifies that the classification and rationale were recorded and defers verification while clarification is pending.

### Adversarial case proposal rules

Use a structured rule that a reviewer confirms against a criterion ID and semantic revision. The rule supplies an explicit expected outcome for each case condition. The rule may be recorded for a criterion from either supported specification format. The original specification remains the source of the expected behavior.

| Rule | Required inputs and generated cases |
|---|---|
| Numeric bound | Identify the field, integer or exact-decimal domain, at least one lower or upper bound, inclusivity at each bound, and a representable step. Integers use a unit step. Decimals declare a positive step at their declared precision. Generate cases one step below, at, and one step above each applicable bound. Evaluate the declared bounds together and use the supplied valid or violation outcome. |
| Field constraint | Identify the field, required status, primitive type (string, Boolean, integer or decimal), and allowed values when constrained. Use a typed valid example and generate missing, wrong-type and correctly typed out-of-domain inputs as applicable. Use the declared outcome for each applicable constraint. Use a reviewer-set counterexample when a representative value is needed. If a violation is impossible for the declared domain, record it as inapplicable. |
| State transition | Declare states and the action, source state and destination for each tested transition. Specify whether each transition is allowed or rejected and its expected outcome. Generate cases for the stated transitions using synthetic records. Undeclared transitions receive no inferred outcome. |
| Documented failure | Name a documented condition such as a timeout and supply its trigger or setup and expected outcome. Generate a draft that records all three. |

Report conflicting, underspecified or unsupported rules with a reason and withhold any inferred expected outcome. Unstructured prose remains available for reviewer clarification or manual case design. Generated cases remain drafts for reviewer approval and execution requires the existing invocation approval flow.

## User journeys

| Journey | Actions | Observable completion |
|---|---|---|
| Audit an existing repository | Open the local app, select a repository and commit, import the original specification, and inspect the baseline and trace candidates. Optionally approve context for AI suggestions. | Requirements and criteria appear with source locations. Findings and unknowns are visible. Export opens as versioned JSON tied to the displayed baseline. |
| Investigate a gap | Open an unlinked criterion or ghost candidate, inspect the indicated artifact and rule, then confirm a trace link, dismiss the candidate with a reason, or leave the gap unresolved. | The graph and Vault retain the reviewer’s decision, provenance, and any unresolved evidence need after reopening the audit. |
| Verify behavior | Review a proposed boundary or failure-path case and approve its expected outcome. Link an existing test, then import its report or approve a controlled run. | The criterion shows the applicable evidence and verdict, or a specific reason such as a skipped test, stale baseline, timeout, or unavailable runner. |

## Feature dependencies and priorities

| Feature | Priority and IDs | Depends on |
|---|---|---|
| Requirement DNA | P0 · SG-R001–SG-R007 | Original specification and reviewer-confirmed meaning |
| Spec-to-Code Traceability Graph | P0 · SG-R008–SG-R013 | Requirement IDs, static snapshot index, reviewer decisions, AI consent for remote suggestions |
| Evidence Vault | P0 · SG-R014–SG-R019 | Pinned baseline, reviewed trace context, report or controlled runner results |
| Ghost Feature Detector | P0 · SG-R020–SG-R023 | Snapshot index and reviewable findings |
| Adversarial Requirement Testing | P0 · SG-R024–SG-R029 | Confirmed criteria, test links, Vault for results |
| Local workflow, security, and operational quality | P0 · SG-R030–SG-R039 | P0 feature contracts, local web boundary, isolation and data-handling policies |
| Visual Reality Check | P1 · SG-R040–SG-R042 | Pinned baseline, controlled scripted fixture, approved reference and threshold |
| Specification Drift Radar | P1 · SG-R043–SG-R045 | Two baselines and confirmed artifact links |
| Release Confidence Index | P1 · SG-R046–SG-R048 | Criterion verdicts and their supporting evidence |
| Verification Intelligence Console | P1 · SG-R049–SG-R051 | Persisted audits, graph, evidence, and baseline comparisons |
| Surgical Repair Engine | P2 · SG-R052–SG-R054 | Confirmed criterion and finding, linked checks, human patch review |

P0 gates MVP. P1 extends the initial workflow after MVP. P2 is stretch scope. The Release Confidence Index communicates measured criterion coverage and open gaps. Coverage is the verified criterion count divided by all criteria in the selected baseline, with no applicable result for an empty baseline.

## Explicit non-goals

- Hosted service, multi-tenant access, or enterprise evidence retention.
- Arbitrary languages, universal natural-language document parsing, production testing, or runtime instrumentation across arbitrary frameworks.
- Absolute correctness certification, calibrated probability of release success, or autonomous release approval.
- Automatic patch application or repository changes.
- External integrations, scheduled audits, and cross-repository analysis in the initial release.

## MVP completion criteria

1. All 53 criteria across the 39 P0 requirements have passing acceptance evidence, including import of the catalog as a self-audit input.
2. In MVP-01, audit the controlled FastAPI and React/Next.js fixture from specification intake through evidence export via the local UI. A mapped assertion shows the omitted export field as failed. An explicit backend stub appears as a ghost candidate under SG-R020-AC01. A separate passing report without a matching assertion leaves its criterion unresolved with an unsupported-proof reason under SG-R029-AC02. The parseable export identifies the pinned baseline and retains the failure, finding and unresolved reason.
3. The same core journey succeeds with AI disabled. A controlled provider verifies the opt-in path, excerpt approval, and withholding of data before approval. A disposable runner demonstrates command approval, isolation, and fail-closed handling.
4. The developer can reopen the completed audit and trace a verdict back to its criterion, source, and admissible evidence. Blocked and unresolved product findings in the fixture are shown with their causes.
5. A reviewer signs off on the P0 criteria and all MVP scenarios using the [test plan](TEST_PLAN.md). Visual Reality Check and the broken-save scenario remain P1 under SG-R040–SG-R042. P2 remains the subsequent Surgical Repair Engine milestone.
