# Provisional user personas

These are research hypotheses for SG-01, not personas validated through interviews. No user interviews or customer observation have been conducted. The product owner selected solo developers using coding agents as the initial primary user; the first target is an existing repository checked against its original specification.

## 1. AI-assisted individual developer (initial primary user)

- **Context:** Uses a coding assistant or agent and has an existing repository with an original, human-readable specification.
- **Job to be done:** Assess whether the current repository fulfills that specification; find missing behavior, placeholder implementation, or weak/missing verification evidence.
- **Potential pain (hypothesis):** The diff, tests, and generated summary may not make a requirement-by-requirement coverage gap obvious.
- **Desired evidence:** Requirement text, candidate source/test locations, exact check commands/results, and explicit unknowns.
- **Risks:** Extra setup or noisy false positives could make a one-person workflow slower than direct inspection.
- **Validation needed:** Observe how developers compare an existing repository to its original specification; ask how they establish which version of the specification applies and what evidence changes their decision.

## 2. Small-team technical lead or reviewer

- **Context:** Reviews changes built by a small team with limited QA capacity and mixed human/AI authorship.
- **Job to be done:** Triage whether each acceptance criterion has implementation and test evidence before merge or release.
- **Potential pain (hypothesis):** Review comments and CI status are distributed across the PR, test reports, tickets, and product notes.
- **Desired evidence:** A compact traceability view, missing/uncertain links, and a reproducible review artifact.
- **Risks:** A tool that overstates completeness or duplicates CI/code review will not earn trust.
- **Validation needed:** Map the team's actual sources of truth, acceptance workflow, and current traceability practice.

## 3. QA or verification practitioner

- **Context:** Creates or reviews acceptance, regression, or exploratory tests from requirements.
- **Job to be done:** Find requirements whose boundary, negative, or business-rule cases lack tests and inspect test execution evidence.
- **Potential pain (hypothesis):** Requirement and test artifacts may use different wording and IDs, requiring manual reconciliation.
- **Desired evidence:** Candidate requirement-test links, edge-case prompts, coverage gaps, and execution provenance.
- **Risks:** Generated tests can simply repeat assumptions in the implementation or be too weak to detect defects.
- **Validation needed:** Determine test design process, acceptable automation, and criteria for a useful generated test.

## 4. Product owner or engineering manager

- **Context:** Needs to decide whether a feature meets agreed scope and whether unresolved gaps are acceptable.
- **Job to be done:** See the specific unproven requirements and the evidence behind a readiness discussion.
- **Potential pain (hypothesis):** A green build or aggregate coverage metric may not communicate business-rule coverage.
- **Desired evidence:** Plain-language requirements, concrete gaps, owners, and links to technical proof.
- **Risks:** A numeric confidence score could create false precision and encourage approval by metric.
- **Validation needed:** Learn what evidence supports release decisions and whether this user is a buyer, reviewer, or out-of-scope stakeholder.
