"""Label-free operational monitors, with explicit cost units from public ops facts."""
import json
from pathlib import Path


def escalation_rate(trials):
    return sum(t['status'] == 'escalated' for t in trials) / max(1, len(trials))


def warehouse_cost_components(trials):
    """Machine and human-review cost per observed ticket, separately per warehouse.

    Standby fees are not allocated here; report.ops.cost includes them globally.
    Real wrongful-refund loss needs reconciliation; it cannot be inferred from
    unlabelled refund amounts. Never count all legitimate refunds as a loss.
    """
    facts = json.loads((Path(__file__).resolve().parents[1] / 'data/world.json').read_text(encoding='utf-8'))['ops_facts']
    grouped = {}
    for trial in trials:
        warehouse = trial.get('warehouse') or '?'
        row = grouped.setdefault(warehouse, {'tickets': 0, 'machine_vnd': 0.0, 'review_vnd': 0.0})
        row['tickets'] += 1
        row['machine_vnd'] += trial['cost_vnd']
        kind = trial.get('review_kind')
        units = (facts['recheck_with_note_units'] if kind == 'recheck' else 1.0) if kind else 0.0
        row['review_vnd'] += units * facts['review_cost_per_ticket_vnd']
    return {warehouse: {'machine_vnd': row['machine_vnd'] / row['tickets'],
                        'review_vnd': row['review_vnd'] / row['tickets'],
                        'operating_vnd': (row['machine_vnd'] + row['review_vnd']) / row['tickets']}
            for warehouse, row in grouped.items()}


def warehouse_cost_max_vnd(trials):
    return max((r['operating_vnd'] for r in warehouse_cost_components(trials).values()), default=0.0)


def warehouse_review_cost_max_vnd(trials):
    return max((r['review_vnd'] for r in warehouse_cost_components(trials).values()), default=0.0)


def llm_cost_max_vnd(trials):
    return max((t['cost_vnd'] for t in trials), default=0)


MONITORS = {
    'escalation_rate': escalation_rate,
    'warehouse_cost_max_vnd': warehouse_cost_max_vnd,
    'warehouse_review_cost_max_vnd': warehouse_review_cost_max_vnd,
    'llm_cost_max_vnd': llm_cost_max_vnd,
}
STARTER_MONITORS = ('escalation_rate',)
