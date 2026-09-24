from __future__ import annotations
import csv, pathlib, sys
import numpy as np
from scipy.optimize import minimize_scalar, root_scalar
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from core_model import Params, national_welfare, government_A_payoff, profile, market_surplus_closed

FIG = ROOT/'figures'; TAB = ROOT/'tables'
FIG.mkdir(exist_ok=True); TAB.mkdir(exist_ok=True)

def best_response(aB, par):
    res = minimize_scalar(lambda x: -government_A_payoff(float(x), float(aB), par),
                          bounds=(0, par.abar), method='bounded', options={'xatol':1e-12})
    if not res.success:
        raise RuntimeError('best-response solve failed')
    return float(res.x)

def local_eq(par):
    xs=np.linspace(0,par.abar,161)
    gaps=[best_response(float(x),par)-float(x) for x in xs]
    for lo,hi,glo,ghi in zip(xs[:-1],xs[1:],gaps[:-1],gaps[1:]):
        if abs(glo) < 1e-10:
            return float(lo)
        if glo*ghi < 0:
            r=root_scalar(lambda z: best_response(float(z),par)-float(z), bracket=(float(lo),float(hi)), xtol=1e-11)
            if r.converged:
                return float(r.root)
    a=0.0
    for _ in range(200):
        na=best_response(a,par)
        if abs(na-a)<1e-10: return na
        a=na
    return a

def planner_sym(par):
    res=minimize_scalar(lambda a:-national_welfare(float(a),float(a),par),
                        bounds=(0,par.abar), method='bounded', options={'xatol':1e-12})
    if not res.success:
        raise RuntimeError('planner solve failed')
    return float(res.x)

rows=[]
for g in np.linspace(0.44,0.54,101):
    par=Params(gamma=float(g)); par.validate()
    rows.append((g,local_eq(par),planner_sym(par)))
with open(TAB/'policy_regime.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['gamma','a_LG','a_SP_symmetric']); w.writerows(rows)

arr=np.asarray(rows)
fig,ax=plt.subplots(figsize=(6.5,4.0))
ax.plot(arr[:,0],arr[:,1],label='Decentralized local governments')
ax.plot(arr[:,0],arr[:,2],label='Coordinated planner')
ax.axvline(0.474589333418,linestyle='--',linewidth=0.9)
ax.axvline(0.498291221704,linestyle='--',linewidth=0.9)
ax.set_xlabel(r'Product substitutability $\gamma$')
ax.set_ylabel(r'Public protection $a$')
ax.legend(frameon=False)
ax.set_xlim(0.44,0.54)
ax.set_ylim(bottom=0)
fig.tight_layout()
fig.savefig(FIG/'policy_regime.pdf',bbox_inches='tight')
fig.savefig(FIG/'policy_regime.eps',format='eps',bbox_inches='tight')
plt.close(fig)

par=Params(gamma=12/25)
AA=profile(0,0,'A','A',par); AB=profile(0,0,'A','B',par)
def fixed_r_welfare(a):
    q=par.q0-a
    Saa=market_surplus_closed(q,q,q,AA['r1'],AA['r2'],par)
    Sab=market_surplus_closed(q,q,q*q,AB['r1'],AB['r2'],par)
    return 0.5*Saa+0.5*Sab+2*par.b-par.c*a*a
h=1e-7
direct=(fixed_r_welfare(h)-fixed_r_welfare(0))/h
total=(national_welfare(h,h,par)-national_welfare(0,0,par))/h
indirect=total-direct
local=(government_A_payoff(h,0,par)-government_A_payoff(0,0,par))/h
with open(TAB/'channel_decomposition.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['object','value'])
    w.writerow(['direct_public_protection_effect_holding_redundancy_fixed',direct])
    w.writerow(['endogenous_redundancy_response_effect',indirect])
    w.writerow(['total_coordinated_marginal_effect',total])
    w.writerow(['local_government_unilateral_marginal_payoff',local])
with open(TAB/'channel_decomposition.tex','w') as f:
    f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
'''%(direct,indirect,total,local))
print('generated figure/table objects')
