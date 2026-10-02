"""Verify the plotted quantities and thresholds, not just exhibit filenames."""
from __future__ import annotations
import csv
from fractions import Fraction as R
import json
from pathlib import Path
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field
from exact_marginals import origin_marginals, canonical_channels

ROOT=Path(__file__).resolve().parents[1]


def main():
    domain,g=field('g',QQ)
    symbolic=origin_marginals(g)
    z=sp.Symbol('gamma')
    def poly(p):
        return sp.Poly.from_dict({index:sp.Rational(str(value)) for index,value in p.items()},z,domain=sp.QQ)
    archived=json.loads((ROOT/'docs/certificate_polynomials.json').read_text())
    normalizations=json.loads((ROOT/'docs/certificate_normalization.json').read_text())
    thresholds={}
    for name in ('MS','ML'):
        numerator,denominator=poly(symbolic[name].numer),poly(symbolic[name].denom)
        reference=sp.Poly.from_list(archived[name+'_num'],z,domain=sp.ZZ).as_expr()/sp.Poly.from_list(archived[name+'_den'],z,domain=sp.ZZ).as_expr()
        factor=sp.Rational(normalizations['objects'][name]['normalization_factor'])
        assert sp.cancel(factor*numerator.as_expr()/denominator.as_expr()-reference)==0
        assert not denominator.intervals(inf=sp.Rational(44,100),sup=sp.Rational(54,100))
        roots=numerator.intervals(eps=sp.Rational(1,10**16),inf=sp.Rational(44,100),sup=sp.Rational(54,100))
        assert len(roots)==1 and roots[0][1]==1
        thresholds[name]=roots[0][0]
    assert thresholds['ML'][1]<thresholds['MS'][0]
    # Every exported point must be the stated exact marginal, rather than a policy.
    with (ROOT/'tables/policy_marginals.csv').open() as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==['gamma','MS','ML','lambda']
        rows=list(reader)
    assert len(rows)==101
    for i,row in enumerate(rows):
        gamma=R(row['gamma'])
        assert gamma==R(440+i,1000)
        expected=origin_marginals(gamma)
        for name in ('MS','ML','lambda'):
            assert R(row[name])==expected[name]
        if thresholds['ML'][1] < sp.Rational(gamma.numerator,gamma.denominator) < thresholds['MS'][0]:
            assert R(row['MS'])<0<R(row['ML'])
    assert not (ROOT/'tables/policy_regime.csv').exists()
    channels=canonical_channels()
    assert channels['direct_public_protection_effect_holding_redundancy_fixed']>0
    assert sum(list(channels.values())[:2])==channels['total_coordinated_marginal_effect']<0
    # Derive the readiness wedge directly from the state-level social objective.
    gamma,si,sj,joint,ri,rj,k=sp.symbols('g si sj J ri rj k')
    pd,pm=1/(2+gamma)**2,sp.Rational(1,4)
    td,tm=(3+gamma)/(2+gamma)**2,sp.Rational(3,8)
    mi,mj=si*(1-ri),sj*(1-rj)
    zz=joint*(1-ri)*(1-rj)
    S=(1-mi-mj+zz)*td+(mi+mj-2*zz)*tm-k*(ri**2+rj**2)/2
    social_at_foc=sp.diff(S,ri).subs(k*ri,pd*si+(pm-pd)*joint*(1-rj))
    target=(2-3*gamma)*si/(8*(2+gamma))+gamma*joint*(1-rj)/(2*(2+gamma))
    assert sp.cancel(social_at_foc-target)==0
    print('exact marginal exhibit: all 101 rational points and both isolated thresholds verified')
    print('readiness wedge identity and exact engineering/response decomposition verified')
    print({name:tuple(map(str,bounds)) for name,bounds in thresholds.items()})


if __name__=='__main__':
    main()
