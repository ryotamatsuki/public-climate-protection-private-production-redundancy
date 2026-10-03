"""Independent exact reconstruction and attacks on production certificates.

Builds economic objects from state enumeration without importing production
modules. The Bernstein implementation solves the triangular coefficient
system of the actual basis, instead of using the production power-to-basis
binomial ratio algorithm. Production imports occur only in compare_bridge().
"""
from __future__ import annotations
import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.fields import field

ROOT=Path(__file__).resolve().parents[1]

def fraction(q):
    return Fraction(int(q.numerator),int(q.denominator))


def basis_convert(power):
    """Forward substitution in P_j = sum_i coeff_j(B_i,n) beta_i."""
    n=len(power)-1
    beta=[]
    for j in range(n+1):
        previous=sum(Fraction(comb(n,i)*comb(n-i,j-i)*(-1)**(j-i))*beta[i]
                     for i in range(j))
        beta.append((power[j]-previous)/comb(n,j))
    return beta


def independent_bernstein(poly,rectangle):
    x,y=poly.ring.gens
    lo,hi,bottom,top=map(QQ.convert,rectangle)
    if lo>hi or bottom>top:
        raise ValueError('Reversed rectangle')
    mapped=poly.compose({x:lo+(hi-lo)*x,y:bottom+(top-bottom)*y})
    if not mapped:
        return {(0,0):Fraction(0)}
    nx,ny=map(int,mapped.degrees())
    nx=max(0,nx); ny=max(0,ny)
    powers=[[fraction(mapped.get((i,j),QQ(0))) for j in range(ny+1)] for i in range(nx+1)]
    columns=[basis_convert([powers[i][j] for i in range(nx+1)]) for j in range(ny+1)]
    coefficients={}
    for i in range(nx+1):
        row=basis_convert([columns[j][i] for j in range(ny+1)])
        coefficients.update({(i,j):row[j] for j in range(ny+1)})
    return coefficients


def rational_sign(value,rectangle):
    betaN=independent_bernstein(value.numer,rectangle)
    betaD=independent_bernstein(value.denom,rectangle)
    def sign(beta):
        if min(beta.values())>0:return 1
        if max(beta.values())<0:return -1
        raise ValueError('No strict whole-domain sign, including endpoints')
    sn,sd=sign(betaN),sign(betaD)
    return sn*sd,dict(numerator_range=[str(min(betaN.values())),str(max(betaN.values()))],
                      denominator_range=[str(min(betaD.values())),str(max(betaD.values()))],
                      bidegrees=[list(value.numer.degrees()),list(value.denom.degrees())])


def primitive_identities():
    x1,x2,g,k,s1,s2,J,r1,r2=sp.symbols('x1 x2 g k s1 s2 J r1 r2')
    U=x1+x2-(x1*x1+x2*x2+2*g*x1*x2)/2
    p1,p2=sp.diff(U,x1),sp.diff(U,x2)
    sol=sp.solve([sp.diff(p1*x1,x1),sp.diff(p2*x2,x2)],(x1,x2))
    assert sol=={x1:1/(g+2),x2:1/(g+2)}
    pd=sp.factor((p1*x1).subs(sol))
    CS=sp.factor((U-p1*x1-p2*x2).subs(sol))
    TD=sp.factor(U.subs(sol))
    assert sp.cancel(pd-1/(g+2)**2)==0
    assert sp.cancel(CS-(1+g)/(g+2)**2)==0
    assert sp.cancel(TD-(3+g)/(g+2)**2)==0
    mono=sp.solve(sp.diff((p1*x1).subs(x2,0),x1),x1)[0]
    assert mono==sp.Rational(1,2)
    pm=sp.Rational(1,4); tm=sp.Rational(3,8)
    delta=pm-pd
    # Enumerated primary-failure and conditional-success law.
    final={(0,0):0,(1,0):0,(0,1):0,(1,1):0}
    for (f1,f2),pr in {(0,0):1-s1-s2+J,(1,0):s1-J,(0,1):s2-J,(1,1):J}.items():
        for h1 in (0,1):
            for h2 in (0,1):
                v=(int(not f1) or h1,int(not f2) or h2)
                final[v]+=pr*(r1 if h1 else 1-r1)*(r2 if h2 else 1-r2)
    final={z:sp.expand(v) for z,v in final.items()}
    assert sp.expand(sum(final.values()))==1
    assert sp.expand(final[(0,0)]-J*(1-r1)*(1-r2))==0
    profit=pd*final[(1,1)]+pm*final[(1,0)]-k*r1*r1/2
    FOC=sp.factor(sp.diff(profit,r1))
    assert sp.cancel(FOC-(pd*s1+delta*J*(1-r2)-k*r1))==0
    assert sp.diff(profit,r1,2)==-k
    S=TD*final[(1,1)]+tm*(final[(1,0)]+final[(0,1)])-k*(r1*r1+r2*r2)/2
    wedge=sp.factor(sp.diff(S,r1).subs(k*r1,pd*s1+delta*J*(1-r2)))
    target=(2-3*g)*s1/(8*(2+g))+g*J*(1-r2)/(2*(2+g))
    # Substitute k via the FOC, since k*r1 may be factored by SymPy.
    wedge=sp.cancel(sp.diff(S,r1).subs(k,(pd*s1+delta*J*(1-r2))/r1))
    assert sp.cancel(wedge-target)==0
    return dict(duopoly_profit=str(pd),CS_D=str(CS),T_D=str(TD),backup_FOC=str(FOC),readiness_wedge=str(target))


