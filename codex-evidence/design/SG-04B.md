# SG-04B Technical Feasibility and Design Gate Proofs

**Lifecycle phase/task:** Design / SG-04B  
**Execution ID:** `SG-04B-20261124-01`  
**Date/timezone:** 2026-11-24, Asia/Calcutta  
**Session ID:** unavailable (not exposed by the connected environment)  
**Actual model / reasoning effort:** GPT-6 Luna / High; developer confirmed in this conversation  
**Selection rationale:** Developer confirmed Luna / High, which fits the model strategy for a bounded but cross-cutting feasibility and evidence task.  
**Execution mode:** Default  
**Starting Git commit:** `81ff5ff03d1b5ee859f23ed6eb38306df64483d9`  
**Starting worktree:** Dirty with uncommitted SG-04A documentation artifacts; these were preserved.  
**Scope:** Synthetic, isolated design proofs only; no production implementation, dependency installation, real secrets, provider calls, runner execution, commit, push, or deployment.

## Decision summary

SG-04B does **not** close M3. All mandatory conditions D01–D12 remain **OPEN**. Twelve synthetic checks passed in the local proof-sketch harness. They show that several proposed primitives are testable with available libraries, but do not establish end-to-end feasibility of the product architecture. D02, D03, D04, D08, D09, D10, D11, and D12 still lack their required controlled service/integration observations; D08, D09, D11, and the full D12 dry run are blocked by missing implemented/selected components or fixtures. This report does not authorize M4 implementation.

The user designated the SG-04A architecture as the approved basis for this task. The checked-in SG-04A artifacts still contain their earlier “approval pending” wording; this task did not rewrite that architecture status.

## Environment and experimental boundary

- Python 3.12.7 was available. The existing environment had PyYAML, Mistune, and defusedxml; no packages were installed.
- Python AST analysis and simple TSX text scanning ran only against synthetic source strings. Neither synthetic nor repository application code was imported or executed.
- Docker, Podman, Firejail, and bubblewrap commands were not available in the checked environment. No project-supported backend was identified or provisioned, and no untrusted command was launched.
- Node was present, but no React/Next.js project or parser/browser test harness was supplied. Playwright and Selenium Python packages were absent.
- The repository has no implemented SpecGuard service, session middleware, runner, provider transport, or selected persistence backend. No remote request was sent.
- All secret-like values were synthetic examples labeled as such. They are not credentials.

The isolated experimental code is [run_proofs.py](../../experiments/sg04b/run_proofs.py). Its output is [results.json](../../experiments/sg04b/results.json). It is not production code, a product acceptance suite, or a real-world security certification.

## Mandatory condition experiments

### D01 — Specification secret intake

- **Hypothesis:** Candidate Markdown/YAML parsers can process synthetic clean inputs while leaving their original input bytes intact; a documented synthetic detector can reject a covered pattern and fail closed before a sink.
- **Associated requirements/conditions:** SG-R001-AC01, SG-R003-AC01–AC02, SG-R004-AC01–AC02, SG-R038-AC01–AC02; D01 (also informs D06 and D10).
- **Test fixture:** Synthetic Markdown with CRLF and UTF-8 content, synthetic YAML, and a fake password value explicitly marked `SyntheticOnly`.
- **Execution method:** E01 called Mistune and PyYAML `safe_load`, and compared SHA-256 input-buffer digests. E02 ran the small synthetic pattern demonstrator, unavailable-inspector branch, sink sentinel, and diagnostic echo check.
- **Expected result:** Clean inputs parse without input mutation; a covered synthetic value is rejected before the sink; inspection failure rejects with a sanitized reason.
- **Actual result:** E01 and E02 passed all recorded assertions. No diagnostic contained the fake value; the modeled sink remained empty after rejection and inspection failure.
- **Limitations:** The detector recognizes only three hard-coded synthetic shapes. No class-coverage claim is made. Buffer equality is not accepted-source persistence, and there was no storage, log, cache, export, source-view, or provider capture to inspect.
- **Reproducible evidence:** `python experiments\sg04b\run_proofs.py`; E01/E02 in `experiments/sg04b/results.json`.
- **Design recommendation:** Preserve the inspect-before-persist gate and exact original byte buffer. Select/document detector classes and limits, then prove rejection against each real sink in an instrumented intake path before implementation approval. **D01 remains OPEN.**

