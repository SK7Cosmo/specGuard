# SpecGuard

SpecGuard compares an original specification with implementation evidence. The first BUILD session provides a local session check and an isolated SQLite migration. Audit workflows are gated.

## Run the local session check

Use Python 3.12, uv, Node.js and npm. From the repository root in PowerShell:

```powershell
uv sync --locked --no-python-downloads
npm.cmd ci --prefix frontend --ignore-scripts
npm.cmd run build --prefix frontend
.\.venv\Scripts\python -m specguard --local-check
```

Open the exact IPv4 loopback URL printed in the interactive terminal and enter its one-time code. The service selects a free port. To select a port explicitly, append `--port 8765`. Use a non-default HTTP port so the browser includes it in Host and Origin. The static UI can establish a session, display its status and revoke it. After expiry or revocation, stop with Ctrl+C and restart for a fresh code. Request access logs and framework build telemetry are disabled.

The launcher uses process memory only. Migration tests create temporary databases, enable foreign keys and WAL, and write application and schema version metadata. Audit inputs and records have no storage or request path.

## Verify

The recorded browser scenario pins Chrome 157.0.8103.79. Set the browser variable to that approved executable. The browser scenario is skipped when the variable is absent. The recorded Chrome version and exact commands are in the [SG-05A evidence](codex-evidence/implement/SG-05A.md).

```powershell
$env:SPECGUARD_TEST_BROWSER = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
.\.venv\Scripts\python -B -m unittest discover -s tests -v
.\.venv\Scripts\python -B experiments/sg04r/validate_documents.py
```

## Project records

- [Milestones and eight development phases](PLANS.md)
- [Implementation roadmap](docs/design/SG-04R-implementation-roadmap.md)
- [Requirements](docs/REQUIREMENTS.yaml) and [verification policy](docs/VERIFICATION_POLICY.md)
- [Local authority decision](docs/adr/SG-05A-local-foundation.md)
- [Evidence index](codex-evidence/EVIDENCE_INDEX.md) and [model usage](codex-evidence/models/MODEL_REPORT.md)
