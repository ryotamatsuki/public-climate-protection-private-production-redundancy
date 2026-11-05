"""Independent exact audit of the JPET analytical sufficient-condition theorem.

No imports from original production/certificate modules.
Proves symbolic policy identities and checks rational witness with strict bounds.
Positive-gamma persistence is an analytic continuity argument, not a numerical certificate.
"""
from __future__ import annotations
import sympy as sp
Q=sp.Rational
q0,k,H,b,c,L,x,y,mu=sp.symbols("q0 k H b c L x y mu",positive=True)
qA,qB=q0-x,q0-y
f=lambda q:(1-q)/4+q*q/(32*k)
t=lambda q:3*(1-q)/8+q*q/(16*k)
p=Q(1,2)+(f(qA)-f(qB))/(2*H)
S=2*(p*t(qA)+(1-p)*t(qB))
W=S+2*b-c*(x*x+y*y)/2
GA=S/2+2*b*p-c*x*x/2
q=q0-(x+y)/2
d=x-y
U=lambda v:1/(32*k)+(4*k-v)*(3*k-v)/(128*H*k*k)
h=lambda v:(4*k-v)/(16*k)
same=lambda a,b:sp.cancel(a-b)==0
assert same(S,2*t(q)+U(q)*d*d)
assert same(p,Q(1,2)+h(q)*d/(2*H))
Uprime=sp.diff(U(q),q0)
Usecond=sp.diff(U(q),q0,2)
assert same(Usecond,1/(64*H*k*k))
assert same(sp.diff(S,x,x),1/(16*k)+2*U(q)+Usecond*d*d/4-2*Uprime*d)
assert same(sp.diff(S,y,y),1/(16*k)+2*U(q)+Usecond*d*d/4+2*Uprime*d)
assert same(sp.diff(S,x,y),1/(16*k)-2*U(q)+Usecond*d*d/4)
assert same(sp.diff(GA,x,x),sp.diff(S,x,x)/2+b/(16*H*k)-c)
m=(H*(3*k-q0)+b*(4*k-q0))/(16*H*k)
ss=c-(H+b)/(16*H*k)
tc=c-1/(8*k)
mu0=(q0-3*k)/(8*k)
assert same(sp.diff(GA,x).subs(y,x),m-ss*x)
assert same(sp.diff(W,x).subs(y,x),-mu0-tc*x)
ap=(mu-mu0)/tc
an=(mu+m)/ss
assert same(sp.diff(W,x).subs({x:ap,y:ap})+mu,0)
assert same(sp.diff(GA,x).subs({x:an,y:an})+mu,0)
assert same(sp.diff(an-ap,mu),(b-H)/(16*H*k*ss*tc))
z={q0:Q(3,10),k:Q(2,25),H:Q(1,100),b:Q(11,200),c:10,L:Q(2,25)}
qlo=z[q0]-z[L];zhi=z[q0]
v=sp.symbols("v")
Uexpr=U(v).subs({k:z[k],H:z[H]})
vals=[qlo,zhi,Q(7,2)*z[k]]
umin=min(sp.cancel(Uexpr.subs(v,i)) for i in vals)
umax=max(sp.cancel(Uexpr.subs(v,i)) for i in vals)
D=max(abs(sp.diff(Uexpr,v).subs(v,i)) for i in [qlo,zhi])
D2=sp.diff(Uexpr,v,2)
costP=1/(8*z[k])+4*umax+2*D*z[L]+D2*z[L]**2/2
costN=Q(1,2)*(1/(8*z[k])+2*umax+2*D*z[L]+D2*z[L]**2/4)+z[b]/(16*z[H]*z[k])
assert (umin,umax,D,D2)==(Q(25,128),Q(325,512),Q(1875,128),Q(15625,64))
assert (costP,costN)==(Q(925,128),Q(3625,512))
assert z[c]>costP and z[c]>costN and umin>0
assert 3*z[k]<z[q0]<4*z[k] and 0<z[L]<z[q0]
assert (4*z[k]-qlo)*z[L]<16*z[k]*z[H]
boundary=sp.factor(sp.diff(W,x).subs(x,0))
expected=(-mu0+y/(16*k)-sp.diff(U(q),q0).subs(x,0)*y*y/2-2*U(q.subs(x,0))*y)
assert same(boundary,expected)  # catches the omitted +y/(16k) term
new_planner_bound=z[L]*max(Q(0),1/(16*z[k])-2*umin)+D*z[L]**2/2
assert new_planner_bound==Q(5,64)
assert mu0.subs(z)==Q(3,32)>new_planner_bound
assert sp.factor(boundary.subs(z).subs(y,z[L]))==-Q(7,128)
assert m.subs(z)>0 and z[b]>z[H]
assert 0<(m/ss).subs(z)==Q(1,126)<z[L]
assert (ap.subs(z).subs(mu,Q(1,10)),an.subs(z).subs(mu,Q(1,10)))==(Q(1,1350),Q(89,3150))
assert Q(3,32)<Q(1,10)<min((mu0+tc*L).subs(z),(ss*L-m).subs(z))
assert sp.diff(an-ap,mu).subs(z)>0
# The global planner corner follows from a negative gradient at the
# origin and strict concavity, NOT from incorrect off-axis boundary signs.
same(sp.diff(W,x).subs({x:0,y:0}),-mu0)
same(sp.diff(W,y).subs({x:0,y:0}),-mu0)
# A second strict primitive witness passes the Hessian and Nash conditions
# but fails the old extra off-axis derivative condition. This illustrates
# that the supporting-hyperplane theorem is materially more general.
z2={q0:Q(49,200),k:Q(2,25),H:Q(1,100),b:Q(11,200),c:20,L:Q(2,25)}
qlo2=z2[q0]-z2[L]
U2=sp.factor(U(v).subs({k:z2[k],H:z2[H]}))
candidates2=[qlo2,z2[q0]]
if qlo2<=sp.Rational(7,2)*z2[k]<=z2[q0]:
    candidates2.append(sp.Rational(7,2)*z2[k])
u2min=min(U2.subs(v,j) for j in candidates2)
u2max=max(U2.subs(v,j) for j in candidates2)
d2=max(abs(sp.diff(U2,v).subs(v,j)) for j in [qlo2,z2[q0]])
d22=sp.diff(U2,v,2)
cp2=1/(8*z2[k])+4*u2max+2*d2*z2[L]+d22*z2[L]**2/2
cg2=Q(1,2)*(1/(8*z2[k])+2*u2max+2*d2*z2[L]+d22*z2[L]**2/4)+z2[b]/(16*z2[H]*z2[k])
assert 3*z2[k]<z2[q0]<4*z2[k] and 0<z2[L]<z2[q0]
assert (4*z2[k]-qlo2)*z2[L]<16*z2[k]*z2[H]
assert u2min>0 and z2[c]>max(cp2,cg2)
assert m.subs(z2)>0 and 0<(m/ss).subs(z2)<z2[L]
assert z2[b]>z2[H]
unnecessary_bound=z2[L]*max(Q(0),1/(16*z2[k])-2*u2min)+d2*z2[L]**2/2
assert mu0.subs(z2)<unnecessary_bound
print("PASS alternative strict witness: original stronger off-axis bound not necessary")

print("PASS analytic primitive-region symbolic identities, global sufficient margins, and welfare comparative static")
print("witness U bounds",umin,umax,"cost bounds",costP,costN)
print("mu=1/10 planner",ap.subs(z).subs(mu,Q(1,10)),"Nash",an.subs(z).subs(mu,Q(1,10)))
