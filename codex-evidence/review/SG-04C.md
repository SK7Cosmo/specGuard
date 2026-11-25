# SG-04C Independent Architecture and Security Review

## Execution record

- Lifecycle phase / milestone / task: Review / M3 / SG-04C.
- Unique execution ID: `SG-04C-20261124-01`.
- Session ID: N/A (not exposed); execution mode: Default.
- Client date / timezone: 2026-11-24 / Asia/Calcutta.
- Actual model / reasoning effort: GPT-6.2 Sol / High. Developer initially confirmed `sol ; high`, then explicitly confirmed that Sol denotes GPT-6.2 Sol; see the [metadata correction](SG-04C-model-metadata.md).
- Selection rationale: Developer-selected Sol / High for independent cross-document architecture, security, evidence and feasibility review; no model switch or escalation occurred in this execution.
- Starting Git commit: `81ff5ff03d1b5ee859f23ed6eb38306df64483d9`.
- Starting worktree: existing modified and untracked SG-04A/SG-04B documents, tracking files and experiments; preserved as review inputs.
- Duration, tokens, cost and resource measurements: N/A; not observed.
- Authorization: independent review and evidence recording only; no requirements changes, fixes, commit, push, deployment or implementation authorization.
- Human intervention: user supplied repository guidance, commissioned SG-04C and confirmed model/effort after the required metadata question.

## Design gate recommendation

**NOT READY FOR IMPLEMENTATION.** All twelve mandatory pre-implementation gates D01–D12 remain unsatisfied. There is no basis for conditional implementation readiness while those gates remain open. This is a technical and evidence conclusion, not a duration estimate or a proposal to reduce approved scope.

The layered architecture is a reasonable responsibility decomposition: deterministic core, controlled adapters, human decisions, isolated runner and optional proposal-only AI. It preserves the product direction and priority order. It is not yet a complete, internally consistent, demonstrated implementation design. Core decisions are still deferred, several required workflows lack contracts, and twelve passing synthetic experiments do not demonstrate the required integrated security boundaries.

Findings: **1 CRITICAL, 9 HIGH, 4 MEDIUM, 0 LOW**. Severity describes the implementation risk or gate impact of a design/evidence deficiency. No production service exists here; this report does not claim an exploited production vulnerability. Observed proof-function behavior and hypothetical design counterexamples are identified separately below.

## Scope, authority and method

Reviewed repository guidance, GOALS, PLANS, README, all documents under `docs/` (discovery, PRD, normative YAML, verification policy, acceptance plan, ADRs and architecture package), SG-04A draft/closure and SG-04B evidence, SG-03C/SG-03D review context, model protocol and evidence navigation. The normative order is the approved catalog and verification policy, supported by PRD, acceptance plan, accepted product-owner ADRs and mandatory-condition register. SG-04A is a proposed interpretation; SG-04B is limited experimental evidence. Historical counts and schedule arguments do not override SG-03D or ADR 0002. External research claims were read as discovery context, not independently revalidated or used to establish security feasibility.

The review checked the working-tree artifacts, including untracked architecture and experiment files, rather than assuming Git HEAD contained them. [Input fingerprints](SG-04C-input-manifest.json) preserve reviewed file hashes and byte lengths, including the initial PLANS bytes. Original architecture, requirements, experiments and SG-04B results were preserved. Model confirmation was requested because actual metadata was unavailable and AGENTS.md explicitly requires confirmation; the user's reply was `sol ; high`.

Deterministic review tooling is [SG-04C-checks.py](SG-04C-checks.py); observations are in [SG-04C-check-results.json](SG-04C-check-results.json). The existing harness was inspected in full before loading it. Only reviewed evidence tooling, installed parser libraries and bounded inert synthetic strings/records ran in the controlled local review process. No untrusted application module, repository test workload, shell invocation from an input, network request, provider or sandbox workload ran. These checks do not test isolation. There was no delegation or separate-model adjudication; independence here means rechecking artifacts and policy without adopting the prior agent's conclusions.

## Architecture completeness and consistency

The package identifies the principal components and data flows, and separates trace candidates from evidence and verdicts. It explicitly retains fail-closed intent, immutable baselines, human review, AI-disabled fallback and P1/P2 sequencing. Those are useful design strengths.

Missing implementation decisions include parser/Git boundaries and numeric limits, a two-stack syntax-aware index, same-origin delivery and session bootstrap, runner host/backend/provisioning, durable approval and recovery transitions, provider transport and endpoint policy, transactional metadata/artifact storage and complete domain/API schemas. A diagram of a boundary is not evidence that the boundary can be enforced. Findings F02–F12 identify specific consequences rather than treating every deferred decision as a proven vulnerability.

The package also contains a substantive verdict ambiguity (F07), an incomplete representation of required mutation workflows (F12), and later-feature mappings that reserve names without specifying their designs (F13). The architecture matrix's uniform verification wording delegates back to the test plan; it is an inventory, not an independent implementation oracle or dry run.

