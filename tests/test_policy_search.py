"""Regressions for the actual false-equilibrium failure, including boundaries."""
from fractions import Fraction
import pathlib
import sys
import pytest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from core_model import Params, government_A_payoff
from policy_search import maximize_interval, symmetric_candidates
from exact_marginals import origin_marginals, canonical_channels


def test_original_non_nash_point_is_rejected_and_no_false_root_returned():
    par=Params(gamma=237/500)
    old=0.0043027129963519005
    assert government_A_payoff(0,old,par)-government_A_payoff(old,old,par)>9e-7
    candidates=symmetric_candidates(lambda x,y:government_A_payoff(x,y,par),par.abar)
    # The original algorithm found a sign change at a jump in its BR selection.
    # Neither that point nor zero is a symmetric equilibrium at these primitives.
    assert candidates==[]


def test_deviation_search_compares_both_boundaries_and_multiple_peaks():
    x,value=maximize_interval(lambda a:max(1-(a-.2)**2,2-10*(a-.8)**2),1)
    assert abs(x-.8)<1e-7 and value>1.99
    x,value=maximize_interval(lambda a:-a,1)
    assert x==0 and value==0
    x,value=maximize_interval(lambda a:a,1)
    assert x==1 and value==1


def test_exact_origin_channels_retain_resource_cost_savings():
    margins=origin_marginals()
    assert margins['MS']==Fraction(-10651615424202276975145722347598033,
                                  1643142955852817767935206845318567220)
    channels=canonical_channels()
    direct=channels['direct_public_protection_effect_holding_redundancy_fixed']
    response=channels['endogenous_redundancy_response_effect']
    assert direct>0 and response<0 and direct+response==margins['MS']
    assert margins['ML']>0


def test_government_primitives_reject_nonpositive_hosting_benefit():
    with pytest.raises(AssertionError):
        Params(b=0).validate()
