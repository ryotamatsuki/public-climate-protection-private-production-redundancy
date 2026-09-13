from core_model import Params, primitives


def direct_profit_and_surplus(s1,s2,J,r1,r2,par: Params):
    pi_d, pi_m, _, t_d, t_m = primitives(par)
    m1 = s1*(1-r1)
    m2 = s2*(1-r2)
    z = J*(1-r1)*(1-r2)
    both = 1-m1-m2+z
    only1 = m2-z
    only2 = m1-z
    neither = z
    probs = [both,only1,only2,neither]
    if min(probs) < -1e-12 or abs(sum(probs)-1) > 1e-10:
        raise ValueError('invalid enumerated state probabilities')
    profit1 = both*pi_d + only1*pi_m - par.k*r1*r1/2
    profit2 = both*pi_d + only2*pi_m - par.k*r2*r2/2
    surplus = both*t_d + (only1+only2)*t_m - par.k*(r1*r1+r2*r2)/2
    return profit1, profit2, surplus, probs
