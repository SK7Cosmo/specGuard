# SpecGuard test plan

## Strategy and fixture

These are planned product checks. The [requirements catalog](REQUIREMENTS.yaml) defines the expected behaviors. The [verification policy](VERIFICATION_POLICY.md) determines admissibility and verdicts. Each case below uses its linked criterion ID as the test case ID. Define the test oracle from the specification before inspecting the implementation. Use test-first development for intake, verdict rules, isolation and consent.

Use a controlled Git fixture with a small FastAPI service, a React/Next.js UI, and its original Markdown and equivalent YAML specifications. Include an export that omits a specified field, an explicit backend stub, an empty click handler, a canned sample response, an incorrect inclusive discount boundary, a timeout path, an invalid state transition, and a control that renders correctly but fails to save. Include functioning examples alongside seeded gaps. Use synthetic records and credentials, a pinned runner environment, JUnit report fixtures, and a controlled provider endpoint that records outbound requests. Add a second commit and specification revision for baseline changes. Fix the browser and viewport for visual checks.

## End-to-end acceptance and additional failure paths

| Case | Run and expected result | Evidence to retain |
|---|---|---|
| MVP-01 | Audit the whole fixture through the local UI with AI disabled. Review candidate links and ghost findings, import or run approved checks, reopen, and export. The omitted field and stub are visible, unresolved proof has a reason, and the export identifies the pinned baseline. | UI observations, baseline digest, graph records, findings, criterion verdicts and JSON export. |
| MVP-02 | Repeat the trace step with the controlled provider. Decline the request, then approve one sanitized request and inspect the suggestion. Verify no pre-consent traffic and no automatic verdict changes. | Consent record, redacted request capture, suggestion and unchanged verdict state. |
| MVP-03 | Approve an existing fixture test and verify isolation controls. Repeat with missing isolation, then run an approved workload that exceeds limits. Verify blocked or incomplete outcomes and earlier evidence remains readable. | Invocation approval, runner configuration and teardown, sanitized result and retained audit state. |
| MVP-04 | Import a fixture report with a passing test from a different commit and a conflicting pair of current results, then inspect a repository with only an unsupported language. Verify unresolved reasons for stale or contradictory results and a visible unsupported coverage message. | Report provenance, baseline comparison, verdict reasons, and unsupported scope message. |
| MVP-05 | Use approved expectations for timeout handling and invalid state transitions. Confirm the failed fixture assertions remain attached to the corresponding criteria. | Reviewed expected outcomes, test links, results, and criterion verdicts. |

For each criterion case, retain the case ID, fixture commit and spec digest, method, expected and actual observations, result, and supporting artifact reference. For static cases retain rule configuration and matching or nonmatching paths. For manual cases retain reproducible steps, reviewer and observation. For automated cases retain the command or harness identity, result, and sanitized output. Record skipped and blocked cases with their causes.

## P0 acceptance cases

