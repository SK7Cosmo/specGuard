"""Independent review checks; evidence tooling only, no product implementation.

Run from repository root: python -B codex-evidence/review/SG-04C-checks.py
Only reviewed tooling and inert synthetic data are executed. No repository
application, test workload, network request or runner is executed.
"""
import contextlib
import csv
import hashlib
import importlib.metadata
import importlib.util
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'codex-evidence/review'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    # Fingerprint all baseline documents, prior stage evidence, and inspected tools.
    # SG-04C outputs and subsequently updated tracking/navigation are excluded.
    paths = {ROOT / p for p in ['AGENTS.md', 'GOALS.md', 'PLANS.md', 'README.md']}
    paths.update((ROOT / 'docs').rglob('*'))
    paths.update((ROOT / 'codex-evidence/design').glob('*.md'))
    paths.update((ROOT / 'codex-evidence/review').glob('SG-03*.md'))
    paths.update((ROOT / 'codex-evidence/specify').glob('*.md'))
    paths.update((ROOT / 'experiments/sg04b').glob('*.py'))
    paths.update((ROOT / 'experiments/sg04b').glob('*.json'))
    paths.add(ROOT / 'codex-evidence/models/MODEL_STRATEGY.md')
    manifest = [{'path': p.relative_to(ROOT).as_posix(), 'sha256': sha(p), 'bytes': p.stat().st_size}
                for p in sorted(paths) if p.is_file()]
    manifest_path = OUT / 'SG-04C-input-manifest.json'
    # Preserve initial review identities on later reruns.
    if not manifest_path.exists():
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')

    catalog = yaml.safe_load((ROOT / 'docs/REQUIREMENTS.yaml').read_text(encoding='utf-8'))
    reqs = catalog['requirements']
    criteria = {ac['id']: (r, ac) for r in reqs for ac in r['acceptance_criteria']}
    with (ROOT / 'docs/architecture/SG-04A-architecture-traceability.csv').open(encoding='utf-8-sig', newline='') as f:
        matrix = list(csv.DictReader(f))
    plan = (ROOT / 'docs/TEST_PLAN.md').read_text(encoding='utf-8')
    cases = {}
    for line in plan.splitlines():
        if re.match(r'^\| SG-R\d{3}-AC\d{2} \|', line):
            cols = [x.strip() for x in line.strip('|').split('|')]
            assert cols[0] not in cases
            cases[cols[0]] = cols
    assert len(reqs) == 54 and len(criteria) == 68 and len(matrix) == 68
    assert set(criteria) == set(cases) == {r['acceptance_criterion_id'] for r in matrix}
    assert len({r['acceptance_criterion_id'] for r in matrix}) == 68
    by_ac = {r['acceptance_criterion_id']: r for r in matrix}
    for ac_id, (r, ac) in criteria.items():
        row = by_ac[ac_id]
        assert row['requirement_id'] == r['id'] and row['priority'] == r['priority']
        assert row['existing_test_plan_case_id'] == ac_id
        assert row['catalog_verification_method'] == r['verification_method']
        assert cases[ac_id][1].replace(' ', '_') == r['verification_method']
        assert cases[ac_id][-1] == ac['expected']
    deps = {r['id']: r['depends_on'] for r in reqs}
    visited, active = set(), set()
    def visit(node):
        assert node not in active
        if node in visited:
            return
        active.add(node)
        for dep in deps[node]:
            assert dep in deps
            visit(dep)
        active.remove(node)
        visited.add(node)
    for node in deps:
        visit(node)
    register = (ROOT / 'docs/adr/SG-03D-m3-mandatory-conditions.md').read_text(encoding='utf-8')
    gates = [line for line in register.splitlines() if re.match(r'^\| D\d{2} [^|]+\| SG-03C', line)]
    assert len(gates) == 12 and all('| OPEN |' in line for line in gates)
    sources = [s for r in reqs for s in r['sources']]
    for s in sources:
        assert (ROOT / 'docs' / s.split('#')[0]).resolve().is_file()

    # Independently assessed requirement-level design gaps. Each criterion is
    # retained separately, with its exact normative expectation in the CSV.
    assessments = {
        1: ('F03 F10', 'E01 Markdown is not the required heading/criterion grammar; no comment/fence/source-span intake proof.'),
        2: ('F03 F10', 'E01 YAML lacks canonical version and required fields; no actual catalog intake proof.'),
        3: ('F03 F05', 'Safe diagnostics intended; numeric bounds, duplicate handling and preservation transaction unproven.'),
        4: ('F03 F05', 'Exact accepted bytes and pre-persistence rejection intended; real sink and span round trip absent.'),
        5: ('F05 F12', 'Semantic identity described; classification record, revision constraints and activation API absent.'),
        6: ('F12', 'No explicit clarification decision record/API with nonempty rationale and verification block.'),
        7: ('F05 F12', 'No staged change/approval activation contract or enforced retirement/lineage constraints.'),
        8: ('F03 F09', 'Minimal AST/lexical fixtures do not cover routers, both Next.js modes, tests or scope classes.'),
        9: ('F09 F10', 'CE01 misses whole criterion ID; no full identifier boundary and source-location proof.'),
        10: ('F12', 'Link review exists; manual source/test link creation and baseline-scoped target validation unspecified.'),
        11: ('F05 F12', 'Origin and review fields exist; reload and review transitions lack schemas/round trip.'),
        12: ('F12', 'Unlinked state described only broadly; candidate versus confirmed source-link query unspecified.'),
        13: ('F11 F12', 'Reference validation intended; no controlled transport/response/taint/fallback proof.'),
        14: ('F03 F05', 'Commit/spec identities intended; no Git or accepted-source persistence implementation/proof.'),
        15: ('F03 F06', 'One XML entity case; no full outcome/limit/import transaction or reviewer relevance contract.'),
        16: ('F04 F06', 'No launched isolated check or persisted complete environment/limits/provenance record.'),
        17: ('F05 F06', 'Digest field intended; no altered-artifact exclusion through reopen/export/evaluator.'),
        18: ('F03 F05 F07', 'No complete export schema/round trip; unsupported-only rule conflicts with evidence exception.'),
        19: ('F05 F12', 'No durable store or historical baseline addressing/restart proof.'),
        20: ('F09 F10', 'One pass-stub pattern only; helper nonmatch oracle does not assert a detector nonmatch.'),
        21: ('F09 F10', 'One literal inline empty handler; resolved local functions and negative controls untested.'),
        22: ('F09 F10', 'No marked literal response/adjacent-comment implementation or proof.'),
        23: ('F05 F12', 'Finding dismissal record intended; no operation contract/reopen/no-verdict-change proof.'),
        24: ('F08', 'No numeric rule schema/generator; accepted envelope lacks field, bound, domain and step.'),
        25: ('F08', 'No confirmed field rule, typed counterexamples or impossible-violation handling proof.'),
        26: ('F08', 'No transition/failure rule schema or conflicting/undeclared outcome generation matrix.'),
        27: ('F08 F12', 'Case approval endpoint proposed; editing, actual revision binding and expected-outcome validation incomplete.'),
        28: ('F06 F12', 'No explicit approved-case to indexed executable test link operation/schema.'),
        29: ('F06 F07', 'Synthetic evidence flags do not establish assertion relevance, admissibility or distinct missing/skipped reasons.'),
        30: ('F01 F12', 'All five MVP scenarios and integrated UI journey unrun; missing required mutations.'),
        31: ('F02', 'No selected bootstrap/proof/topology or controlled Host/Origin/session request matrix.'),
        32: ('F03', 'No Git fixture, missing/malformed object, path/symlink/submodule or retrieval sentinel proof.'),
        33: ('F04 F10', 'Sequential used flag only; changed invocation tested after token already consumed.'),
        34: ('F04 F05', 'No supported/provisioned sandbox or durable teardown/recovery state proof.'),
        35: ('F04', 'No numeric limits, telemetry, limit-overrun or descendant termination proof.'),
        36: ('F05 F12', 'No crash-atomic metadata/artifact/idempotency/recovery procedure or retained-work proof.'),
        37: ('F05 F09', 'Repeat of unchanged small index only; complete finding/link/verdict ordering not proven.'),
        38: ('F03 F11', 'Synthetic password sketch only; class coverage and every persistent/display/outbound sink unproven.'),
        39: ('F11', 'Consent flag only; exact audit/endpoint/revocation/serialization/redirect transport unproven.'),
        40: ('F13', 'P1 reservation only; no capture/flow/environment/approval binding contract.'),
        41: ('F13', 'P1 reservation only; no reference identity, comparison metric or threshold contract.'),
        42: ('F13', 'Separate image/interaction intent preserved; no distinct result schema or controlled P1 flow.'),
        43: ('F05 F13', 'Stable revisions reserved; concrete baseline comparison contract remains for M7 design.'),
        44: ('F13', 'Diff adapter named; linked change/removal selection contract remains for M7 design.'),
        45: ('F05 F13', 'Applicability intent exists; selective reassessment and retained provenance unproven.'),
        46: ('F07 F13', 'Denominator formula in PRD; no executable summary contract or empty-baseline proof.'),
        47: ('F13', 'No-score-override intent preserved; P0 review-list query contract absent.'),
        48: ('F13', 'Summary drilldown named only; contributing-set contract absent.'),
        49: ('F13', 'UI filter intent exists; findings filter/query contract not specified.'),
        50: ('F13', 'Detail view intent exists; complete baseline-scoped response contract absent.'),
        51: ('F05 F13', 'History reserved; changed-verdict versus retired criterion comparison not designed.'),
        52: ('F13', 'P2 adapter named only; scoped proposal type/authority and finding binding absent.'),
        53: ('F13', 'Read-only diff intent preserved; patch validation/representation contract absent.'),
        54: ('F13', 'Mapped validation checks reserved; repair-check association contract absent.'),
    }
    with (OUT / 'SG-04C-criterion-review.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['requirement_id', 'criterion_id', 'priority',
            'expected', 'verification_method', 'mapped_case', 'findings', 'independent_assessment', 'verification_status'])
        writer.writeheader()
        for ac_id, (r, ac) in criteria.items():
            findings, note = assessments[int(r['id'][-3:])]
            writer.writerow(dict(requirement_id=r['id'], criterion_id=ac_id, priority=r['priority'],
                expected=ac['expected'], verification_method=r['verification_method'], mapped_case=cases[ac_id][0],
                findings=findings, independent_assessment=note,
                verification_status='Product acceptance not run; design/review evidence only'))

    # Source reviewed before loading; main() prints only results and parses inert
    # fixtures. Its module has no launch/network/storage behavior at import.
    source = ROOT / 'experiments/sg04b/run_proofs.py'
    spec = importlib.util.spec_from_file_location('reviewed_sg04b', source)
    proof = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(proof)
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = proof.main()
    reproduced = json.loads(stream.getvalue())
    original = json.loads((ROOT / 'experiments/sg04b/results.json').read_text(encoding='utf-8'))
    assert code == 0
    same_results = reproduced == original

    # Counterexamples use independently stated normative expectations. They
    # characterize proof insufficiency, not a nonexistent product implementation.
    fake_report = {'baseline': 'base-A', 'case_id': 'SG-R029-AC02',
                   'criterion_ids': ['SG-R029-AC02'], 'assertion_ids': ['invented-assertion']}
    altered = {'outcome': 'passed', 'relevant': True, 'baseline_current': True,
               'integrity': 'altered', 'provenance': 'inferred', 'reviewed': False}
    proposal = {'criterion_id': 'SG-R024-AC01', 'rule_type': 'numeric_boundary',
                'source_revision': 'rev-999', 'expected_outcome': 'accept'}
    counterexamples = [
        {'id': 'CE01', 'input': 'SG-R001-AC01', 'policy_expected': ['SG-R001-AC01'],
         'actual': proof.exact_id_refs('SG-R001-AC01', {'SG-R001', 'SG-R001-AC01'}),
         'finding': 'F09'},
        {'id': 'CE02', 'input': 'self-declared invented assertion; no reviewer or observed assertion',
         'policy_expected': 'not sufficient for criterion support',
         'actual_relevant': proof.relevant(fake_report, 'base-A', 'SG-R029-AC02', 'SG-R029-AC02'),
         'finding': 'F06'},
        {'id': 'CE03', 'input': altered, 'policy_expected': 'unresolved',
         'actual': proof.verdict([altered]), 'finding': 'F06'},
        {'id': 'CE04', 'input': proposal,
         'policy_expected': 'not an adoptable numeric rule: no actual revision match, field, bound, domain or step',
         'actual_envelope_accepted': proof.validate_rule_proposal(proposal, {'SG-R024-AC01'}),
         'finding': 'F08'},
        {'id': 'CE05', 'input': 'id: SG-R001\nid: SG-R002\n',
         'policy_expected': 'duplicate key rejected by specification intake',
         'actual_candidate_safe_load': yaml.safe_load('id: SG-R001\nid: SG-R002\n'), 'finding': 'F03'},
    ]
    assert counterexamples[0]['actual'] == []
    assert counterexamples[1]['actual_relevant'] is True
    assert counterexamples[2]['actual'] == 'verified'
    assert counterexamples[3]['actual_envelope_accepted'] is True
    assert counterexamples[4]['actual_candidate_safe_load'] == {'id': 'SG-R002'}
    summary = {
        'scope': 'independent structural checks, reviewed synthetic harness reproduction and counterexamples; no product acceptance',
        'python': sys.version.split()[0],
        'packages': {name: importlib.metadata.version(name) for name in ['PyYAML', 'mistune', 'defusedxml']},
        'requirements': len(reqs), 'criteria': len(criteria),
        'requirement_priorities': dict(Counter(r['priority'] for r in reqs)),
        'criterion_priorities': dict(Counter(r['priority'] for r, ac in criteria.values())),
        'exact_case_matrix_matches': 68, 'catalog_source_paths_resolved': len(sources),
        'dependency_graph': 'acyclic', 'mandatory_gates_open': len(gates),
        'reproduced_harness': {'passed': reproduced['passed'], 'failed': reproduced['failed'],
                               'matches_stored_result_json': same_results},
        'counterexamples': counterexamples,
        'measurement_limits': 'No token/cost/session/duration/resource measurements; no service, browser, runner, provider or persistence proof.'
    }
    (OUT / 'SG-04C-check-results.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