### D02 — Objective rule-generation observations

- **Hypothesis:** A strict typed proposal envelope can reject undeclared fields, invalid criterion IDs, and outcomes outside a small explicit set; candidate ghost rules can be tested against positive and adjacent negative fixtures.
- **Associated requirements/conditions:** SG-R009-AC01, SG-R020-AC01, SG-R021-AC01, SG-R022-AC01, SG-R024-AC01, SG-R025-AC01, SG-R026-AC01–AC02; D02.
- **Test fixture:** Synthetic FastAPI route/helper, TSX control and no-op handler, plus valid and hostile hand-authored JSON proposal records.
- **Execution method:** E07 ran deliberately narrow route-stub and no-op indicators. E08 validated exact proposal keys, known criterion ID, allowlisted rule type, revision format, and declared outcome.
- **Expected result:** Explicit route-stub candidate appears; undecorated helper is not a route stub; hostile/underspecified proposal fields are refused and no proposal is implicitly approved.
- **Actual result:** E07/E08 passed their narrow assertions. The intentional no-op control was identified as an ambiguity; E08 rejected extra instruction text and a path-like unknown criterion.
- **Limitations:** No case generator was implemented or tested for numeric boundaries, field violations, transitions, conflicts, or independent expected outcomes. The hostile proposal was written by the harness author, not generated by an AI model. The TSX/route checks are not complete analyzers.
- **Reproducible evidence:** E07/E08 in `experiments/sg04b/results.json`; rerun with the command above.
- **Design recommendation:** Keep proposal generation separate from outcome authority; require exact source criterion revision, explicit outcome, independent oracle, and reviewer approval. Prepare the full positive/negative/conflict matrix before closing D02. **D02 remains OPEN; full generation proof is BLOCKED.**

### D03 — Single-use runner authorization

- **Hypothesis:** A one-attempt authorization state can be represented as bound to an invocation digest and consumed before an attempt.
- **Associated requirements/conditions:** SG-R033-AC01, SG-R034-AC01–AC02, SG-R035-AC01–AC02; D03.
- **Test fixture:** In-memory synthetic approval token bound to `sha256:fixture-a`; same-digest replay and modified-digest attempt.
- **Execution method:** E10 ran a local in-memory state sketch. It only recorded eligibility and executed no command.
- **Expected result:** First matching attempt is eligible; replay and modified invocation are denied.
- **Actual result:** E10 passed those three state assertions; no command was executed.
- **Limitations:** No application approval store, concurrent request, durable transaction, service restart, backend launch, setup failure, or recovery transition was exercised. The state sketch is not a runner proof.
- **Reproducible evidence:** E10 in `experiments/sg04b/results.json`.
- **Design recommendation:** Bind approval to the immutable invocation and baseline, atomically consume it, and prove replay/race/restart/failure recovery against the selected persistent service and runner. **D03 remains OPEN; controlled replay proof is BLOCKED.**

### D04 — Safe rendering of untrusted content

- **Hypothesis:** HTML escaping encodes a synthetic hostile string as text without changing its underlying content.
- **Associated requirements/conditions:** SG-R001-AC01, SG-R003-AC01–AC02, SG-R004-AC01–AC02, SG-R015-AC01–AC02, SG-R018-AC01; D04.
- **Test fixture:** Inert string containing synthetic `<img onerror>` and `<script>` markup.
- **Execution method:** E09 applied Python `html.escape` and checked the encoded string and round trip.
- **Expected result:** Markup is escaped and the raw script element is absent from the encoded output.
- **Actual result:** All E09 assertions passed.
- **Limitations:** No React/Next.js view, Markdown renderer configuration, report/source/evidence/export-preview sink, browser navigation, state change, CSP, or DOM behavior was exercised.
- **Reproducible evidence:** E09 in `experiments/sg04b/results.json`.
- **Design recommendation:** Treat this as a primitive check only. Exercise the actual UI and every rendering sink with hostile Markdown, YAML, and JUnit fixtures in a browser harness. **D04 remains OPEN; browser rendering proof is BLOCKED.**

