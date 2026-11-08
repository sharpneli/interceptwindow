"""Propagate catalogue bodies on fixed Kepler rails and compare with JPL Horizons (2030-01-01 TDB)."""
import csv, os, math
rows = {r['id']: r for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bodies.csv'), encoding='utf-8'))}
def pos(r, jd):
    a=float(r['a_km']); e=float(r['e']); i=math.radians(float(r['i_deg']))
    dt=jd-float(r['epoch_jd_tdb'])
    O=math.radians(float(r['node_deg'])+float(r['node_rate_deg_day'] or 0)*dt)
    w=math.radians(float(r['argp_deg'])+float(r['argp_rate_deg_day'] or 0)*dt)
    M=math.radians(float(r['mean_anomaly_deg'])+float(r['mean_motion_deg_day'])*dt)
    E=M
    for _ in range(50): E=E-(E-e*math.sin(E)-M)/(1-e*math.cos(E))
    x=a*(math.cos(E)-e); y=a*math.sqrt(1-e*e)*math.sin(E)
    cO,sO,cw,sw,ci,si=math.cos(O),math.sin(O),math.cos(w),math.sin(w),math.cos(i),math.sin(i)
    return [ (cO*cw-sO*sw*ci)*x+(-cO*sw-sO*cw*ci)*y,
             (sO*cw+cO*sw*ci)*x+(-sO*sw+cO*cw*ci)*y,
             (sw*si)*x+(cw*si)*y ]
truth = {  # Horizons VECTORS, ecliptic J2000, km, 2462502.5
 'earth':(-2.601082351081690E+07,1.447862966155714E+08,-9.718194760441780E+03),
 'mars':(1.912791417331397E+08,-7.798058850782205E+07,-6.323760608081851E+06),
 'jupiter':(-6.010760440796928E+08,-5.443627842805721E+08,1.571096932979363E+07),
 'neptune':(4.399119171212728E+09,7.631870158310293E+08,-1.171074622258869E+08),
 '1-ceres':(4.227234369186072E+08,-1.158180297181367E+08,-8.152202337929752E+07),
 '433-eros':(-1.599192080307115E+08,-1.349357915448751E+08,-3.980479798138122E+07),
 '99942-apophis':(3.635520569562901E+06,1.957816850431222E+08,-6.904107933998272E+06),
 '617-patroclus':(-8.062003988851614E+08,2.162174193048385E+08,2.910273802499561E+08),
 'moon':(-1.930715952026768E+05,-3.088137693432682E+05,-1.530692750991951E+04),
 'io':(-8.958023858966297E+03,-4.201431207556154E+05,-1.499569936235636E+04),
 'titan':(-1.141084518586077E+06,-4.002549740379473E+05,3.197260580005819E+05),
 'triton':(1.661760696065918E+05,-1.499993280599275E+05,-2.752609431814979E+05),
 'himalia':(1.038655145400021E+07,-1.492530583884852E+06,-3.825819803930584E+06),
}
print(f"{'body':16}{'epoch':>12}{'yrs':>7}{'err km':>14}{'err/dist':>10}{'angle deg':>10}")
for k,t in truth.items():
    r=rows[k]; p=pos(r,2462502.5)
    err=math.dist(p,t); d=math.hypot(*t)
    ang=math.degrees(math.acos(max(-1,min(1,sum(a*b for a,b in zip(p,t))/(math.hypot(*p)*d)))))
    yrs=(2462502.5-float(r['epoch_jd_tdb']))/365.25
    print(f"{k:16}{float(r['epoch_jd_tdb']):12.1f}{yrs:7.1f}{err:14.0f}{err/d:10.4f}{ang:10.2f}")
