"""Independent economic/certificate regressions, with boundary attacks."""
from fractions import Fraction
from pathlib import Path
import sys
import numpy as np
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import independent_model_audit as model
import independent_exact_audit as exact


@pytest.mark.parametrize('joint',[.3,.09])
@pytest.mark.parametrize('r1,r2',[(0,0),(1,0),(0,1),(1,1),(.37,.89)])
def test_probability_law_matches_primary_and_conditional_backup_draws(joint,r1,r2):
    z=model.states(.3,.3,joint,r1,r2)
    assert sum(z.values())==pytest.approx(1)
    assert min(z.values())>=-1e-15
    assert z[(0,0)]==pytest.approx(joint*(1-r1)*(1-r2))
    assert z[(0,0)]+z[(0,1)]==pytest.approx(.3*(1-r1))
    assert z[(0,0)]+z[(1,0)]==pytest.approx(.3*(1-r2))


def test_clipped_map_is_not_an_interior_map_even_with_interior_equilibrium():
    assert model.clipped_backup_response(.3,.3,0.)==1
    cp=model.continuation(0,0,(0,0))
    r=model.clipped_backup_fixed_point(.3,.3,.3)
    assert np.all(r>0) and np.all(r<1)
    assert np.max(abs(r-np.array([cp['r1'],cp['r2']])))<2e-13


@pytest.mark.parametrize('s1,s2',[(0.,.01),(.3,.01),(.3,.3)])
def test_boundary_backup_optimum_against_direct_state_payoff_grid(s1,s2):
    par={**model.ZERO_DELTA,'k':.05}
    joint=s1*s2
    r=model.clipped_backup_fixed_point(s1,s2,joint,par=par)
    m=model.market(0.)
    grid=np.linspace(0,1,2001)
    def profit(own):
        p=model.states(s1,s2,joint,own,r[1])
        return m['pd']*p[(1,1)]+m['pm']*p[(1,0)]-par['k']*own**2/2
    assert max(profit(grid))-profit(r[0])<1e-14
    assert r[0]==pytest.approx(min(1,5*s1))


def test_consumer_producer_resource_and_hosting_accounting_after_asymmetric_deviation():
    for aA,aB in [(0.,.08),(.017,.039),(.08,0.)]:
        ev=model.policies(aA,aB)
        m=model.market(model.WITNESS['gamma'])
        p=ev['p']
        weights={(0,0):p*p,(0,1):p*(1-p),(1,0):p*(1-p),(1,1):(1-p)**2}
        independent_surplus=0.
        for loc,cp in ev['profiles'].items():
            cs=cp['states'][(1,1)]*m['csd']+(cp['states'][(1,0)]+cp['states'][(0,1)])*.125
            independent_surplus+=weights[loc]*(cs+cp['profit1']+cp['profit2'])
        costs=model.WITNESS['c']*(aA*aA+aB*aB)/2
        assert ev['W']==pytest.approx(independent_surplus+2*model.WITNESS['b']-costs,abs=1e-14)
        assert ev['GA']+ev['GB']==pytest.approx(ev['W'],abs=1e-14)


def test_independent_transform_nonunit_and_degenerate_domains_and_strict_sign_rejections():
    evidence=exact.sanity_tests()
    assert evidence['exact_reconstruction_checks']==792
    assert evidence['known_root_tests']==2


def test_utility_and_state_based_exact_identities():
    identities=exact.primitive_identities()
    assert identities['duopoly_profit']=='(g + 2)**(-2)'
