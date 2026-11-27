# SG-05A-META Vercel deployment readiness

- **Status:** Adopted as a forward-looking architectural constraint. Hosted capability details and activation still require the design and gate approvals listed below.
- **Date:** 2026-11-27.
- **Scope:** Preserve the approved Local Engineering Mode while preparing a separate static Hosted Demo Mode; make sanitized model metrics consumable by a Next.js build without Python or serverless functions at runtime.
- **Authority:** Product-owner instruction in SG-05A-META. This decision does not change product requirements, D01–D12 statuses, or authorize deployment.

## Context

The approved product baseline is local-first. SG-05A currently has a controlled loopback FastAPI boundary, in-process session state, a local SQLite migration, and a static Next.js export served by the Python application. D01–D12 remain OPEN. The new constraint calls for eventual Vercel deployment and an interactive hosted demonstration of approved capabilities while explicitly withholding approval for public protected access, remote repositories, external persistence, and remote workload execution.

This creates a profile boundary. The current Local Engineering Mode remains authoritative for approved local operations. Hosted Demo Mode is a separate, static-first presentation of sanitized development analytics and synthetic fixtures. It must not route hosted requests into the local authority surface or imply that a gated product capability has been approved for public access.

## Decision

1. Preserve Local Engineering Mode, including its loopback binding, terminal bootstrap, local SQLite boundary, and fail-closed capability gates.
2. Host only a separate Hosted Demo Mode until an explicitly designed and reviewed hosted capability is approved. It may present sanitized model analytics and synthetic demonstration state. The currently implemented local session page and `/api/v1/session` boundary are not the hosted demo.
3. Treat `frontend/public/analytics/model-metrics.json` as a build-time static artifact. The ledger/report generator emits it together with `MODEL_REPORT.md` and `MODEL_METRICS.json`. A Next.js client can read the static JSON from the deployment's asset path; a Python runtime, Vercel Function, database, or network call is not needed to render aggregate charts.
4. Treat every deployed static file as publicly readable. Keep the JSON schema versioned and allow-listed. Exclude raw notes, task scopes, selection rationales, absolute paths, credentials, session tokens, platform session IDs, and execution IDs. Keep unavailable measurements unavailable. Do not add raw evidence files to the frontend public directory.
5. Set a future Vercel project's root directory to `frontend`, after a hosted-specific entry page and static build checks exist. Do not deploy from the repository root, which includes the local Python application, development tooling, tests, lockfiles, and evidence.
6. Compatibility labels in this register are design assessments, not deployment evidence. Re-check current Vercel documentation and run environment-specific builds before any compatibility or deployment claim.

## Deployment compatibility register

| Capability / component | Compatibility | Constraints and evidence still required |
|---|---|---|
| Sanitized model metrics JSON | **Vercel-compatible** as a static asset; **deployment verification required** | Generated during development or CI, checked as a versioned JSON artifact, and bundled from `frontend/public`. Validate the field allow-list and ensure the canonical and frontend copies match. No runtime Python, function, or database. |
| Next.js static assets and reusable presentational components | **Vercel-compatible** in principle; **deployment verification required** | The frontend is already a Next.js static export. Reuse presentation components across profiles only after dependencies on `/api/v1/session` are separated. Run a clean Vercel-equivalent static build and inspect output routing. |
| Current Local Session page and session API | **Local-only** | Page calls `/api/v1/session`; FastAPI serves that route and statically exported files. Hosted demo must use a separate entry point or an approved adapter; do not expose local-only routes or pretend that the route works on static hosting. |
| FastAPI application and loopback authority boundary | **Local-only** in current form; hosted authentication **requires architectural approval** | Binds `127.0.0.1`, verifies loopback peer/Host/Origin, and receives the bootstrap code through an interactive terminal. These controls must not be loosened to make the server public. Any hosted identity and authorization design needs independent security review and explicit approval. |
| Session, revocation, and authorization state | **Local-only** in current form; hosted durable state would require **external infrastructure and architectural approval** | `specguard/session.py` stores proofs in process memory and resets them on application lifespan end. Serverless instances scale/recycle independently. Do not use function memory for durable sessions or revocation. Hosted protected access is not currently authorized. |
| SQLite and future audit/evidence persistence | **Local-only** in current form; hosted durable persistence requires **external infrastructure and architectural approval** | `specguard/storage.py` validates a local SQLite connection and is schema metadata only today. Vercel Function filesystems are read-only except instance-local temporary storage; that temporary storage is not durable or shared. Any hosted product records require an approved managed store, D11 review, and migration/recovery design. No migration to a hosted database is approved here. |
| Local repository ingestion and Git snapshot | **Local-only** under the current operating boundary | Remote repository access is expressly not authorized. Hosted ingestion would require explicit product-owner authorization, a reviewed trust/credential boundary, D01/D06 evidence, and external infrastructure decisions. |
| Isolated test/workload runner | **External infrastructure required; requires architectural and activation approval** | Keep execution outside ordinary Vercel Functions. SG-05H still requires an approved isolated VM host/image, resource enforcement, egress limits, teardown and recovery evidence. No hosted or Vercel execution is authorized. |
| Optional AI provider | **External infrastructure required; requires architectural and activation approval** | No provider, endpoint, consent flow, secret handling or egress permission is added by this decision. Keep SG-05G dispatch disabled until applicable D01/D04/D08/D10/D11 evidence and separate approval exist. |
| Interactive hosted product demonstration | Static shell is **Vercel-compatible**; capability selection **requires architectural approval** and **deployment verification** | Use only synthetic records and capabilities explicitly approved for hosted exposure. The current product exposes only a local synthetic session check; it does not yet provide the requested hosted product demonstration. D04, D08, D11, D12, and any capability-specific conditions remain OPEN. |
| Model evidence, build/test tooling, and local application packages | **Development-only; exclude from hosted artifact except the allow-listed JSON** | Do not bundle tests, `.venv`, browser binaries, local repositories, generated evidence archives, credentials, or the whole repository tree. Review the static output and deployment file list before deployment. |

