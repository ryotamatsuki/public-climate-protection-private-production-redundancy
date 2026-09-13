#!/usr/bin/env python3
"""
Exact Stage 11A global certificate for PCPPR.

The certificate uses exact rational-function arithmetic over QQ(x,y)
and tensor-product Bernstein coefficients on rectangles.

Certified statements at the canonical witness:
1. every downstream continuation used by the theorem is interior and regular
   on the full policy square [0, 2/25]^2;
2. dW/da_A < 0 and dW/da_B < 0 on the full policy square, hence (0,0)
   is the unique coordinated optimum;
3. the diagonal local-government FOC has exactly one root alpha in
   (0, 2/25);
4. for every rival action y in the exact isolating interval for alpha,
   d^2 G_A / da_A^2 < 0 on the full own-action interval. Therefore, at
   y=alpha, the stationary point x=alpha is the unique global best response.

No floating-point arithmetic is used in the certificate.
"""
from math import comb
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field

F, x, y = field("x,y", QQ)
Q = QQ

gamma = Q(12, 25)
q0 = Q(3, 10)
k = Q(169, 3000)
H = Q(1, 100)
b = Q(11, 200)
c = Q(3, 1)
abar = Q(2, 25)

pi_d = Q(625, 3844)
pi_m = Q(1, 4)
delta = Q(84, 961)
t_d = Q(2175, 3844)
t_m = Q(3, 8)


def backup_equilibrium(s1, s2, joint):
    den = k*k - (delta*joint)**2
    r1 = (k*(pi_d*s1 + delta*joint)
          - delta*joint*(pi_d*s2 + delta*joint)) / den
    r2 = (k*(pi_d*s2 + delta*joint)
          - delta*joint*(pi_d*s1 + delta*joint)) / den
    return r1, r2, den


def firm_profit(si, sj, joint, ri, rj):
    return (pi_d - pi_d*si*(1-ri) + delta*sj*(1-rj)
            - delta*joint*(1-ri)*(1-rj) - k*ri*ri/2)


def market_surplus(s1, s2, joint, r1, r2):
    m1 = s1*(1-r1)
    m2 = s2*(1-r2)
    z = joint*(1-r1)*(1-r2)
    return (t_d + (t_m-t_d)*(m1+m2) + (t_d-2*t_m)*z
            - k*(r1*r1+r2*r2)/2)


qA = q0 - x
qB = q0 - y


def profile(l1, l2):
    s1 = qA if l1 == "A" else qB
    s2 = qA if l2 == "A" else qB
    if l1 == l2 == "A":
        joint = qA
    elif l1 == l2 == "B":
        joint = qB
    else:
        joint = qA*qB
    r1, r2, bden = backup_equilibrium(s1, s2, joint)
    return {
        "r1": r1,
        "r2": r2,
        "bden": bden,
        "p1": firm_profit(s1, s2, joint, r1, r2),
        "S": market_surplus(s1, s2, joint, r1, r2),
    }


AA = profile("A", "A")
AB = profile("A", "B")
BA = profile("B", "A")
BB = profile("B", "B")

dA = AA["p1"] - BA["p1"]
dB = AB["p1"] - BB["p1"]
location_den = 2*H - dA + dB
p = (H + dB) / location_den

ES = (p*p*AA["S"]
      + 2*p*(1-p)*AB["S"]
      + (1-p)*(1-p)*BB["S"])
W = ES + 2*b - c*(x*x + y*y)/2
GA = ES/2 + 2*b*p - c*x*x/2


