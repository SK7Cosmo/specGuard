# SG-03 independent requirements review

## Review record

| Field | Value |
|---|---|
| Lifecycle phase | Review |
| Task | SG-03: independent review of the SG-02 PRD, requirements catalog, and test plan |
| Date | 2026-11-24, Asia/Calcutta |
| Starting Git commit | `2e7b6fdf70d4da58c48677d32907fe15810571a8` |
| Review scope | `docs/PRD.md`, `docs/REQUIREMENTS.yaml`, `docs/TEST_PLAN.md`, `docs/VERIFICATION_POLICY.md`, `docs/FAILURE_SCENARIOS.md`, `GOALS.md`, and SG-02 evidence |
| Method | Read-only document review and cross-document comparison. No product code or untrusted repository code was run; no product acceptance tests were executed. |
| Approved-requirements changes | None |

## Overall assessment

The baseline is unusually explicit about evidence provenance, human review, unsupported coverage, stale evidence, and fail-closed test execution. Its principal risk is feasibility: the P0 gate combines a local web product, requirement/spec ingestion, two framework families, static indexing and heuristics, evidence persistence, imported reports, a disposable test runner, remote AI consent and redaction, export, and security controls. Several criteria are also fixture-specific or underspecified, so passing the current fixture would not establish the broader capability implied by the feature names.

**One-month solo assessment: not realistic for the approved P0 gate as written.** A tightly bounded demonstrator could be plausible, but only after the product owner authorizes a narrower P0 milestone or a longer schedule. This review does not change that gate.

## Findings by severity

### Critical — P0 scope does not fit the one-month solo hypothesis

