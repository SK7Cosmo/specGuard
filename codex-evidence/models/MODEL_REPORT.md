# Codex development model usage report

This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.

## Recorded activity

| Measure | Count |
|---|---:|
| Sessions with available ID | 0 |
| Records missing session ID | 2 |
| Task executions | 2 |
| Malformed or duplicate rows | 0 |

Task executions count unique, valid `execution_id` records. Sessions count unique available session IDs. Duplicate execution IDs are skipped.

### Model usage distribution

| Value | Count | Distribution |
|---|---:|---|
| GPT-6 Luna | 2 | ████████████████████ (100.0%) |

### Reasoning effort distribution

| Value | Count | Distribution |
|---|---:|---|
| Medium | 2 | ████████████████████ (100.0%) |

### Model usage by lifecycle phase

| Lifecycle phase | Task executions | Models used |
|---|---:|---|
| automate | 1 | GPT-6 Luna: 1 |
| plan | 1 | GPT-6 Luna: 1 |

### Task completion

| Status | Count |
|---|---:|
| complete | 2 |

Completed: **2 / 2** task executions.

### Escalations

| Measure | Count |
|---|---:|
| Escalations among known values | 0 / 0 |
| Records missing escalation value | 2 |

### Duration and token statistics

| Measure | Available count | Total | Mean | Missing measurement count |
|---|---:|---:|---:|---:|
| Duration (seconds) | 0 | N/A | N/A | 2 |
| Input tokens | 0 | N/A | N/A | 2 |
| Output tokens | 0 | N/A | N/A | 2 |

Missing duration measurements: **2**; missing token measurements: **4** (input and output token fields counted separately).

Only numeric, non-negative measurements are aggregated. Blank, `N/A`, unavailable, and invalid measurements are not treated as zero.
