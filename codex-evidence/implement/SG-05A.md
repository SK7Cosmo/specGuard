# Phase 04 | BUILD | SG-05A | Foundation and Local Authority

Execution `SG-05A-20261125-01`, Codex session `01a21174-22e0-7d13-84d1-c24622a8d257` (CODEX_SESSION_ID), 2026-11-25 Asia/Calcutta. Starting HEAD on main was `4bed4560b8990d11df5a618ef59238829223317a`. Existing SG-04E/R changes in the plan, evidence index/design/ledger/report, ADRs, architecture, design and experiment directories predated this task. Developer confirmed GPT-6.2 Astra / High for this session. The critical security boundary warrants the strategy’s critical-engineering selection. Session duration, tokens, cost and resource usage N/A.

## Scope at entry

| Component | Contract and oracle | Activation |
|---|---|---|
| Local entry point, config, request filter, lifecycle and safe errors | SG-R031-AC01, verification policy, API/security contracts and SG-05A roadmap. Exact loopback Host including port, reject a foreign Origin, require Origin on mutations, deny before reading protected data or changing state. | D08 OPEN. Public inert foundation only. Bootstrap, proof lifetime/transport and revocation require owner disposition and independent D08 observations. |
| Static UI | SG-R030-AC01 and SG-R031-AC01, same-origin delivery, static assets carry no authority. | D04/D08 OPEN. No audit workflow or untrusted content rendering. |
| Versioned migration | D11 and shared durability obligations, SG-R005–007 and SG-R014. Proposed SQLite/file layout requires review. | Schema metadata only in controlled fixtures. No product audit/specification/evidence persistence. |

SG-03D requires rejection of a covered or uninspectable specification before persistence, sanitized resubmission and exact bytes for accepted sources. Intake is outside SG-05A. The developer subsequently approved the session and SQLite choices for controlled tests in the [SG-05A decision](../../docs/adr/SG-05A-local-foundation.md). No runtime LLM was involved.

## Implementation and traceability

Status **PARTIAL**. The first build has passed its controlled component checks. The roadmap also requires reviewed D08 evidence. No independent reviewer or gate disposition has been recorded.

| Obligation | Implementation | Executable observation | Remaining acceptance |
|---|---|---|---|
| SG-R031-AC01 local authority | `specguard/local.py`, `server.py`, `app.py`, `session.py`, `__main__.py` | [ASGI and config tests](../../tests/test_local_authority.py) and [HTTP, process and browser tests](../../tests/test_local_ingress.py). The operator-only entry point binds one IPv4 loopback socket, derives the allowed authority from that socket and rejects redirected terminal bootstrap. A single event loop exchanges the code once. Session validation precedes protected response or revoke. Unknown routes and request bodies are denied. | Synthetic status and revoke only. Independent D08 review and later access to an actual audit remain outstanding. |
| SG-R030-AC01 local UI | Static Next.js Pages export under `frontend/`, served by the same FastAPI process | Chrome DOM entry, session status, cookie hidden from script, reload and revoke, empty web storage and zero off-origin page requests. | Full manual intake, review and export scenario NOT RUN. |
| SG-R005-AC01, SG-R014-AC01 shared identity | Immutable audit/baseline/object/revision reference in `specguard/domain.py` | [Identity tests](../../tests/test_baseline_identity.py) distinguish scopes and reject incomplete references. | History, commit and digest binding belong to subsequent components. |
| D11 migration, preparation for SG-R019-AC01 reopen | `specguard/storage.py` validates the caller-designated empty/v1 schema, enables WAL and foreign keys, and updates the application ID and schema version within one immediate transaction. Version 1 has no tables. | [SQLite tests](../../tests/test_foundation_storage.py) check retry, reopen, future/foreign refusal and transaction rollback after an injected SQLite authorization failure. | Audit round trip, idempotency, artifact integrity, stale history, rejected-source exclusion and crash recovery require product records. |

