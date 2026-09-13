import json, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize, minimize_scalar, root_scalar
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from core_model import Params, national_welfare, government_A_payoff, location_probability

par=Params(); par.validate()
W00=national_welfare(0.0,0.0,par)
# 2D planner audit: grid plus multistart continuous optimization.
grid=np.linspace(0,par.abar,81)
max_grid=(-1e99,None)
failures=0
for aA in grid:
    for aB in grid:
        try:
            w=national_welfare(float(aA),float(aB),par)
            if w>max_grid[0]: max_grid=(w,(float(aA),float(aB)))
        except Exception:
            failures+=1
assert failures==0
assert max_grid[1]==(0.0,0.0)

starts=[(0,0),(par.abar,0),(0,par.abar),(par.abar,par.abar),(par.abar/2,par.abar/2),(par.abar/4,3*par.abar/4)]
opts=[]
for x0 in starts:
    res=minimize(lambda x:-national_welfare(float(x[0]),float(x[1]),par),x0=np.array(x0,dtype=float),
                 bounds=[(0,par.abar),(0,par.abar)],method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-14,'maxiter':5000})
    assert res.success
    opts.append((res.x.tolist(),-res.fun))
assert max(v for _,v in opts) <= W00+1e-10

# Symmetric local-government equilibrium as fixed point of global best response.
def br(aB):
    res=minimize_scalar(lambda x:-government_A_payoff(float(x),float(aB),par),bounds=(0,par.abar),method='bounded',
                        options={'xatol':1e-13,'maxiter':1000})
    if not res.success: raise RuntimeError('best-response optimization failed')
    return float(res.x),float(-res.fun)

def gap(a): return br(a)[0]-a
root=root_scalar(gap,bracket=(0.023,0.024),xtol=1e-12)
assert root.converged
aeq=float(root.root)
br_eq,_=br(aeq)
assert abs(br_eq-aeq)<2e-7

# Direct finite global-deviation grid at the equilibrium rival action.
eq_pay=government_A_payoff(aeq,aeq,par)
dev_grid=np.linspace(0,par.abar,2001)
dev_pays=[]
for x in dev_grid:
    dev_pays.append(government_A_payoff(float(x),aeq,par))
assert max(dev_pays) <= eq_pay+2e-7

# Continuation interiority ledger on all material deviations.
min_p,max_p=1.0,0.0; min_r,max_r=1.0,0.0
for x in dev_grid:
    p,profiles=location_probability(float(x),aeq,par)
    min_p=min(min_p,p); max_p=max(max_p,p)
    for pr in profiles.values():
        min_r=min(min_r,pr['r1'],pr['r2']); max_r=max(max_r,pr['r1'],pr['r2'])
assert 0<min_p<=max_p<1 and 0<min_r<=max_r<1

out={'planner_W00':W00,'planner_grid_max':max_grid,'planner_multistart':opts,'a_LG':aeq,
     'government_deviation_max_gap':max(dev_pays)-eq_pay,'location_p_range':[min_p,max_p],
     'backup_r_range':[min_r,max_r],'unresolved':0,'numerical_failures':0}
print(json.dumps(out,indent=2))
print('PASS numerical/global-deviation audit')
