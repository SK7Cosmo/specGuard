# SG-03C Independent Requirements Re-review

## Verdict

**READY WITH EXPLICIT CONDITIONS**

SG-03B made substantive changes to the requirements and acceptance cases. The revised baseline distinguishes a failed product assertion from a passing report that supplies insufficient evidence, defines observable security and recovery outcomes, and keeps the approved P0, P1, and P2 gates. M3 can begin with the conditions below. The owner decision on secret-bearing specifications gates the affected intake and storage design. Runtime feasibility still depends on M3 evidence, and the P0 acceptance gate still belongs to M5.

## Original finding dispositions

IDs follow the SG-03B mapping of the eight findings in the [original SG-03 review](SG-03-requirements-review.md#findings-by-severity). The dispositions assess requirements and acceptance oracles.

| Finding | Disposition | Independent assessment |
|---|---|---|
| F01 Technical feasibility | Deferred Design decision | ADR 0002 superseded the schedule premise. The technical concern remains open. The M3 register names the intake, two-stack indexing, persistence, local access, isolation, provider, and integration dependencies and their required exit evidence. A failed proof blocks the associated M4 work. See [ADR 0002](../../docs/adr/0002-milestone-driven-development-baseline.md#sg-03-finding-disposition) and the [M3 decision register](../../docs/adr/SG-03B-design-decision-register.md). |
| F02 P0 fixture and broken-save gate | Resolved | MVP-01 and SG-R029-AC02 distinguish the omitted field's mapped failing assertion from the unrelated passing report. The latter leaves a separate criterion unresolved and retains the report's provenance. The P1 broken-save flow separately records a passing screenshot comparison and failing save/readback under SG-R042-AC01. See the [PRD exit gate](../../docs/PRD.md#mvp-completion-criteria) and [fixture plan](../../docs/TEST_PLAN.md#strategy-and-fixture). |
| F03 Security acceptance boundaries | Partially resolved | SG-R031, SG-R034–SG-R035, and SG-R038 now cover authorization before disclosure or mutation, fail-closed execution, cleanup, and bounded redaction. SG-03B records the approved browser-origin threat boundary. A covered secret in an otherwise valid original specification still has no defined intake, retention, or exact-source-view outcome. Existing runner approval and safe-rendering oracles also need explicit fixture observations. See [security and failure handling](../../docs/VERIFICATION_POLICY.md#security-and-failure-handling) and conditions C1–C2. |
| F04 Objective and generalizable acceptance | Partially resolved | SG-R006-AC01 checks the recorded reviewer decision. SG-R009 and SG-R020–SG-R022 use finite rules and positive and negative examples. SG-R024–SG-R026 define typed inputs and reviewer-confirmed outcomes. The fixtures still leave parts of that contract unexercised, including jointly evaluated bounds, an impossible field violation, and conflicting rules. See the [analyzer boundary](../../docs/PRD.md#deterministic-analyzer-boundary), [proposal rules](../../docs/PRD.md#adversarial-case-proposal-rules), and condition C2. |
| F05 AI consent and provider failures | Resolved | SG-R039 binds approval to the audit, exact sanitized bytes and endpoint at dispatch. Its cases cover denial, revocation, mutations after approval, fresh approval, and redirect withholding. SG-R013 and SG-R038 exercise provider and redaction failures with deterministic or manual fallback and prior verdict retention. The separate intake privacy issue is recorded in F03. See [remote suggestion policy](../../docs/VERIFICATION_POLICY.md#redaction-and-remote-suggestions) and [P0 cases](../../docs/TEST_PLAN.md#p0-acceptance-cases). |
| F06 Requirement and criterion identity | Resolved | SG-R005 and SG-R007 distinguish wording changes, semantic revisions within a continuing obligation, replacements, splits, and retirement. The cases verify approval gating, stable or new IDs as applicable, lineage, prior evidence attribution, and stale evidence after semantic change. See the [catalog contract](../../docs/PRD.md#canonical-catalog-contract) and [P0 cases](../../docs/TEST_PLAN.md#p0-acceptance-cases). |
| F07 Import and runner failure coverage | Resolved | SG-R015, SG-R032, SG-R034–SG-R036 and MVP-03 add observable failures for invalid snapshots, malformed or excessive reports, prohibited XML declarations, setup, process-tree cleanup, teardown across restart, and recovery. Results preserve earlier evidence and identify the failure. M3 still selects and validates limits and containment under C3. See the [failure paths](../../docs/TEST_PLAN.md#end-to-end-acceptance-and-additional-failure-paths) and [P0 cases](../../docs/TEST_PLAN.md#p0-acceptance-cases). |
| F08 Unsupported coverage and sign-off | Resolved | SG-R008-AC02, SG-R018-AC02, and MVP-04 test supported, mixed, and unsupported-only audits. Repository scope notices survive reopening and export, and affected unresolved criteria reference the notices. Independent admissible evidence can still yield a verified or failed verdict. See the [coverage contract](../../docs/PRD.md#coverage-and-export) and [MVP scenarios](../../docs/TEST_PLAN.md#end-to-end-acceptance-and-additional-failure-paths). |

The recorded threat model excludes developer-account compromise, hostile local processes able to steal session proof, compromised hosts or runner backends, and attacks outside the configured resource model. Exceeding configured limits still triggers rejection or termination. Handling supported inputs that contain sensitive data remains an open question within that boundary. [Approved boundary evidence](SG-03B.md#execution-record) · [Verification policy](../../docs/VERIFICATION_POLICY.md#threat-model-and-local-audit-access)

## Cross-cutting review

### Requirement completeness and consistency

The catalog retains all 54 requirements and all 57 original criterion IDs. SG-03B added exactly the ten recorded P0 criteria and revised 23 existing outcomes. All 67 entries match the test plan by ID, priority, method, and expected result. The dependency graph is acyclic and every dependency has the same or higher priority. All five MVP scenarios and 85 catalog sources resolve. SG-R042 is the only P1 catalog change and makes the failed readback explicit. The P1 fixtures for SG-R043 and SG-R051 now name retirement as the form of removal, with the same expected outcomes. The P2 catalog and case rows are unchanged. [Catalog](../../docs/REQUIREMENTS.yaml) · [Test plan](../../docs/TEST_PLAN.md) · [SG-03B approval and counts](SG-03B.md#requirement-and-acceptance-counts)

### Objective acceptance criteria

The fixture redesign supplies independently observable outcomes. For example, a passing test of the wrong behavior and a failing assertion of the right behavior now produce different audit outcomes. The bounded analyzer rules can be checked at named snapshot locations, and the proposal rules can be checked against independently authored expected outcomes. The remaining proposal fixtures need to exercise combined predicates, inapplicable violations and conflicting rules so a narrow generator cannot satisfy sign-off by recognizing the seeded examples. [Fixture strategy](../../docs/TEST_PLAN.md#strategy-and-fixture) · [Proposal rules](../../docs/PRD.md#adversarial-case-proposal-rules)

### Security and privacy boundaries

SG-R004-AC01 requires the exact retained source span. The PRD also requires exact-byte hashing and retention of the imported specification alongside redaction before persistence or transmission. SG-R038 cases use secrets in logs and trace context and exercise injected redaction and validation failures. The outcome for a valid source specification containing a covered secret is unspecified. Rejecting the import, preserving raw bytes under an explicit storage policy, or limiting exact-span display would give different externally visible results and privacy boundaries. C1 requires an owner decision before dependent design is finalized. [PRD scope and inputs](../../docs/PRD.md#supported-inputs-and-limits) · [Redaction policy](../../docs/VERIFICATION_POLICY.md#redaction-and-remote-suggestions) · [P0 cases](../../docs/TEST_PLAN.md#p0-acceptance-cases)

### Evidence provenance and verification semantics

The policy preserves observed, imported, inferred and reviewer-confirmed provenance. A Vault digest checks artifact integrity against the recorded digest. An imported result needs confirmation of baseline, test identity, criterion mapping, and relevance. A matching ID or reviewed link can identify a candidate source of evidence. To prove the underlying behavior, the observation must directly address the expected outcome. MVP-04 checks stale and conflicting results, SG-R017 checks altered artifacts, and SG-R029 checks skipped, missing, failing and insufficient results. For the passing JUnit report in MVP-01, the fixture must retain the independently inspected assertion or recorded reviewer relevance decision because the stated JUnit input contract supplies test identity and outcome. The overall SpecGuard acceptance case passes when the seeded audit records the expected failed or unresolved verdict. [Provenance and verdict policy](../../docs/VERIFICATION_POLICY.md#evidence-and-provenance) · [Test plan exit criteria](../../docs/TEST_PLAN.md#exit-criteria)

### Failure-path coverage

The revised cases specify rejection or bounded failure for invalid specification, Git and JUnit intake, unauthorized requests, runner setup, limits and unverified teardown, and provider and redaction failures. They require preserved prior state on the specified failures and visible distinctions among blocked, incomplete, failed and unresolved outcomes. Recovery after unverified teardown requires demonstrated cleanup and fresh approval. SG-R033 calls for one attempted run per approval, while its listed actions only change arguments or baseline. A direct unchanged-invocation replay check and a separate check that untrusted stored text is rendered safely are needed for the existing safeguards under C2. [Security and failure policy](../../docs/VERIFICATION_POLICY.md#security-and-failure-handling) · [P0 cases](../../docs/TEST_PLAN.md#p0-acceptance-cases)

### Technical feasibility and dependencies

Pinning and parsing the snapshot precede indexing and stable source references. Those references are prerequisites for linking, imported-result attribution, and provider-reference validation. Evidence storage and revision history carry those decisions through reopen and export. Local authorization protects audit operations and approvals. Isolated execution and remote suggestions have separate containment and consent gates. Integration depends on all of these behaving consistently across both supported frameworks. The register assigns seven decisions to M3 with controlled exit evidence. Windows with WSL2/Docker is a candidate in that register. Backend selection, numeric limits, proof of containment, and the complete integrated fixture remain M3 work. [Decision register](../../docs/adr/SG-03B-design-decision-register.md) · [Milestones](../../PLANS.md)

### Preservation of approved product scope

The primary user remains the solo developer auditing one pinned local Git snapshot against its original specification. The approved scope retains the loopback web workflow, both framework families, report import, approved isolated execution, opt-in remote AI suggestions, and the deterministic and manual workflow. All approved P0, P1, and P2 features and their milestone order remain. [SG-02 approvals](../specify/SG-02.md#scope-and-approvals) · [ADR 0001](../../docs/adr/0001-audit-operating-boundary.md)

### Compliance with ADR 0002

Active development gates are based on milestone deliverables and validated acceptance and preserve all eight lifecycle stages. The schedule premise appears as superseded or historical context. Runtime timeouts, performance requirements, resource limits, and security timing controls remain applicable. [ADR 0002](../../docs/adr/0002-milestone-driven-development-baseline.md) · [Goals](../../GOALS.md) · [Milestones](../../PLANS.md)

### Mandatory evidence tracking

The original SG-03 report, SG-03A, SG-02 evidence, both ADRs, and the model strategy and experiment files match the starting commit after line-ending normalization. The existing ledger and aggregate report agreed before this review. The original SG-03 report has a phase, task, date and Git reference. The tracked evidence has no corresponding SG-03 ledger row, and the original report supplies no model, effort, or session ID. This is a historical evidence gap. It was preserved for developer follow-up if the original metadata can be confirmed. The SG-03C records cover both actual executions and use the developer's confirmed model label. [Original review record](SG-03-requirements-review.md#review-record) · [Model strategy](../models/MODEL_STRATEGY.md) · [Evidence index](../EVIDENCE_INDEX.md)

## Conditions for developer review

| ID | Accountable role | Required decision or evidence | Gate |
|---|---|---|---|
| C1 | Product owner, with M3 intake and Vault design owners | Decide the behavior for a valid Markdown or YAML specification containing a covered secret. Specify acceptance or rejection, what may be retained or displayed before and after restart, how exact digest and source-span guarantees apply, and the result or sanitized reason visible to the user. Require a controlled fixture showing the approved behavior through intake, storage, source view, reopen, and export. Any normative change needs owner authorization. | Clear before signing off on the affected intake, Vault, and source-view design. Independent M3 work can proceed. |
| C2 | M3 Design and acceptance-fixture owner | Define explicit fixture observations for jointly enforced bounds, an impossible field violation, a conflicting rule with no inferred outcome, unchanged-command replay under one consumed approval, and safe rendering of untrusted stored text. For MVP-01 and SG-R029-AC02, record the independent assertion inspection or reviewer relevance decision alongside the imported JUnit outcome. Use these observations to verify the existing contracts at M5. | Clear the fixture design before dependent M4 work and record passing evidence at M5. |
| C3 | M3 Design owner | Resolve the existing decision register with controlled evidence for snapshot and parser boundaries, both framework indexes, local session authorization, runner containment and recovery, exact provider consent and fallback, Vault round-trip and revision behavior, and full-gate fixture mapping. Record unresolved or failed proofs against the affected capability. | Clear each decision before dependent M4 work. M5 still requires all 52 P0 criteria and five MVP scenarios. |

## Session evidence

| Field | Plan Mode | Report execution |
|---|---|---|
| Lifecycle phase and task | Review, SG-03C | Review, SG-03C |
| Unique execution ID | `SG-03C-20261124-01` | `SG-03C-20261124-02` |
| Platform session ID | N/A | N/A |
| Client date and timezone | 2026-11-24, Asia/Calcutta | 2026-11-24, Asia/Calcutta |
| Starting Git commit | `957c138c4720c9783c47b23aa9ffc19dc44d29e6` | `957c138c4720c9783c47b23aa9ffc19dc44d29e6` |
| Actual model and reasoning effort | Sol / High, developer confirmed | Sol / High, separately developer confirmed |
| Selection rationale | Independent cross-document review and security and evidence analysis | Independent cross-document review and security and evidence analysis |
| Session duration, tokens, cost, and resource usage | N/A | N/A |

The developer approved execution of the plan and separately confirmed model, effort and rationale for both executions. Git and PowerShell were used for inspection. Python and PyYAML were used for independent comparison and evidence validation. Execution was limited to documentation and evidence-tool checks. Product acceptance and Design proofs remain pending.

### Commands and observed results

| Execution | Command or check | Result |
|---|---|---|
| Planning and report | `git status --short --branch`, `git rev-parse HEAD`, and scoped `git diff` | Both executions started on the recorded commit with existing SG-03B working-tree changes. The read-only diff was the baseline for the review. |
| Planning | Inline read-only `python -B -` validator using PyYAML and the ledger report function | Confirmed all 54 IDs, 57 retained criteria, 67 exact case rows, five MVP rows, 85 source references, valid dependencies, and an aggregate report matching seven existing unique ledger entries. |
| Report | Expanded inline read-only `python -B -` validator | The initial comparison surfaced the SG-R042 clarification and two P1 fixture-only edits. Direct inspection confirmed their existing gates and intent. The verified comparison found the ten approved additions, 23 revised outcomes, preserved dependency and priority metadata, and 137 working-tree Markdown links before adding this report. SHA-256 fingerprints identify the reviewed files and tracked diff. |
| Planning and report | `python -B -m unittest discover -s tests -v` | All ten report-generator tests passed in each execution. |
| Report | `python -B -m scripts.generate_model_report` and in-memory comparison | Regenerated the aggregate from nine unique records, including the two SG-03C entries. The checked report matched the ledger with zero malformed or duplicate rows. |
| Report | `git -c core.safecrlf=false diff --check HEAD`, plus local link, whitespace and before/after file fingerprint checks | Passed. All 181 local Markdown links resolved after adding the report. The only SG-03C changes were the four evidence files below. |

Evidence files changed: this report, the [evidence index](../EVIDENCE_INDEX.md), the [model usage ledger](../models/MODEL_USAGE.csv), and the [generated model report](../models/MODEL_REPORT.md).

### Reviewed baseline fingerprints

The tracked requirements and roadmap diff against the starting commit has SHA-256 `87afa83a844377dde870b249225f71797511f81edcb40ab19f76cc4b84d67272`. Reproduce it with `git -c core.safecrlf=false diff --no-ext-diff --no-textconv --no-color --binary HEAD -- GOALS.md PLANS.md docs` from the reviewed checkout. This diff covers the paths below. The untracked SG-03B decision register and review record are identified separately by their file hashes.

| Tracked path | Added lines | Removed lines |
|---|---:|---:|
| `GOALS.md` | 1 | 1 |
| `PLANS.md` | 4 | 4 |
| `docs/FAILURE_SCENARIOS.md` | 2 | 1 |
| `docs/PRD.md` | 43 | 8 |
| `docs/REQUIREMENTS.yaml` | 59 | 39 |
| `docs/RESEARCH.md` | 2 | 8 |
| `docs/TEST_PLAN.md` | 52 | 32 |
| `docs/VERIFICATION_POLICY.md` | 30 | 9 |
| `docs/adr/README.md` | 1 | 0 |

| Reviewed input | SHA-256 of working-tree bytes |
|---|---|
| `GOALS.md` | `89c15aa271611d42f3050342ca7d3eaaccf394d7caa8d72c4cda03e69770784f` |
| `PLANS.md` | `f9c98be28a2f3c275014dd737878d373d1bf0082bd8fdefc107bc53fa6c8e2ed` |
| `docs/PRD.md` | `363bb509abe0a116ad62db545656c87c226a8e6aa300a7e8bbfb5eea1ebfe03d` |
| `docs/REQUIREMENTS.yaml` | `8232eb404c7a1bcdc5a8394cadf189a1136fec970c4f0ae5acc6f5753d5753b7` |
| `docs/TEST_PLAN.md` | `fa4924dd1d562b455eee5812ee6ce74443b83481596a735696d8e7aef47d8818` |
| `docs/VERIFICATION_POLICY.md` | `6871c7aa0053f04fbcb69d4a0c88bc59681db7df0641fa85d8366915e7a5b112` |
| `docs/FAILURE_SCENARIOS.md` | `b6eb7670e20acbc315c98d1bb56d7ecf76220faa69492332f751e30324618c19` |
| `docs/RESEARCH.md` | `14e91a2452023d901cb004f65fc111a39def6b127a7095157a7e74f4d04d3d2f` |
| `docs/adr/README.md` | `d11b5d751d7a9f690f933e9b739a2ca17bf7fff9c2d40347a3c42d1a8f22340a` |
| `docs/adr/0001-audit-operating-boundary.md` | `1c5a70352282528fb4df38bd36d369ed5252d71abb2b44179c5fc49098287c3e` |
| `docs/adr/0002-milestone-driven-development-baseline.md` | `8b602246fbba8e8798f4a1d1e6afcadbf05657b24747e7ce1fcec8caa211a355` |
| `docs/adr/SG-03B-design-decision-register.md` | `02aa12152b465616d555b521d06a57dc9d3ff22558cc44865e4753bbbd1bc24f` |
| `codex-evidence/specify/SG-02.md` | `d4d2425cf358edf4f2394910cf94a31019f2985efe58cffbefdad41be0203f79` |
| `codex-evidence/review/SG-03-requirements-review.md` | `13826192147d96bac742a2e1827d609e3632d752dd22c28e5dbf755b629a352c` |
| `codex-evidence/review/SG-03A.md` | `aee38fc9265eb0d3058ff100828c8299f1449751265d8d507f938c89b29e74e9` |
| `codex-evidence/review/SG-03B.md` | `a167b4b6a177686713ffce4564ac8ebfeb66ee1d8e595439df773fb433c44644` |
