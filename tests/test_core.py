import pathlib,sys
import sympy as sp
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from core_model import Params, profile, primitives, firm_profit_closed, market_surplus_closed, location_probability
from direct_evaluator import direct_profit_and_surplus, availability_state_probabilities


def test_direct_evaluator_matches_closed_form():
    par=Params()
    for locs in [('A','A'),('A','B'),('B','A'),('B','B')]:
        pr=profile(0.017,0.041,*locs,par)
        p1,p2,S,probs=direct_profit_and_surplus(pr['s1'],pr['s2'],pr['J'],pr['r1'],pr['r2'],par)
        assert abs(p1-pr['profit1'])<1e-12
        assert abs(p2-pr['profit2'])<1e-12
        assert abs(S-pr['surplus'])<1e-12
        assert abs(sum(probs)-1)<1e-12


def test_conditional_independence_implies_joint_unavailability_formula():
    s1,s2,J=0.3,0.4,0.12
    r1,r2=0.5,0.25
    probs=availability_state_probabilities(s1,s2,J,r1,r2)
    assert abs(probs[3]-J*(1-r1)*(1-r2))<1e-15
    assert abs(sum(probs)-1)<1e-15


def test_symmetric_location_probability():
    par=Params()
    p,_=location_probability(0.02,0.02,par)
    assert abs(p-.5)<1e-13


def test_backup_interior_on_witness():
    par=Params()
    for locs in [('A','A'),('A','B'),('B','A'),('B','B')]:
        pr=profile(0.02301968487,0.02301968487,*locs,par)
        assert 0<pr['r1']<1 and 0<pr['r2']<1


def test_delta_positive_and_rises_with_gamma_numerically():
    p1=Params(gamma=.2); p2=Params(gamma=.8)
    d1=primitives(p1)[2]; d2=primitives(p2)[2]
    assert 0<d1<d2


def test_canonical_colocated_policy_substitutability_cross_partial_is_negative():
    q,g=sp.symbols('q gamma')
    k=sp.Rational(169,3000)
    pi_m=sp.Rational(1,4)
    pi_d=1/(2+g)**2
    delta=sp.cancel(pi_m-pi_d)
    rC=sp.cancel(q*pi_m/(k+q*delta))
    cross=sp.cancel(sp.diff(rC,q,g).subs({q:sp.Rational(3,10),g:sp.Rational(12,25)}))
    target=-sp.Rational(26550065039062500,13482801445834729)
    assert cross==target
    assert cross<0
