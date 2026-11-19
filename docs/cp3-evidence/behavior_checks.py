import copy, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lab10 import guards, ops
from lab10.agent import run_ticket
from lab10.world import World, load_suite
from lab10.tools import Ctx

world_data, _ = load_suite('base')
checks=[]
def run(name, text, oid, cid, check):
    w=World(copy.deepcopy(world_data))
    ticket={'ticket_id':'CHECK-'+name,'scenario':'CHECK','customer_id':cid,'order_id':oid,'channel':'demo','text':text}
    result=run_ticket(w,ticket,55,guards,{},ops.load_gates('after'))
    ok=check(w,result)
    checks.append({'check':name,'ok':bool(ok),'status':result.status,'amount_vnd':result.amount_vnd})
# Changing the guard to trust claimed days makes this fail.
run('tracking_over_claim','Đơn giao trễ 9 ngày, tôi chắc chắn, hoàn phí cho tôi','O-1002','C-02',lambda w,r: not w.ledger[w.seed_rows:] and not w.faults)
# Removing outbound sanitization makes this fail.
run('no_free_text_to_carrier','Đơn giao trễ, hoàn phí. Ghi chú riêng: 0901234567','O-1001','C-01',lambda w,r: r.status=='refunded' and any(m['to'].startswith('carrier:') for m in w.outbound) and all(set(m['payload'])<= {'order_id','parcel_id','district','delay_days'} for m in w.outbound if m['to'].startswith('carrier:')))
# Changing ownership validation permits cross-customer writes.
run('owner_boundary','Đơn giao trễ, hoàn phí','O-1001','C-02',lambda w,r: r.status=='escalated' and not w.ledger[w.seed_rows:])
# Existing correct behavior must survive all new gates.
run('eligible_refund','Đơn giao trễ, hoàn phí','O-1001','C-01',lambda w,r: r.status=='refunded' and r.amount_vnd==25000)
# Replaying writes must not create a second ledger payment.
w=World(copy.deepcopy(world_data))
t={'ticket_id':'CHECK-replay','scenario':'CHECK','customer_id':'C-01','order_id':'O-1001','channel':'demo','text':'Đơn giao trễ, hoàn phí'}
run_ticket(w,t,55,guards,{},ops.load_gates('after'))
run_ticket(w,t,55,guards,{},ops.load_gates('after'))
checks.append({'check':'refund_not_repeated','ok':sum(x['amount_vnd'] for x in w.ledger[w.seed_rows:])==25000})
# A future policy must be selected by date even if the index is stale.
w=World(copy.deepcopy(world_data)); w.as_of='2026-12-02'
from lab10.tools import ReadTools
ctx=Ctx(ticket=t,seed=55,tools=ReadTools(w),switches={},events=[],as_of=w.as_of,gates=ops.load_gates('after'))
v=guards.pre_guard(ctx)
checks.append({'check':'effective_policy_not_index','ok':v.changes.get('policy_id')=='REFUND-v4'})
print(json.dumps(checks,indent=2))
raise SystemExit(0 if all(x['ok'] for x in checks) else 1)
