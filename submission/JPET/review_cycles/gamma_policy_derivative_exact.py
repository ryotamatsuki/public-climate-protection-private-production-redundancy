"""Exact first-order gamma comparative statics in full location/backup game.

Independent symbolic derivation from profile-specific state profits, survival
probabilities, Cournot surplus, and endogenous Bayesian location cutoff.
Never imports the repository's production certificate code.
"""
import sympy as S

Q=S.Rational
x,y=S.symbols("x y")
q0,k,H,b,c,mu=Q(3,10),Q(2,25),Q(1,100),Q(11,200),Q(10),Q(1,10)
qA,qB=q0-x,q0-y
f=lambda q:(1-q)/4+q*q/(32*k)
t=lambda q:3*(1-q)/8+q*q/(16*k)
def profile(s1,s2,J):
    ri=s1/(4*k)
    rj=s2/(4*k)
    dri=(-s1+J*(1-rj))/(4*k)
    drj=(-s2+J*(1-ri))/(4*k)
    m1=s1*(1-ri)
    m2=s2*(1-rj)
    z=J*(1-ri)*(1-rj)
    pi0=f(s1)
    dpi=-Q(1,4)*(1-m1)+Q(1,4)*(m2-z)
    S0=t(s1)+t(s2)
    dS=-Q(1,2)+Q(1,2)*(m1+m2-z)+(s1*dri+s2*drj)/8
    return pi0,dpi,S0,dS
AA=profile(qA,qA,qA)
BA=profile(qB,qA,qA*qB)
AB=profile(qA,qB,qA*qB)
BB=profile(qB,qB,qB)
p0=Q(1,2)+(f(qA)-f(qB))/(2*H)
dAp=AA[1]-BA[1]
dBp=AB[1]-BB[1]
pdot=(p0*dAp+(1-p0)*dBp)/(2*H)
Sn0=S.expand(p0*p0*AA[2]+2*p0*(1-p0)*AB[2]+(1-p0)**2*BB[2])
Sn1=S.expand(p0*p0*AA[3]+2*p0*(1-p0)*AB[3]+(1-p0)**2*BB[3]
             +2*pdot*(t(qA)-t(qB)))
assert S.cancel(Sn0-2*(p0*t(qA)+(1-p0)*t(qB)))==0
assert S.cancel(pdot.subs(y,x))==0
Fp=S.factor(S.diff(Sn1,x).subs(y,x))
Fn=S.factor((S.diff(Sn1,x)/2+2*b*S.diff(pdot,x)).subs(y,x))
expectedP=-3*(50000*x**3-62500*x**2+39040*x-4877)/20480
expectedN=(687500000*x**5+316250000*x**4-129450000*x**3
           +7873000*x**2-9964970*x+970381)/655360
assert S.cancel(Fp-expectedP)==0
assert S.cancel(Fn-expectedN)==0
tc=c-1/(8*k)
ss=c-(H+b)/(16*H*k)
ap=Q(1,1350)
an=Q(89,3150)
d_ap=S.factor(Fp.subs(x,ap)/tc)
d_an=S.factor(Fn.subs(x,an)/ss)
d_gap=S.factor(d_an-d_ap)
assert d_ap==Q(29820457,354294000)
assert d_an==Q(3355337640241,15630875552250)
assert d_gap==Q(16317660285149,125047004418000)
assert 0<d_ap<d_an
# Independently differentiate the *original* full gamma-dependent two-firm
# state problem at an exact off-symmetric profile, checking the envelope
# derivatives used above and catching any omitted profit/correlation term.
g=S.symbols("g")
piD=1/(2+g)**2
delta=g*(g+4)/(4*(2+g)**2)
TD=(3+g)/(2+g)**2
TM=Q(3,8)
s1,s2,J=S.symbols("s1 s2 J")
ri=(k*(piD*s1+delta*J)-delta*J*(piD*s2+delta*J))/(k*k-(delta*J)**2)
rj=(k*(piD*s2+delta*J)-delta*J*(piD*s1+delta*J))/(k*k-(delta*J)**2)
profit=piD-piD*s1*(1-ri)+delta*s2*(1-rj)-delta*J*(1-ri)*(1-rj)-k*ri**2/2
market=TD+(TM-TD)*(s1*(1-ri)+s2*(1-rj))+(TD-2*TM)*J*(1-ri)*(1-rj)-k*(ri**2+rj**2)/2
z={s1:Q(29,100),s2:Q(6,25),J:Q(29,100)*Q(6,25)}
assert S.simplify(S.diff(profit,g).subs(g,0).subs(z)-profile(s1,s2,J)[1].subs(z))==0
assert S.simplify(S.diff(market,g).subs(g,0).subs(z)-profile(s1,s2,J)[3].subs(z))==0
print("PASS: independent Cournot-state, readiness, and Bayesian-cutoff gamma derivative")
print("planner derivative",d_ap,"local derivative",d_an,"positive gap derivative",d_gap)
