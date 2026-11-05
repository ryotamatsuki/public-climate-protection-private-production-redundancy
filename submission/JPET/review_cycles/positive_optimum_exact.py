"""Independent exact symbolic and Bernstein audit for JPET positive-optimum extension.
No calls to the paper's production model, certificates, or proof pipeline.
"""
from __future__ import annotations
from math import comb
import sympy as S

q0, k, H, b, c, mu, a, d = S.symbols('q0 k H b c mu a d')
Q = S.Rational
qA, qB = q0-a, q0-d
f = lambda q: (1-q)/4 + q**2/(32*k)
t = lambda q: 3*(1-q)/8 + q**2/(16*k)
p = Q(1,2) + (f(qA)-f(qB))/(2*H)
market = 2*(p*t(qA)+(1-p)*t(qB))
planner = market + 2*b - c*(a*a+d*d)/2 + mu*(a+d)
local_A = market/2 + 2*b*p -c*a*a/2+mu*a
parameters = {q0:Q(3,10),k:Q(2,25),H:Q(1,100),b:Q(11,200),c:10}
L=Q(2,25)
def same(lhs,rhs):
    assert S.cancel(lhs-rhs)==0, (lhs,rhs)

def bernstein_bounds(poly):
    P=S.Poly(S.expand(poly.subs(parameters).subs({a:a*L,d:d*L})),a,d)
    m,n=P.degree(a),P.degree(d)
    values=[]
    for i in range(m+1):
        for j in range(n+1):
            coeff=sum(P.coeff_monomial(a**u*d**v)*Q(comb(i,u),comb(m,u))*Q(comb(j,v),comb(n,v)) for u in range(i+1) for v in range(j+1))
            values.append(S.cancel(coeff))
    return min(values),max(values)

assert f(q0).free_symbols == {q0,k}
same(S.diff(planner,a).subs(parameters).subs(d,a),mu-Q(3,32)-Q(135,16)*a)
same(S.diff(local_A,a).subs(parameters).subs(d,a),mu+Q(5,128)-Q(315,64)*a)
same(S.diff(planner,a).subs(parameters).subs({a:0,d:0,mu:0})*2,-Q(3,16))
same(S.diff(local_A,a).subs(parameters).subs({a:0,d:0,mu:0}),Q(5,128))
Waa=S.diff(planner,a,a);Wdd=S.diff(planner,d,d);Wad=S.diff(planner,a,d)
GAaa=S.diff(local_A,a,a)
assert bernstein_bounds(Waa)==(-Q(2485,256),-Q(1885,256))
assert bernstein_bounds(Wdd)==(-Q(2485,256),-Q(1885,256))
assert bernstein_bounds(Waa*Wdd-Wad**2)==(Q(128925,2048),Q(2607175,32768))
assert bernstein_bounds(GAaa)==(-Q(2845,512),-Q(2245,512))
ap=(32*mu-3)/270
an=(128*mu+5)/630
same(S.diff(planner,a).subs(parameters).subs({a:ap,d:ap}),0)
same(S.diff(planner,d).subs(parameters).subs({a:ap,d:ap}),0)
same(S.diff(local_A,a).subs(parameters).subs({a:an,d:an}),0)
same(an-ap,2*(40*mu+9)/945)
assert Q(3,32)>0 and Q(227,640)<Q(123,160)
for m in [Q(3,32)+Q(1,100000),Q(1,10),Q(227,640)-Q(1,100000)]:
    assert 0<ap.subs(mu,m)<L and 0<an.subs(mu,m)<L
r_lo=(Q(3,10)-L)/(4*Q(2,25));r_hi=Q(3,10)/(4*Q(2,25))
assert (r_lo,r_hi)==(Q(11,16),Q(15,16))
assert p.subs(parameters).subs({a:0,d:L})==Q(5,16)
assert p.subs(parameters).subs({a:L,d:0})==Q(11,16)
# Explicit primitive band in the no-incremental-rent case.
qbar, kk, hh, bb = S.symbols('qbar kk hh bb', positive=True)
MS=(3*kk-qbar)/(4*kk)
engineering=S.Rational(3,4)*(1-qbar/(4*kk))
response=-qbar/(16*kk)
location=(4*kk-qbar)/(32*hh*kk)
ML=S.cancel(MS/4+2*bb*location)
same(MS, engineering+response)
same(ML,(hh*(3*kk-qbar)+bb*(4*kk-qbar))/(16*hh*kk))
witness_band={qbar:Q(3,10),kk:Q(2,25),hh:Q(1,100),bb:Q(11,200)}
assert 3*Q(2,25)<Q(3,10)<4*Q(2,25)
assert MS.subs(witness_band)<0<ML.subs(witness_band)
assert engineering.subs(witness_band)>0 and response.subs(witness_band)<0

# A positive social optimum with overprovision persists even when hosting
# is zero: this augmented case is a robustness result, not a novelty theorem.
no_host=local_A.subs(b,0).subs({q0:Q(3,10),k:Q(2,25),H:Q(1,100),c:10})
a_nohost=Q(17,2950)
same(S.diff(no_host,a).subs({a:a_nohost,d:a_nohost,mu:Q(1,10)}),0)
assert 0<ap.subs(mu,Q(1,10))<a_nohost<an.subs(mu,Q(1,10))<L
assert bernstein_bounds(GAaa.subs(b,0))==(-Q(5045,512),-Q(4445,512))
print('PASS: independent exact positive-planner-optimum and global Nash concavity audit')
print('W_AA',bernstein_bounds(Waa),'W determinant',bernstein_bounds(Waa*Wdd-Wad**2),'GA_AA',bernstein_bounds(GAaa))
print('mu=1/10 planner=',ap.subs(mu,Q(1,10)),'local=',an.subs(mu,Q(1,10)),'no-hosting-local=',a_nohost)
