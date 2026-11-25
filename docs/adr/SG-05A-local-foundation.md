# SG-05A local foundation decision

On 2026-11-25 the product owner approved the SG-04R session policy for implementation and controlled verification. A local interactive terminal receives a one-time 256-bit bootstrap code. The browser exchanges possession for an opaque HttpOnly, SameSite=Strict, Path=/ session cookie on the same origin. Secure applies over HTTPS. Idle expiry is 30 minutes and absolute expiry is eight hours. Revoke consumes the session. Restart invalidates the code and session. Only the operator holding the code can perform the synthetic check. Audit operations remain disabled pending designated D08 review.

The owner approved the SG-04R SQLite layout for isolated temporary or explicitly designated development databases, synthetic fixtures, and nondestructive versioned migrations. SG-05A stores schema metadata only. D11 review precedes any product persistence.

Official registry packages may be fetched as necessary using project-local environments, pins and locks, with framework telemetry disabled. The approval covers the minimum same-origin frontend and controlled tests. All twelve conditions remain OPEN. See the [implementation evidence](../../codex-evidence/implement/SG-05A.md).