def economic_objects(gamma=QQ(12,25),k=QQ(169,3000),c=QQ(3)):
    f,x,y=field('own,rival',QQ)
    q0,H,b,abar=QQ(3,10),QQ(1,100),QQ(11,200),QQ(2,25)
    pd=1/(2+gamma)**2; pm=QQ(1,4); delta=pm-pd
    td=(3+gamma)/(2+gamma)**2; tm=QQ(3,8)
    qs=[q0-x,q0-y]
    profiles={}
    for l1 in (0,1):
        for l2 in (0,1):
            s1,s2=qs[l1],qs[l2]
            J=s1 if l1==l2 else qs[0]*qs[1]
            cross=delta*J
            A=pd*s1+cross; B=pd*s2+cross
            # Eliminate r2 from the two own FOCs, then back-substitute.
            r1=(A-cross*B/k)/(k-cross*cross/k)
            r2=(B-cross*r1)/k
            final={(0,0):f(0),(1,0):f(0),(0,1):f(0),(1,1):f(0)}
            for (fail1,fail2),pr in {(0,0):1-s1-s2+J,(1,0):s1-J,(0,1):s2-J,(1,1):J}.items():
                for h1 in (0,1):
                    for h2 in (0,1):
                        z=(int(not fail1) or h1,int(not fail2) or h2)
                        final[z]+=pr*(r1 if h1 else 1-r1)*(r2 if h2 else 1-r2)
            pi1=pd*final[(1,1)]+pm*final[(1,0)]-k*r1*r1/2
            S=td*final[(1,1)]+tm*(final[(1,0)]+final[(0,1)])-k*(r1*r1+r2*r2)/2
            profiles[(l1,l2)]=dict(r1=r1,r2=r2,profit1=pi1,S=S,determinant=k*k-cross*cross)
    d0=profiles[(0,0)]['profit1']-profiles[(1,0)]['profit1']
    d1=profiles[(0,1)]['profit1']-profiles[(1,1)]['profit1']
    u0=QQ(1,2)+d1/(2*H); u1=QQ(1,2)+d0/(2*H)
    slope=u1-u0
    # Subtract the two probability equations: (1+B)(p1-p2)=0.
    # Solve the remaining common-probability equation.
    p=u0/(1-slope)
    weights={(0,0):p*p,(0,1):p*(1-p),(1,0):p*(1-p),(1,1):(1-p)**2}
    S=sum(weights[z]*profiles[z]['S'] for z in weights)
    W=S+2*b-c*(x*x+y*y)/2
    GA=S/2+2*b*p-c*x*x/2
    GB=S/2+2*b*(1-p)-c*y*y/2
    assert GA+GB==W
    return dict(field=f,x=x,y=y,profiles=profiles,p=p,u0=u0,u1=u1,slope=slope,W=W,GA=GA,S=S,abar=abar,delta=delta,k=k)


def diagonal(frac):
    z=sp.Symbol('a')
    def convert(poly):
        return sp.Poly.from_dict({(d,):sum(sp.Rational(c) for (i,j),c in poly.items() if i+j==d)
                                  for d in set(sum(m) for m in poly.keys())},z,domain=sp.QQ)
    n,d=convert(frac.numer),convert(frac.denom)
    return sp.cancel(n.as_expr()/d.as_expr()),z