## Coverage of 54 requirements and 68 acceptance criteria

Independent structural checks found **54 requirements: 39 P0, 12 P1, 3 P2**, and **68 criteria: 53 P0, 12 P1, 3 P2**. All 68 catalog criteria match exactly one architecture row and one test-plan case, including parent requirement, priority, method and expected outcome. All 85 catalog source paths resolve and dependencies are acyclic. These observations establish structural coverage, not successful product verification.

The [independent criterion review](SG-04C-criterion-review.csv) records every one of the 68 criteria, its exact normative expectation, priority/method/case, specific review assessment and related finding IDs. No criterion is claimed acceptance-tested. The 53 P0 cases and MVP-01–MVP-05 have no integrated execution evidence. P1 and P2 remain approved later milestones; their placeholder mapping does not prove their feasibility and does not make them missing P0 functionality.

| Requirement group | Independent coverage assessment | Findings |
|---|---|---|
| SG-R001–SG-R007 | Intake, source identity and revision intent present; no complete intake, clarification and change-approval design/proof | F03, F05, F10, F12 |
| SG-R008–SG-R013 | Static candidates and review intent present; actual criterion matching defective in proof, broader indexing/manual mutation/provider contracts incomplete | F09–F12 |
| SG-R014–SG-R019 | Baseline/provenance/export entities present; storage integrity, relevance and unsupported verdict behavior insufficient | F03, F05–F07, F12 |
| SG-R020–SG-R023 | Rule names present; narrow fixture checks do not cover full positives/negatives or persisted dismissal | F09, F10, F12 |
| SG-R024–SG-R029 | Case approval intent present; rule schemas/generation, relevance and test associations unproven | F06–F08, F12 |
| SG-R030–SG-R039 | Security and operational intent present; no integrated journey, sessions, runner, limits, persistence or provider boundary proof | F01–F05, F09–F12 |
| SG-R040–SG-R051 | All twelve P1 criteria mapped; feature-specific models/contracts still reserved for M7 | F05, F07, F13 |
| SG-R052–SG-R054 | All three P2 criteria mapped; repair authority and read-only diff/check contracts still reserved for M8 | F13 |

## Evidence for the twelve mandatory conditions

`OPEN` below is the independent disposition under the existing register. Partial evidence earns no closure. Component prototypes can be authorized as bounded M3 experiments; the absence of production code does not justify bypassing gates or require implementing the product first.

| Gate | Evidence inspected/reproduced | Why insufficient / required next observation | Finding IDs | Disposition |
|---|---|---|---|---|
| D01 | E01 buffer/parser primitives; E02 synthetic detector and list sink | Define covered classes; instrument clean/secret/error Markdown/YAML across real receive, temp, log, cache, source, evidence, export and outbound boundaries; byte-exact accepted round trip | F03, F05, F10 | OPEN |
| D02 | E07 narrow regex indicators; E08 hand-authored proposal envelope | No combined-bound, impossible-field, conflict, transition or documented-failure generator/oracle matrix; AI did not generate proposals | F08–F10 | OPEN |
| D03 | E10 sequential in-memory used flag | No atomic concurrent consumption, durable attempt identity, actual replay, setup/crash/restart/recovery; changed-input test occurs after consumption | F04, F05, F10 | OPEN |
| D04 | E09 Python escaping round trip | No actual React/Next.js sink, browser DOM/network/navigation/state observations; escaping primitive cannot establish all-context safety | F03, F10, F11 | OPEN |
| D05 | E05 XML plus hand-built relevance flags; E06 reducer | No actual reviewer assertion inspection/rationale, transaction or complete admissibility; CE02/CE03 demonstrate gaps | F06, F07 | OPEN |
| D06 | E01 candidate parsers and E05 one entity fixture | No Git fixture, canonical grammar, duplicate/limit corpus, external-retrieval sentinel, location or atomic-preservation proof | F03, F10 | OPEN |
| D07 | E03 AST/TSX lexical names; E04 repeat; E07 one route/handler | No full FastAPI/React/both Next.js routing modes, mixed scope, moved references or full exact-ID/ghost matrix; CE01 fails | F09, F10 | OPEN |
| D08 | Policy and request matrix descriptions only; no request issued in SG-04B | Select topology/bootstrap/proof/expiry/revocation and demonstrate allowed/denied requests before data release or mutation | F02 | OPEN |
| D09 | SG-04B records missing candidate CLI tools; no launch | No selected supported host/backend, provisioning or numeric limits; absence on PATH is not universal host infeasibility | F04 | OPEN |
| D10 | E12 consent Boolean/redaction/digest sketch; no traffic | Exact bytes/destination/revocation, endpoint/address policy, redirect refusal, bounds, response validation and failure retention need controlled captures | F03, F11 | OPEN |
| D11 | Logical entities only; no store | Crash-atomic metadata/artifacts, revision lineage, stale/integrity checks, all coverage statuses, rejection and idempotent recovery need actual round trips | F05, F12 | OPEN |
| D12 | E11 counts matching P0 matrix IDs | No pinned integrated application/spec pair, independent 53-case oracle dry run or all five MVP scenarios | F01, F10, F12 | OPEN |

