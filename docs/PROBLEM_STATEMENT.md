# Problem statement

## SG-01: Understand

### Problem

AI-assisted coding tools can produce changes that look complete and pass the checks that happen to exist while still omitting a stated behavior, using a placeholder, breaking a business rule, or mishandling an edge case. Existing review and test practices provide important evidence, but a green test run or plausible diff does not by itself prove that every original requirement is fulfilled.

SpecGuard's product goal is to independently assess whether software fulfills its original specification and make the evidence and unresolved gaps reviewable. “Independently” is a product intent, not a claim that a separate model can establish correctness without human judgment. The system should distinguish observed evidence, inferred links, and unknowns.

### Problem framing and evidence status

- **Verified research:** DORA's 2024 survey reported that 39% of respondents had little or no trust in AI-generated code. DORA also reported mixed effects across outcomes; its 2025 report frames AI as amplifying existing organizational strengths and weaknesses. These are survey/research findings, not proof that AI code is generally defective.
- **Verified research:** A 2026 ICSE study of plausible patches from three issue-solving tools on SWE-bench Verified reported that 7.8% counted as correct by the benchmark failed the full developer-written test suite, while 29.6% differed behaviorally from the ground-truth patch. The study is limited to its benchmark and sample; it does not measure production defect prevalence.
- **Verified research:** Requirements traceability literature identifies the effort of creating and maintaining links and the quality/trustworthiness of those links as persistent challenges.
- **Personal observation:** This SG-01 work has not included interviews, repository audits of customer systems, experiments, or hands-on comparisons of commercial products. No first-person developer pain claim is treated as validated user evidence.
- **Hypothesis:** Teams using coding agents may need a review artifact that answers “which requirements are implemented, where is the evidence, what has not been demonstrated?” more directly than a generic code review or coverage percentage.

### User and job hypothesis

Primary user for the initial product focus: a solo developer using coding agents. First verification target: an existing repository assessed against its original specification. The job is to find requirement-level omissions and weak proof in the repository quickly, while keeping the developer in control. This focus was confirmed by the product owner during SG-01 on 2026-11-24. Stack, interface, and concrete specification inputs are intentionally deferred to Specify and Design; they are not blockers for this Understand-stage framing.

### Boundaries

SpecGuard should initially report evidence and gaps, not certify absolute correctness, replace code review, or autonomously approve releases. Development scope and progression follow the approved milestone and acceptance gates; the external Codex Build Challenge duration does not constrain product requirements or feature priorities. See the [SG-03A development baseline decision](adr/0002-milestone-driven-development-baseline.md).

### References

See the dated, annotated sources in [RESEARCH.md](RESEARCH.md#references).