def sturm_count(poly,low,high):
    sequence=sp.sturm(poly.as_expr(),poly.gen)
    def variations(t):
        signs=[sp.sign(z.subs(poly.gen,t)) for z in sequence]
        signs=[s for s in signs if s]
        return sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))
    return variations(low)-variations(high)


def sanity_tests():
    from sympy.polys.rings import ring
    r,x,y=ring('t,u',QQ)
    rng=random.Random(20261003)
    rectangles=[(QQ(0),QQ(1),QQ(0),QQ(1)),(QQ(-2),QQ(3,7),QQ(1,11),QQ(5,4)),
                (QQ(0),QQ(2,25),QQ(7,1000),QQ(1,80)),(QQ(0),QQ(2,25),QQ(1,126),QQ(1,126))]
    polynomials=[r.zero,r.one,x,y,x*x-2*x*y+3*y*y, (1-x)**2+2*x*(1-x)+x*x]
    for _ in range(60):
        polynomials.append(sum(QQ(rng.randint(-10,10))*x**i*y**j for i in range(rng.randrange(1,6)) for j in range(rng.randrange(1,6))))
    checks=0
    for poly in polynomials:
        for rect in rectangles:
            beta=independent_bernstein(poly,rect)
            nx=max(i for i,j in beta); ny=max(j for i,j in beta)
            for a,b in [(QQ(0),QQ(0)),(QQ(1),QQ(1)),(QQ(1,3),QQ(2,7))]:
                reconstructed=sum(QQ.convert(v)*comb(nx,i)*a**i*(1-a)**(nx-i)*comb(ny,j)*b**j*(1-b)**(ny-j) for (i,j),v in beta.items())
                value=poly.evaluate([(x,rect[0]+(rect[1]-rect[0])*a),(y,rect[2]+(rect[3]-rect[2])*b)])
                assert reconstructed==value
                checks+=1
    f,xx,yy=field('t,u',QQ)
    for obj in [xx,1/(xx-QQ(1,2)),1/(xx-1)]:
        try:rational_sign(obj,(0,1,0,1))
        except ValueError:pass
        else:raise AssertionError('Strict sign must reject zero or pole')
    assert rational_sign(-1/(1+xx+yy),(0,1,0,1))[0]==-1
    assert rational_sign((1+xx)/(-2-yy),(0,1,0,1))[0]==-1
    try:independent_bernstein(x,(1,0,0,1))
    except ValueError:pass
    else:raise AssertionError('Reversed endpoints accepted')
    a=sp.Symbol('z')
    known=sp.Poly((a-QQ(1,3))*(a-QQ(2,3))*(a+1),a)
    assert sturm_count(known,0,1)==2
    assert sturm_count(sp.Poly((a-QQ(1,3))**2,a),0,1)==1
    return dict(polynomials=len(polynomials),exact_reconstruction_checks=checks,known_root_tests=2)


