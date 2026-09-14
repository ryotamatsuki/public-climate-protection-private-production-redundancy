from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
coeff = json.loads((ROOT / 'docs/certificate_polynomials.json').read_text())
meta = json.loads((ROOT / 'docs/certificate_normalization.json').read_text())

q0 = sp.Rational(3, 10)
k = sp.Rational(169, 3000)
H = sp.Rational(1, 100)
bplant = sp.Rational(11, 200)
c = sp.Rational(3, 1)


@dataclass(frozen=True)
class Dual:
    """Exact forward-mode derivative pair (value, derivative)."""
    v: sp.Expr
    d: sp.Expr = sp.Integer(0)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Dual) else Dual(sp.sympify(x), sp.Integer(0))

    def __add__(self, other):
        o = Dual.coerce(other)
        return Dual(self.v + o.v, self.d + o.d)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.v, -self.d)

    def __sub__(self, other):
        return self + (-Dual.coerce(other))

    def __rsub__(self, other):
        return Dual.coerce(other) - self

    def __mul__(self, other):
        o = Dual.coerce(other)
        return Dual(self.v * o.v, self.d * o.v + self.v * o.d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = Dual.coerce(other)
        return Dual(self.v / o.v, (self.d * o.v - self.v * o.d) / o.v**2)

    def __rtruediv__(self, other):
        return Dual.coerce(other) / self

    def __pow__(self, power: int):
        if not isinstance(power, int):
            raise TypeError('Dual powers must be integers')
        if power == 0:
            return Dual(sp.Integer(1), sp.Integer(0))
        if power < 0:
            return Dual(sp.Integer(1), sp.Integer(0)) / (self ** (-power))
        return Dual(self.v**power, power * self.v**(power - 1) * self.d)


def stored_rational(prefix: str, z: sp.Symbol) -> sp.Expr:
    num = sp.Poly.from_list(coeff[f'{prefix}_num'], gens=z, domain=sp.ZZ).as_expr()
    den = sp.Poly.from_list(coeff[f'{prefix}_den'], gens=z, domain=sp.ZZ).as_expr()
    return num / den


def primitives(g):
    pi_d = 1 / (2 + g) ** 2
    pi_m = sp.Rational(1, 4)
    delta = pi_m - pi_d
    t_d = (3 + g) / (2 + g) ** 2
    t_m = sp.Rational(3, 8)
    return pi_d, delta, t_d, t_m


def profile_dual(qA: Dual, qB: Dual, l1: str, l2: str, g):
    pi_d, delta, t_d, t_m = primitives(g)
    s1 = qA if l1 == 'A' else qB
    s2 = qA if l2 == 'A' else qB
    if l1 == l2 == 'A':
        J = qA
    elif l1 == l2 == 'B':
        J = qB
    else:
        J = qA * qB

    den = k**2 - (delta * J)**2
    r1 = (k * (pi_d * s1 + delta * J)
          - delta * J * (pi_d * s2 + delta * J)) / den
    r2 = (k * (pi_d * s2 + delta * J)
          - delta * J * (pi_d * s1 + delta * J)) / den

    profit1 = (pi_d - pi_d * s1 * (1 - r1)
               + delta * s2 * (1 - r2)
               - delta * J * (1 - r1) * (1 - r2)
               - k * r1**2 / 2)
    m1 = s1 * (1 - r1)
    m2 = s2 * (1 - r2)
    z = J * (1 - r1) * (1 - r2)
    surplus = (t_d + (t_m - t_d) * (m1 + m2)
               + (t_d - 2 * t_m) * z
               - k * (r1**2 + r2**2) / 2)
    return profit1, surplus


def expected_dual(qA: Dual, qB: Dual, g):
    AA = profile_dual(qA, qB, 'A', 'A', g)
    AB = profile_dual(qA, qB, 'A', 'B', g)
    BA = profile_dual(qA, qB, 'B', 'A', g)
    BB = profile_dual(qA, qB, 'B', 'B', g)
    dA = AA[0] - BA[0]
    dB = AB[0] - BB[0]
    p = (H + dB) / (2 * H - dA + dB)
    S = p**2 * AA[1] + 2 * p * (1 - p) * AB[1] + (1 - p)**2 * BB[1]
    return p, S


def exact_zero(expr: sp.Expr) -> bool:
    num, _ = sp.fraction(sp.cancel(sp.together(expr)))
    return sp.Poly(sp.expand(num)).is_zero


def assert_scaled_identity(prefix: str, z: sp.Symbol, economic: sp.Expr):
    factor = sp.Rational(meta['objects'][prefix]['normalization_factor'])
    raw = stored_rational(prefix, z)
    assert exact_zero(raw - factor * economic), f'{prefix} normalization identity failed'
    print(f'{prefix}: stored/economic = {factor}')


# MS and ML at the symmetric origin, varying gamma.  Forward differentiation
# evaluates the policy derivative at a=0 before symbolic simplification, so the
# only remaining indeterminate is gamma.
g = sp.symbols('gamma')
qA_common = Dual(q0, -1)
qB_common = Dual(q0, -1)
_, S_common = expected_dual(qA_common, qB_common, g)
MS = S_common.d  # public-cost derivative is zero at the origin
assert_scaled_identity('MS', g, MS)

qA_unilateral = Dual(q0, -1)
qB_unilateral = Dual(q0, 0)
p_uni, S_uni = expected_dual(qA_unilateral, qB_unilateral, g)
ML = S_uni.d / 2 + 2 * bplant * p_uni.d
assert_scaled_identity('ML', g, ML)

# F and W' at the canonical gamma.  The policy level a remains symbolic, but
# the derivative direction is propagated exactly without first building a
# two-policy symbolic objective.
a = sp.symbols('a')
g0 = sp.Rational(12, 25)
q = q0 - a
p_local, S_local = expected_dual(Dual(q, -1), Dual(q, 0), g0)
F = S_local.d / 2 + 2 * bplant * p_local.d - c * a
assert_scaled_identity('F', a, F)

_, S_diag = expected_dual(Dual(q, -1), Dual(q, -1), g0)
Wprime = S_diag.d - 2 * c * a
assert_scaled_identity('W', a, Wprime)

print('PASS auxiliary certificate normalization identities')
