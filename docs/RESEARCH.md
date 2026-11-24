# SG-01 research notes

## Scope and method

Lifecycle phase: **Understand**. Task: **SG-01**. Research date: **2026-11-24** (Asia/Calcutta). Codex execution mode: **Plan mode** (developer confirmed). This is desk research based on public primary documentation, an industry research report, and peer-reviewed/systematic literature. Search results were followed to the cited pages/papers where available. No user interviews, surveys, product trials, customer repository inspection, or quantitative analysis were conducted. Therefore there are no interview findings, measured user pain rates, or hands-on competitor comparisons in this record.

Evidence labels used below:

- **Verified research** means a claim attributed to a linked public source, with the source's context and limitations retained.
- **Personal observation** means a direct observation made during this SG-01 research activity, not a general claim about users.
- **Hypothesis** means a product or user assumption that needs validation.

## Developer pain points

### Verified research

- DORA's 2024 report described positive associations between AI adoption and some developer and code-quality outcomes, alongside lower software delivery stability and uncertainty about product performance. Google Cloud's report summary says 39% of respondents reported little or no trust in AI-generated code. Survey associations should not be read as causal effects or universal developer experience. ([DORA 2024 report announcement](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report?hl=en); [DORA 2024 report](https://dora.dev/research/2024/dora-report/2024-dora-accelerate-state-of-devops-report.pdf))
- DORA's 2025 summary characterizes AI as an amplifier of the organization's existing strengths and weaknesses, emphasizing workflow and organizational capability rather than tool use alone. ([DORA 2025 report](https://dora.dev/research/2025/dora-report/))
- GitHub's guidance for reviewing AI-generated code recommends human review, testing, and documented team practices. GitHub's Copilot documentation says AI code review supplies suggested findings/fixes in pull requests and does not replace required human approvals by default. ([Review AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code); [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review))
- A systematic mapping study of 63 traceability papers (2000–2020) found traceability supports multiple maintenance activities, while creating and maintaining links is a main cost and link quality/tool performance remain challenges. The authors called for stronger industry evidence. ([Mapping study](https://arxiv.org/abs/2108.02133))

### Personal observation

- The public sources describe multiple distinct tasks—finding defects in a diff, running tests, recovering trace links, and making a release decision. They do not establish that one current workflow reliably answers requirement-by-requirement fulfillment for every codebase.
- In this research, some published claims and product docs describe capabilities, not independent evaluations of their accuracy. No accuracy comparison was attempted.

### Hypotheses to test

- Reviewing agent-produced code may impose extra interpretation work when the author cannot explain the implementation or tests. Validate through interviews and observation, rather than inferring it from broad AI adoption statistics.
- A structured “requirement → implementation evidence → verification evidence → unresolved question” view may reduce search and handoff effort.
- Product trust may depend more on transparent, inspectable evidence and calibrated uncertainty than on a single numeric score.

## Target users

**Provisional, unvalidated segments:**

1. **AI-assisted individual developer:** wants a fast independent pass over a change before merge and needs actionable evidence rather than a generic “looks good.”
2. **Small-team technical lead/reviewer:** needs to see which acceptance criteria lack implementation or tests and share a reviewable decision record.
3. **QA/verification practitioner:** needs requirement-linked test ideas and execution evidence; may value reproducibility and edge-case coverage.
4. **Product owner or engineering manager:** needs a bounded view of unresolved requirement risk, but should not be assumed to want a scalar release score.

These are persona hypotheses, not interviewed personas. Product-owner clarification received on 2026-11-24 selects the **AI-assisted individual developer** as the initial primary user and an **existing repository assessed against its original specification** as the first verification target. This is a product direction decision, not evidence of user validation.

## Current verification workflows and approaches

### Verified research and product documentation

Common documented controls include human pull-request review, CI test execution, static analysis/security scanning, test generation, and review of AI-generated code. GitHub and GitLab document AI-assisted pull request reviews; these operate inside existing review workflows and produce findings/suggestions. GitLab's documentation describes the context it sends for non-agentic review and notes that large-request fallback can reduce review context. ([GitHub Copilot review overview](https://docs.github.com/en/copilot/concepts/agents/code-review); [GitLab Duo Code Review](https://docs.gitlab.com/user/gitlab_duo/code_review/))

The NIST Secure Software Development Framework recommends integrating secure development practices into existing SDLCs and documenting security testing and remediation; it is a framework, not a requirement-to-implementation product. ([NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)) NASA's systems engineering handbook illustrates a more formal approach: uniquely identify requirements and map verification methods/results in a requirements verification matrix. This is a useful mature traceability pattern, but it is not representative of every team's day-to-day process. ([NASA Systems Engineering Handbook, Appendix D](https://www.nasa.gov/reference/system-engineering-handbook-appendix/))

### Representative approaches and verified public positioning

| Approach | Publicly documented role | What SG-01 can infer (hypothesis) |
|---|---|---|
| Human code review / pull request review | Reviewers inspect change intent, implementation, and discussion; GitHub documents AI-assisted review in the PR lifecycle. | Review comments are useful but may not give a complete requirement-to-evidence ledger without explicit criteria. |
| Automated tests / CI | Run selected unit, integration, acceptance, and regression checks. | A passing suite only speaks to exercised assertions and configured environments; requirement completeness depends on test design. |
| Static analysis / security scanning | Detect classes of code and dependency issues. | Useful deterministic signals, but not a direct verdict on product requirements. |
| Traceability matrix | Link requirement IDs to verification methods/results (formal example in NASA guidance). | Comprehensive traceability can aid coverage, but manual upkeep creates cost. |
| AI code review (GitHub Copilot, GitLab Duo) | Review changes and suggest issues/fixes within host review workflows. | Adjacent solutions validate diffs; public documentation alone does not show independent exhaustive specification fulfillment. |

The last column is explicitly an inference from scope descriptions, not a competitor benchmark or claim that a named tool cannot support custom instructions or other traceability workflows.

## Requirement traceability challenges

### Verified research

Traceability connects requirements to downstream artifacts such as design, source, and tests; systematic literature reports value for change management and maintenance. The cost of establishing and maintaining links, stale links, link quality, scalability, and trust are recurring concerns. Automated trace-link recovery can suggest candidates, but should not be represented as ground truth without review. ([Mapping study](https://arxiv.org/abs/2108.02133); [Barriers to traceability in practice](https://doi.org/10.1007/s00766-023-00408-9); [Traceability technology review](https://www.sciencedirect.com/science/article/pii/S0164121218301754))

### Hypotheses for SpecGuard

- Natural-language requirements are often ambiguous, compound, or implicit; splitting them into smaller “requirement atoms” could expose ambiguity but might alter meaning. Keep original text and require human confirmation for material decomposition.
- Code links are inherently probabilistic for cross-cutting behaviors, configuration, data, and UI flows. Present candidate links with provenance and confidence, not as definitive trace links.
- Link validity can decay after changes. Git-based change detection may flag candidates for reassessment, but cannot determine whether a requirement has drifted without context.

## Limitations of current approaches and representative failure evidence

The strongest direct evidence reviewed is the ICSE 2026 empirical study of SWE-bench Verified: among plausible patches from three issue-solving tools, it reports benchmark validations that missed failures and behavior differences against ground-truth patches. It supports the narrow proposition that test-based evaluation can miss behavioral discrepancies in that benchmark. It does **not** establish how often deployed AI-generated features omit business requirements. ([Wang, Pradel & Liu, ICSE 2026](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf))

Other failure scenarios in [FAILURE_SCENARIOS.md](FAILURE_SCENARIOS.md) are analytically constructed examples, not observed incidents or prevalence estimates. They illustrate risks that interviews and prototype evaluations should explore.

## Technical complexity and feasibility considerations

The following are qualitative discovery observations, not delivery estimates or grounds for changing approved priorities. SG-02 subsequently approved the feature set and P0/P1/P2 priorities in the [requirements catalog](REQUIREMENTS.yaml) and [PRD](PRD.md). The active development baseline uses milestone acceptance evidence and assesses feasibility through technical complexity, dependencies, security, correctness, and maintainability.

| Capability area | Technical considerations to resolve or validate |
|---|---|
| Requirement DNA | Stable identity, safe structured-input parsing, source locations, ambiguity handling, and reviewer-approved meaning changes. |
| Spec-to-Code Traceability Graph | Snapshot indexing across the approved Python/FastAPI and React/Next.js targets, provenance, review states, and stale-link handling. |
| Ghost Feature Detector | Finite deterministic rules, fixture coverage, false-positive boundaries, and unsupported-language reporting. |
| Evidence Vault | Immutable baseline and artifact provenance, persistence/reopen behavior, export integrity, and secret handling. |
| Adversarial Requirement Testing | Supported criterion forms, deterministic proposal behavior, human approval of expected outcomes, and execution evidence mapping. |
| Visual Reality Check (P1) | Controlled browser, viewport, reference-image governance, threshold semantics, and independent interaction evidence. |
| Specification Drift Radar (P1) | Versioned specification comparison, stable IDs, linked-change detection, and reassessment rules. |
| Release Confidence Index (P1) | Transparent coverage semantics, unresolved-status presentation, and safeguards against implying calibrated release probability. |
| Verification Intelligence Console (P1) | Persisted audit contracts, filtering, comparison semantics, and traceable detail views. |
| Surgical Repair Engine (P2) | Proposal isolation, scoped diffs, unchanged working tree, mapped checks, and human review. |

The approved P0 baseline spans a loopback web workflow, two framework families, specification intake, trace review, deterministic findings, evidence persistence, JUnit import, an isolated runner, remote-AI consent and redaction, export, and security controls. Their dependencies and interactions require architecture and security decisions before implementation. This is a technical feasibility concern, not a schedule estimate. The SG-03 review's schedule-based conclusion is superseded by the product-owner decision; its technical complexity observations remain open for design and validation.

SG-03B defines the product boundaries for local access, isolation failure, redaction and consent, supported analyzer rules, malformed Git and XML, and unsupported coverage. The [SG-03B assessment](../codex-evidence/review/SG-03B.md#technical-feasibility-and-dependencies) records implementation dependencies and blockers. The [Design decision register](adr/SG-03B-design-decision-register.md) assigns platform selection, enforceable limits and other architecture decisions to M3 with required evidence. Technical feasibility remains open pending that validation.

## Decisions and questions deferred to later stages

The product owner confirmed on 2026-11-24 that selecting a technical stack, integration points, and the example repository/specification is intentional work for the subsequent Specify and Design stages. These are not blockers for SG-01 completion. No technology, architecture, or sample repository is selected in this stage.

The product owner also confirmed the initial-user and first-target direction: solo developers using coding agents; an existing repository checked against its original specification. These choices are product direction, not interview evidence or user validation.

SG-02 set the supported repository stacks, local audit interface and optional reviewer-controlled AI candidate links. The product's implementation stack, controlled example repository and specification, runner contract and supporting architecture remain M3 decisions. See the [PRD](PRD.md) and [Design decision register](adr/SG-03B-design-decision-register.md).

## Development-baseline update (SG-03A)

The product owner replaced the one-month development feasibility constraint with milestone-driven, quality-first progression. Calendar-based development targets, assumed working days, developer-hour/FTE estimates, and duration-driven feature reduction are removed from the active baseline. Runtime execution timeouts, performance requirements, resource limits, and security timing controls are unchanged. The discovery-era schedule hypothesis is retained only in historical SG-01 evidence; see [decision 0002](adr/0002-milestone-driven-development-baseline.md).

## References

1. DORA, *Accelerate State of DevOps Report 2024* and announcement: [PDF](https://dora.dev/research/2024/dora-report/2024-dora-accelerate-state-of-devops-report.pdf), [Google Cloud summary](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report?hl=en).
2. DORA, *State of AI-assisted Software Development 2025*: [report page](https://dora.dev/research/2025/dora-report/).
3. Wang, Pradel & Liu, *Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study*, ICSE 2026: [paper](https://software-lab.org/publications/icse2026_SWE-bench-correctness.pdf).
4. NIST, *Secure Software Development Framework (SSDF) Version 1.1*, SP 800-218: [publication](https://csrc.nist.gov/pubs/sp/800/218/final).
5. NASA, *Systems Engineering Handbook*, Appendix D: [requirements verification matrix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/).
6. GitHub Docs: [review AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code), [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review).
7. GitLab Docs: [Duo Code Review](https://docs.gitlab.com/user/gitlab_duo/code_review/).
8. Mäder et al., *The impact of traceability on software maintenance and evolution: A mapping study*: [paper](https://arxiv.org/abs/2108.02133).
9. *Why don’t we trace? A study on the barriers to software traceability in practice*: [DOI](https://doi.org/10.1007/s00766-023-00408-9).
10. *Requirements traceability technologies and technology transfer decision support: A systematic review*: [paper](https://www.sciencedirect.com/science/article/pii/S0164121218301754).