def compare_bridge(obj):
    # Production modules are first imported AFTER independent construction.
    import verify_global_certificate as prod
    pairs=[(obj['p'],prod.p),(obj['W'],prod.W),(obj['GA'],prod.GA),
           (obj['u0'],prod.u0),(obj['u1'],prod.u1)]
    for own,original in pairs:
        original=obj['field'].from_expr(original.as_expr().subs({sp.Symbol('x'):sp.Symbol('own'),sp.Symbol('y'):sp.Symbol('rival')}))
        assert own==original
    from sympy.polys.rings import ring
    rr,t,u=ring('t,u',QQ)
    rng=random.Random(73)
    for _ in range(40):
        pol=sum(QQ(rng.randint(-9,9))*t**i*u**j for i in range(5) for j in range(4))
        rect=(QQ(-1,7),QQ(2,25),QQ(1,126),QQ(1,126)+QQ(1,10**10))
        a=independent_bernstein(pol,rect)
        b=prod.bernstein_coeffs(pol,*rect)
        assert all(a[z]==fraction(b[z]) for z in a)
    F,z=diagonal(obj['GA'].diff(obj['x']))
    Wprime,_=diagonal(obj['W'].diff(obj['x'])+obj['W'].diff(obj['y']))
    archive=json.loads((ROOT/'docs/certificate_polynomials.json').read_text())
    for prefix,econ,factor in [('F',F,sp.Integer(-76880)),('W',Wprime,-sp.Rational(19220,3))]:
        stored=sp.Poly.from_list(archive[prefix+'_num'],z).as_expr()/sp.Poly.from_list(archive[prefix+'_den'],z).as_expr()
        assert sp.cancel(stored-factor*econ)==0
    evidence=dict(exact_economic_object_matches=len(pairs),random_production_transform_comparisons=40,exact_archive_normalizations=['F','W'])
    # Independently attach T9's terminal rationals to our primitive-derived
    # rational functions. This does not rely on Lean's DualQ implementation.
    import re
    witness=(ROOT/'formal/PCPPR/CanonicalWitness.lean').read_text()
    def at_origin(value):
        denominator=value.denom.get((0,0),QQ(0))
        assert denominator!=0
        return value.numer.get((0,0),QQ(0))/denominator
    checkpoints={
        'MS0':at_origin(obj['W'].diff(obj['x'])+obj['W'].diff(obj['y'])),
        'ML0':at_origin(obj['GA'].diff(obj['x'])),
        'lambda0':at_origin(obj['p'].diff(obj['x'])),
    }
    for name,value in checkpoints.items():
        match=re.search(r'def '+name+r' : ℚ :=\s*(-?\d+)\s*/\s*(\d+)',witness)
        assert match is not None
        assert fraction(value)==Fraction(int(match[1]),int(match[2]))
    evidence['Lean_T9_economic_checkpoints']={k:str(fraction(v)) for k,v in checkpoints.items()}
    # Attack the actual generated payload, including its different rectangles
    # and the raw (unreduced after diagonal substitution) numerator used in Lean.
    generated_path=ROOT/'formal/GENERATED_CERTIFICATE_ARCHIVE.json'
    if not generated_path.exists():
        raise FileNotFoundError('Run make formal-certificates before this bridge check')
    generated=json.loads(generated_path.read_text())
    full=(QQ(0),obj['abar'],QQ(0),obj['abar'])
    for prefix,econ,rect in [
        ('planner_x',obj['W'].diff(obj['x']),full),
        ('planner_y',obj['W'].diff(obj['y']),full),
        ('local_second',obj['GA'].diff(obj['x']).diff(obj['x']),tuple(prod.LOCAL)),
        ('diagonal_foc_policy_derivative',obj['GA'].diff(obj['x']).diff(obj['x'])+obj['GA'].diff(obj['x']).diff(obj['y']),tuple(prod.ROOT_SQUARE)),
    ]:
        for label,poly in [('numerator',econ.numer),('denominator',econ.denom)]:
            own_beta=independent_bernstein(poly,rect)
            actual=generated[prefix+'_'+label+'_bernstein']
            expected=[Fraction(*q) for q in actual['coefficients']]
            assert [own_beta[z] for z in sorted(own_beta)]==expected
            sign=1 if min(expected)>0 else -1 if max(expected)<0 else 0
            assert sign==actual['strict_sign'] and sign!=0
    raw=obj['GA'].diff(obj['x']).numer
    P=sp.Poly.from_dict({(degree,):sum(sp.Rational(q) for (i,j),q in raw.items() if i+j==degree)
                        for degree in {sum(z) for z in raw.keys()}},z,domain=sp.QQ)
    gc=generated['diagonal_foc']
    low,high=map(lambda q:sp.Rational(*q),(gc['alphaL'],gc['alphaU']))
    assert low<high and P.degree()==gc['degree']
    for bound,name in [(low,'value_at_alphaL'),(high,'value_at_alphaU')]:
        assert P.eval(bound)==sp.Rational(*gc[name])
    # The derivative is P'(a), evaluated after domain mapping, not dP/dt.
    t=sp.Symbol('t')
    mapped=sp.Poly(sp.expand(P.diff().as_expr().subs(z,low+(high-low)*t)),t,domain=sp.QQ)
    beta=basis_convert([fraction(mapped.nth(j)) for j in range(mapped.degree()+1)])
    assert beta==[Fraction(*q) for q in gc['derivative_bernstein']]
    assert max(beta)<0 and len(beta)==52
    encoded=(ROOT/'formal/PCPPR/GeneratedCertificates.lean').read_text()
    import re
    def naturals(name):
        match=re.search(r'def '+name+r' : Fin 52 → ℕ := !\[(.*?)\]',encoded,re.S)
        assert match is not None
        return list(map(int,re.findall(r'\d+',match.group(1))))
    ns=naturals('diagonalFOCDerivativeBernsteinNumeratorMagnitudePred')
    ds=naturals('diagonalFOCDerivativeBernsteinDenominatorPred')
    assert [Fraction(-(n+1),d+1) for n,d in zip(ns,ds)]==beta
    assert all(n>=0 for n in ns+ds) and len(ns)==len(ds)==52
    evidence['generated_payload']=dict(bivariate_vectors=8,raw_FOC_degree=P.degree(),
        root_interval=[str(low),str(high)],endpoint_values_checked=2,
        raw_derivative_coefficients_checked=len(beta),structural_Lean_rational_encodings_checked=len(ns))
    return evidence


