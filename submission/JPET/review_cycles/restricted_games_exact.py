"""Exact independent fixed-readiness and fixed-location policy game check."""
import sympy as S
Q=S.Rational
x,y=S.symbols('x y')
q0=Q(3,10);k=Q(2,25);H=Q(1,100);b=Q(11,200);c=10
qA,qB=q0-x,q0-y
f=lambda q:(1-q)/4+q*q/(32*k)
t=lambda q:3*(1-q)/8+q*q/(16*k)
r0=Q(15,16)
ff=lambda q:(1-q*(1-r0))/4-k*r0*r0/2
tf=lambda q:Q(3,8)*(1-q*(1-r0))-k*r0*r0/2
p=Q(1,2)+(ff(qA)-ff(qB))/(2*H)
market=2*(p*tf(qA)+(1-p)*tf(qB))
W=market+2*b-c*(x*x+y*y)/2
GA=market/2+2*b*p-c*x*x/2
same=lambda a,b: S.cancel(a-b)==0
assert same(S.diff(W,x).subs(y,x),Q(3,128)-10*x)
assert same(S.diff(GA,x).subs(y,x),Q(25,256)-10*x)
assert S.diff(W,x,x)==-Q(10165,1024)
assert S.diff(W,y,y)==-Q(10165,1024)
assert S.diff(W,x,y)==-Q(75,1024)
assert S.diff(GA,x,x)==-Q(20405,2048)
assert (p.subs({x:0,y:Q(2,25)}),p.subs({x:Q(2,25),y:0}))==(Q(7,16),Q(9,16))
assert same(S.diff(W,x).subs({x:Q(3,1280),y:Q(3,1280)}),0)
assert same(S.diff(GA,x).subs({x:Q(5,512),y:Q(5,512)}),0)
assert Q(3,1280)<Q(5,512)<Q(2,25)
# Fixed-location p=1/2, privately re-optimize readiness independently.
Sfixed=t(qA)+t(qB)
Wfixed=Sfixed+2*b-c*(x*x+y*y)/2
Gfixed=Sfixed/2+b-c*x*x/2
assert same(S.diff(Wfixed,x),-Q(3,32)-Q(135,16)*x)
assert same(S.diff(Gfixed,x),-Q(3,64)-Q(295,32)*x)
assert same(S.diff(Wfixed,y),-Q(3,32)-Q(135,16)*y)
assert 0 < Q(3,1280) < Q(5,512)
print('PASS: exact fixed-readiness planner/Nash and fixed-location planner/Nash counterfactual games')
print('fixed-readiness: planner = 3/1280, local = 5/512; fixed-location: both zero')


# Common direct-benefit parameter: full-endogenous, fixed-readiness,
# fixed-location counterfactual differences.
mu=S.symbols('mu',real=True)
ap_full=(32*mu-3)/270
an_full=(128*mu+5)/630
ap_ready=(mu+Q(3,128))/10
an_ready=(mu+Q(25,256))/10
ap_location=Q(16,135)*(mu-Q(3,32))
an_location=Q(32,295)*(mu-Q(3,64))
assert same(S.diff(an_full-ap_full,mu),Q(16,189))
assert same(S.diff(an_ready-ap_ready,mu),0)
assert same(S.diff(an_location-ap_location,mu),-Q(16,1593))
assert same(an_ready-ap_ready,Q(19,2560))
for value in (Q(3,32)+Q(1,10000), Q(1,10),Q(1,8)-Q(1,10000)):
    assert all(0<expression.subs(mu,value)<Q(2,25) for expression in
               (ap_full,an_full,ap_ready,an_ready,ap_location,an_location))
# All affected stationary points solve their globally concave policy games.
assert same(S.diff(W,x).subs({x:ap_ready,y:ap_ready})+mu,0)
assert same(S.diff(GA,x).subs({x:an_ready,y:an_ready})+mu,0)
assert same(S.diff(Wfixed,x).subs(x,ap_location)+mu,0)
assert same(S.diff(Gfixed,x).subs(x,an_location)+mu,0)
print('PASS: three distinct exact benefit-gap slope signs; positive, zero, negative')
