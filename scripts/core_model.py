from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Params:
    gamma: float = 12/25
    q0: float = 3/10
    k: float = 169/3000
    H: float = 1/100
    b: float = 11/200
    c: float = 3.0
    abar: float = 2/25

    def validate(self) -> None:
        assert 0 <= self.gamma < 1
        assert 0 < self.abar < self.q0 < 1
        assert self.k > 0 and self.H > 0 and self.c > 0


def primitives(par: Params):
    g = par.gamma
    pi_d = 1/(2+g)**2
    pi_m = 1/4
    delta = pi_m-pi_d
    t_d = (3+g)/(2+g)**2
    t_m = 3/8
    return pi_d, pi_m, delta, t_d, t_m


def backup_equilibrium(s1: float, s2: float, J: float, par: Params):
    pi_d, _, delta, _, _ = primitives(par)
    den = par.k**2-(delta*J)**2
    if den <= 0:
        raise ValueError('backup linear system is singular/nonregular')
    r1 = (par.k*(pi_d*s1+delta*J)-delta*J*(pi_d*s2+delta*J))/den
    r2 = (par.k*(pi_d*s2+delta*J)-delta*J*(pi_d*s1+delta*J))/den
    if not (0 <= r1 <= 1 and 0 <= r2 <= 1):
        raise ValueError('backup equilibrium outside frozen interior branch')
    return r1, r2


def firm_profit_closed(si, sj, J, ri, rj, par: Params):
    pi_d, _, delta, _, _ = primitives(par)
    return (pi_d - pi_d*si*(1-ri) + delta*sj*(1-rj)
            - delta*J*(1-ri)*(1-rj) - par.k*ri**2/2)


def market_surplus_closed(s1, s2, J, r1, r2, par: Params):
    _, _, _, t_d, t_m = primitives(par)
    m1 = s1*(1-r1)
    m2 = s2*(1-r2)
    z = J*(1-r1)*(1-r2)
    return (t_d + (t_m-t_d)*(m1+m2) + (t_d-2*t_m)*z
            - par.k*(r1*r1+r2*r2)/2)


def profile(aA: float, aB: float, l1: str, l2: str, par: Params):
    qA, qB = par.q0-aA, par.q0-aB
    s1 = qA if l1 == 'A' else qB
    s2 = qA if l2 == 'A' else qB
    if l1 == l2 == 'A':
        J = qA
    elif l1 == l2 == 'B':
        J = qB
    else:
        J = qA*qB
    r1, r2 = backup_equilibrium(s1, s2, J, par)
    p1 = firm_profit_closed(s1, s2, J, r1, r2, par)
    p2 = firm_profit_closed(s2, s1, J, r2, r1, par)
    S = market_surplus_closed(s1, s2, J, r1, r2, par)
    return {'s1': s1, 's2': s2, 'J': J, 'r1': r1, 'r2': r2,
            'profit1': p1, 'profit2': p2, 'surplus': S}


def location_probability(aA: float, aB: float, par: Params):
    AA = profile(aA,aB,'A','A',par)
    AB = profile(aA,aB,'A','B',par)
    BA = profile(aA,aB,'B','A',par)
    BB = profile(aA,aB,'B','B',par)
    dA = AA['profit1']-BA['profit1']
    dB = AB['profit1']-BB['profit1']
    den = 2*par.H-dA+dB
    if abs(den) < 1e-14:
        raise ValueError('location fixed point singular')
    p = (par.H+dB)/den
    if not (0 <= p <= 1):
        raise ValueError('location probability outside frozen interior branch')
    return p, {'AA':AA,'AB':AB,'BA':BA,'BB':BB}


def expected_surplus(aA: float, aB: float, par: Params):
    p, prof = location_probability(aA,aB,par)
    return (p*p*prof['AA']['surplus']
            + 2*p*(1-p)*prof['AB']['surplus']
            + (1-p)**2*prof['BB']['surplus'])


def national_welfare(aA: float, aB: float, par: Params):
    return (expected_surplus(aA,aB,par)+2*par.b
            - par.c*(aA*aA+aB*aB)/2)


def government_A_payoff(aA: float, aB: float, par: Params):
    p, _ = location_probability(aA,aB,par)
    return expected_surplus(aA,aB,par)/2 + 2*par.b*p - par.c*aA*aA/2