def main():
    evidence=dict(primitive_identities=primitive_identities(),transform_sanity=sanity_tests())
    obj=economic_objects()
    x,y=obj['x'],obj['y']; full=(QQ(0),obj['abar'],QQ(0),obj['abar'])
    targets={}
    for z,p in obj['profiles'].items():
        for label in ('r1','r2'):
            targets[str(z)+label]=(p[label],full,1)
            targets[str(z)+'1-'+label]=(1-p[label],full,1)
        targets[str(z)+'determinant']=(p['determinant'],full,1)
    for name in ('u0','u1','p'):
        targets[name]=(obj[name],full,1); targets['1-'+name]=(1-obj[name],full,1)
    targets['location_contraction+']=(1+obj['slope'],full,1)
    targets['location_contraction-']=(1-obj['slope'],full,1)
    targets['planner_A']=(obj['W'].diff(x),full,-1)
    targets['planner_B']=(obj['W'].diff(y),full,-1)
    foc,a=diagonal(obj['GA'].diff(x))
    n,d=sp.fraction(foc)
    pn,pd=sp.Poly(n,a),sp.Poly(d,a)
    assert sturm_count(pn,0,sp.Rational(2,25))==1
    assert sturm_count(pd,0,sp.Rational(2,25))==0
    # Rational sign bisection: does not consume the production isolation interval.
    low,high=sp.Rational(0),sp.Rational(2,25)
    assert foc.subs(a,low)>0 and foc.subs(a,high)<0
    for _ in range(48):
        mid=(low+high)/2
        if foc.subs(a,mid)>0:low=mid
        else:high=mid
    lo,hi=QQ.convert(low),QQ.convert(high)
    targets['local_concavity']=(obj['GA'].diff(x).diff(x),(QQ(0),obj['abar'],lo,hi),-1)
    targets['diagonal_FOC_derivative']=(obj['GA'].diff(x).diff(x)+obj['GA'].diff(x).diff(y),(lo,hi,lo,hi),-1)
    cert={}
    for name,(value,rect,expected) in targets.items():
        sign,info=rational_sign(value,rect)
        assert sign==expected,(name,sign)
        cert[name]={**info,'rectangle':list(map(str,rect)),'sign':sign}
        print('independent exact target:',name,flush=True)
    evidence['certificates']=cert
    evidence['root']=dict(lower=str(low),upper=str(high),count=1,denominator_roots=0)
    evidence['backup_contraction']=str(obj['delta']*QQ(3,10)/obj['k'])
    assert obj['delta']*QQ(3,10)/obj['k']<1
    zobj=economic_objects(QQ(0),QQ(2,25),QQ(10))
    zf,za=diagonal(zobj['GA'].diff(zobj['x']))
    assert sp.expand(zf-(sp.Rational(5,128)-sp.Rational(315,64)*za))==0
    assert zf.subs(za,sp.Rational(1,126))==0
    for label,v,rect in [('planner_A',zobj['W'].diff(zobj['x']),full),('planner_B',zobj['W'].diff(zobj['y']),full),
                         ('local_concavity',zobj['GA'].diff(zobj['x']).diff(zobj['x']),(QQ(0),obj['abar'],QQ(1,126),QQ(1,126)))]:
        sign,info=rational_sign(v,rect);assert sign<0
        evidence.setdefault('zero_delta',{})[label]=info
    evidence['production_bridge']=compare_bridge(obj)
    out=ROOT/'dist'/'independent_exact_audit_2026-10-03.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(evidence,indent=2,sort_keys=True)+'\n')
    print('Independent economic reconstruction, exact signs, Sturm root count, and production bridge PASS')


if __name__=='__main__':main()
