import json, pathlib
import sympy as sp
ROOT=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'docs/certificate_polynomials.json').read_text())
a=sp.symbols('a')
abar=sp.Rational(2,25)

def poly(name):
    return sp.Poly.from_list(data[name], gens=a, domain=sp.ZZ)
PF=poly('F_num'); PDF=poly('F_den'); PW=poly('W_num'); PDW=poly('W_den')
roots=PF.intervals(eps=sp.Rational(1,10**12),inf=0,sup=abar)
assert len(roots)==1 and roots[0][1]==1
assert not PDF.intervals(inf=0,sup=abar)
assert not PW.intervals(inf=0,sup=abar)
assert not PDW.intervals(inf=0,sup=abar)
(lo,hi),_=roots[0]
# The archived exact planner derivative at zero is negative.
dW0=sp.Rational(-10651615424202276975145722347598033,1643142955852817767935206845318567220)
assert dW0 < 0
print('a_LG in', (lo,hi), '=', (float(lo),float(hi)))
print('planner derivative numerator has no root on [0,abar] and dW(0)<0')
print('PASS exact policy certificate')