## Findings

### F01 — CRITICAL — Mandatory Design gates and feasibility exit remain unsatisfied

**Affected requirements:** All 39 P0 requirements SG-R001–SG-R039 / all 53 P0 criteria; D01–D12; MVP-01–MVP-05.

**Evidence:** The authoritative [mandatory register](../../docs/adr/SG-03D-m3-mandatory-conditions.md) forbids dependent M4 implementation until applicable gates pass. All twelve rows are OPEN. SG-04A §14 defers central technology/control decisions. SG-04B D08/D09/D11 and full D12 report missing prerequisites. Independent reproduction confirms 12 passing synthetic experiments, not a service, runner, store or integrated fixture.

**Counterexample and impact:** A team could implement all components behind the documented interfaces and still have no usable supported runner or safe session bootstrap. Counting E11's 53 matching IDs as D12 closure would advance the milestone without exercising a single UI/API/security interaction. Implementation readiness would be unsupported and contrary to an explicit progression gate.

**Recommended remediation:** Keep M3 open. Prepare individually bounded Design experiments with selected candidate technologies and reproducible fixtures, resolve the dependent decisions, and obtain review of the required observations. Do not authorize dependent production work by renaming outstanding gates as implementation conditions.

**Required verification:** The twelve condition-specific controlled results above, complete independent 53-case Design dry run and all five MVP mappings, reviewed failures/limitations and explicit product-owner disposition. M5 still requires actual product acceptance evidence; Design proofs do not substitute for it.

### F02 — HIGH — Local session establishment and delivery topology are not designed

**Affected requirements:** SG-R031-AC01; SG-R030-AC01, SG-R033-AC01, SG-R039-AC01 as protected consumers; D08.

**Evidence:** Architecture §4 says only that the browser obtains a short-lived local proof. §14 leaves frontend/backend delivery topology unresolved. API conventions require proof on protected operations but define no bootstrap, logout/revocation or proof transport. SG-04B D08 issued no request.

**Counterexample and impact:** A UI on one port calling FastAPI on another cannot satisfy an exact same-origin mutation rule without a defined proxy/topology. If an otherwise acceptable same-origin session-establishment POST requires no preexisting proof or local possession mechanism, another browser tab able to open the public local UI may bootstrap authority. A token in a URL or persistent browser storage creates a different exposure than a session cookie. Host/Origin allowlists alone do not decide who may establish proof. These are unresolved design cases, not observed exploits.

**Recommended remediation:** Select one deployment origin, loopback authorities (including port and IPv4/IPv6 behavior), proof establishment/transport/storage/lifetime/revocation and restart behavior. Explain how bootstrap obtains local authority and how reads, mutations and credential-free static assets differ. Apply the existing originless-read rule precisely; reject originless mutations, including establishment.

**Required verification:** Controlled allowed and denied Host/Origin requests, originless reads/mutations, missing/expired/revoked proof, cross-port variants, bootstrap/restart/revocation and protected export/approval calls, with sentinels proving denial before disclosure/mutation.

### F03 — HIGH — Secret-safe intake and bounded parsing stop at an application-level promise

**Affected requirements:** SG-R001–SG-R004, SG-R014–SG-R015, SG-R018, SG-R032, SG-R038 (all their criteria); D01, D04, D06, D10.

**Evidence:** Architecture §4 promises inspection in a nonpersistent transient buffer before downstream sinks, while §14 leaves parsers, detector scope and numeric limits undecided. The security design lists no concrete ingress/middleware/temp-file or per-context rendering configuration. E01 uses noncanonical Markdown and YAML; its byte checks compare an input buffer with a copy. CE05 shows the selected `yaml.safe_load` primitive silently keeps the last duplicate key (`SG-R002`). The candidate is not a complete specification validator.

**Counterexample and impact:** A framework upload spools bytes to a temporary file or request-body logger before the intake function detects a synthetic covered password. A source excerpt, artifact path, test name or exception containing a covered token is persisted outside the excerpt redactor. An aliased/deep YAML object remains within byte limits but expands work; a duplicate key silently replaces the first ID. A safe HTML text escape does not establish safety in URL, attribute or script serialization contexts. All are within the stated untrusted-input boundary.

**Recommended remediation:** Specify the ingress-to-discard path including multipart/streaming behavior, temporary storage, errors, access logs and derived metadata. Document bounded secret classes and fail-closed errors. Select parser/schema/duplicate/alias/depth/count limits and Git object access that cannot invoke hooks, filters, lazy fetch or repository code. Define raw-source versus sanitized-evidence storage and safe rendering/export for every context, without silently changing accepted specifications.

