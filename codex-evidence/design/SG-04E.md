# SG-04E Mandatory Gate Remediation Planning

- **Lifecycle and milestone** Design, M3 corrective planning
- **Task and execution** SG-04E, `SG-04E-20261125-01`
- **Session** `01a210f9-6878-7a10-b9a0-0c429a7e3900`, observed as `CODEX_SESSION_ID` and corroborated by Codex chat metadata
- **Date and mode** 2026-11-25 (Asia/Calcutta), Default
- **Starting commit** `4bed4560b8990d11df5a618ef59238829223317a`, clean `main` tracking `origin/main`
- **Actual model and effort** GPT-6.2 Sol / High, confirmed by the developer as `sol; high` and normalized using the recorded alias convention. The task rationale is complex cross-gate engineering, security-boundary analysis, and dependency/feasibility planning under the model strategy. The developer supplied the model and effort.
- **Measurements** Duration, token counts, and resource usage/cost are N/A. SpecGuard runtime LLM calls were not made.

The developer authorized corrective planning and reported that the SG-05A entry attempt was blocked. The [mandatory conditions register](../../docs/adr/SG-03D-m3-mandatory-conditions.md) and [SG-04D closure](SG-04D-closure.md) record all 12 gates as OPEN. The [remediation plan](../../docs/design/SG-04E-gate-remediation-plan.md) proposes controlled proof work for separate authorization.

## Inputs and planning decisions

- Reviewed repository guidance, goals, milestone plan, requirements, PRD, verification policy, test plan, SG-04A architecture/contracts/traceability, the ADR and mandatory conditions records, SG-04A through SG-04D stage evidence, the evidence index and model strategy/ledger/report/experiment records. The plan preserves the earlier evidence and distinguishes its scope from the proposed controlled observations.
- D01–D12 each have criterion references, present evidence and its limitations, a controlled proof with environment and pass/fail observations, dependencies, blocked components, qualitative complexity and approval/resource needs. Candidate selection is provisional. Upstream documents linked in the plan were read for technology feasibility and do not establish local capability or project-specific outcomes.
- Proposed PRD-compliant hyphen token boundaries, inapplicable handling for an impossible field violation, and an explicit D06 cross-reference to SG-R032-AC02. No normative documents, architecture decisions or authoritative progression rules changed. PLANS records the blocked attempt and the current planning disposition.
- Proposed F0 intake/authorization, F1–F7 component batches and F8 composed D12 design rehearsal, followed by independently reviewed evidence in SG-04G. This preserves M5 product acceptance and the approved P1/P2 progression.

## Observed environment and limitations

Command-name discovery resolved Git, Python, Node, npm and the WSL launcher. The same lookup did not resolve Docker, Podman, Firejail, bubblewrap, Chrome or Edge. Installed features, alternate executable paths, package versions, browser launch, runner controls, permissions beyond the workspace contract and credentials/destination were not verified. The runner proof requires a separately provisioned approved environment. Browser, local service and TLS receiver proofs require approved provisioning and capability checks. Model/effort confirmation was the developer's only intervention during the documented work.

## Validation commands and results

- `git status --short --branch`, `git rev-parse HEAD`, `git log -5 --oneline`, `rg --files`, `rg -n` and PowerShell `Get-Content` inspected the starting baseline, records and deliverables. PowerShell `Get-Command` performed command-name inventory only.
- `python -B -m unittest discover -s tests -v` ran the existing model report unit tests. **10 passed.**
- Inline read-only `python -B -` compared the authoritative register, catalog, acceptance table, architecture CSV and proposed batch ranges. It found 12 OPEN gates with complete plan sections, 54 requirements and 68 criteria, all 53 exact P0 mappings across 39 requirements partitioned into seven primary batches, and five scenario rehearsal rows. All 68 local Markdown path references resolved and new-document whitespace passed. Heading anchors were outside that check.
- `python -B -m scripts.generate_model_report` regenerated the aggregate. An inline read-only `python -B -` reconciliation initially failed on the expected ledger count. Inspection showed 17 baseline rows. After correcting the assumption, the check confirmed those 17 rows were preserved, 18 execution IDs were unique, SG-04E metadata matched the recorded session and commit, and an in-memory render matched the generated report.
- `git -c core.safecrlf=false diff --check HEAD` passed. `git diff --name-only HEAD`, `git ls-files --others --exclude-standard` and `git status --short --untracked-files=all` confirmed the six expected paths, including the two new documents.

No SG-04B/SG-04D or new feasibility harness, dependency installation, browser/server/runner/provider runtime, product acceptance test or untrusted repository workload ran. No commits, pushes or deployments occurred.

## Files changed

- Created [SG-04E stage evidence](SG-04E.md) and the [remediation plan](../../docs/design/SG-04E-gate-remediation-plan.md).
- Updated the [milestone plan](../../PLANS.md), [evidence index](../EVIDENCE_INDEX.md), [model usage ledger](../models/MODEL_USAGE.csv) and [generated model report](../models/MODEL_REPORT.md).

**READY WITH MANDATORY DEVELOPER DECISIONS.** SG-05A remains blocked. SG-04F awaits explicit developer approval and resource disposition.