## Current incompatibilities and proposed adjustments

- `specguard/server.py` binds to IPv4 loopback and runs Uvicorn as a long-lived server. A Vercel Function is request-invoked and managed by the platform; the existing socket lifecycle is not a drop-in Function handler. Keep this adapter local. If hosted APIs are later approved, design a separate stateless request adapter around profile-neutral domain services.
- `specguard/app.py` wires framework endpoints and uses `Path(__file__).resolve().parents[1] / "frontend" / "out"` for exported UI files. This repository-relative asset path is acceptable for the local package layout but couples packaging to the checkout. Before sharing core UI or domain logic, make asset and storage providers explicit at the environment boundary; do not move absolute local paths into core domain code.
- `specguard/session.py` stores authorization state in memory for a process lifespan. Keep it limited to the local single-process profile. A hosted authorization design must use a reviewed identity and revocation model with appropriate external state, and must be approved before implementation.
- `specguard/storage.py` is SQLite-specific. The connection is supplied by its caller, but no hosted persistence port, database adapter, record schema, or migration exists. Continue to use it only for the approved local development boundary until a separate persistence design is reviewed.
- `frontend/pages/index.jsx` is a local session interface, not a reusable hosted demo entry point. Extract profile-neutral display components only when the approved capabilities and data contracts are ready; isolate local bootstrap and API access behind a local-only adapter.
- `RevisionRef` in `specguard/domain.py` is a framework-independent frozen value object and is a suitable boundary pattern for future domain services. No broader domain/service decomposition has yet been implemented or verified.
- Python runtime dependencies are separated from the `dev` group in `pyproject.toml`; the static hosted frontend needs only its locked Next.js/React dependencies and pre-generated JSON. Preserve this separation and avoid adding hosted-only packages to the local runtime without need.
- The repository contains no Vercel project configuration or deployment evidence. A future project must use a frontend-only root directory and explicitly exclude local application/evidence inputs. A green Next.js build alone is insufficient to claim Vercel compatibility.

### Approved task boundary and conflicts for owner review

The existing local-first baseline and D08/D11 controls conflict with exposing the current protected application through a public hosted service. The safe proposed resolution is to keep Local Engineering Mode unchanged and limit Hosted Demo Mode to static analytics and synthetic, non-protected capabilities selected through an approved design. The product owner must review the specific interactive demonstration flows and hosted identity/data boundary before any protected hosted capability is implemented or exposed. No requirement or gate status is changed by this record.

## Analytics artifact contract

`MODEL_METRICS.json` now has `schema_name` and numeric `schema_version`, deterministic ordering, all P01–P08 entries, numeric counts and measurements, and privacy-limited chronology. Timeline entries omit execution IDs and all platform session IDs; aggregate known/missing session counts remain available. `scripts.generate_model_report` writes the same serialized payload to `frontend/public/analytics/model-metrics.json`, which is a static build input. Next.js can package and serve that file without Python at request time. The dataset can be regenerated with `python -m scripts.generate_model_report` during development or a future CI job. There is currently no CI workflow to run this command automatically.

This is data and packaging readiness only. No dashboard or chart UI was built. A future visual layer must treat this dataset as public, validate its schema, and use only the fields in the allow-listed generated contract.

## Official platform documentation checked

Checked 2026-11-27 against official Vercel documentation:

- [Next.js on Vercel](https://vercel.com/docs/frameworks/full-stack/nextjs) describes Next.js deployments and distinguishes statically generated content from server-side rendering through Vercel Functions.
- [Vercel Function runtimes](https://vercel.com/docs/functions/runtimes) document read-only Function filesystems, instance-local `/tmp`, non-durable SQLite limitations, and bundling files read by Functions.
- [Configuring a build](https://vercel.com/docs/builds/configure-a-build) documents framework build commands, output directories, and configuring a frontend subdirectory as a project root.
- [Vercel CDN cache](https://vercel.com/docs/caching/cdn-cache) states that static files are automatically cached across Vercel's global network for the deployment lifetime.

These sources establish platform behavior only. They do not prove that SpecGuard is compatible, secure, or deployed. No Vercel account, project, environment, credential, or external infrastructure was accessed or configured.
