"""Exact mechanism benchmark and explicitly limited continuation recoveries."""
from __future__ import annotations
import json
from math import comb
from pathlib import Path
import sympy as sp
from core_model import Params, profile, primitives, location_probability

ROOT = Path(__file__).resolve().parents[1]
R = sp.Rational


def polynomial_bounds(expr, x, y, rectangle):
    t, u = sp.symbols('t u')
    lo, hi, low, high = rectangle
    poly = sp.Poly(sp.expand(expr.subs({x:lo+(hi-lo)*t, y:low+(high-low)*u},
                                     simultaneous=True)), t, u, domain=sp.QQ)
    nx, ny = poly.degree(t), poly.degree(u)
    coefficients = [sum(poly.nth(i,j)*R(comb(I,i),comb(nx,i))*R(comb(J,j),comb(ny,j))
                        for i in range(I+1) for j in range(J+1))
                    for I in range(nx+1) for J in range(ny+1)]
    return min(coefficients), max(coefficients)


def zero_delta_benchmark():
    x, y, a = sp.symbols('x y a')
    q0, k, H, b, c, abar = R(3,10), R(2,25), R(1,100), R(11,200), R(10), R(2,25)
    def f(q): return (1-q)/4+q*q/(32*k)
    def t(q): return R(3,8)*(1-q)+q*q/(16*k)
    qa, qb = q0-x, q0-y
    p = R(1,2)+(f(qa)-f(qb))/(2*H)
    S = 2*(p*t(qa)+(1-p)*t(qb))
    W = S+2*b-c*(x*x+y*y)/2
    GA = S/2+2*b*p-c*x*x/2
    foc = sp.expand(sp.diff(GA,x).subs({x:a,y:a}))
    alpha = R(1,126)
    assert foc == R(5,128)-R(315,64)*a
    assert foc.subs(a,alpha) == 0 and 0 < alpha < abar
    ms = sp.diff(W.subs({x:a,y:a}),a).subs(a,0)
    ml = sp.diff(GA,x).subs({x:0,y:0})
    assert ms == -R(3,16) and ml == R(5,128)
    full = (0,abar,0,abar)
    objects = {'p': (p,full,1), '1-p': (1-p,full,1),
               'W_A': (sp.diff(W,x),full,-1), 'W_B': (sp.diff(W,y),full,-1),
               'G_A_AA': (sp.diff(GA,x,2),(0,abar,alpha,alpha),-1)}
    certificates = {}
    for name,(expr,rect,sign) in objects.items():
        lo,hi = polynomial_bounds(expr,x,y,rect)
        assert lo > 0 if sign == 1 else hi < 0
        certificates[name] = {'lower':str(lo),'upper':str(hi),'sign':sign}
    assert 0 < (q0-abar)/(4*k) < q0/(4*k) < 1
    return {'parameters': {'gamma':'0','q0':str(q0),'k':str(k),'H':str(H),
                           'b':str(b),'c':str(c),'abar':str(abar)},
            'MS':str(ms),'ML':str(ml),'diagonal_FOC':str(foc),'alpha':str(alpha),
            'readiness_range':[str((q0-abar)/(4*k)),str(q0/(4*k))],
            'certificates':certificates,
            'scope':'global witness with Delta=0; own-product monopoly pricing remains'}


def main():
    # These recover continuations only. They do not solve restricted policy games.
    par = Params()
    pd,pm,delta,_,_ = primitives(par)
    q = par.q0
    rc,rd = q*pm/(par.k+q*delta), q*(pd+q*delta)/(par.k+q*q*delta)
    assert abs(profile(0,0,'A','A',par)['r1']-rc) < 1e-12
    assert abs(profile(0,0,'A','B',par)['r1']-rd) < 1e-12
    assert rc > rd and abs(location_probability(0,0,par)[0]-.5) < 1e-14
    result = zero_delta_benchmark()
    out = ROOT/'docs'/'mechanism_benchmark.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    print('exact Delta=0 global ranking verified; restricted policy games are not claimed solved')


if __name__ == '__main__':
    main()