### D05 — Imported-evidence provenance and relevance

- **Hypothesis:** A bounded XML parser can accept a small JUnit document, reject a DTD/entity fixture, and keep report provenance separate from assertion-to-criterion relevance.
- **Associated requirements/conditions:** SG-R015-AC01–AC02, SG-R018-AC01–AC02, SG-R029-AC01–AC02; D05.
- **Test fixture:** Synthetic one-test JUnit report with case property and assertion text; synthetic DTD/entity document; in-memory same- and different-baseline evidence records.
- **Execution method:** E05 used defusedxml to parse the benign report and attempted the forbidden-construct fixture. It computed a digest and exercised an in-memory relevance predicate. E06 ran a deterministic evidence/verdict table including irrelevant and conflicting evidence.
- **Expected result:** Valid report parses with provenance; forbidden XML is rejected; only a same-baseline, mapped record with an assertion is relevant; unrelated and conflicting evidence cannot produce a verified verdict.
- **Actual result:** E05 and E06 passed all assertions; the hostile DTD/entity fixture was rejected; conflicting and irrelevant evidence reduced to unresolved in E06.
- **Limitations:** No importer transaction, malformed/oversized corpus, XML resource-limit exercise, report storage, reviewer decision/rationale, or production evidence evaluator was present. The synthetic relevance predicate is not the SpecGuard implementation.
- **Reproducible evidence:** E05/E06 in `experiments/sg04b/results.json`.
- **Design recommendation:** Keep imported result, assertion detail, baseline, test/case identity, criterion mapping, and reviewer relevance decision as distinct provenance fields. Verify transactionality and report-level-pass-without-assertion cases against the eventual importer. **D05 remains OPEN.**

### D06 — Snapshot, Markdown/YAML and JUnit parser feasibility

- **Hypothesis:** Available parser candidates can process representative synthetic Markdown/YAML/JUnit inputs and reject a forbidden XML construct without executing source content.
- **Associated requirements/conditions:** SG-R001-AC01, SG-R002-AC01, SG-R003-AC01–AC02, SG-R004-AC01–AC02, SG-R015-AC01–AC02, SG-R032-AC01; D06.
- **Test fixture:** E01 clean Markdown/YAML byte strings; E05 benign and DTD/entity JUnit strings. No Git repository fixture was created.
- **Execution method:** Mistune, PyYAML `safe_load`, and defusedxml were invoked from the local proof sketch; input digest and parse outcomes were recorded.
- **Expected result:** Synthetic valid forms parse, byte buffers remain unchanged, and forbidden XML is refused.
- **Actual result:** E01/E05 assertions passed with the available versions; no source module ran and no external retrieval was requested.
- **Limitations:** No pinned Git commit/tree/blob, malformed YAML/Markdown corpus, duplicate-ID/depth/size limits, path escape/symlink/submodule case, missing-object behavior, prior-state atomicity, or external retrieval sentinel was tested. Parser candidate suitability is not final library approval.
- **Reproducible evidence:** E01/E05 in `experiments/sg04b/results.json`; environment inspection recorded in this report.
- **Design recommendation:** Continue with a bounded parser-selection spike using pinned synthetic Git objects, explicit numeric limits, duplicate-key/oversize cases, and forbidden XML/path fixtures. **D06 remains OPEN.**

### D07 — Python and React/Next.js indexing, references, ghost indicators