**Required verification:** Canonical clean/secret/error inputs in both formats, invalid UTF-8 and duplicate/unsafe/deep/oversize cases; inspect every real sink and external sentinel. Prove exact accepted bytes/spans on reopen. Test hostile spec/report/source/provider text and secret-bearing metadata in actual browser views/export with no active behavior or retained covered values. No claim of universal secret detection is required.

### F04 — HIGH — Runner authority, host support, limits and crash-safe recovery remain unspecified

**Affected requirements:** SG-R016-AC01, SG-R032-AC01–AC02, SG-R033-AC01, SG-R034-AC01–AC02, SG-R035-AC01–AC02, SG-R036-AC01; D03, D09.

**Evidence:** No supported host/backend/provisioning path or numeric wall/CPU/memory/process/output limits is selected. SG-04B found no candidate runner executable in its checked environment and launched nothing. E10 is a sequential dictionary flag. API approval digests do not define executable resolution, working directory, environment allowlist, prepared dependency/image identity, mount layout or durable launch/recovery transaction.

**Counterexample and impact:** Two dispatches race on one unconsumed grant, or the service crashes after launch but before recording the environment identity; restart can then replay or fail to locate descendants. An unchanged executable name resolves to a different binary or prepared image after approval. A per-audit recovery block permits an orphan from one audit while a second audit starts another run. Read-only source without an explicit writable disposable work area may make normal test tools fail; dependency provisioning must not require network access during the approved run.

**Recommended remediation:** Select and document a supported host/backend and controlled provisioning, explicit invocation/environment binding and numeric limits. Define atomic single-use consumption before attempts, durable intent/environment records, concurrency and retry behavior, service-wide containment block where cleanup uncertainty affects later runs, reconciliation and verified recovery. Keep the no-host-fallback rule.

**Required verification:** Benign isolated sentinels for network, credentials, writable mounts, nonprivilege and every limit; concurrent unchanged replay and changed invocation under a fresh grant; partial setup, launch/record crash boundaries, descendant timeout, teardown failure, multi-audit restart block and fresh approval after verified cleanup. Missing tool inventory alone neither proves nor disproves Windows/WSL2/container feasibility.

### F05 — HIGH — Persistence integrity and operation recovery have no transactional design

**Affected requirements:** SG-R004-AC01–AC02, SG-R005-AC01, SG-R007-AC01–AC02, SG-R014-AC01, SG-R017-AC01, SG-R018-AC01–AC02, SG-R019-AC01, SG-R034-AC02, SG-R036-AC01, SG-R037-AC01; D03, D11.

**Evidence:** Data model “Open storage decisions” defers database/file split, transactions, migrations, retention and crash recovery. `Operation` has an idempotency key but no key scope, payload-match rule or state machine. There is no atomic metadata/artifact commit or durable runner block specification. SG-04B D11 performed no storage operation.

**Counterexample and impact:** A process writes the accepted artifact, crashes before committing its baseline pointer, and a retry either duplicates evidence or references an absent blob. Reusing an idempotency key with changed bytes returns an earlier operation incorrectly. Reopen can show a cached verified verdict after its artifact is altered unless integrity is checked on every verdict-serving path. A crash between cleanup failure and block persistence loses the containment decision.

**Recommended remediation:** Define transactional/commit order, durable state and pointer activation, artifact publication/integrity verification, startup reconciliation, schema migration and safe deletion/retention rules. Specify idempotency identity, mismatch handling and retry transitions. Keep old baselines/evidence immutable and distinguish sanitized stored bytes from any pre-redaction input identity.

**Required verification:** Fault injection at metadata/blob/activation and approval/launch/block boundaries; kill/restart/retry with changed and unchanged keys; artifact corruption before read/evaluate/export; lineage and stale-evidence round trips; all coverage states and failed-intake preservation. Inspect persistent/temp surfaces for rejected values.

### F06 — HIGH — Synthetic assertion IDs and admissibility flags can manufacture support

**Affected requirements:** SG-R015-AC01–AC02, SG-R016-AC01, SG-R017-AC01, SG-R018-AC01–AC02, SG-R028-AC01, SG-R029-AC01–AC02, SG-R037-AC01; D05, D11.

**Evidence:** `run_proofs.py:70–85` treats nonempty assertion IDs plus claimed mapping/baseline as relevance and reduces verdicts using only `relevant`/`baseline_current`. E05 constructs its report fields independently of XML content. CE02 accepts an invented assertion identifier with no actual observation or reviewer record. CE03 returns `verified` for a passing item explicitly marked altered, inferred and unreviewed. These are proof-sketch results, not product behavior.

**Counterexample and impact:** A fabricated imported report names the right commit and criterion and prints `assertion: required field present`, while its real test checks nothing. A digest makes those bytes stable but cannot authenticate the producer or establish relevance. An implementation copied from the reducer could promote AI/incomplete/altered evidence or a fake test mapping. The architecture's good prose does not make this predicate sufficient.

