# ADR 0001 — Local audit operating boundary

**Status** Approved for product requirements in SG-02

## Context

The initial user is a solo developer assessing an existing repository against its original specification. Evidence and review need to be usable even when the developer cannot run tests locally through SpecGuard or declines AI assistance. Repository content and tests can contain untrusted code and sensitive information.

## Decision

Use a loopback web audit of one pinned Git snapshot. Accept imported test reports and approved existing test invocations in disposable isolation. Allow opt-in remote AI trace suggestions only after per-audit authorization of the displayed sanitized excerpts and destination. Preserve a complete deterministic and manual workflow with AI disabled.

## Alternatives and consequences

A CLI and report-import-only workflow would reduce initial interface and runner scope. A local-only model would keep AI context on the machine. The product owner selected the local web workflow, isolated execution, and per-audit authorization for remote suggestions. This adds acceptance obligations for the local web boundary, exact-command approval, runner isolation, excerpt redaction, consent, and unavailable-provider fallback. M3 selects the architecture and runner. See the [verification policy](../VERIFICATION_POLICY.md).
