# Model strategy

Use the least capable model that can reliably handle the bounded task. Record actual model and reasoning effort in `MODEL_USAGE.csv` when observable; describe unavailable fields as `unavailable`, never infer measurements.

| Task complexity | Preferred model | Guidance |
|---|---|---|
| Routine, bounded tasks | GPT-6 Luna Medium | Use for straightforward edits, summaries, and low-risk scoped work. |
| Moderately complex implementation | GPT-6 Luna High | Use when the task needs deeper reasoning but remains bounded. |
| Complex engineering | GPT-6.2 Sol Medium or High | Select effort based on complexity and risk. |
| Critical escalation | GPT-6.2 Astra High, if available | Reserve for critical cases where escalation is justified and the model is available. |

Record the task scope and selection rationale, not just the model name. Capture validation results, elapsed duration, and resource usage only when actually observable. Keep experiments reproducible by recording the prompt/task, model, effort, inputs, method, and outcome. Do not use model output as a substitute for deterministic verification where deterministic checks apply.