**Recommended remediation:** Define and prove a complete admissibility pipeline, separate reported outcome, inspected test/assertion content, reviewer relevance rationale, integrity, baseline/revision freshness and execution completeness. Ordinary JUnit need not contain assertion detail: require an independently inspected pinned test or recorded manual observation when it does not. Reject unsupported support claims without rewriting imported provenance. Keep imported trust limitations explicit; independent cryptographic attestation is outside the current baseline.

**Required verification:** Independently authored irrelevant/forged/mapped/unmapped assertions; matching IDs with wrong semantics; altered, stale, skipped, setup-failed, incomplete and AI-origin inputs; current pass/fail conflicts; known relevant passing and failing controls. Verify UI/export retain the original result and specific unresolved reason. Importer-provided booleans must not be the test oracle.

### F07 — HIGH — Unsupported-only verdict language can override admissible independent evidence

**Affected requirements:** SG-R008-AC02, SG-R018-AC02, SG-R029-AC01–AC02; SG-R046-AC01 as a later consumer; D05, D07, D12.

**Evidence:** Architecture §9 item 4 states that a criterion whose required scope is unsupported remains unresolved in an unsupported-only audit. The normative verification policy says a scope notice does not itself determine a verdict and sufficient independent supported evidence follows ordinary pass/fail/conflict rules. Architecture §9 item 5 explicitly provides that exception only for partial coverage. The blanket wording is therefore inconsistent or materially ambiguous.

**Counterexample and impact:** In an unsupported-only source repository, a criterion has an independently recorded admissible demonstration of the specified output, or a directly relevant supported imported assertion. Repository analyzer coverage remains unsupported, but that observation can still establish the criterion outcome. Applying item 4 unconditionally suppresses verified/failed evidence and misstates exported results. Conversely, an unrelated green report must remain unresolved regardless of coverage label.

**Recommended remediation:** Align the design interpretation to the unchanged normative policy: repository coverage and criterion support are independent decisions. Scope-driven unresolved status applies when unsupported dependence prevents sufficient evidence; retain all notice references/reasons and conflicts. This is a recommendation only; this review does not edit policy or architecture.

**Required verification:** A full coverage × admissibility matrix: supported/partial/unsupported-only repositories with no independent evidence, relevant pass, relevant fail and conflict, plus unrelated green reports and unaffected criteria; assert UI/reopen/export agreement and stable notice IDs.

### F08 — HIGH — Requirement-derived case generation has neither a complete input schema nor an oracle proof

**Affected requirements:** SG-R024-AC01, SG-R025-AC01, SG-R026-AC01–AC02, SG-R027-AC01, SG-R028-AC01; D02.

**Evidence:** The data model has only `rule/condition` and an expected outcome; API contracts omit confirmed rule creation/editing. E08 accepts four envelope fields, permits only accept/reject outcomes, and has no documented-failure rule. CE04 accepts `rev-999` numeric-boundary input without field, actual revision match, numeric domain, bound or step. The report admits no generator was tested.

**Counterexample and impact:** Independently validating an upper and lower bound can generate contradictory outcomes at their intersection. A Boolean field has no correctly typed out-of-domain value if both Boolean values are allowed. Binary accept/reject cannot represent a documented timeout's specified response or state observation. A human approval click cannot recover missing rule semantics or establish an independent oracle.

**Recommended remediation:** Specify typed, criterion-revision-bound rule records for all four approved rule families, exact decimal/domain handling, joint bounds, inapplicable violations, conflicts and undeclared transitions; carry their explicit outcomes into immutable reviewed case revisions. Keep deterministic generation separate from any AI draft and from execution authority.

**Required verification:** Independent expected case sets for both approved seed examples and renamed/new thresholds/fields/states; combined bounds, impossible domains, contradictory rules, declared failure setup/trigger/outcome and stale rule revisions. Reject underspecified rules without inferred outcomes; prove review does not auto-execute.

### F09 — MEDIUM — Exact criterion matching and two-stack analyzer feasibility are not established

**Affected requirements:** SG-R008-AC01–AC02, SG-R009-AC01, SG-R010-AC01, SG-R020-AC01, SG-R021-AC01, SG-R022-AC01, SG-R037-AC01; D02, D07.

**Evidence:** CE01 calls the proof's `exact_id_refs` with known `SG-R001` and `SG-R001-AC01`; whole input `SG-R001-AC01` yields `[]`. Its regex only recognizes requirement IDs and excludes the trailing hyphen, so it cannot produce the required criterion candidate. E04's separate `re.search` accepts an embedded substring and does not exercise that matcher. E03 extracts Python names and TSX lexical names; E07 covers only one `pass` route and literal inline handler, with no canned-response implementation.

**Counterexample and impact:** A source comment containing only a correct criterion ID produces no trace, while a substring check in `test_case_for_SG-R001-AC01` misleadingly passes the proof even though underscores are identifier-token characters under the PRD. String/comment decoys, aliases, routers, async handlers and resolved local functions need syntax-aware handling. Unchanged-fixture repetition does not prove full deterministic finding/link/verdict behavior.