| Case and criterion ID | Method | Fixture and action | Expected result |
|---|---|---|---|
| SG-R001-AC01 | automated test | Upload a Markdown file with two requirement sections, an HTML comment, and a fenced example containing a requirement heading. | Exactly the two top-level requirement sections are imported in source order with their criteria. The example and comment produce no records. |
| SG-R002-AC01 | automated test | Load the SpecGuard requirements catalog as a specification. | All 54 requirements and their criterion IDs are available for review with no manual transcription. |
| SG-R003-AC01 | automated test | Submit separate inputs with an invalid UTF-8 byte, a missing required property, a duplicate ID, and an unsupported schema version. | Each rejection identifies the source location or field and the reason. The prior active baseline is still available. |
| SG-R003-AC02 | automated test | Submit YAML with a duplicate key, an unsafe tag, and data that exceed the configured parser limits. | Each input is rejected before activation, with the violated rule or limit identified. |
| SG-R004-AC01 | automated test | Import a Markdown requirement and a YAML requirement containing distinct whitespace, then open each source reference. | Each reference resolves to the original retained input and exact text span. |
| SG-R005-AC01 | automated test | Reorder records and change their descriptions while retaining their IDs. Import the revised version. | The existing IDs are preserved and evidence remains attributable to the revision on which it was collected. |
| SG-R006-AC01 | manual demonstration | Review a fixture containing “respond quickly” without a limit, a requirement declaring two separate obligations, and an explicit numeric criterion. | The vague and compound requirements can each be marked needs clarification with a reason. The explicit criterion can proceed to verification. |
| SG-R007-AC01 | automated test | Propose a revised threshold and a split of a compound record. Open the active baseline before and after approval. | Before approval the original baseline governs verification. After approval the revised threshold uses the existing ID and the children have new IDs linked to the retired parent. |
| SG-R008-AC01 | automated test | Index a FastAPI router, a React component, Next.js App Router and Pages Router pages, and named Python and JavaScript tests. | Each fixture artifact appears with its snapshot path and location. The index is built without importing or running application modules. |
| SG-R008-AC02 | automated test | Inspect a repository that contains an unsupported framework alongside supported FastAPI and React artifacts. | The index identifies unsupported content as outside coverage and still lists the supported artifacts. |
| SG-R009-AC01 | automated test | Place a valid requirement ID in one code reference and one test reference. Include a near-match and an unrelated reference. | The exact matches produce candidate links with their matching signal. The near-match and unrelated reference produce no links. |
| SG-R010-AC01 | manual demonstration | Add a source link and a test link for a requirement with no exact-ID match. | Both links persist and reopen at the chosen snapshot locations. |
| SG-R011-AC01 | automated test | Create a deterministic candidate and a reviewer-authored link, then confirm and reject separate candidates. | The graph shows the origin, current review state, and reviewer attribution where applicable after reloading. |
| SG-R012-AC01 | automated test | Audit one requirement with no link, one with only a candidate link, and one with a confirmed implementation link. | The first two requirements appear as unlinked. The third resolves to its confirmed link. |
| SG-R013-AC01 | manual demonstration | Use a controlled provider response with a valid snapshot path and an invented path. | The valid suggestion appears as inferred and awaiting review. The invented path is rejected and no criterion becomes verified. |
| SG-R014-AC01 | automated test | Audit a pinned commit and specification, then edit the working tree and specification file. | The existing audit retains the original commit and digest. A new audit identifies changed specification bytes by a different digest. |
| SG-R015-AC01 | automated test | Import a report with passing, failing, and skipped cases, then submit malformed XML. | The valid cases retain their reported outcomes and imported provenance. The malformed report produces an actionable error and adds no results. |
| SG-R015-AC02 | automated test | Submit a JUnit XML report with an external reference to a harmless local sentinel. | The reference is not fetched and no sentinel content is added to the audit. |
| SG-R016-AC01 | automated test | Run an approved benign fixture test in the isolated runner. | The completed result records the baseline, command arguments, environment identity, start and finish times, exit status, outcome, and sanitized output reference. |
| SG-R017-AC01 | automated test | Change one byte of a stored, sanitized artifact while keeping the recorded digest unchanged. | Inspection marks the artifact as altered and excludes it from verification. |
| SG-R018-AC01 | automated test | Export an audit with a confirmed link, a finding, a blocked criterion, and sanitized results. | A JSON parser can read the version, baseline, requirement and criterion IDs, link provenance, finding, verdict, reason, and evidence references. |
| SG-R019-AC01 | manual demonstration | Complete an audit, restart the local app, and reopen the audit. | The original baseline, criteria, verdicts, findings, links and available evidence references are retrievable. |
| SG-R020-AC01 | static analysis | Scan a fixture with a route body that only raises NotImplementedError and an implemented route. | Only the stub produces a backend candidate with its rule and source location. |
| SG-R021-AC01 | static analysis | Scan a button with an empty click handler and another that invokes a real action. | Only the empty handler produces a UI candidate with its rule and source location. |
| SG-R022-AC01 | static analysis | Scan routes returning explicitly marked sample data and routes returning service-derived data. | Only the marked sample data produces a candidate with its rule and source location. |
| SG-R023-AC01 | automated test | Dismiss an acknowledged fixture stub and record the reason, then reopen the audit. | The candidate is shown as dismissed with its rationale and reviewer attribution, and dismissal does not verify its criterion. |
| SG-R024-AC01 | automated test | Use the confirmed requirement “discount applies through 100 inclusive” with integer inputs. | The proposed cases include 99, 100, and 101, with expected outcomes derived from the specification. |
| SG-R025-AC01 | automated test | Use a confirmed required-field criterion and an allowed-value criterion for a form. | Proposals include a missing required value and an out-of-domain value, each linked to its source criterion. |
| SG-R026-AC01 | automated test | Use a confirmed workflow that permits review before payment. | The case set covers the specified allowed transition and an attempt to skip the required review state using synthetic records. |
| SG-R027-AC01 | manual demonstration | Edit and approve one draft case while leaving another in draft. | The approved case preserves the reviewed expected outcome and reviewer attribution. The draft stays unapproved. |
| SG-R028-AC01 | automated test | Link an approved case to an indexed test and try to link to an unknown test reference. | The valid relationship is persisted and browsable. The unknown reference is rejected. |
| SG-R029-AC01 | automated test | Provide one same-baseline passing result for a mapped case, a skipped result for a second, and no result for a third. | Only the first case has passing execution evidence. The remaining two show distinct unresolved reasons. |
| SG-R030-AC01 | manual demonstration | Select a snapshot, import its specification, review trace links and findings, and export evidence with AI disabled. | Each step is available through the interface for the selected audit and the export identifies that audit. |
| SG-R031-AC01 | automated test | Inspect enabled listeners and submit state-changing requests using a disallowed Host or Origin or without the required session proof. | The service binds to loopback only and each unauthorized request is rejected without a state change. |
| SG-R032-AC01 | automated test | Use a harmless sentinel outside the snapshot and reference it through a relative escape, symlink, and submodule path. | Each out-of-scope reference is refused and sentinel contents are absent from the audit. |
| SG-R033-AC01 | automated test | Approve a benign fixture command, then change its arguments or baseline before execution. | The approved invocation is eligible to run once. Modified invocations require fresh approval. |
| SG-R034-AC01 | automated test | Run a benign fixture command with a configured runner, and inspect its identity, mounts, network policy, and teardown. Repeat with no isolation backend. | The first run is non-privileged, blocks network access, has no host credentials or writable source mount, and is removed afterward. The second run is blocked without launching a host process. |
| SG-R035-AC01 | automated test | Use benign fixture workloads that exceed configured wall-time or output caps and inspect CPU, memory, and process limits. | The configured limits apply. Overruns stop or truncate as appropriate, produce an incomplete result, and never appear as a pass. |
| SG-R036-AC01 | automated test | Interrupt a check after import and link review, then reopen the audit. | Earlier results and reviewed links remain accessible. The failed step has a reason and can be retried without duplicating earlier evidence. |
| SG-R037-AC01 | automated test | Run the same fixture and analyzer rules twice with optional AI disabled. | Stable finding IDs, normalized links, ordering, and criterion verdicts match across runs. Run-specific timestamps and audit IDs may differ. |
| SG-R038-AC01 | automated test | Use synthetic credentials in a test log and proposed trace context, then inspect persistence, export, and provider request capture. | The synthetic credentials are absent from persisted outputs, exports, and the provider payload, with redaction recorded. |
| SG-R039-AC01 | automated test | Capture traffic while declining, approving, then changing an excerpt or provider destination, and while starting a new audit. | Only the approved sanitized payload goes to the displayed destination. A new audit or a change in payload or destination requires fresh consent. |