**References:** [GOALS.md](../../GOALS.md) one-month hypothesis; [PRD.md](../../docs/PRD.md#approved-product-scope) and `#mvp-completion-criteria`; [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml) SG-R001–SG-R039; [TEST_PLAN.md](../../docs/TEST_PLAN.md#p0-acceptance-cases).

P0 requires at least 42 criterion cases across 39 requirements, plus the end-to-end gate. It spans Python/FastAPI and React/Next.js, Markdown and YAML ingestion, source indexing, trace review, three ghost heuristics, adversarial case proposals, JUnit import, persistence/reopen/export, a local web UI, a disposable isolated runner, remote-provider consent, redaction, and security verification. The MVP gate requires all P0 criteria to pass. This is materially broader than the discovery-stage hypothesis of one language/runtime, explicit criteria, and existing deterministic checks. With an assumed 20 working days, 42 P0 criteria alone average over two passing criteria per day, before architecture, implementation, integration, fixture work, security review, and defect correction. No time budget or prior implementation is documented.

**Recommended correction:** Before M3, make an explicit product-owner decision: either extend the delivery window, or approve a smaller first gate with named deferred capabilities and a corresponding requirements-baseline revision. A plausible demonstration slice would use one stack, imported JUnit only, explicit structured requirements, deterministic/manual links, and no remote AI or command execution. Treat that only as a proposal; it is not authorized by this review.

**Clarification:** Is “one month” a fixed delivery commitment, and how many developer days are available? If fixed, which P0 obligations may be moved out of the first release gate?

### High — P0 fixture and MVP gate disagree about the broken-save behavior

**References:** [PRD.md](../../docs/PRD.md#mvp-completion-criteria), item 2; [TEST_PLAN.md](../../docs/TEST_PLAN.md#strategy-and-fixture), fixture description; `#p0-acceptance-cases`, SG-R040–SG-R042; [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml), SG-R042.

The test fixture includes a control that looks correct but fails to save. The only criterion that explicitly checks this behavior is SG-R042-AC01, which is P1. Yet the P0 MVP gate says the fixture must surface “unsupported proof,” without defining that phrase or mapping it to an acceptance case. The P0 end-to-end cases do not state an expected result for the broken-save behavior. As written, the P0 gate can be read as requiring this behavior while the catalog classifies its only explicit check as out of gate.

**Recommended correction:** Either remove the broken-save control from the P0 fixture and reserve it for P1, or define the exact P0 evidence and expected result and reconcile its priority. Replace “unsupported proof” with a named seeded condition and criterion ID.

**Clarification:** Does “unsupported proof” mean the broken persistence behavior, a test report with no matching assertion, or a different fixture defect?

### High — Security acceptance depends on controls that are not concretely specified

**References:** [VERIFICATION_POLICY.md](../../docs/VERIFICATION_POLICY.md#security-and-failure-handling); [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml), SG-R031, SG-R034–SG-R035, SG-R038; [TEST_PLAN.md](../../docs/TEST_PLAN.md), SG-R031-AC01, SG-R034-AC01, SG-R035-AC01, SG-R038-AC01.

The policy requires “local session proof” for state-changing requests, but the product requirements do not define session establishment, lifetime, or proof. SG-R031's test uses disallowed Host/Origin or missing session proof without specifying which requests are authorized or how the client gets proof. Runner limits are deferred to M3; SG-R035 only requires configured limits to apply, without numeric defaults or a supported runner/platform contract. Redaction is tested against synthetic credentials, but neither the covered secret classes nor the behavior when a real-world secret is not recognized is bounded. These controls are important P0 obligations, but the current acceptance oracles do not establish their intended security boundary.

**Recommended correction:** In M3, state the local request threat model and an observable session flow; select the supported isolation backend/platform and define its required properties and resource-limit defaults; define the secret classes/redaction contract and fail-closed behavior. Add tests for missing/invalid session proof, runner setup and teardown failure, process-tree termination, and redaction failure. Keep security claims limited to the tested threat model.

**Clarification:** Which host OS and runner backend must the MVP support? Is the product intended to defend against another local process/user, or only accidental browser-origin requests? Which credential formats must the redactor detect?

### High — Test-case outcomes are not consistently objective or generalizable

**References:** [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml), SG-R006, SG-R009, SG-R020–SG-R026; [TEST_PLAN.md](../../docs/TEST_PLAN.md#p0-acceptance-cases), corresponding cases.

Several P0 expectations encode one hand-built fixture rather than a repeatable behavioral rule. SG-R006 asks a reviewer to recognize vague and compound requirements but has no rubric; its manual case proves only that a status can be applied, not that clarification decisions are consistent. SG-R024 fixes the boundary values at 99/100/101, SG-R025 specifies two invalid inputs, and SG-R026 specifies one state transition, without defining the supported input grammar or how expected outcomes are derived. SG-R009 proves exact-ID matching but does not define any broader deterministic signals. SG-R020–SG-R022 use a single stub, empty handler, and explicitly marked sample, while “Only” asserts zero false positives over an unspecified fixture universe.

**Recommended correction:** Define a small supported requirement schema for machine-generated cases and test its boundaries, or explicitly limit these requirements to reviewer-authored, fixture-specific proposals. For subjective clarification, make the objectively testable requirement about recording a reviewer-selected status and rationale, not classifying prose correctly. Specify finite analyzer rules and positive/negative examples; replace unbounded “Only” language with assertions over named fixture files and recognized patterns.

**Clarification:** Is SpecGuard expected to infer vague/compound prose and expected outcomes, or only preserve reviewer decisions and propose cases from structured criteria? Which exact patterns and syntax are in the P0 analyzer contract?

### High — AI consent and redaction lack failure coverage for payload/provider edge cases

**References:** [PRD.md](../../docs/PRD.md#approved-product-scope); [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml), SG-R013, SG-R038–SG-R039; [TEST_PLAN.md](../../docs/TEST_PLAN.md), SG-R013-AC01 and SG-R038–SG-R039.

The user-facing promise covers the exact sanitized excerpts and destination, fresh consent after a change, and safe fallback. Current tests cover an invented path, synthetic credentials, decline/approve, payload changes, and destination changes. They do not explicitly cover provider timeout/error, malformed or oversized responses, redirects or destination changes after approval, redaction failure, or a payload modified between display and send. The policy requires provider failure fallback and withholding when validation/redaction fails, but the P0 acceptance cases do not exercise those branches.

**Recommended correction:** Add deterministic provider-failure cases and assert no verdict is promoted, no unapproved payload is sent, and prior audit data remains available. Define destination identity (including redirect behavior) and the point at which the displayed payload is bound to the submitted payload.

**Clarification:** Are provider redirects prohibited? Which failure classes must be tested as P0, and should AI transport failures leave the audit usable without any state change?

### Medium — Revision identity rules mix stable IDs with meaning changes

**References:** [PRD.md](../../docs/PRD.md#canonical-catalog-contract); [REQUIREMENTS.yaml](../../docs/REQUIREMENTS.yaml), SG-R005 and SG-R007; [TEST_PLAN.md](../../docs/TEST_PLAN.md), SG-R005-AC01 and SG-R007-AC01.

The PRD says preserve IDs across revisions of the same obligation, require approval for an edit that changes meaning, and reassess evidence before reuse. SG-R005's test changes descriptions while keeping IDs but does not state whether meaning changed. SG-R007 changes a threshold and expects the existing ID to remain, while also splitting a compound item. The baseline does not say whether an ID identifies a continuing obligation independently of its wording, or whether a materially revised criterion should receive a new ID. Manual reviewer approval is mentioned, but no explicit classification is part of the test oracle.

**Recommended correction:** Define identity rules with examples: wording-only edit, threshold change within the same obligation, changed obligation, and split/retirement. Have the reviewer explicitly classify the edit and record approval; verify baseline/evidence behavior from that recorded decision rather than expecting software to infer semantic change.

**Clarification:** Should a changed threshold retain the requirement and criterion IDs when it is the same obligation, or create a new criterion identity and supersession link?

### Medium — Import and runner failure scenarios omit important boundaries

**References:** [TEST_PLAN.md](../../docs/TEST_PLAN.md#end-to-end-acceptance-and-additional-failure-paths); [VERIFICATION_POLICY.md](../../docs/VERIFICATION_POLICY.md#security-and-failure-handling); SG-R003, SG-R015, SG-R034–SG-R036.

The tests cover malformed YAML, one local XML external reference, missing isolation, time/output overruns, and interrupted work. They do not define acceptance for malformed or truncated Git objects, missing commits, deeply nested/oversized XML, XML external network retrieval/entity expansion, runner teardown failure, or child-process survival after timeout. These are meaningful failure modes for untrusted repositories and reports and for the required disposable runner.

**Recommended correction:** Select a bounded threat model and add at least one deterministic test per failure class that is in scope. Require safe rejection or an incomplete/blocked result, no source mutation or external fetch, preservation of prior evidence, and a visible reason. If a class is explicitly out of scope, state that boundary rather than implying general resilience.

**Clarification:** Which malformed-Git and XML resource-abuse cases are in the MVP threat model, and what is the required outcome when runner teardown itself fails?

### Medium — Unsupported scope and success criteria leave room for divergent sign-off

**References:** [PRD.md](../../docs/PRD.md#supported-inputs-and-limits), lines describing unsupported coverage and MVP item 2; [TEST_PLAN.md](../../docs/TEST_PLAN.md), MVP-04 and SG-R008-AC02.

“Unsupported content,” “unsupported proof,” “visible unsupported coverage message,” and “surfaces the seeded omitted behavior” do not identify a stable output schema or a required relationship between uncovered artifacts and criterion verdicts. MVP-04 uses a repository with only an unsupported language, while SG-R008-AC02 uses a mixed repository with both supported and unsupported content. Those are compatible cases, but the expected user-visible behavior and whether unsupported coverage blocks a criterion are not explicit.

**Recommended correction:** Specify the unsupported-coverage record fields and distinguish repository-level scope notices from criterion-level unresolved verdicts. Add expected output for both mixed and unsupported-only fixtures, including export behavior.

**Clarification:** Does an unsupported artifact make all criteria unresolved, only criteria linked to that artifact, or just add a scope notice?

## Feasibility judgment

The one-month solo hypothesis is not credible for the complete P0 gate as currently approved. The constraint is not merely the raw number of criteria: security architecture, runner design, two-framework indexing, audit persistence, consent/redaction, end-to-end integration, and reviewable evidence all have substantial cross-component work and must be completed before the gate can pass. The existing discovery record itself estimated one language/runtime and deterministic evidence as the plausible slice and considered broad proof and robust autonomous testing infeasible. There is no implementation to build on in the repository yet; M3 design is not started.

**Recommended decision before implementation:** Set a fixed calendar/time budget and make an explicit scope decision. If the one-month limit is fixed, approve a narrowly scoped demonstrator and update the requirements through the authorized baseline process. If all 39 P0 requirements remain mandatory, revise the schedule and reserve time for security review and end-to-end stabilization. Do not describe the narrower slice as satisfying the current MVP gate.

## Questions for product-owner clarification

1. Is the one-month target fixed, and how many full-time-equivalent developer days are available?
2. Which P0 features are essential to the first demonstration if the complete gate cannot fit?
3. What does “unsupported proof” refer to, and should the broken-save fixture remain P1 or be promoted with explicit P0 acceptance?
4. Which host OS and runner backend must be supported, and what local attacker is in scope?
5. Is AI case generation intended, or only deterministic proposals from structured criteria plus reviewer approval?
6. What exact rule patterns constitute P0 ghost detection, and what false-positive/false-negative behavior is acceptable?
7. What secret formats and provider failures must the P0 redaction/consent controls handle?
8. What does unsupported coverage do to a criterion verdict and to an unsupported-only audit export?
9. How should criterion IDs behave when a threshold or expected outcome changes?

## Review outcome and limitations

This is an independent review report, not a requirements change or implementation approval. Findings are recommendations for owner disposition before M3/M4. The document-only review cannot establish user value, implementation effort from an existing codebase, security adequacy, or actual runtime behavior. The repository's SG-01 research says user segments and scenario prevalence remain unvalidated. Existing documentation validation was recorded in SG-02; this review did not rerun those checks or any product tests.