**Recommended remediation:** Design complete identifier token matching and syntax-aware static indexing for both approved stacks, including positive/negative ghost rules and explicit unsupported diagnostics. Keep source locations bound to the pinned baseline; do not require unchanged line numbers across genuinely changed commits.

**Required verification:** Whole requirement/criterion IDs, case and token boundaries, no requirement-prefix double candidate; FastAPI stub variants and negatives; inline/local React handlers and negatives; both Next.js routing modes; marked literals with adjacent comments; renamed/moved artifacts, mixed/unsupported scope and repeated normalized outputs. No application import or execution.

### F10 — MEDIUM — Several passing experiments cannot detect the failure they name

**Affected requirements:** SG-R001-AC01, SG-R002-AC01, SG-R004-AC01, SG-R020-AC01, SG-R021-AC01, SG-R027-AC01, SG-R033-AC01, SG-R037-AC01; D01–D04, D06–D07, D12.

**Evidence:** E07's `undecorated_helper_not_a_route_stub` is `helper_only and route_stub`; it never asks a detector whether the helper was flagged. `potential_false_positive_is_reviewable_candidate` and E08's `draft_is_not_approval_or_verdict` are literal `True`. E10 tests a changed invocation only after consuming the token, so the assertion cannot distinguish used-token rejection from binding validation. E01/E12 digest equality against copied identical bytes cannot prove persistence or consent binding.

**Counterexample and impact:** An analyzer that also flags every helper still passes the E07 nonmatch check. A reusable-approval bug on fresh changed invocations is invisible to E10's sequence. Calling these checks green is accurate for their expressions but lends no evidence to the named boundary. SG-04B discloses many limitations; its cautious conclusion is appropriate, but individual check labels still overstate observations.

**Recommended remediation:** Use independently specified observable outputs and sentinels, not constant flags or fixture-presence checks. Separate each negative control and approval state. Keep primitive checks labelled as primitives and preserve historical results; do not retroactively present planned tests as run.

**Required verification:** Show that each check fails under a deliberately defective detector/approval/state implementation and passes under the intended behavior. Record actual outputs and independent expected results; rerun only within a controlled Design experiment. No mutation experiments were performed by this review.

### F11 — HIGH — Provider transport and prompt-injection containment are only policy statements

**Affected requirements:** SG-R013-AC01–AC02, SG-R038-AC01–AC02, SG-R039-AC01–AC02; D04, D10.

**Evidence:** Architecture §7 has appropriate consent, redirect and proposal-only intent, but §14 defers transport, DNS/endpoint validation, proxy behavior and credentials. E12 uses a Boolean and a local password regex; it exercises no destination, serialization, revocation, redirect, response or request capture. E08 is a hand-authored case-rule envelope, not an AI trace-response schema or prompt-injection test. Data-model language calling provider proposals an evidence class needs an enforceable separation from admissible observations.

**Counterexample and impact:** An injected source comment tells the model to claim that tests ran and emit a plausible existing path/line with a fabricated verification rationale. Valid references alone do not make that claim evidence. A permitted string field can carry instructions or active links even when extra JSON fields are rejected. A transport serializes different bytes from the preview, a revocation races dispatch, or a configurable endpoint/proxy leaks authentication to an unintended destination. No such transmission was attempted here.

**Recommended remediation:** Define a strict trace-proposal schema and taint boundary through review, persistence, rendering and export; no tools, executable actions, evidence creation or verdict authority may arise from model text. Select endpoint/scheme/address/TLS/proxy/credential policy and exact request serialization, credentials handling, bounded streaming and dispatch/revocation linearization. Resolve endpoint policy within the approved product boundary rather than silently imposing new product requirements.

**Required verification:** Two controlled endpoints with exact byte capture, changed audit/payload/full endpoint, revoke-before-dispatch, redirect refusal, timeout/error/oversize/malformed/invalid-reference responses and sanitized logs. Hostile source/report/provider strings should include schema-valid fabricated claims and instruction text; prove they remain inert inferred suggestions and cannot mutate requirements, evidence, approvals or verdicts. Deterministic/manual workflows and prior results must remain available.

### F12 — HIGH — API and data model cannot yet express the complete approved workflow consistently

**Affected requirements:** SG-R004–SG-R007, SG-R010–SG-R012, SG-R015–SG-R019, SG-R023, SG-R024–SG-R030, SG-R036 (all their criteria); D01, D02, D05, D11, D12.

**Evidence:** The API table defines review of an existing link, case approval and report upload, but no explicit manual link creation, clarification classification, staged semantic change/replacement/split/retirement approval, finding dismissal, rule editing or assertion relevance mapping operation. There are no complete request/response schemas or transition tables. The data model lacks first-class change proposals and clarification decisions. `Artifact` requires paths inside the pinned repository even though an uploaded original specification may be outside it. Baseline immutability, later index/coverage production and baseline activation/sealing order are not reconciled. Requirement/method placement differs between the canonical catalog and criterion record without a translation contract.

