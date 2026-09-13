import json, pathlib
import sympy as sp

ROOT=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'docs/certificate_polynomials.json').read_text())
g=sp.symbols('gamma')

def poly(name):
    return sp.Poly.from_list(data[name], gens=g, domain=sp.ZZ)

# Primitive symbolic identities.
piD=1/(2+g)**2; piM=sp.Rational(1,4)
Delta=sp.cancel(piM-piD)
assert sp.simplify(Delta-g*(g+4)/(4*(g+2)**2)) == 0
assert sp.simplify(sp.diff(Delta,g)-2/(g+2)**3) == 0

# Exact witness signs from the derivation archived at Stage 7.5.
MS_w=sp.Rational(-10651615424202276975145722347598033,1643142955852817767935206845318567220)
ML_w=sp.Rational(717004319683029789719275067656347639039338956556328208736741107,
                371338299758534039173259783433492599466444392472176495572868210320)
assert MS_w < 0 < ML_w

PMS=poly('MS_num'); PML=poly('ML_num')
DMS=poly('MS_den'); DML=poly('ML_den')
rootsS=[x for x in PMS.intervals(eps=sp.Rational(1,10**12)) if x[0][1]>0 and x[0][0]<1]
rootsL=[x for x in PML.intervals(eps=sp.Rational(1,10**12)) if x[0][1]>0 and x[0][0]<1]
assert len(rootsS)==1 and len(rootsL)==1
Llo,Lhi=rootsL[0][0]; Slo,Shi=rootsS[0][0]
assert Lhi < Slo
assert not DMS.intervals(inf=0,sup=1)
assert not DML.intervals(inf=0,sup=1)

print('exact MS(12/25)=',MS_w)
print('exact ML(12/25)=',ML_w)
print('gamma_L in', (Llo,Lhi), '=', (float(Llo),float(Lhi)))
print('gamma_S in', (Slo,Shi), '=', (float(Slo),float(Shi)))
print('PASS symbolic threshold certificate')
