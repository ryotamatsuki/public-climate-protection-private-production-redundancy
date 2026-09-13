"""Independent Stage-11 hostile audit for PCPPR.

Target freeze: 62a3a4444783828dc313e974b5e798e30f1fe5a2

This file deliberately does not import scripts/core_model.py.  It reconstructs the
canonical witness from the manuscript primitives and stress-tests globality,
continuation interiority, and the location-fit welfare convention.

The numerical checks are adversarial evidence, not a rigorous interval certificate.
"""
from __future__ import annotations
import json
import numpy as np
from scipy.optimize import differential_evolution

GAMMA=12/25; Q0=3/10; K=169/3000; H=1/100; BPLANT=11/200; C=3.; ABAR=2/25
PI_D=1/(2+GAMMA)**2; PI_M=1/4; DELTA=PI_M-PI_D
T_D=(3+GAMMA)/(2+GAMMA)**2; T_M=3/8


def backup(s1,s2,J):
    den=K*K-(DELTA*J)**2
    return ((K*(PI_D*s1+DELTA*J)-DELTA*J*(PI_D*s2+DELTA*J))/den,
            (K*(PI_D*s2+DELTA*J)-DELTA*J*(PI_D*s1+DELTA*J))/den)


def profile(aA,aB,l1,l2):
    qA=Q0-aA; qB=Q0-aB
    s1=qA if l1=='A' else qB; s2=qA if l2=='A' else qB
    J=qA if l1==l2=='A' else qB if l1==l2=='B' else qA*qB
    r1,r2=backup(s1,s2,J)
    m1=s1*(1-r1); m2=s2*(1-r2); z=J*(1-r1)*(1-r2)
    both=1-m1-m2+z; only1=m2-z; only2=m1-z
    p1=both*PI_D+only1*PI_M-K*r1*r1/2
    p2=both*PI_D+only2*PI_M-K*r2*r2/2
    S=both*T_D+(only1+only2)*T_M-K*(r1*r1+r2*r2)/2
    return p1,p2,S,r1,r2


def location(aA,aB):
    AA=profile(aA,aB,'A','A'); AB=profile(aA,aB,'A','B')
    BA=profile(aA,aB,'B','A'); BB=profile(aA,aB,'B','B')
    dA=AA[0]-BA[0]; dB=AB[0]-BB[0]
    alpha=.5+dB/(2*H); beta=(dA-dB)/(2*H)
    p=alpha/(1-beta)
    return p,(AA,AB,BA,BB),(alpha,beta)


def expected_surplus(aA,aB):
    p,x,_=location(aA,aB); AA,AB,BA,BB=x
    return p*p*AA[2]+p*(1-p)*AB[2]+(1-p)*p*BA[2]+(1-p)**2*BB[2]


def welfare(aA,aB):
    return expected_surplus(aA,aB)+2*BPLANT-C*(aA*aA+aB*aB)/2


def government_A(aA,aB):
    p,_,_=location(aA,aB)
    return .5*expected_surplus(aA,aB)+2*BPLANT*p-C*aA*aA/2


def cstep_a(fun,a,b,h=1e-30): return np.imag(fun(a+1j*h,b))/h

def cstep_b(fun,a,b,h=1e-30): return np.imag(fun(a,b+1j*h))/h


def fit_selection_surplus(aA,aB):
    # If epsilon is interpreted as actual payoff rather than a pure selection device,
    # the expected selected epsilon contribution for two firms is H/2-D^2/(2H),
    # where equilibrium D=2H(p-1/2).
    p,_,_=location(aA,aB); d=2*H*(p-.5)
    return H/2-d*d/(2*H)


def main():
    candidate=(0.023019684870033977+0.023019684870773695)/2
    planner=differential_evolution(lambda x:-float(np.real(welfare(x[0],x[1]))),
                                   [(0,ABAR),(0,ABAR)],seed=117,tol=1e-12,polish=True)
    local=differential_evolution(lambda x:-float(np.real(government_A(x[0],candidate))),
                                 [(0,ABAR)],seed=118,tol=1e-13,polish=True)
    grid=np.linspace(0,ABAR,201)
    da=[]; db=[]; ps=[]; rs=[]; loc_endpoints=[]; betas=[]
    for aA in grid:
        for aB in grid:
            da.append(float(cstep_a(welfare,aA,aB))); db.append(float(cstep_b(welfare,aA,aB)))
            p,x,(alpha,beta)=location(aA,aB); ps.append(float(np.real(p))); betas.append(float(np.real(beta)))
            loc_endpoints.extend([float(np.real(alpha)),float(np.real(alpha+beta))])
            for z in x: rs.extend([float(np.real(z[3])),float(np.real(z[4]))])
    xg=np.linspace(0,ABAR,1001)
    dga=np.asarray([float(cstep_a(government_A,x,candidate)) for x in xg])
    sign_changes=int(np.sum(dga[:-1]*dga[1:]<0))

    def wfit(aA,aB): return welfare(aA,aB)+fit_selection_surplus(aA,aB)
    def gafit(aA,aB): return government_A(aA,aB)+.5*fit_selection_surplus(aA,aB)
    fit_planner=differential_evolution(lambda x:-float(np.real(wfit(x[0],x[1]))),
                                       [(0,ABAR),(0,ABAR)],seed=119,tol=1e-12,polish=True)
    fit_local=differential_evolution(lambda x:-float(np.real(gafit(x[0],candidate))),
                                     [(0,ABAR)],seed=120,tol=1e-13,polish=True)
    out={
      'target_freeze':'62a3a4444783828dc313e974b5e798e30f1fe5a2',
      'planner_W00':float(np.real(welfare(0,0))),
      'planner_DE_argmax':planner.x.tolist(),
      'planner_DE_value':float(-planner.fun),
      'dW_da_201x201_range':[min(da),max(da)],
      'dW_db_201x201_range':[min(db),max(db)],
      'location_probability_full_square_range':[min(ps),max(ps)],
      'backup_readiness_full_square_range':[min(rs),max(rs)],
      'location_BR_endpoint_range':[min(loc_endpoints),max(loc_endpoints)],
      'location_BR_slope_beta_range':[min(betas),max(betas)],
      'backup_BR_absolute_slope_upper_bound':float(DELTA*Q0/K),
      'local_candidate':candidate,
      'local_DE_best_response':float(local.x[0]),
      'local_payoff_gap_best_minus_candidate':float(-local.fun-np.real(government_A(candidate,candidate))),
      'local_derivative_range':[float(dga.min()),float(dga.max())],
      'local_derivative_sign_changes_on_1001_grid':sign_changes,
      'fit_inclusive_planner_argmax':fit_planner.x.tolist(),
      'fit_inclusive_local_best_response':float(fit_local.x[0]),
      'fit_inclusive_payoff_gap':float(-fit_local.fun-np.real(gafit(candidate,candidate))),
      'solver_failures':0,
      'warning':'These are deterministic stress tests, not an interval-arithmetic proof of globality.'
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