**Counterexample and impact:** A reviewer uploads a threshold change and the specification endpoint returns accepted: the contract does not say whether that merely stages the source or activates the changed baseline before SG-R007 approval. A manually linked test can have an artifact locator but no executable identity/mapping operation. A second baseline can reuse criterion revision 1; a verdict referencing only that revision and an evidence-set digest needs explicit audit/baseline identity to prevent collision or wrong export. A valid specification uploaded outside Git cannot satisfy a repository-only artifact path invariant literally.

**Recommended remediation:** Specify the domain records and typed API transitions needed for the already approved workflows, including audit/baseline-scoped composite identities, source kind/locator, staged versus activated baselines, review decisions, provenance and idempotency/concurrency checks. Define how imported catalog fields map to domain types and how verdicts/history/export bind the exact snapshot and evidence set. Endpoint naming can remain flexible; behavioral contracts cannot.

**Required verification:** Walk every P0 case and MVP scenario through concrete requests, state transitions and persisted records, including pending/declined/approved changes, replacement/split/retirement, manual links, clarification and relevance decisions. Negative tests must reject cross-audit/baseline references, concurrent stale updates, reused retired IDs and invalid transitions; round-trip external accepted specs and historical verdicts. Do not implement these changes as part of this review.

### F13 — MEDIUM — P1/P2 coverage is nominal, with no feature-specific design contracts

**Affected requirements:** SG-R040–SG-R054 / their fifteen criteria; M7 and M8.

**Evidence:** Matrix rows name future adapters and point mainly to architecture §§11/15, baseline/history prose or summary intent. No capture/reference/metric/threshold records, drift/comparison contracts, release summary contributing-set schemas or repair/diff/check records are defined. P1 visual flow remains explicitly assigned to M7, which correctly preserves the baseline.

**Counterexample and impact:** A screenshot passes a comparison while the save/readback fails; a single generic evidence outcome could collapse those independent observations. A repair proposal can alter test expectations rather than product behavior unless the later contract limits it. Mapping these rows is not evidence that those later capabilities are designed or feasible.

**Recommended remediation:** Explicitly carry these as later Design deliverables before their dependent M7/M8 implementation, preserving all approved features and priorities. Reserve distinct capture/interaction/reference and repair proposal types and authority boundaries as needed. Detailed P1/P2 implementation is not required to close P0 acceptance, but broad claims of full architecture completion are premature.

**Required verification:** Later feature-specific contract review and all twelve P1/three P2 acceptance cases, including broken-save independent results, threshold/missing-reference states, added/retired comparison, empty coverage, unresolved P0 drilldown, read-only scoped diff and mapped validation checks.

### F14 — MEDIUM — Historical proof output lacks a self-contained reproducibility/provenance envelope

**Affected requirements:** SG-R014-AC01, SG-R016-AC01, SG-R017-AC01, SG-R037-AC01 as the evidence-design obligations under review; D06, D07, D12. This is a development-evidence limitation, not a claim that these unimplemented product requirements have failed acceptance.

**Evidence:** `experiments/sg04b/results.json` includes Python version and check Booleans but not harness/input hashes, dependency versions, actual process invocation metadata or captured environment inventory. Harness `main()` prints JSON and does not write `results.json`; reproducing the stored artifact requires explicit capture or comparison. The starting Git commit does not identify untracked SG-04A/SG-04B files. SG-04B inventory observations are narrative, without a raw inventory artifact.

**Counterexample and impact:** An unchanged-looking results file can outlive a modified harness or a changed parser dependency, while the HEAD identifier remains identical. Twelve PASS labels then do not identify which bytes produced them. Current reproduction matched the entire stored JSON; that supports current reproducibility but cannot retroactively authenticate the historical run or its environment inventory.

**Recommended remediation:** Future proof records should capture invocation/result, tool versions, input/harness hashes, bounded fixture identities and scope/limitations together. Preserve historical claims as historical; record unavailable fields rather than inventing them. Store observed inventory output when it supports a feasibility claim.

**Required verification:** Regenerate in a documented controlled environment, compare output against identified inputs, and show a changed harness/fixture/version changes the provenance envelope or is explicitly accounted for. This review supplies current hashes, versions and an exact JSON comparison; it does not manufacture missing historical metadata.

## Failure recovery, feasibility and approved schedule

Atomic intake, retained prior work, fresh approvals, resource overruns as incomplete and restart-persistent cleanup blocks are correctly stated as required behavior. They remain unverified and need concrete storage/runner state machines (F04/F05/F12). Error labels and idempotency keys alone do not make retries safe. Reconciliation must handle the gap between durable local state and external runner allocation; rollback of a database transaction cannot undo a launched process.

There is no active approved calendar delivery target. GOALS and ADR 0002 explicitly replace the historical one-month hypothesis with milestone-driven progression and prohibit developer-hour/FTE or calendar-based scope cuts. Therefore no calendar feasibility verdict is inferred. The approved scope remains 39 P0 requirements, followed by twelve P1 requirements across four features and three P2 requirements. No requirement, priority or acceptance criterion is changed here.

