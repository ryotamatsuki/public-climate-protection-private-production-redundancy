from __future__ import annotations

import json
import pathlib
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
coeff = json.loads((ROOT / 'docs/certificate_polynomials.json').read_text())
meta = json.loads((ROOT / 'docs/certificate_normalization.json').read_text())

q0 = sp.Rational(3, 10)
k = sp.Rational(169, 3000)
H = sp.Rational(1, 100)
bplant = sp.Rational(11, 200)
c = sp.Rational(3, 1)


def stored_rational(prefix: str, z: sp.Symbol) -> sp.Expr:
    num = sp.Poly.from_list(coeff[f'{prefix}_num'], gens=z, domain=sp.ZZ).as_expr()
    den = sp.Poly.from_list(coeff[f'{prefix}_den'], gens=z, domain=sp.ZZ).as_expr()
    return sp.cancel(num / den)


def primitives(g):
    pi_d = 1 / (2 + g) ** 2
    pi_m = sp.Rational(1, 4)
    delta = sp.cancel(pi_m - pi_d)
    t_d = (3 + g) / (2 + g) ** 2
    t_m = sp.Rational(3, 8)
    return pi_d, delta, t_d, t_m


def profile_from_q(qA, qB, l1: str, l2: str, g):
    pi_d, delta, t_d, t_m = primitives(g)
    s1 = qA if l1 == 'A' else qB
    s2 = qA if l2 == 'A' else qB
    if l1 == l2 == 'A':
        J = qA
    elif l1 == l2 == 'B':
        J = qB
    else:
        J = qA * qB
    den = k**2 - (delta * J) ** 2
    r1 = sp.cancel((k * (pi_d * s1 + delta * J)
                    - delta * J * (pi_d * s2 + delta * J)) / den)
    r2 = sp.cancel((k * (pi_d * s2 + delta * J)
                    - delta * J * (pi_d * s1 + delta * J)) / den)
    profit1 = sp.cancel(pi_d - pi_d * s1 * (1 - r1)
                        + delta * s2 * (1 - r2)
                        - delta * J * (1 - r1) * (1 - r2)
                        - k * r1**2 / 2)
    m1 = s1 * (1 - r1)
    m2 = s2 * (1 - r2)
    z = J * (1 - r1) * (1 - r2)
    surplus = sp.cancel(t_d + (t_m - t_d) * (m1 + m2)
                        + (t_d - 2 * t_m) * z
                        - k * (r1**2 + r2**2) / 2)
    return profit1, surplus


def expected_objects(aA, aB, g):
    qA, qB = q0 - aA, q0 - aB
    AA = profile_from_q(qA, qB, 'A', 'A', g)
    AB = profile_from_q(qA, qB, 'A', 'B', g)
    BA = profile_from_q(qA, qB, 'B', 'A', g)
    BB = profile_from_q(qA, qB, 'B', 'B', g)
    dA = sp.cancel(AA[0] - BA[0])
    dB = sp.cancel(AB[0] - BB[0])
    p = sp.cancel((H + dB) / (2 * H - dA + dB))
    S = sp.cancel(p**2 * AA[1] + 2 * p * (1 - p) * AB[1] + (1 - p)**2 * BB[1])
    W = sp.cancel(S + 2 * bplant - c * (aA**2 + aB**2) / 2)
    GA = sp.cancel(S / 2 + 2 * bplant * p - c * aA**2 / 2)
    return W, GA


def assert_scaled_identity(prefix: str, z: sp.Symbol, economic: sp.Expr):
    factor = sp.Rational(meta['objects'][prefix]['normalization_factor'])
    raw = stored_rational(prefix, z)
    diff = sp.cancel(raw - factor * sp.cancel(economic))
    assert diff == 0, f'{prefix} normalization identity failed: {diff}'
    print(f'{prefix}: stored/economic = {factor}')


# MS: common-policy derivative at the origin, varying gamma.
g = sp.symbols('gamma')
a = sp.symbols('a')
# Along the symmetric path p=1/2 by symmetry, which avoids introducing a
# redundant location fixed-point expression into the common-policy derivative.
q = q0 - a
AA = profile_from_q(q, q, 'A', 'A', g)[1]
AB = profile_from_q(q, q, 'A', 'B', g)[1]
Ssym = sp.cancel((AA + AB) / 2)
Wsym = sp.cancel(Ssym + 2 * bplant - c * a**2)
MS = sp.cancel(sp.diff(Wsym, a).subs(a, 0))
assert_scaled_identity('MS', g, MS)

# ML: unilateral local-policy derivative at the symmetric origin.
x = sp.symbols('x')
_, GA_unilateral = expected_objects(x, sp.Integer(0), g)
ML = sp.cancel(sp.diff(GA_unilateral, x).subs(x, 0))
assert_scaled_identity('ML', g, ML)

# F: diagonal local-government first-order condition at canonical gamma.
g0 = sp.Rational(12, 25)
y = sp.symbols('y')
_, GA_xy = expected_objects(x, y, g0)
F = sp.cancel(sp.diff(GA_xy, x).subs(x, a).subs(y, a))
assert_scaled_identity('F', a, F)

# W: common-policy planner derivative at canonical gamma.
Wdiag = sp.cancel(Wsym.subs(g, g0))
Wprime = sp.cancel(sp.diff(Wdiag, a))
assert_scaled_identity('W', a, Wprime)

print('PASS auxiliary certificate normalization identities')