- **Hypothesis:** Python AST and a conservative source-text recognizer can produce repeatable path/symbol/line references on small fixtures without importing or executing application code.
- **Associated requirements/conditions:** SG-R008-AC01–AC02, SG-R009-AC01, SG-R010-AC01, SG-R020-AC01, SG-R021-AC01, SG-R022-AC01, SG-R023-AC01; D07.
- **Test fixture:** Synthetic FastAPI module, TSX component, exact/embedded/wrong-boundary requirement IDs, one stub route, helper, wired action, and intentional empty event handler.
- **Execution method:** E03 parsed Python with `ast` and lexically scanned TSX names. E04 repeated the same fixture extraction and checked exact ID boundaries, baseline/path/line/symbol shape, and criterion case ID. E07 checked the narrow ghost patterns.
- **Expected result:** Deterministic path/line/symbol references on repeat, exact ID matches only, positive explicit stub detection, and no route-stub candidate for the undecorated helper.
- **Actual result:** E03/E04/E07 passed the recorded assertions. Both language fixtures were data strings; neither was executed.
- **Limitations:** TSX parsing is regex-based, no real Next.js project or package/parser was available, and no rename/move/rebase/line-shift stability or mixed/unsupported coverage case was tested. An intentional no-op interactive handler can look like a defect and is a known candidate false positive. No reviewer dismissal persistence was tested.
- **Reproducible evidence:** E03/E04/E07 in `experiments/sg04b/results.json`.
- **Design recommendation:** Use syntax-aware, non-executing indexers for both stacks; version locations to the pinned baseline and distinguish candidate findings from confirmed behavior. Require reviewer disposition for ambiguous no-op handlers. **D07 remains OPEN.**

### D08 — Local authority and session feasibility

- **Hypothesis:** The proposed loopback, Host/Origin, and session-proof policy can reject unauthorized requests before disclosure or mutation.
- **Associated requirements/conditions:** SG-R031-AC01; D08.
- **Test fixture:** Required controlled HTTP request matrix: permitted and disallowed Host/Origin, originless mutation, and missing/invalid/expired/revoked session proof.
- **Execution method:** **BLOCKED.** No SpecGuard local web service or session middleware exists in this repository; only the policy and test-plan description are available.
- **Expected result:** Allowed local session works; prohibited authority/origin/proof requests fail before protected data or state changes.
- **Actual result:** No request was issued; therefore no pass/fail observation exists.
- **Limitations:** Mechanism, proof lifetime, revocation and service authority are unselected and unimplemented. A hand-written policy simulation would not establish the required request boundary.
- **Reproducible evidence:** Prerequisite inventory: `Get-Command node,npm,docker,podman,firejail,bwrap -ErrorAction SilentlyContinue`; repository inventory found no application service. Policy target: `docs/TEST_PLAN.md`, SG-R031-AC01.
- **Design recommendation:** Select the session mechanism/lifetime and run the full request matrix against a controlled loopback service before protected local operations are implemented. **D08 remains OPEN and BLOCKED.**

### D09 — Supported runner backend and resource limits

- **Hypothesis:** A selected backend can provide a disposable, non-privileged, network-blocked environment without credentials or writable source, enforce all required limits, terminate process trees, and recover fail-closed.
- **Associated requirements/conditions:** SG-R033-AC01, SG-R034-AC01–AC02, SG-R035-AC01–AC02, SG-R036-AC01; D09.
- **Test fixture:** Required benign synthetic command with network, credential, mount, CPU, memory, wall-time, process-count, output, teardown, restart and recovery sentinels.
- **Execution method:** **BLOCKED.** Environment inventory found no Docker, Podman, Firejail, or bubblewrap executable, and the project has no selected/provisioned runner backend. No command was launched.
- **Expected result:** Backend contains the exact approved command, enforces configured numeric limits and teardown, blocks restart execution after uncertain cleanup, and never falls back to host execution.
- **Actual result:** No runner observation or resource-limit measurement was made.
- **Limitations:** Supported host platform/backend, numeric limits, provisioning, telemetry and recovery are unresolved. Testing a mock or host subprocess would not prove isolation and is not reported as such.
- **Reproducible evidence:** Prerequisite inventory command above; required controlled observations are specified in `docs/adr/SG-03D-m3-mandatory-conditions.md` D09 and `docs/TEST_PLAN.md` SG-R034/035.
- **Design recommendation:** Select a supported backend and numeric limits first, then run the D09 benign sentinel matrix inside that backend. Do not enable runner work before containment and recovery evidence. **D09 remains OPEN and BLOCKED.**

