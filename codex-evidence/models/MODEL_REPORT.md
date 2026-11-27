# Codex development model usage report

This report summarizes **Codex development model usage only**. It does not describe SpecGuard runtime LLM usage.
Execution counts are record counts; they do not represent token usage, monetary cost, or computational consumption.

`MODEL_METRICS.json` uses schema `specguard-model-metrics` version 1. The same sanitized JSON is emitted to `frontend/public/analytics/model-metrics.json` for static frontend builds.

## Recorded activity

| Measure | Count |
|---|---:|
| Recorded executions | 22 |
| Distinct tasks | 17 |
| Known platform sessions | 4 |
| Missing session IDs | 17 |
| Retrospective records | 1 |

Lifecycle progression status is unavailable from execution counts and is not inferred.

## Lifecycle phases

| Phase | ID | Recorded executions | Progression status |
|---|---|---:|---|
| Understand | P01 | 3 | unavailable |
| Plan | P02 | 8 | unavailable |
| Design | P03 | 8 | unavailable |
| Build | P04 | 3 | unavailable |
| Test | P05 | 0 | unavailable |
| Debug & Improve | P06 | 0 | unavailable |
| Deploy | P07 | 0 | unavailable |
| Automate | P08 | 0 | unavailable |

## Model distribution

| Value | Count |
|---|---:|
| GPT-6 Luna | 12 |
| GPT-6.2 Astra | 1 |
| GPT-6.2 Sol | 8 |
| unavailable | 1 |

## Reasoning effort distribution

| Value | Count |
|---|---:|
| High | 16 |
| Medium | 5 |
| unavailable | 1 |

## Activity type distribution

| Value | Count |
|---|---:|
| architecture | 9 |
| automation | 1 |
| implementation | 1 |
| initialization | 1 |
| metadata_maintenance | 1 |
| research | 1 |
| review | 7 |
| specification | 1 |

## Execution mode distribution

| Value | Count |
|---|---:|
| agent | 1 |
| default | 11 |
| plan | 4 |
| unavailable | 6 |

## Completion status distribution

| Value | Count |
|---|---:|
| complete | 21 |
| partial | 1 |

## Phase by model

| Phase | GPT-6 Luna | GPT-6.2 Astra | GPT-6.2 Sol | unavailable |
|---|---:|---:|---:|---:|
| understand | 3 | 0 | 0 | 0 |
| plan | 2 | 0 | 5 | 1 |
| design | 5 | 0 | 3 | 0 |
| build | 2 | 1 | 0 | 0 |
| test | 0 | 0 | 0 | 0 |
| debug_improve | 0 | 0 | 0 | 0 |
| deploy | 0 | 0 | 0 | 0 |
| automate | 0 | 0 | 0 | 0 |

## Phase by reasoning effort

| Phase | High | Medium | unavailable |
|---|---:|---:|---:|
| understand | 1 | 2 | 0 |
| plan | 6 | 1 | 1 |
| design | 8 | 0 | 0 |
| build | 1 | 2 | 0 |
| test | 0 | 0 | 0 |
| debug_improve | 0 | 0 | 0 |
| deploy | 0 | 0 | 0 |
| automate | 0 | 0 | 0 |

## Escalations

Known escalation values: 14; escalated: 0; unavailable: 8.

## Resource measurements

| Measure | Available | Missing | Total |
|---|---:|---:|---:|
| duration_seconds | 0 | 22 | N/A |
| input_tokens | 0 | 22 | N/A |
| output_tokens | 0 | 22 | N/A |
| resource_usage | 0 | 22 | N/A |

## Timeline records

Chronological, privacy-limited task records are available in `MODEL_METRICS.json`; execution/session IDs, sensitive request content and raw notes are excluded.