The decomposition is technically plausible, but available evidence does not establish that the selected product can meet its P0 obligations on any supported host with enforceable limits. Backend inventory in SG-04B establishes only what was found in that environment. Most blockers are unresolved Design selections/proofs, not demonstrated impossibility. The next authorized work should be bounded M3 proof preparation/execution and review, after the product owner approves that scope; it must not be represented as M4 implementation approval.

## Commands, observed results and limitations

- `Get-Content`, `rg --files` and `rg -n` inspected guidance, baseline, architecture, decisions, proof source/results and model/evidence tooling. `git status --short` and `git rev-parse HEAD` established the dirty working-tree review boundary and starting commit.
- `python -B codex-evidence/review/SG-04C-checks.py`: initial run failed with `KeyError: requirement_id` because the new reviewer script did not account for the existing CSV's UTF-8 BOM. The reviewer script was corrected to read `utf-8-sig`; no input artifact changed. Subsequent runs passed. This was a review-tool error, not a product finding.
- Independent structural check passed: 54 requirements, 68 exact catalog/case/matrix mappings, 85 source paths, acyclic dependencies, all twelve mandatory rows OPEN. Source-heading anchors were not independently validated by this check.
- Reviewed SG-04B harness rerun through its `main()` reproduced **12 PASS, 0 FAIL**, with the complete resulting JSON equal to the stored JSON. Current packages: Python 3.12.7, PyYAML 6.0.3, Mistune 3.4.0, defusedxml 0.7.1. These are current observations, not recovered SG-04B dependency metadata.
- Five independent counterexamples reproduced the observed outputs CE01–CE05; these characterize incomplete proof functions/candidate primitives, not actual product behavior. Other counterexamples in findings are reasoned test cases and were not executed.
- Product acceptance, browser/session, actual runner/isolation/resource, provider transport, crash-injection, persistence and integrated MVP tests were **not run**. No benchmark, real secret, model-generated proposal experiment or remote provider request occurred.

Final validation completed:

- `python -B -m unittest discover -s tests -v`: **10/10 passed**. These test the existing evidence/model-report tooling, not SpecGuard product behavior.
- `python -B -m scripts.generate_model_report`: completed; an independent in-memory comparison matched the generated file. Ledger contains **15 unique executions**, including exactly one `SG-04C-20261124-01` row; no duplicate execution IDs.
- Inline final validator passed: 14 unique findings with the stated severity distribution; all 68 independent criterion-review rows across 54 requirements refer to valid finding IDs; **49 local Markdown paths** resolve across the review, review README, evidence index and plan. Heading anchors were not checked.
- SHA-256 reconciliation found **41 reviewed input files unchanged**, excluding the explicitly updated PLANS review-status row. Requirements, architecture documents, prior stage reports and original experiment source/results remained byte-identical to this review's captured inputs.
- `git -c core.safecrlf=false diff --check HEAD`: passed. Git's LF/CRLF notices are working-copy configuration notices, not failed checks.

## Files changed by SG-04C

Evidence artifacts created:

- [SG-04C.md](SG-04C.md): this independent report, findings, gate recommendation, actual metadata, commands/results and approval boundary.
- [SG-04C-criterion-review.csv](SG-04C-criterion-review.csv): 68-criterion independent coverage assessment.
- [SG-04C-checks.py](SG-04C-checks.py): reproducible review tooling; no product fix.
- [SG-04C-check-results.json](SG-04C-check-results.json): actual structural/reproduction/counterexample observations and current tool versions.
- [SG-04C-input-manifest.json](SG-04C-input-manifest.json): initial review input hashes and sizes.

Evidence/navigation records updated:

- [Review README](README.md) and [EVIDENCE_INDEX.md](../EVIDENCE_INDEX.md).
- [MODEL_USAGE.csv](../models/MODEL_USAGE.csv): unique developer-confirmed Sol / High review execution; unavailable measurements N/A.
- [MODEL_REPORT.md](../models/MODEL_REPORT.md): regenerated aggregate of Codex development usage, separate from SpecGuard runtime LLM use.
- [PLANS.md](../../PLANS.md): M3 status records this review and its pending product-owner approval; no milestone exit criteria changed.

MODEL_STRATEGY.md and MODEL_EXPERIMENTS.md were not changed. No controlled model comparison occurred. Existing dirty-worktree changes from previous tasks remain outside this execution's change set.

## Product-owner approval boundary

The independent review is submitted for product-owner approval with **NOT READY FOR IMPLEMENTATION**. Accepting the review does not close any gate or authorize requirements changes or production implementation. Recommended follow-up is to authorize a bounded M3 remediation/proof plan addressing the findings and required condition evidence, then request another design gate review. This execution stops after evidence recording and verification. No fixes are implemented and no commit, push or deployment is performed.