### D10 — Remote AI consent, transport and secret-safe boundary

- **Hypothesis:** A consent gate and synthetic redactor can produce a payload only after consent and remove a covered synthetic value before payload construction.
- **Associated requirements/conditions:** SG-R013-AC01–AC02, SG-R038-AC01–AC02, SG-R039-AC01–AC02; D10 (also informs D01).
- **Test fixture:** Synthetic excerpt containing a fake password value; consent true/false; no real provider or credential.
- **Execution method:** E02 tested a narrow synthetic detector. E12 tested pure in-memory consent/payload construction, redaction and digest equality. No HTTP/provider request was made.
- **Expected result:** No consent yields no payload; an approved payload contains only the sanitized synthetic excerpt and can be bound to exact bytes.
- **Actual result:** E02/E12 assertions passed. They establish behavior of the proof functions only.
- **Limitations:** No consent UI or revocation, endpoint validation, DNS/address policy, redirect block, timeout/size limits, response validation, provider capture, failure sanitization, or prior-verdict retention was exercised. No AI model generated suggestions.
- **Reproducible evidence:** E02/E12 in `experiments/sg04b/results.json`.
- **Design recommendation:** Bind consent to the displayed endpoint and exact sanitized bytes; validate again immediately before dispatch; reject redirects; keep provider response proposal-only. Prove with two controlled local endpoints and synthetic payloads once transport exists. **D10 remains OPEN; transport proof is BLOCKED.**

### D11 — Evidence storage and revision feasibility

- **Hypothesis:** A selected store can round-trip accepted pinned audits and preserve atomicity, provenance, revisions, stale state and retry idempotency while excluding rejected source.
- **Associated requirements/conditions:** SG-R004-AC01–AC02, SG-R005-AC01, SG-R007-AC01–AC02, SG-R014-AC01, SG-R017-AC01, SG-R018-AC01–AC02, SG-R036-AC01; D11.
- **Test fixture:** Required accepted/rejected source pair, two baselines, evidence artifact altered after ingestion, coverage states, interrupted import and retry.
- **Execution method:** **BLOCKED.** No persistence technology or product store is selected or implemented. The synthetic intake sink check in E02 is not persistence.
- **Expected result:** Accepted records round-trip; rejected source is absent; revisions and history remain stable; failed intake is atomic and retry is idempotent.
- **Actual result:** No storage operation was performed; no round-trip or atomicity result is claimed.
- **Limitations:** Schema/versioning, transactional semantics, artifact vault, migration, retention and reopen/export behavior remain design choices.
- **Reproducible evidence:** D11 condition in `docs/adr/SG-03D-m3-mandatory-conditions.md`; SG-04A logical model in `docs/architecture/SG-04A-data-model.md`. No executable storage proof exists.
- **Design recommendation:** Select a persistence boundary and schema/version policy, then run the synthetic round-trip, corruption, interruption, atomic rejection and idempotent retry matrix. **D11 remains OPEN and BLOCKED.**

### D12 — Integrated P0 fixture and gate mapping

- **Hypothesis:** Existing SG-04A traceability records provide a complete criterion-to-case inventory that can seed a later P0 dry run.
- **Associated requirements/conditions:** All 53 P0 criteria across SG-R001–SG-R039 and MVP-01–MVP-05; D12.
- **Test fixture:** Existing requirements catalog and `SG-04A-architecture-traceability.csv`; no integrated repository commit or runtime fixture.
- **Execution method:** E11 parsed the catalog/matrix and counted P0 criteria, ensuring every P0 criterion has a row with the same case ID.
- **Expected result:** The mapping inventory contains 53 P0 criteria and exact matching case IDs; a full dry run would additionally attach independent observations/oracles for each case and MVP scenario.
- **Actual result:** E11 passed the structural inventory checks. No independent oracle review, P0 case dry run, or MVP scenario execution occurred.
- **Limitations:** The pinned fixture, harness, synthetic application/specification pair, and independent oracles are not selected or prepared. A mapping check is not the required design-level dry run.
- **Reproducible evidence:** E11 in `experiments/sg04b/results.json`; source mapping `docs/architecture/SG-04A-architecture-traceability.csv`.
- **Design recommendation:** Retain the existing trace mapping, select a pinned all-stack synthetic fixture, review each expected outcome independently, and dry-run every P0 case plus MVP-01–MVP-05 before M4 integration. **D12 remains OPEN; full dry run is BLOCKED.**

