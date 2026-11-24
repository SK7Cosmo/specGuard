# Codex development model usage report

This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.

## Recorded activity

| Measure | Count |
|---|---:|
| Sessions with available ID | 0 |
| Records missing session ID | 11 |
| Task executions | 11 |
| Malformed or duplicate rows | 0 |

Task executions count unique, valid `execution_id` records. Sessions count unique available session IDs. Duplicate execution IDs are skipped.

### Model usage distribution

| Value | Count | Distribution |
|---|---:|---|
| GPT-6 Luna | 3 | █████ (27.3%) |
| GPT-6.2 Sol | 1 | ██ (9.1%) |
| Luna | 2 | ████ (18.2%) |
| Sol | 4 | ███████ (36.4%) |
| unavailable | 1 | ██ (9.1%) |

### Reasoning effort distribution

| Value | Count | Distribution |
|---|---:|---|
| High | 7 | █████████████ (63.6%) |
| Medium | 3 | █████ (27.3%) |
| unavailable | 1 | ██ (9.1%) |

### Model usage by lifecycle phase

| Lifecycle phase | Task executions | Models used |
|---|---:|---|
| automate | 1 | GPT-6 Luna: 1 |
| plan | 1 | GPT-6 Luna: 1 |
| review | 7 | Luna: 2, Sol: 4, unavailable: 1 |
| specify | 1 | GPT-6.2 Sol: 1 |
| understand | 1 | GPT-6 Luna: 1 |

### Task completion

| Status | Count |
|---|---:|
| complete | 11 |

Completed: **11 / 11** task executions.

### Escalations

| Measure | Count |
|---|---:|
| Escalations among known values | 0 / 5 |
| Records missing escalation value | 6 |

### Duration and token statistics

| Measure | Available count | Total | Mean | Missing measurement count |
|---|---:|---:|---:|---:|
| Duration (seconds) | 0 | N/A | N/A | 11 |
| Input tokens | 0 | N/A | N/A | 11 |
| Output tokens | 0 | N/A | N/A | 11 |

Missing duration measurements: **11**; missing token measurements: **22** (input and output token fields counted separately).

Only numeric, non-negative measurements are aggregated. Blank, `N/A`, unavailable, and invalid measurements are not treated as zero.
