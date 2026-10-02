"""Origin derivatives from availability-state enumeration, without finite differences.

Arithmetic works over Fraction and the rational-function field QQ(g). This
module imports neither the closed-form evaluator nor a coefficient archive.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q

@dataclass(frozen=True)
class Jet:
    value: object
    da: object = 0
    db: object = 0

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Jet) else Jet(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet(self.value+other.value, self.da+other.da, self.db+other.db)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.da, -self.db)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        return Jet(self.value*other.value,
                   self.da*other.value+self.value*other.da,
                   self.db*other.value+self.value*other.db)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        return Jet(self.value/other.value,
                   (self.da*other.value-self.value*other.da)/other.value**2,
                   (self.db*other.value-self.value*other.db)/other.value**2)

    def __rtruediv__(self, other):
        return self.coerce(other)/self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Jet supports nonnegative integer powers")
        if n == 0:
            return Jet(1)
        return Jet(self.value**n, n*self.value**(n-1)*self.da,
                   n*self.value**(n-1)*self.db)


def origin_marginals(gamma=Q(12, 25), *, freeze_backup=False):
    q0, k, H, b = Q(3, 10), Q(169, 3000), Q(1, 100), Q(11, 200)
    pi_d, pi_m = 1/(2+gamma)**2, Q(1, 4)
    delta = pi_m-pi_d
    td, tm = (3+gamma)/(2+gamma)**2, Q(3, 8)
    risk = (Jet(q0, -1, 0), Jet(q0, 0, -1))

    def profile(i, j):
        si, sj = risk[i], risk[j]
        joint = si if i == j else si*sj
        det = k*k-(delta*joint)**2
        ri = (k*(pi_d*si+delta*joint)-delta*joint*(pi_d*sj+delta*joint))/det
        rj = (k*(pi_d*sj+delta*joint)-delta*joint*(pi_d*si+delta*joint))/det
        if freeze_backup:
            ri, rj = Jet(ri.value), Jet(rj.value)
        mi, mj, z = si*(1-ri), sj*(1-rj), joint*(1-ri)*(1-rj)
        both, only_i, only_j = 1-mi-mj+z, mj-z, mi-z
        profit = both*pi_d+only_i*pi_m-k*ri**2/2
        surplus = both*td+(only_i+only_j)*tm-k*(ri**2+rj**2)/2
        return profit, surplus

    profiles = {ij: profile(*ij) for ij in ((0, 0), (0, 1), (1, 0), (1, 1))}
    d_a = profiles[0, 0][0]-profiles[1, 0][0]
    d_b = profiles[0, 1][0]-profiles[1, 1][0]
    p = (H+d_b)/(2*H-d_a+d_b)
    surplus = (p**2*profiles[0, 0][1]
               + p*(1-p)*(profiles[0, 1][1]+profiles[1, 0][1])
               + (1-p)**2*profiles[1, 1][1])
    ms, ml = surplus.da+surplus.db, surplus.da/2+2*b*p.da
    if ml != ms/4+2*b*p.da:
        raise AssertionError("plant-attraction decomposition failed")
    return {"MS": ms, "ML": ml, "lambda": p.da}


def canonical_channels():
    total = origin_marginals()
    direct = origin_marginals(freeze_backup=True)["MS"]
    return {"direct_public_protection_effect_holding_redundancy_fixed": direct,
            "endogenous_redundancy_response_effect": total["MS"]-direct,
            "total_coordinated_marginal_effect": total["MS"],
            "local_government_unilateral_marginal_payoff": total["ML"]}
