# Representative failure scenarios

These scenarios are constructed examples for eliciting and testing product needs. They are not observed incidents, interview evidence, or estimates of frequency. Each should be converted into a concrete example only after selecting a user and stack.

| Scenario | Requirement-level failure | Why ordinary signals may miss it | Potential SpecGuard evidence |
|---|---|---|---|
| Omitted acceptance criterion | A requested export includes a required column, but implementation omits it. | Tests cover only the common fields, or no test asserts the full output schema. | Requirement-to-code/test gap; compare expected column list to output assertions. |
| Unsupported proof | A passing report is associated with a criterion whose expected outcome its assertions do not substantiate. | Passing status shows the recorded assertion outcome and can obscure the missing verification. | The P0 fixture retains the report and provenance and leaves the criterion unresolved under SG-R029-AC02. |
| Placeholder path | A button routes to an empty handler or returns canned/sample data. | UI renders; shallow component tests pass; the happy path appears complete. | Stub/TODO/static sample-data signals and runtime flow evidence marked as a candidate, not a verdict. |
| Business-rule boundary | Discount is allowed at the threshold but incorrectly rejected at exactly the maximum eligible amount. | Tests cover values below and above, not equality or decimal/rounding edges. | Requirement-derived boundary test proposal; execute only in a controlled test environment. |
| Authorization omission | A feature checks that a user is signed in but omits the requirement that they own the resource. | Authentication tests pass; tests do not exercise a second user's resource. | Link access-control requirement to route/policy and negative cross-user test evidence. |
| Partial error handling | A retry requirement is implemented for one exception type while timeout errors escape. | Unit tests mock the expected exception only; integration environment behaves differently. | Exception-path test gap and recorded integration command/output. |
| Incorrect state transition | A workflow permits “approved” to jump directly to “paid,” skipping required review. | UI happy-path tests and endpoint status checks pass without transition matrix tests. | State-machine requirement breakdown and transition coverage matrix. |
| UI visually present but functionally disconnected | A control matches a visual description but does not persist the chosen value. | Screenshot checks and component render tests pass without end-to-end assertions. | The P1 broken-save fixture retains the passing comparison and the failing save/readback assertion separately under SG-R042-AC01. |
| Specification drift | Code changes after a requirement or policy update, but tests and linked implementation are not revised. | CI verifies code against old assertions; trace links are stale. | Changed requirement/code baseline and stale candidate links requiring review. |
| Test mirrors implementation assumption | Generated code and generated tests share the same misunderstanding of a vague requirement. | Tests pass because both encode the same mistaken interpretation. | Highlight ambiguity; independent requirement interpretation and human-approved expected outcomes. |

## Research boundary

The SWE-bench correctness study cited in [RESEARCH.md](RESEARCH.md#references) provides direct empirical evidence that benchmark tests missed some behavioral discrepancies for its studied tasks and tools. It does not validate the prevalence of the scenarios above in production. These scenarios are product discovery probes, not statistical claims.
