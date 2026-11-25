"""Bounded SG-04D design-contract checks using inert synthetic records only.

This is review evidence, not SpecGuard application code or an M3 gate closure.
Run from the repository root with: python -B experiments/sg04d/verify_design_contracts.py
"""
from __future__ import annotations

import hashlib
import json
import platform
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "codex-evidence" / "design" / "SG-04D-contract-check-results.json"
EXECUTION_ID = "SG-04D-20261124-01"
STARTING_COMMIT = "81ff5ff03d1b5ee859f23ed6eb38306df64483d9"

CRITERION_TOKEN = re.compile(r"(?<![A-Za-z0-9_])SG-R\d{3}-AC\d{2}(?![A-Za-z0-9_])")
REQUIREMENT_TOKEN = re.compile(r"(?<![A-Za-z0-9_])SG-R\d{3}(?!(?:[A-Za-z0-9_]|-AC\d))")


def identify_tokens(text: str) -> list[str]:
    """Return complete catalog tokens and avoid criterion-prefix duplication."""
    criteria = list(CRITERION_TOKEN.finditer(text))
    result = [m.group(0) for m in criteria]
    masked = list(text)
    for match in criteria:
        masked[match.start():match.end()] = " " * (match.end() - match.start())
    result.extend(m.group(0) for m in REQUIREMENT_TOKEN.finditer("".join(masked)))
    return result


def admissible(record: dict, baseline: str, criterion: str) -> bool:
    return (
        record.get("source_kind") in {"imported", "manual", "runner"}
        and record.get("baseline_id") == baseline
        and record.get("criterion_id") == criterion
        and record.get("inspected") is True
        and record.get("complete") is True
        and record.get("integrity_valid") is True
        and record.get("fresh") is True
        and record.get("reviewer_relevance") is True
        and bool(record.get("reviewer_rationale"))
        and record.get("outcome") in {"pass", "fail"}
    )


def evaluate(coverage: str, evidence: list[dict], baseline: str, criterion: str) -> dict:
    """Keep coverage separate from evidence admissibility and preserve notice."""
    outcomes = {
        item["outcome"] for item in evidence
        if admissible(item, baseline, criterion)
    }
    if outcomes == {"pass"}:
        verdict = "verified"
    elif outcomes == {"fail"}:
        verdict = "failed"
    else:
        verdict = "unresolved"
    return {
        "verdict": verdict,
        "coverage_notice_retained": coverage != "supported",
    }


def evidence(outcome="pass", **overrides):
    record = {
        "source_kind": "imported", "baseline_id": "base-1",
        "criterion_id": "SG-R001-AC01", "inspected": True,
        "complete": True, "integrity_valid": True, "fresh": True,
        "reviewer_relevance": True, "reviewer_rationale": "reviewed synthetic assertion",
        "outcome": outcome,
    }
    record.update(overrides)
    return record


def main() -> None:
    token_cases = [
        ("SG-R001-AC01", ["SG-R001-AC01"]),
        ("SG-R001", ["SG-R001"]),
        ("test_case_for_SG-R001-AC01", []),
        ("xSG-R001-AC01", []),
        ("(SG-R001-AC01), SG-R002", ["SG-R001-AC01", "SG-R002"]),
        ("SG-R001-AC010", []),
    ]
    for source, expected in token_cases:
        actual = identify_tokens(source)
        assert actual == expected, (source, expected, actual)

    scenarios = {
        "no_evidence": [],
        "relevant_pass": [evidence("pass")],
        "relevant_fail": [evidence("fail")],
        "conflicting_relevant": [evidence("pass"), evidence("fail", source_kind="manual")],
        "unrelated_green": [evidence("pass", criterion_id="SG-R002-AC01")],
        "ai_claim": [evidence("pass", source_kind="ai")],
    }
    expected = {
        "no_evidence": "unresolved", "relevant_pass": "verified",
        "relevant_fail": "failed", "conflicting_relevant": "unresolved",
        "unrelated_green": "unresolved", "ai_claim": "unresolved",
    }
    matrix = []
    for coverage in ("supported", "partial", "unsupported"):
        for name, records in scenarios.items():
            result = evaluate(coverage, records, "base-1", "SG-R001-AC01")
            assert result["verdict"] == expected[name], (coverage, name, result)
            assert result["coverage_notice_retained"] == (coverage != "supported")
            matrix.append({"coverage": coverage, "scenario": name, **result})

    # Sensitivity control: the old blanket unsupported-only rule suppresses
    # independently admissible evidence and therefore disagrees with the oracle.
    valid_pass = [evidence("pass")]
    def blanket_unsupported_mutant(coverage, records):
        if coverage == "unsupported":
            return "unresolved"
        return evaluate(coverage, records, "base-1", "SG-R001-AC01")["verdict"]

    defective = blanket_unsupported_mutant("unsupported", valid_pass)
    assert defective != expected["relevant_pass"]

    fixtures = {
        "token_cases": token_cases,
        "coverage_scenarios": {k: v for k, v in expected.items()},
        "coverage_values": ["supported", "partial", "unsupported"],
        "sensitivity_control": "blanket unsupported-only suppression contradicts relevant-pass oracle",
    }
    fixture_bytes = json.dumps(fixtures, sort_keys=True, separators=(",", ":")).encode()
    harness_bytes = Path(__file__).read_bytes()
    result = {
        "execution_id": EXECUTION_ID,
        "task_id": "SG-04D",
        "starting_commit": STARTING_COMMIT,
        "execution_mode": "Default",
        "session_id": "N/A",
        "command": "python -B experiments/sg04d/verify_design_contracts.py",
        "runtime": {"python": sys.version.split()[0], "platform": platform.platform()},
        "inputs": {
            "harness_sha256": hashlib.sha256(harness_bytes).hexdigest(),
            "fixture_sha256": hashlib.sha256(fixture_bytes).hexdigest(),
            "fixture_count": len(token_cases) + len(matrix),
        },
        "observations": {
            "criterion_token_cases": len(token_cases),
            "coverage_admissibility_cases": len(matrix),
            "all_expected_results_matched": True,
            "sensitivity_control_detected_defect": True,
            "status": "PASS",
        },
        "coverage_matrix": matrix,
        "limitations": [
            "Inert synthetic strings and records only; no SpecGuard application code executed.",
            "Does not establish parser, browser, storage, runner, provider, or integrated feasibility.",
            "Design-contract checks do not close D05, D07, or D12; all mandatory conditions remain open.",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "token_cases": len(token_cases),
                      "coverage_cases": len(matrix), "output": OUT.as_posix()}, indent=2))


if __name__ == "__main__":
    main()
