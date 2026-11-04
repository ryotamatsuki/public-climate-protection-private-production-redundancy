"""Independent exact audit: smooth incidence and availability-dependent hosting.

Re-derive the complete gamma=0 private continuation directly from
primitive profit and surplus functions. Do NOT import production certificates.
A finite-parameter exact Bernstein certificate illustrates the analytical
open-set persistence argument in Proposition 'incidence robustness'.
"""
from __future__ import annotations
from math import comb
import sympy as S

Q = S.Rational
x,y,mu,eta,rho = S.symbols("x y mu eta rho")
q0,k,H,b,c,L = Q(3,10), Q(2,25), Q(1,100), Q(11,200), Q(10), Q(2,25)
qA,qB = q0-x, q0-y
r = lambda q: q/(4*k)
f = lambda q: (1-q)/4+q*q/(32*k)
t = lambda q: 3*(1-q)/8+q*q/(16*k)
h = lambda q: (4*k-q)/(16*k)
p = Q(1,2)+(f(qA)-f(qB))/(2*H)
Smarket = 2*(p*t(qA)+(1-p)*t(qB))
# Hosting is linked to whether the original primary plant operates,
# not whether remote backup keeps the firm available elsewhere.
vA = 1-qA
vB = 1-qB
thetaA = Q(1,2)+eta*(p-Q(1,2))
GA = S.expand(thetaA*Smarket+2*b*p*(1-rho+rho*vA)-c*x*x/2+mu*x)
GB = S.expand((1-thetaA)*Smarket+2*b*(1-p)*(1-rho+rho*vB)-c*y*y/2+mu*y)
W = S.expand(GA+GB)
base_W = Smarket+2*b-c*(x*x+y*y)/2+mu*(x+y)
base_GA = Smarket/2+2*b*p-c*x*x/2+mu*x
def same(lhs,rhs):
    assert S.cancel(lhs-rhs)==0, (lhs,rhs)
same(W.subs({eta:0,rho:0}),base_W)
same(GA.subs({eta:0,rho:0}),base_GA)
same(W.subs({rho:0}),base_W)  # incidence redistribution is welfare-neutral
same(GA.subs({eta:0,rho:0}).diff(x),base_GA.diff(x))
same(GA.subs({eta:0,rho:0}).diff(x).subs(y,x),
     (H*(3*k-q0)+b*(4*k-q0))/(16*H*k)+mu-(c-(H+b)/(16*H*k))*x)
s = c-(H+b)/(16*H*k)
same(S.diff(GA,x).subs(y,x),
     (H*(3*k-q0)+b*(4*k-q0))/(16*H*k)+mu-s*x+
     eta*t(q0-x)*h(q0-x)/H+
     S.diff(GA,x).subs({eta:0,rho:rho,y:x})-
     S.diff(GA,x).subs({eta:0,rho:0,y:x}))
an = Q(89,3150)
incidence_slope = S.cancel(t(q0-an)*h(q0-an)/(H*s))
assert incidence_slope == Q(19956004,78764805)
assert incidence_slope > 0

def bernstein_range(expr, parameters):
    expr = S.Poly(S.expand(expr.subs(parameters).subs({x:x*L,y:y*L})),x,y)
    nx,ny=expr.degree(x),expr.degree(y)
    vals=[]
    for i in range(nx+1):
        for j in range(ny+1):
            z = sum(expr.coeff_monomial(x**u*y**v)*
                    Q(comb(i,u),comb(nx,u))*Q(comb(j,v),comb(ny,v))
                    for u in range(i+1) for v in range(j+1))
            vals.append(S.cancel(z))
    return min(vals),max(vals)

parameters={mu:Q(1,10),eta:Q(1,100),rho:Q(1,100)}
Wxx = W.diff(x,2)
Wyy = W.diff(y,2)
Wxy = W.diff(x,y)
Gxx = GA.diff(x,2)
bounds_W = bernstein_range(Wxx,parameters)
bounds_det = bernstein_range(Wxx*Wyy-Wxy**2,parameters)
bounds_local = bernstein_range(Gxx,parameters)
assert bounds_W == (-Q(62103,6400), -Q(47059,6400))
assert bounds_det == (Q(32157,512),Q(1628262121,20480000))
assert bounds_local == (-Q(1691781,327680),-Q(6830383,1638400))
assert bounds_W[1]<0 and bounds_det[0]>0 and bounds_local[1]<0
Fpl=S.diff(W,x).subs(y,x).subs(parameters)
Floc=S.diff(GA,x).subs(y,x).subs(parameters)
def interior_real_root(expr):
    all_roots=S.nroots(expr, maxsteps=200)
    roots=[float(S.re(z)) for z in all_roots if abs(float(S.im(z)))<1e-12
           and 0<float(S.re(z))<float(L)]
    assert len(roots)==1,roots
    return roots[0]
ap=interior_real_root(Fpl)
anew=interior_real_root(Floc)
assert 0<ap<anew<float(L)
# This numerical root check is only an illustration; global proof comes
# from exact Bernstein bounds and algebraic signs / strict concavity.
dFp=float(S.diff(S.diff(W,x).subs(y,x),x).subs(parameters).subs(x,ap))
dFn=float(S.diff(S.diff(GA,x).subs(y,x),x).subs(parameters).subs(x,anew))
assert dFp<0 and dFn<0
# Each FOC has +mu, so da/dmu=-1/F_a.
gap_slope=-1/dFn+1/dFp
assert gap_slope>0
print("PASS exact incidence/hosting surplus conservation and welfare tests")
print("PASS independent full-rectangle Bernstein Hessian certificates")
print("planner",ap,"local",anew,"gap slope",gap_slope)
print("planner Hessian range",bounds_W,"det range",bounds_det,
      "government own curvature range",bounds_local)
print("incidence policy derivative at eta=0",incidence_slope)
