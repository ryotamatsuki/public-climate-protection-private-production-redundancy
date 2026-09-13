#!/usr/bin/env python3
"""Independent Stage 11B re-audit of the Stage 11A exact certificate.

This script deliberately does not import verify_global_certificate.py or core_model.py.
It reconstructs the witness from primitives and uses an independently coded,
direct affine-expansion / tensor-Bernstein conversion.
"""
from math import comb
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field

F, x, y = field("x,y", QQ)
Q = QQ

gamma=Q(12,25); q0=Q(3,10); k=Q(169,3000); H=Q(1,100)
b=Q(11,200); c=Q(3,1); abar=Q(2,25)
pi_d=1/(Q(2)+gamma)**2
pi_m=Q(1,4); delta=pi_m-pi_d
t_d=(Q(3)+gamma)/(Q(2)+gamma)**2; t_m=Q(3,8)


def backup(s1,s2,J):
    den=k*k-(delta*J)**2
    r1=(k*(pi_d*s1+delta*J)-delta*J*(pi_d*s2+delta*J))/den
    r2=(k*(pi_d*s2+delta*J)-delta*J*(pi_d*s1+delta*J))/den
    return r1,r2,den


def profit(si,sj,J,ri,rj):
    return pi_d-pi_d*si*(1-ri)+delta*sj*(1-rj)-delta*J*(1-ri)*(1-rj)-k*ri**2/2


def surplus(s1,s2,J,r1,r2):
    m1=s1*(1-r1); m2=s2*(1-r2); z=J*(1-r1)*(1-r2)
    return t_d+(t_m-t_d)*(m1+m2)+(t_d-2*t_m)*z-k*(r1*r1+r2*r2)/2

qA=q0-x; qB=q0-y

def profile(l1,l2):
    s1=qA if l1=="A" else qB
    s2=qA if l2=="A" else qB
    J=qA if l1==l2=="A" else qB if l1==l2=="B" else qA*qB
    r1,r2,den=backup(s1,s2,J)
    return {"r1":r1,"r2":r2,"den":den,"p1":profit(s1,s2,J,r1,r2),"S":surplus(s1,s2,J,r1,r2)}

AA=profile("A","A"); AB=profile("A","B"); BA=profile("B","A"); BB=profile("B","B")
dA=AA["p1"]-BA["p1"]
dB=AB["p1"]-BB["p1"]
loc_den=2*H-dA+dB
p=(H+dB)/loc_den
ES=p*p*AA["S"]+2*p*(1-p)*AB["S"]+(1-p)*(1-p)*BB["S"]
W=ES+2*b-c*(x*x+y*y)/2
GA=ES/2+2*b*p-c*x*x/2


def direct_bernstein(poly,x0,x1,y0,y1):
    """Independent direct conversion of p(x,y) to Bernstein coefficients.

    First expands x=x0+(x1-x0)u and y=y0+(y1-y0)v term by term.
    Then applies b_IJ=sum_{r<=I,s<=J} a_rs*C(I,r)/C(n,r)*C(J,s)/C(m,s).
    """
    nx=poly.degree(0); ny=poly.degree(1)
    dx=x1-x0; dy=y1-y0
    power={}
    for (i,j),coef in poly.items():
        for r in range(i+1):
            cx=Q(comb(i,r),1)*x0**(i-r)*dx**r
            for s in range(j+1):
                power[(r,s)]=power.get((r,s),Q(0))+coef*cx*Q(comb(j,s),1)*y0**(j-s)*dy**s
    out={}
    for I in range(nx+1):
        for J in range(ny+1):
            z=Q(0)
            for r in range(I+1):
                wx=Q(comb(I,r),comb(nx,r))
                for s in range(J+1):
                    z += power.get((r,s),Q(0))*wx*Q(comb(J,s),comb(ny,s))
            out[(I,J)]=z
    return out


def sign_poly(poly,rect):
    vals=direct_bernstein(poly,*rect).values()
    lo=min(vals); hi=max(vals)
    if lo>0: return 1
    if hi<0: return -1
    return 0


def sign_rat(frac,rect):
    sn=sign_poly(frac.numer,rect); sd=sign_poly(frac.denom,rect)
    assert sn and sd
    return 1 if sn==sd else -1


def between01(frac,rect):
    sd=sign_poly(frac.denom,rect)
    sn=sign_poly(frac.numer,rect)
    sr=sign_poly(frac.denom-frac.numer,rect)
    return sd and sn==sd and sr==sd

FULL=(Q(0),abar,Q(0),abar)

# 1. Reproduce full-square continuation interiority independently.
for name,obj in (("AA",AA),("AB",AB),("BA",BA),("BB",BB)):
    assert sign_rat(obj["den"],FULL)>0, name
    assert between01(obj["r1"],FULL), name+" r1"
    assert between01(obj["r2"],FULL), name+" r2"
assert sign_rat(loc_den,FULL)>0
assert between01(p,FULL)

# 2. Reproduce the global planner certificate independently.
dWdx=W.diff(x); dWdy=W.diff(y)
assert sign_rat(dWdx,FULL)<0
assert sign_rat(dWdy,FULL)<0

# 3. Reproduce exact local root and global-own-action concavity.
dGdx=GA.diff(x); ddG=dGdx.diff(x)
a=sp.symbols("a")
def diag(poly):
    expr=sp.Integer(0)
    for (i,j),coef in poly.items():
        expr += sp.Rational(int(coef.numerator),int(coef.denominator))*a**(i+j)
    return sp.Poly(expr,a,domain=sp.QQ)
fn=diag(dGdx.numer); fd=diag(dGdx.denom)
roots=fn.intervals(eps=sp.Rational(1,10**15),inf=0,sup=sp.Rational(2,25))
assert len(roots)==1 and roots[0][1]==1
assert not fd.intervals(inf=0,sup=sp.Rational(2,25))
(lo_sp,hi_sp),_=roots[0]
lo=Q(int(lo_sp.p),int(lo_sp.q)); hi=Q(int(hi_sp.p),int(hi_sp.q))
LOCAL=(Q(0),abar,lo,hi)
assert sign_rat(ddG,LOCAL)<0

# 4. Additional Stage 11B attack omitted from the Stage 11A certificate:
# certify that the Bayesian location best-response map is globally untruncated
# and has |slope|<1 for every first-stage policy deviation.
u0=(H+dB)/(2*H)  # P(A) if rival chooses A with probability zero
u1=(H+dA)/(2*H)  # P(A) if rival chooses A with probability one
B=(dA-dB)/(2*H)
assert between01(u0,FULL)
assert between01(u1,FULL)
assert sign_rat(1-B,FULL)>0
assert sign_rat(1+B,FULL)>0

print("PASS independent direct-Bernstein reconstruction")
print("PASS planner full-rectangle global certificate")
print("PASS local exact-root / global-concavity reconstruction")
print("PASS additional location-map no-clipping and |slope|<1 checks")
print("root interval:",lo_sp,hi_sp)
