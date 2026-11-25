"""Deterministic SG-04R requirement, gate, traceability, and roadmap checks."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
START = "4bed4560b8990d11df5a618ef59238829223317a"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def starting_bytes(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{START}:{path}"], cwd=ROOT)


def check_markdown_links(paths: list[str]) -> int:
    checked = 0
    for name in paths:
        source = ROOT / name
        body = source.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", body):
            target = target.strip().strip("<>")
            if not target or target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            resolved = (source.parent / local).resolve()
            assert resolved.exists(), f"Missing local link in {name}: {target}"
            checked += 1
    return checked


def main() -> None:
    catalog_bytes = (ROOT / "docs/REQUIREMENTS.yaml").read_bytes()
    catalog = yaml.safe_load(catalog_bytes)
    requirements = catalog["requirements"]
    criteria = [ac for req in requirements for ac in req["acceptance_criteria"]]
    req_by_priority = Counter(req["priority"] for req in requirements)
    ac_by_priority = Counter(req["priority"] for req in requirements for _ in req["acceptance_criteria"])

    # Normative records are byte-identical to the task's starting Git commit.
    normative = ["docs/PRD.md", "docs/REQUIREMENTS.yaml", "docs/VERIFICATION_POLICY.md", "docs/TEST_PLAN.md"]
    hashes = {}
    for path in normative:
        current = (ROOT / path).read_bytes()
        baseline = starting_bytes(path)
        assert current == baseline, f"Normative document changed: {path}"
        hashes[path] = hashlib.sha256(current).hexdigest()

    plan = read("docs/TEST_PLAN.md")
    cases = set(re.findall(r"^\| (SG-R\d{3}-AC\d{2}) \|", plan, re.M))
    mvp_scenarios = set(re.findall(r"\b(MVP-0[1-5])\b", plan))
    assert len(requirements) == 54
    assert len(criteria) == 68 and len({ac["id"] for ac in criteria}) == 68
    assert req_by_priority == {"P0": 39, "P1": 12, "P2": 3}
    assert ac_by_priority == {"P0": 53, "P1": 12, "P2": 3}
    assert len(re.findall(r"^\| SG-R\d{3}-AC\d{2} \|", plan, re.M)) == 68
    assert cases == {ac["id"] for ac in criteria}
    assert mvp_scenarios == {f"MVP-{i:02d}" for i in range(1, 6)}
    catalog_feature_labels = sorted({req["feature"] for req in requirements})

    with (ROOT / "docs/architecture/SG-04A-architecture-traceability.csv").open(
        encoding="utf-8-sig", newline=""
    ) as f:
        trace = list(csv.DictReader(f))
    assert len(trace) == 68
    assert {row["acceptance_criterion_id"] for row in trace} == cases
    r032 = next(row for row in trace if row["acceptance_criterion_id"] == "SG-R032-AC02")
    assert "D06" in r032["open_condition_ids"] and "D12" in r032["open_condition_ids"]

    gates = read("docs/adr/SG-03D-m3-mandatory-conditions.md")
    historical = gates.split("## SG-04B feasibility observations", 1)[0]
    gate_rows = re.findall(r"^\| (D\d{2})\b.*$", historical, re.M)
    assert gate_rows == [f"D{i:02d}" for i in range(1, 13)]
    assert all(re.search(rf"^\| {gate} .*\| OPEN \|", historical, re.M) for gate in gate_rows)
    activation = gates.split("## SG-04R prospective progression and activation policy", 1)[1]
    activation_rows = re.findall(r"^\| (D\d{2}) \|", activation, re.M)
    assert activation_rows == gate_rows
    d06_history_row = next(line for line in historical.splitlines() if line.startswith("| D06 "))
    assert "SG-R032-AC02" in d06_history_row

    roadmap = read("docs/design/SG-04R-implementation-roadmap.md")
    task_ids = re.findall(r"^\| \*\*(SG-05[A-Z])\b", roadmap, re.M)
    assert task_ids == [f"SG-05{c}" for c in "ACDEFGHIJKLMN"]
    task_position = {task: i for i, task in enumerate(task_ids)}
    # Verify every dependency reference points to an earlier roadmap task.
    task_rows = [line for line in roadmap.splitlines() if line.startswith("| **SG-05")]
    assert len(task_rows) == len(task_ids)
    for row in task_rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        task = re.search(r"\*\*(SG-05[A-Z])", cells[0]).group(1)
        for dep in re.findall(r"SG-05[A-Z]", cells[2]):
            assert dep in task_position and task_position[dep] < task_position[task], (task, dep)
    assert "SG-05A Foundation and local authority" in roadmap
    assert "SG-05N" in roadmap

    # Historical evidence is still present and no gate is recorded closed.
    closure_path = "codex-evidence/design/SG-04D-closure.md"
    assert (ROOT / closure_path).read_bytes() == starting_bytes(closure_path)
    preserved_evidence = {}
    for path in [
        "codex-evidence/design/SG-04D-closure.md",
        "codex-evidence/design/SG-04D-document-check-results.json",
        "codex-evidence/design/SG-04D-contract-check-results.json",
    ]:
        assert (ROOT / path).exists()
        preserved_evidence[path] = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    historical_result = json.loads(read("codex-evidence/design/SG-04R-document-check-results.json"))
    assert preserved_evidence == historical_result["preserved_historical_evidence_sha256"]
    for phrase in ["all 53 P0 criteria", "all five MVP scenarios", "unverified", "fail closed"]:
        assert phrase.casefold() in roadmap.casefold()
    links_checked = check_markdown_links([
        "PLANS.md", "README.md", "GOALS.md", "AGENTS.md",
        "docs/adr/SG-05A-local-foundation.md", "codex-evidence/implement/SG-05A.md",
        "docs/architecture/SG-04A-system-architecture.md",
        "docs/architecture/SG-04A-condition-matrix.md",
        "docs/architecture/README.md",
        "docs/adr/SG-03D-m3-mandatory-conditions.md",
        "docs/adr/SG-03B-design-decision-register.md",
        "docs/adr/SG-04A-architecture-boundaries.md",
        "docs/adr/SG-04R-lifecycle-restructuring.md",
        "docs/adr/SG-04R-implementation-decisions.md",
        "docs/adr/README.md",
        "docs/architecture/SG-04A-deliverables.md",
        "docs/design/SG-04R-implementation-roadmap.md",
        "codex-evidence/design/README.md",
        "codex-evidence/EVIDENCE_INDEX.md",
        "codex-evidence/design/SG-04R.md",
    ])

    result = {
        "check": "current working tree against SG-04R baseline",
        "starting_commit": START,
        "status": "PASS",
        "requirements": len(requirements),
        "criteria": len(criteria),
        "requirements_by_priority": dict(req_by_priority),
        "criteria_by_priority": dict(ac_by_priority),
        "test_plan_case_mappings": len(cases),
        "mvp_scenarios": sorted(mvp_scenarios),
        "catalog_feature_labels": catalog_feature_labels,
        "mandatory_conditions_open": gate_rows,
        "prospective_activation_rows": len(activation_rows),
        "traceability_rows": len(trace),
        "d06_sg_r032_ac02_mapping": r032["open_condition_ids"],
        "roadmap_tasks": task_ids,
        "roadmap_dependencies_acyclic_by_order": True,
        "local_markdown_links_checked": links_checked,
        "historical_closure_record_unchanged": True,
        "preserved_historical_evidence_sha256": preserved_evidence,
        "normative_document_sha256": hashes,
        "limitations": [
            "Document, catalog, mapping, and roadmap structure only; no product acceptance or runtime feasibility test.",
            "Document checks do not establish service settings or runtime behavior.",
            "SG-04E is an untracked input at the starting commit; its evidence file was preserved by leaving it unchanged.",
        ],
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
