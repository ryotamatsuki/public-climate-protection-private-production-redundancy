#!/usr/bin/env python3
from __future__ import annotations
import json, math, pathlib, sys
import numpy as np
from scipy.optimize import minimize, minimize_scalar, brentq

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from core_model import Params, primitives

par=Params(); par.validate()
EXPECTED=json.loads((ROOT/"docs/v2_4_portability_results.json").read_text())

def backup_equilibrium(s1,s2,J):
    pi_d,_,delta,_,_=primitives(par)
    den=par.k**2-(delta*J)**2
    if den<=0: raise ValueError("backup system nonregular")
    r1=(par.k*(pi_d*s1+delta*J)-delta*J*(pi_d*s2+delta*J))/den
    r2=(par.k*(pi_d*s2+delta*J)-delta*J*(pi_d*s1+delta*J))/den
    if not (0<r1<1 and 0<r2<1): raise ValueError("backup outside interior")
    return r1,r2

def profit(si,sj,J,ri,rj):
    pi_d,_,delta,_,_=primitives(par)
    return pi_d-pi_d*si*(1-ri)+delta*sj*(1-rj)-delta*J*(1-ri)*(1-rj)-par.k*ri**2/2

def surplus(s1,s2,J,r1,r2):
    _,_,_,td,tm=primitives(par)
    m1=s1*(1-r1); m2=s2*(1-r2); z=J*(1-r1)*(1-r2)
    return td+(tm-td)*(m1+m2)+(td-2*tm)*z-par.k*(r1*r1+r2*r2)/2

def q_linear(a): return par.q0-a
def q_nonlinear(a): return par.q0*math.exp(-a/par.q0)

def profile_set(aA,aB,qfun):
    qA,qB=qfun(aA),qfun(aB)
    out={}
    for l1,l2 in (("A","A"),("A","B"),("B","A"),("B","B")):
        s1=qA if l1=="A" else qB
        s2=qA if l2=="A" else qB
        J=qA if l1==l2=="A" else qB if l1==l2=="B" else qA*qB
        r1,r2=backup_equilibrium(s1,s2,J)
        out[l1+l2]={
            "r1":r1,"r2":r2,
            "profit1":profit(s1,s2,J,r1,r2),
            "surplus":surplus(s1,s2,J,r1,r2),
        }
    return out

def location_uniform(aA,aB,qfun):
    pr=profile_set(aA,aB,qfun)
    dA=pr["AA"]["profit1"]-pr["BA"]["profit1"]
    dB=pr["AB"]["profit1"]-pr["BB"]["profit1"]
    den=2*par.H-dA+dB
    if abs(den)<1e-14: raise ValueError("uniform location singular")
    p=(par.H+dB)/den
    contraction=abs(dA-dB)/(2*par.H)
    if not (0<p<1 and contraction<1): raise ValueError("uniform location invalid")
    return p,pr,contraction

def logistic(x):
    if x>=0:
        z=math.exp(-x); return 1/(1+z)
    z=math.exp(x); return z/(1+z)

def location_logistic(aA,aB,qfun):
    pr=profile_set(aA,aB,qfun)
    dA=pr["AA"]["profit1"]-pr["BA"]["profit1"]
    dB=pr["AB"]["profit1"]-pr["BB"]["profit1"]
    sL=par.H/2
    contraction=abs(dA-dB)/(4*sL)
    if contraction>=1: raise ValueError("logistic location not contraction-certified")
    def gap(p):
        D=p*dA+(1-p)*dB
        return logistic(D/sL)-p
    p=brentq(gap,0.0,1.0,xtol=1e-14)
    if not 0<p<1: raise ValueError("logistic root not interior")
    return p,pr,contraction

def expected_surplus(aA,aB,locfun,qfun):
    p,pr,contraction=locfun(aA,aB,qfun)
    S=p*p*pr["AA"]["surplus"]+p*(1-p)*pr["AB"]["surplus"]+(1-p)*p*pr["BA"]["surplus"]+(1-p)**2*pr["BB"]["surplus"]
    return S,p,pr,contraction

def W(aA,aB,locfun,qfun):
    S,_,_,_=expected_surplus(aA,aB,locfun,qfun)
    return S+2*par.b-par.c*(aA*aA+aB*aB)/2

def G(aA,aB,locfun,qfun):
    S,p,_,_=expected_surplus(aA,aB,locfun,qfun)
    return S/2+2*par.b*p-par.c*aA*aA/2

