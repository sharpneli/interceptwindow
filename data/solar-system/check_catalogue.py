import csv, os, math, sys
from collections import Counter
rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bodies.csv'), encoding='utf-8')))
ids = [r['id'] for r in rows]
dup = [k for k, v in Counter(ids).items() if v > 1]
byid = {r['id']: r for r in rows}
errs = []
if dup: errs.append(f'duplicate ids {dup}')
need = ['a_km','e','i_deg','node_deg','argp_deg','mean_anomaly_deg','mean_motion_deg_day','mass_kg','radius_km','gm_km3_s2','epoch_jd_tdb']
for r in rows:
    if r['id'] == 'sun': continue
    for c in need:
        if r[c] == '': errs.append(f"{r['id']} missing {c}")
    if r['parent'] not in byid: errs.append(f"{r['id']} parent {r['parent']} missing")
    if float(r['e']) >= 1: errs.append(f"{r['id']} e>=1")
    if not (0 <= float(r['i_deg']) <= 180): errs.append(f"{r['id']} bad i")
# moons: period vs Kepler with parent GM, and inside parent's Hill sphere
G=6.6743e-20; GMS=1.32712440041279e11; AU=149597870.7
worst=[]
for r in rows:
    if r['category']!='moon': continue
    p=byid[r['parent']]; gm=float(p['gm_km3_s2'])+float(r['gm_km3_s2'])
    a=float(r['a_km']); P=2*math.pi*math.sqrt(a**3/gm)/86400
    ratio=P/float(r['period_days']); worst.append((abs(ratio-1),r['id'],ratio))
    rh=float(p['a_km'])*(1-float(p['e']))*(float(p['gm_km3_s2'])/(3*GMS))**(1/3)
    if a*(1+float(r['e']))>rh: errs.append(f"{r['id']} apoapsis outside parent Hill sphere")
worst.sort(reverse=True)
print('bodies', len(rows)); print(Counter(r['category'] for r in rows))
print('moon period vs Kepler, worst 5:', [(i, round(x,3)) for _,i,x in worst[:5]])
print('groups:', Counter(r['group'] for r in rows if r['category'] in ('jupiter_trojan','mars_trojan','neptune_trojan')))
print('mass basis:', Counter(r['mass_basis'].split(' (')[0] for r in rows))
print('radius basis:', Counter(r['radius_basis'].split(' (')[0].split(' with')[0] for r in rows))
print('ERRORS' if errs else 'no structural errors', errs[:20])