The approved decision and API/security contracts supplied the expected outcomes before the implementation. This session authored the tests and the implementation. Protected product operations have no routes. No provider, runner, telemetry client, persistent session store or specification intake was configured. The session uses an HTTP-only loopback listener and a host-only session cookie named for its port. Browser cookies are host-scoped, so the cookie name is a routing convenience and local process compromise remains outside the verification policy's threat model. The public entry point offers no HTTPS or IPv6 mode. No proposed parser or runner limits were adopted.

## Environment and command record

Windows 11 build 26200, Python 3.12.7, SQLite 3.45.3, uv 0.11.21, Node 26.3.0, npm 11.16.0. Python, pip, uv, Node, npm and a pnpm shim were present. The starting tree had the model-report tests and design checkers, with no application package, frontend or dependency declarations. The selected runtime is project-local. Exact Python lock resolutions, hashes and registry locations are in [uv.lock](../../uv.lock), and the frontend tree and integrity hashes are in [package-lock.json](../../frontend/package-lock.json). Browser verification used the existing Chrome 157.0.8103.79 executable.

| Command / check | Result |
|---|---|
| `uv lock --default-index https://pypi.org/simple --no-python-downloads`; initial project-local npm install | BLOCKED by sandbox DNS, both exit 1. Retried with the required network permission. |
| `uv sync --default-index https://pypi.org/simple --no-python-downloads` | PASS, exit 0. Created .venv and installed 17 locked packages including FastAPI 0.139.0, Uvicorn 0.49.0, HTTPX 0.28.1 and PyYAML 6.0.3. |
| `uv add --dev --bounds exact --default-index https://pypi.org/simple --no-python-downloads playwright` and same command for `ruff` | PASS, both exit 0. Playwright 1.65.2, greenlet 3.5.6 and Ruff 0.17.6 installed locally. |
| In frontend, `npm.cmd install --save-exact next react react-dom --ignore-scripts --registry=https://registry.npmjs.org/` | PASS, exit 0, 21 packages added. Next 16.4.6, React and React DOM 19.3.1. |
| `uv sync --locked --offline --no-python-downloads` | Sandbox cache write initially denied. Retried with cache access, PASS, exit 0, 20 installed packages checked. |
| In frontend, `npm.cmd ci --ignore-scripts --registry=https://registry.npmjs.org/`; from root, `npm.cmd run build --prefix frontend` | PASS, both exit 0. Clean locked install added 21 packages and generated the static export. The initial build also passed with NEXT_TELEMETRY_DISABLED=1. The checked-in build command sets it for the child process. |

## RED, GREEN and regression

Use the project Python executable `.venv\Scripts\python` for the commands below. Only trusted project checks and synthetic fixtures executed. The application fixtures used temporary listeners, browser contexts and SQLite databases.

| Command / stage | Observed result |
|---|---|
| `python -B -m unittest discover -s tests -p test_local_authority.py -v` and corresponding `test_foundation_storage.py` | RED, each exit 1 before the application package existed. After adding a bare FastAPI shell, authorization tests saw 404 instead of 403 and no bootstrap issuance (2 failures, 5 errors). Config validation already passed in that run. The migration contract produced 3 NotImplementedError errors. |
| Windows asyncio preflight | The sandboxed authority run stalled before the test body. A five-second faulthandler probe exited 1 in the Windows loopback socket-pair accept. Terminated the stalled run and used permitted local networking for the behavioral RED and subsequent HTTP/browser checks. The stall is environment evidence only. |
| `python -B -m unittest discover -s tests -p test_local_ingress.py -v`; corresponding `test_baseline_identity.py` | RED before the listener module and domain type existed respectively, exit 1. Browser and extended HTTP tests are recorded as observations where no individual behavioral RED was captured. |
| Migration suite after implementation | GREEN, 3/3 passed, exit 0. |
| `python -B -m unittest discover -s tests -v` with SPECGUARD_TEST_BROWSER set to Chrome | First GREEN 23/23, exit 0. After refactoring, the locked rebuild and additional boundary coverage, **29/29 passed**, exit 0 in 12.298 s, zero skips. 2 domain, 3 migration, 8 authority/config, 5 ingress/CLI, 1 browser and 10 existing model-report regression tests. |
| Ruff check and format check on `specguard` and the four SG-05A test modules | Initial lint found two import ordering issues, one implicit subprocess check, one unused binding and a loop clock capture. Corrected them and reformatted. Final lint and format PASS, both exit 0, 12 files formatted. |
| `python -m compileall -q specguard tests experiments/sg04r` | PASS, exit 0. |