def diagnose(locfun,qfun):
    grid=np.linspace(0,par.abar,41)
    best=(-1e99,None); minp=1.0; maxp=0.0; minr=1.0; maxr=0.0; maxc=0.0
    failures=0
    for aA in grid:
        for aB in grid:
            try:
                S,p,prs,contr=expected_surplus(float(aA),float(aB),locfun,qfun)
                minp=min(minp,p); maxp=max(maxp,p); maxc=max(maxc,contr)
                for v in prs.values():
                    minr=min(minr,v["r1"],v["r2"]); maxr=max(maxr,v["r1"],v["r2"])
                w=S+2*par.b-par.c*(aA*aA+aB*aB)/2
                if w>best[0]: best=(w,(float(aA),float(aB)))
            except Exception:
                failures+=1
    assert failures==0
    W00=W(0.0,0.0,locfun,qfun)
    assert best[1]==(0.0,0.0)
    starts=[(0,0),(par.abar,0),(0,par.abar),(par.abar,par.abar),(par.abar/2,par.abar/2),(par.abar/4,3*par.abar/4)]
    optpol=[]
    for x0 in starts:
        z=minimize(lambda x:-W(float(x[0]),float(x[1]),locfun,qfun),np.array(x0,dtype=float),
                   bounds=[(0,par.abar),(0,par.abar)],method="Nelder-Mead",
                   options={"xatol":1e-12,"fatol":1e-14,"maxiter":5000})
        assert z.success and -z.fun<=W00+1e-10
        optpol.append([float(z.x[0]),float(z.x[1])])
    def br(aB):
        z=minimize_scalar(lambda x:-G(float(x),float(aB),locfun,qfun),
                          bounds=(0,par.abar),method="bounded",
                          options={"xatol":1e-13,"maxiter":1000})
        assert z.success
        return float(z.x)
    scan=np.linspace(0,par.abar,401)
    gaps=[br(float(a))-float(a) for a in scan]
    roots=[]
    for i in range(len(scan)-1):
        if gaps[i]*gaps[i+1]<0:
            x=brentq(lambda a:br(a)-a,float(scan[i]),float(scan[i+1]),xtol=1e-12)
            if not roots or abs(x-roots[-1])>1e-7: roots.append(float(x))
    assert len(roots)==1 and 0<roots[0]<par.abar
    aeq=roots[0]
    eq=G(aeq,aeq,locfun,qfun)
    dev=np.linspace(0,par.abar,2001)
    devgap=max(G(float(x),aeq,locfun,qfun) for x in dev)-eq
    assert devgap<=2e-7
    h=1e-6
    MS=(W(h,h,locfun,qfun)-W(0,0,locfun,qfun))/h
    ML=(G(h,0,locfun,qfun)-G(0,0,locfun,qfun))/h
    assert MS<0<ML
    return {
      "planner_grid_max_policy":[best[1][0],best[1][1]],
      "planner_W00":W00,
      "planner_multistart_policies":optpol,
      "continuation_failures":failures,
      "location_probability_range":[minp,maxp],
      "backup_readiness_range":[minr,maxr],
      "max_location_contraction_bound":maxc,
      "symmetric_local_equilibria":roots,
      "max_unilateral_deviation_gain_grid":devgap,
      "origin_MS_forward_diff":MS,
      "origin_ML_forward_diff":ML,
    }

def close(a,b,tol=5e-8):
    if isinstance(a,list):
        return len(a)==len(b) and all(close(x,y,tol) for x,y in zip(a,b))
    return abs(float(a)-float(b))<=tol

results={
  "alternative_A_nonlinear_risk":diagnose(location_uniform,q_nonlinear),
  "alternative_B_logistic_location":diagnose(location_logistic,q_linear),
}
for alt,vals in results.items():
    exp=EXPECTED[alt]
    for key in ("planner_W00","max_location_contraction_bound","origin_MS_forward_diff","origin_ML_forward_diff"):
        assert close(vals[key],exp[key]), (alt,key,vals[key],exp[key])
    assert close(vals["symmetric_local_equilibria"],exp["symmetric_local_equilibria"],2e-7)
    assert vals["planner_grid_max_policy"]==[0.0,0.0]
    assert vals["continuation_failures"]==0

print(json.dumps(results,indent=2,sort_keys=True))
print("PASS v2.4 pre-specified portability diagnostics")
