# Codex development model usage report

This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.

## Recorded activity

| Measure | Count |
|---|---:|
| Sessions with available ID | 0 |
| Records missing session ID | 17 |
| Task executions | 17 |
| Malformed or duplicate rows | 0 |

Task executions count unique, valid `execution_id` records. Sessions count unique available session IDs. Duplicate execution IDs are skipped.

### Model usage distribution

| Value | Count | Distribution |
|---|---:|---|
| GPT-6 Luna | 9 | ███████████ (52.9%) |
| GPT-6.2 Sol | 7 | ████████ (41.2%) |
| unavailable | 1 | █ (5.9%) |

### Reasoning effort distribution

| Value | Count | Distribution |
|---|---:|---|
| High | 13 | ███████████████ (76.5%) |
| Medium | 3 | ████ (17.6%) |
| unavailable | 1 | █ (5.9%) |

### Model usage by lifecycle phase

| Lifecycle phase | Task executions | Models used |
|---|---:|---|
| automate | 1 | GPT-6 Luna: 1 |
| design | 4 | GPT-6 Luna: 4 |
| plan | 1 | GPT-6 Luna: 1 |
| review | 9 | GPT-6 Luna: 2, GPT-6.2 Sol: 6, unavailable: 1 |
| specify | 1 | GPT-6.2 Sol: 1 |
| understand | 1 | GPT-6 Luna: 1 |

### Task completion

| Status | Count |
|---|---:|
| complete | 17 |

Completed: **17 / 17** task executions.

### Escalations

| Measure | Count |
|---|---:|
| Escalations among known values | 0 / 10 |
| Records missing escalation value | 7 |

### Duration and token statistics

| Measure | Available count | Total | Mean | Missing measurement count |
|---|---:|---:|---:|---:|
| Duration (seconds) | 0 | N/A | N/A | 17 |
| Input tokens | 0 | N/A | N/A | 17 |
| Output tokens | 0 | N/A | N/A | 17 |

Missing duration measurements: **17**; missing token measurements: **34** (input and output token fields counted separately).

Only numeric, non-negative measurements are aggregated. Blank, `N/A`, unavailable, and invalid measurements are not treated as zero.
