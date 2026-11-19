"""Round-1 system gates: trusted facts, financial writes, third-party writes.

Only public read tools and policy/operations facts are used. Ticket wording,
IDs, seeds, grader labels and incident packs do not decide an exception.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # Gate 1: date-valid policy and authenticated order/parcel boundary.
    policies = [p for p in ctx.tools.lookup_policies()
                if p['effective_from'] <= ctx.as_of
                and (not p.get('effective_to') or ctx.as_of <= p['effective_to'])]
    if len(policies) != 1:
        return Verdict.escalate('Missing or ambiguous effective policy')
    order = ctx.tools.lookup_order(ctx.ticket.get('order_id'))
    if order is not None:
        if order['customer_id'] != ctx.ticket['customer_id']:
            return Verdict.escalate('Customer does not own this order')
        pid = ctx.ticket.get('parcel_id')
        if pid and not any(p['parcel_id'] == pid for p in order.get('parcels', [])):
            return Verdict.escalate('Parcel does not belong to this order')
    return Verdict.allow(policy_id=policies[0]['policy_id'])


def write_gate(ctx, action):
    tool = action.get('tool')
    if action.get('ticket_id') != ctx.ticket['ticket_id']:
        return Verdict.escalate('Write belongs to a different ticket')
    if tool == 'send_reply':
        if action.get('customer_id') != ctx.ticket['customer_id']:
            return Verdict.escalate('Reply recipient differs from authenticated customer')
        return Verdict.allow()

    order = ctx.tools.lookup_order(ctx.ticket.get('order_id'))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or policy is None or not order.get('parcels'):
        return Verdict.escalate('Missing order, parcel or effective policy for write')
    if order['customer_id'] != ctx.ticket['customer_id']:
        return Verdict.escalate('Customer does not own this order')
    if tool != 'notify_carrier' and action.get('order_id') != order['order_id']:
        return Verdict.escalate('Write order differs from authenticated order')
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    try:
        delay = H.db_delay_days(parcel, ctx.as_of)
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate('Tracking dates are missing or invalid')
    cause = parcel.get('delay_cause')
    limits = ctx.tools.ops_limits()

    if tool == 'issue_refund':
        # Gate 2: rederive entitlement, remaining balance and approval from DB.
        if delay > 0 and cause is None:
            return Verdict.escalate('Delayed parcel has no recorded cause')
        rows = ctx.tools.ledger_rows(order_id=order['order_id'])
        if any(r['ticket_id'] == ctx.ticket['ticket_id'] for r in rows):
            return Verdict.deny('This ticket already has a committed refund')
        entitlement = H.entitlement_vnd(policy, order, delay, cause)
        remaining = max(0, entitlement - sum(r['amount_vnd'] for r in rows))
        if remaining == 0:
            return Verdict.deny('No remaining refund entitlement under current policy')
        # Verify the actual approval, rather than the customer text or an index.
        approvals = ctx.tools.lookup_approvals(ticket_id=ctx.ticket['ticket_id'],
                                               order_id=order['order_id'],
                                               customer_id=order['customer_id'])
        approver = (ctx.gates or {}).get('operations', {}).get('approver_id')
        valid = [a for a in approvals if a.get('status') == 'valid'
                 and a.get('expires_at', '') >= ctx.as_of
                 and a.get('max_vnd', 0) >= remaining
                 and a.get('approver_id')
                 and (not approver or a.get('approver_id') == approver)]
        approval = next((a for a in valid if a['approval_id'] == action.get('approval_id')), None)
        if approval is None and valid:
            approval = valid[0]
        if action.get('approval_id') and approval is None:
            return Verdict.escalate('Approval is invalid, expired or outside ticket scope')
        if remaining > policy['auto_limit_vnd'] and approval is None:
            return Verdict.escalate('Amount exceeds automatic limit without valid approval')
        if approval is None:
            customer_total = sum(r['amount_vnd'] for r in ctx.tools.ledger_rows(customer_id=order['customer_id'])
                                 if not r.get('approval_id'))
            if customer_total + remaining > limits['max_auto_refund_per_customer_per_day_vnd']:
                return Verdict.escalate('Customer automatic refund cap requires human review')
            cap = (ctx.gates or {}).get('business', {}).get('daily_refund_cap_vnd')
            cap = min(limits['daily_auto_refund_budget_vnd'], cap) if cap is not None else limits['daily_auto_refund_budget_vnd']
            if ctx.tools.auto_refund_today_vnd() + remaining > cap:
                return Verdict.escalate('Daily automatic refund budget requires human review')
        if H.carrier_at_fault(policy, parcel, delay):
            faults = ctx.tools.fault_rows(carrier_id=parcel['carrier_id'])
            if len(faults) >= limits['max_auto_strikes_per_carrier_per_day']:
                return Verdict.escalate('Carrier daily strike limit requires review before writes')
        changes = {'amount_vnd': remaining, 'payer': 'LOGIX',
                   'approval_id': approval['approval_id'] if approval else None, 'basis': 'policy'}
        if any(action.get(k) != v for k, v in changes.items()):
            return Verdict.modify('Refund reconciled to current policy and ledger', **changes)
        return Verdict.allow()

    # Gate 3: recorded responsibility and minimal, structured third-party data.
    if tool == 'file_carrier_fault':
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny('No recorded carrier responsibility under current policy')
        if ctx.tools.fault_rows(ticket_id=ctx.ticket['ticket_id'], parcel_id=parcel['parcel_id']):
            return Verdict.deny('Carrier fault for this ticket and parcel already recorded')
        if len(ctx.tools.fault_rows(carrier_id=parcel['carrier_id'])) >= limits['max_auto_strikes_per_carrier_per_day']:
            return Verdict.deny('Carrier strike limit reached; manual review required')
        changes = {'parcel_id': parcel['parcel_id'], 'carrier_id': parcel['carrier_id'],
                   'driver_id': parcel.get('driver_id'), 'delay_days': delay}
        if any(action.get(k) != v for k, v in changes.items()):
            return Verdict.modify('Carrier fault reconciled to the actual parcel tracking', **changes)
        return Verdict.allow()
    if tool == 'notify_carrier':
        faults = ctx.tools.fault_rows(ticket_id=ctx.ticket['ticket_id'], parcel_id=parcel['parcel_id'],
                                      carrier_id=parcel['carrier_id'])
        if not faults or not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny('No verified fault record for carrier notification')
        safe = {'order_id': order['order_id'], 'parcel_id': parcel['parcel_id'],
                'district': order.get('recipient', {}).get('district'), 'delay_days': delay}
        allowed = set(policy.get('carrier_notice_fields', []))
        safe = {k: v for k, v in safe.items() if k in allowed}
        return Verdict.modify('Carrier receives only policy-approved structured facts',
                              carrier_id=parcel['carrier_id'], payload=safe)
    return Verdict.deny('Unknown write tool')