## Requirement areas requested outside/alongside condition grouping

| Investigation | Experiment evidence | Feasibility result |
|---|---|---|
| Markdown/YAML parsing and exact-byte preservation | E01 | Synthetic parser/buffer primitive passed; persistence and limits remain unproven. |
| Secret detection, rejection and fail-closed inspection | E02 | Synthetic pattern sketch passed; detector coverage and all real sinks remain unproven. |
| Python and React/Next.js source indexing | E03 | Python AST and lexical TSX sketch passed; complete Next.js indexing is unproven. |
| Stable requirement-to-code-to-test references | E04 | Repeatable unchanged-fixture references passed; revision/move stability is unproven. |
| Imported JUnit evidence parsing, provenance and relevance | E05/E06 | Parser security and synthetic predicate checks passed; importer and reviewer workflow remain unproven. |
| Deterministic verdict calculation | E06 | Proposed simple truth table passed; full normative precedence is unproven. |
| Ghost implementation detection and known false positives | E07 | Narrow candidate rule passed; intentional no-op is a documented ambiguity requiring review. |
| Adversarial AI-generated rule proposals | E08 | Hand-authored hostile envelope rejected; no AI generation or adversarial model behavior was tested. |
| Safe rendering of untrusted content | E09 | Escaping primitive passed; product/browser rendering remains blocked. |
| Single-use runner authorization | E10 | In-memory state sketch passed; durable runner replay/recovery remains blocked. |
| Supported execution isolation backend and resource limits | D09 | **BLOCKED:** no selected/available backend; no untrusted command run. |
| Remote AI consent and secret-safe data boundaries | E12 | Payload-construction sketch passed; consent UI, transport and controlled endpoint proof remain blocked. |

## Commands and actual results

- `Get-Content`/`rg --files` inspected the guidance, requirements, decisions, SG-04A artifacts, test plan, verification policy, evidence templates and tracking files.
- `git status --short` and `git rev-parse HEAD` recorded the dirty SG-04A baseline and starting commit above.
- `python --version` reported Python 3.12.7. A module availability probe confirmed PyYAML, Mistune and defusedxml; Playwright, Selenium, SQLAlchemy and tree-sitter language packages were absent.
- `python experiments\sg04b\run_proofs.py` — **12 synthetic checks passed, 0 failed**. This is proof-sketch output, not product acceptance testing.
- No unrelated project test suite was run. No real secret, untrusted application execution, remote request, or runner command was used.

## Condition status and authorization boundary

The evidence adds observations but does not meet all required condition-specific controlled criteria. D01–D12 therefore remain OPEN in the authoritative register. SG-04B is submitted for approval; stop here. Do not begin production implementation or advance to M4 from this report alone.

## Files changed for this execution

- `experiments/sg04b/run_proofs.py` — isolated synthetic-only experimental harness.
- `experiments/sg04b/results.json` — actual reproducible harness output.
- `codex-evidence/design/SG-04B.md` — this report.
- `docs/adr/SG-03D-m3-mandatory-conditions.md` — addendum links partial observations while preserving OPEN status.
- `codex-evidence/design/README.md` and `codex-evidence/EVIDENCE_INDEX.md` — evidence navigation.
- `PLANS.md` — M3 remains in progress; SG-04B evidence linked.
- `codex-evidence/models/MODEL_USAGE.csv` and generated `codex-evidence/models/MODEL_REPORT.md` — execution tracking.

**Unobserved measurements:** Session ID, duration, token counts and resource usage are unavailable; no estimates are substituted.