Real HTTP observations include exact Host and Origin, originless mutation, bad proof, single-session access, rejection before mutation, revoke, shutdown and fresh-process rejection of both an outstanding code and an issued cookie. Idle and absolute expiry use a controlled monotonic clock at the HTTP boundary rather than an eight-hour wall-clock run. The ASGI receive tripwire checks denial before body consumption. The ingress diagnostic check sent a synthetic request marker and malformed HTTP and observed safe responses and no marker in captured server stdout/stderr. The Chrome test exercised the actual static export. Its local test harness received the ephemeral code in memory. It did not exercise a human typing into an interactive terminal. No proof value was written to this evidence.

## Governance and disposition

The owner authorized reuse of SG-05A and supplied the model and policy decisions during execution. The active roadmap has 13 distinct tasks, SG-05A followed by SG-05C–N. Historical SG-04E/R evidence and the original SG-04R JSON still describe the earlier numbering. The live document validator checks current references without regenerating that historical evidence. SG-04F0–F8 and SG-04G have no execution record. The eight-phase title convention lives in [PLANS.md](../../PLANS.md#development-phases). All D01–D12 are OPEN. D04 remains open for untrusted rendering, D08 for reviewed authority evidence, D11 for product persistence/recovery and D12 for integrated acceptance. Other gates retain the restrictions in the [condition register](../../docs/adr/SG-03D-m3-mandatory-conditions.md).

Production/source changes are the `specguard/` package, `pyproject.toml`, `uv.lock`, and the frontend package/lock, registry config, build wrapper, Next config, two page modules and stylesheet. Other session changes are the four linked test modules, `.gitignore`, README, AGENTS, GOALS, PLANS, active roadmap, ADR index and SG-04R decision addendum, SG-05A ADR, condition register addendum, architecture traceability CSV, SG-04R document validator, this evidence, the evidence index and the development model ledger/report. Prior SG-04E/R working changes were preserved. The next roadmap task is **SG-05C Requirement DNA and safe Git ingestion**. It was not started. The next action for SG-05A itself is independent D08 evidence review. No commit, push or deployment occurred.

## Final integrity checks

- Final browser-version-pinned suite rerun with the README commands: PASS, 29/29 in 8.564 s, exit 0. Chrome reported 157.0.8103.79. All disposable listeners stopped.
- `python -B experiments/sg04r/validate_documents.py`: PASS, exit 0. Verified 54 requirements, 68 unique criteria, 68 exact case mappings and architecture rows, five scenarios, all 12 OPEN gate rows and activation restrictions, and 13 ordered roadmap IDs without collisions or forward dependencies. Checked 172 local Markdown targets. Counts by priority (requirements/criteria) are P0 39/53, P1 12/12, P2 3/3.
- The PRD, catalog, verification policy and test plan matched starting Git bytes. `git diff --exit-code HEAD -- docs/PRD.md docs/REQUIREMENTS.yaml docs/VERIFICATION_POLICY.md docs/TEST_PLAN.md docs/adr/SG-03D-secret-handling-decision.md` exited 0. The preserved SG-04D evidence digests matched the historical SG-04R record.
- Reran `experiments.sg04d.verify_design_contracts.main()` and `experiments.sg04d.verify_document_closure.main()` with each module's OUT set to check.json under a TemporaryDirectory. Both exited 0. Six token cases, 18 coverage cases, 14 historical findings and 68 mappings passed their document/contract checks.
- `python -B -m scripts.generate_model_report` exited 0. Compared the regenerated report to generate_report() and checked execution IDs with csv.DictReader. PASS, exit 0, 20 distinct executions and one SG-05A row. Unavailable session measurements are N/A.
- `git diff --check HEAD` passed with working-copy line-ending notices. A separate whitespace scan passed on all 25 new/untracked files touched by SG-05A. The worktree is uncommitted on main at its starting HEAD.
