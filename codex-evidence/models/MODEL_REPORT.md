# Codex development model usage report

This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.

## Recorded activity

| Measure | Count |
|---|---:|
| Sessions with available ID | 0 |
| Records missing session ID | 5 |
| Task executions | 5 |
| Malformed or duplicate rows | 0 |

Task executions count unique, valid `execution_id` records. Sessions count unique available session IDs. Duplicate execution IDs are skipped.

### Model usage distribution

| Value | Count | Distribution |
|---|---:|---|
| GPT-6 Luna | 3 | ████████████ (60.0%) |
| GPT-6.2 Sol | 1 | ████ (20.0%) |
| Luna | 1 | ████ (20.0%) |

### Reasoning effort distribution

| Value | Count | Distribution |
|---|---:|---|
| High | 2 | ████████ (40.0%) |
| Medium | 3 | ████████████ (60.0%) |

### Model usage by lifecycle phase

| Lifecycle phase | Task executions | Models used |
|---|---:|---|
| automate | 1 | GPT-6 Luna: 1 |
| plan | 1 | GPT-6 Luna: 1 |
| review | 1 | Luna: 1 |
| specify | 1 | GPT-6.2 Sol: 1 |
| understand | 1 | GPT-6 Luna: 1 |

### Task completion

| Status | Count |
|---|---:|
| complete | 5 |

Completed: **5 / 5** task executions.

### Escalations

| Measure | Count |
|---|---:|
| Escalations among known values | 0 / 0 |
| Records missing escalation value | 5 |

### Duration and token statistics

| Measure | Available count | Total | Mean | Missing measurement count |
|---|---:|---:|---:|---:|
| Duration (seconds) | 0 | N/A | N/A | 5 |
| Input tokens | 0 | N/A | N/A | 5 |
| Output tokens | 0 | N/A | N/A | 5 |

Missing duration measurements: **5**; missing token measurements: **10** (input and output token fields counted separately).

Only numeric, non-negative measurements are aggregated. Blank, `N/A`, unavailable, and invalid measurements are not treated as zero.
