# Goals and boundaries

## Product goal

Build SpecGuard, an evidence-driven software verification platform that detects gaps between original software requirements and actual implementation.

## Challenge objectives

- Demonstrate eight software development lifecycle stages from Understand through Automate.
- Use disciplined model selection and record actual model use when observable.
- Demonstrate engineering quality and effective Codex capability utilization.
- Support conclusions with traceable evidence; never fabricate tests, evidence, or usage measurements.

## Development principles

- Work in bounded, milestone-based increments.
- Prefer deterministic tools before LLM reasoning.
- Use test-driven development for critical functionality.
- Execute untrusted code only with security-conscious isolation and controls.
- Do not alter requirements without authorization.
- Do not commit, push, or deploy without approval.

## Scope boundary

This initialization establishes documentation and evidence structure only. It does not authorize implementing application functionality or changing the product requirements.

## Development constraint baseline (SG-03A)

Development progresses through milestones when their deliverables and acceptance criteria are complete and validated. Feasibility is assessed from technical complexity, dependencies, security, correctness, and maintainability. Do not set calendar-based development targets, estimate developer working hours or FTE, or remove or demote an approved capability solely because of development duration.

The Codex Build Challenge is the external submission context. Its duration does not set internal product requirements, feature priorities, or engineering acceptance criteria. Preserve the eight lifecycle stages—Understand, Specify, Plan, Design, Implement, Verify, Review, and Automate—and all approved P0, P1, and P2 capabilities and SG-02 decisions. Runtime execution timeouts, performance requirements, resource limits, and security timing controls remain governed by the product baseline.

SG-01 discovery remains the basis for the problem hypothesis, user direction, and unvalidated research status. Its one-month feasibility hypothesis is superseded as an active development constraint by [SG-03A decision 0002](docs/adr/0002-milestone-driven-development-baseline.md). Product direction remains solo developers using coding agents and existing repositories checked against their original specifications. The approved MVP uses a local web audit with optional, consent-controlled AI trace suggestions for reviewer consideration. Implementation technology and the example repository and specification remain Design decisions. See the [PRD](docs/PRD.md).