## P1 acceptance cases

| Case and criterion ID | Method | Fixture and action | Expected result |
|---|---|---|---|
| SG-R040-AC01 | automated test | Render a seeded Next.js page at a declared browser and viewport using a controlled fixture flow. | The captured screenshot is bound to the baseline, browser, viewport, and named flow step. |
| SG-R041-AC01 | automated test | Compare an unchanged image, a deliberately changed image above the approved threshold, and a capture with no reference. | Results show within threshold, visual difference, and unresolved with missing reference respectively. |
| SG-R042-AC01 | automated test | Use a control that looks correct but fails to persist the selected value. | The screenshot comparison passes and the interaction assertion fails in separate evidence records. |
| SG-R043-AC01 | automated test | Add one criterion, edit one under the same ID, remove one, and leave one unchanged. | The comparison identifies additions, edits, and removals by stable ID and omits the unchanged criterion. |
| SG-R044-AC01 | static analysis | Compare two commits with one linked file changed, another removed, and an unrelated file changed. | The linked change and removal appear with their commit references. The unrelated file does not appear as a linked change. |
| SG-R045-AC01 | automated test | Compare baselines with one changed criterion, one changed linked artifact, and one unaffected link. | Only affected links are marked for reassessment and retain their earlier provenance. |
| SG-R046-AC01 | automated test | Summarize a baseline with two verified, one failed, and one unresolved criterion. Repeat with no criteria. | The report shows 2 of 4 with the status breakdown. An empty baseline shows no applicable coverage. |
| SG-R047-AC01 | automated test | Summarize an audit with an unresolved P0 criterion and an unresolved P1 criterion. | The P0 criterion appears in the P0 review list with its reason, regardless of the aggregate coverage. |
| SG-R048-AC01 | manual demonstration | Open the verified, failed, and unresolved counts for an audit. | Each count opens the corresponding criterion set, with the status and its supporting evidence or unresolved reason. |
| SG-R049-AC01 | manual demonstration | Apply filters to an audit containing findings with distinct features, priorities and verdicts. | The visible findings match all selected filters and clearing filters restores all findings. |
| SG-R050-AC01 | manual demonstration | Open a linked finding from the filtered console. | The detail view shows the original criterion, baseline, trace links, and applicable evidence or unresolved reason. |
| SG-R051-AC01 | manual demonstration | Select two audits with a changed verdict and a removed criterion. | The comparison identifies the changed verdict and distinguishes the removed criterion from an unresolved one. |

## P2 acceptance cases

| Case and criterion ID | Method | Fixture and action | Expected result |
|---|---|---|---|
| SG-R052-AC01 | manual demonstration | Select a confirmed missing export field and request a proposal. | The proposal identifies the affected behavior, criterion, finding and target snapshot, with a scoped repair limited to the product behavior. |
| SG-R053-AC01 | automated test | Request a repair proposal for the missing export field and compare the working tree before and after. | The proposed diff is inspectable and the working tree is unaffected. |
| SG-R054-AC01 | manual demonstration | Review a repair for a missing export field with a mapped export test. | The proposal lists the mapped acceptance check with its expected result and identifies the product behavior to recheck. |

## Exit criteria

SG-02 checks document structure, references, criterion mapping and catalog integrity. MVP verification requires passing evidence for every P0 case and the MVP scenarios. Record outstanding P1 and P2 cases without counting them against the MVP gate. Review failure reports and retain their actual outcomes with the relevant baseline.