def bernstein_coeffs(poly, x0, x1, y0, y1):
    """Exact tensor-product Bernstein coefficients after mapping to [0,1]^2."""
    nx = poly.degree(0)
    ny = poly.degree(1)
    dx = x1 - x0
    dy = y1 - y0

    cpower = [[Q(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for (i, j), coef in poly.items():
        cpower[i][j] = coef

    tx = [[Q(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for j in range(ny+1):
        for r in range(nx+1):
            z = Q(0)
            for i in range(r, nx+1):
                z += cpower[i][j] * Q(comb(i, r), 1) * x0**(i-r) * dx**r
            tx[r][j] = z

    apower = [[Q(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for r in range(nx+1):
        for s in range(ny+1):
            z = Q(0)
            for j in range(s, ny+1):
                z += tx[r][j] * Q(comb(j, s), 1) * y0**(j-s) * dy**s
            apower[r][s] = z

    bx = [[Q(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for s in range(ny+1):
        for I in range(nx+1):
            z = Q(0)
            for r in range(I+1):
                z += apower[r][s] * Q(comb(I, r), comb(nx, r))
            bx[I][s] = z

    out = {}
    for I in range(nx+1):
        for J in range(ny+1):
            z = Q(0)
            for s in range(J+1):
                z += bx[I][s] * Q(comb(J, s), comb(ny, s))
            out[(I, J)] = z
    return out


def strict_sign_poly(poly, rect):
    vals = bernstein_coeffs(poly, *rect).values()
    lo = min(vals)
    hi = max(vals)
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise AssertionError("Bernstein coefficients do not certify a strict sign")


def strict_sign_rational(frac, rect):
    sn = strict_sign_poly(frac.numer, rect)
    sd = strict_sign_poly(frac.denom, rect)
    return 1 if sn == sd else -1


def certify_between_zero_one(frac, rect):
    sd = strict_sign_poly(frac.denom, rect)
    sn = strict_sign_poly(frac.numer, rect)
    s1 = strict_sign_poly(frac.denom-frac.numer, rect)
    assert sn == sd, "failed positivity"
    assert s1 == sd, "failed upper bound by one"


FULL = (Q(0), abar, Q(0), abar)

# Regularity and interiority of every downstream continuation.
for obj in (AA, AB, BA, BB):
    assert strict_sign_rational(obj["bden"], FULL) > 0
    certify_between_zero_one(obj["r1"], FULL)
    certify_between_zero_one(obj["r2"], FULL)

assert strict_sign_rational(location_den, FULL) > 0
certify_between_zero_one(p, FULL)

# Exact global planner certificate.
dWdx = W.diff(x)
dWdy = W.diff(y)
assert strict_sign_rational(dWdx, FULL) < 0
assert strict_sign_rational(dWdy, FULL) < 0

# Exact diagonal root isolation for the local-government FOC.
dGdx = GA.diff(x)
ddGdxx = dGdx.diff(x)
a = sp.symbols("a")


def diagonal_poly(poly):
    data = {}
    for (i, j), coef in poly.items():
        deg = i + j
        rat = sp.Rational(int(coef.numerator), int(coef.denominator))
        data[(deg,)] = data.get((deg,), sp.Integer(0)) + rat
    return sp.Poly.from_dict(data, a, domain=sp.QQ)


Fnum = diagonal_poly(dGdx.numer)
Fden = diagonal_poly(dGdx.denom)
roots = Fnum.intervals(
    eps=sp.Rational(1, 10**15),
    inf=sp.Rational(0),
    sup=sp.Rational(2, 25),
)
assert len(roots) == 1 and roots[0][1] == 1
assert not Fden.intervals(inf=sp.Rational(0), sup=sp.Rational(2, 25))
(lo_sp, hi_sp), _ = roots[0]
lo = Q(int(lo_sp.p), int(lo_sp.q))
hi = Q(int(hi_sp.p), int(hi_sp.q))

# For every rival action in the root enclosure, G_A is strictly concave in
# own protection throughout [0, abar]. At the exact root alpha this makes
# the stationary point x=alpha the unique global best response.
LOCAL = (Q(0), abar, lo, hi)
assert strict_sign_rational(ddGdxx, LOCAL) < 0

print("planner: exact Bernstein certificate PASS")
print("continuations: exact regularity/interiority certificate PASS")
print("local FOC root interval:", lo_sp, hi_sp)
print("local global best response: exact root isolation + strict-concavity certificate PASS")
print("PASS Stage 11A rigorous global certificate")
