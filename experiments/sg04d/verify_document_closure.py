"""Deterministic SG-04D documentation and traceability closure checks."""
from __future__ import annotations

import csv
import hashlib
import json
import platform
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "codex-evidence" / "design" / "SG-04D-document-check-results.json"
EXECUTION_ID = "SG-04D-20261124-01"
STARTING_COMMIT = "81ff5ff03d1b5ee859f23ed6eb38306df64483d9"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    catalog = yaml.safe_load((ROOT / "docs/REQUIREMENTS.yaml").read_text(encoding="utf-8"))
    requirements = catalog["requirements"]
    criteria = {ac["id"] for req in requirements for ac in req["acceptance_criteria"]}
    with (ROOT / "docs/architecture/SG-04A-architecture-traceability.csv").open(
        encoding="utf-8-sig", newline=""
    ) as f:
        rows = list(csv.DictReader(f))
    plan = (ROOT / "docs/TEST_PLAN.md").read_text(encoding="utf-8")
    cases = set(re.findall(r"^\| (SG-R\d{3}-AC\d{2}) \|", plan, re.M))
    assert len(requirements) == 54 and len(criteria) == 68 and len(rows) == 68
    assert {row["acceptance_criterion_id"] for row in rows} == criteria == cases
    assert all(row.get("sg04c_finding_ids") is not None for row in rows)
    assert all(row.get("sg04d_remediation_reference") and row.get("sg04d_status") for row in rows)

    register = (ROOT / "docs/adr/SG-03D-m3-mandatory-conditions.md").read_text(encoding="utf-8")
    main_register = register.split("## SG-04B feasibility observations", 1)[0]
    gate_ids = re.findall(r"^\| (D\d{2})\b", main_register, re.M)
    assert gate_ids == [f"D{i:02d}" for i in range(1, 13)]
    for gate in gate_ids:
        line = next(row for row in main_register.splitlines() if row.startswith(f"| {gate} "))
        cells = [cell.strip() for cell in line.split("|")]
        assert "OPEN" in cells and cells[-2].endswith("OPEN."), gate

    closure = (ROOT / "codex-evidence/design/SG-04D-closure.md").read_text(encoding="utf-8")
    assert all(f"F{i:02d}" in closure for i in range(1, 15))
    assert all(f"D{i:02d}" in closure for i in range(1, 13))
    result_file = ROOT / "codex-evidence/design/SG-04D-contract-check-results.json"
    result = json.loads(result_file.read_text(encoding="utf-8"))
    harness = ROOT / "experiments/sg04d/verify_design_contracts.py"
    assert result["inputs"]["harness_sha256"] == sha(harness)
    assert result["observations"]["status"] == "PASS"
    assert result["observations"]["criterion_token_cases"] == 6
    assert result["observations"]["coverage_admissibility_cases"] == 18

    output = {
        "execution_id": EXECUTION_ID,
        "task_id": "SG-04D",
        "starting_commit": STARTING_COMMIT,
        "command": "python -B experiments/sg04d/verify_document_closure.py",
        "runtime": {"python": sys.version.split()[0], "platform": platform.platform()},
        "harness_sha256": sha(Path(__file__)),
        "observations": {
            "requirements": len(requirements), "criteria": len(criteria),
            "exact_test_plan_case_mappings": len(cases), "traceability_rows": len(rows),
            "condition_gates": len(gate_ids), "all_gates_open": True,
            "findings_in_closure_report": 14,
            "contract_result_matches_harness": True,
            "contract_token_cases": 6, "contract_admissibility_cases": 18,
            "status": "PASS",
        },
        "limitations": [
            "Documentation, traceability, and evidence-integrity structure only.",
            "Does not validate product behavior, implementation feasibility, or security controls.",
        ],
    }
    OUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output["observations"], indent=2))


if __name__ == "__main__":
    main()
