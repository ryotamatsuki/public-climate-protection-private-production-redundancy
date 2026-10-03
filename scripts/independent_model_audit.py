"""Independent final-audit evaluator derived from manuscript primitives.

No production model, marginal, search, or certificate module is imported.
The production implementation is compared only by the separate bridge audit.
Numerical searches below are falsification evidence, not proof.
"""
from __future__ import annotations

import itertools
import csv
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution, least_squares, minimize, minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
# Transcribed from equations (witness) and (zero-delta-witness), not core_model.
WITNESS = dict(gamma=12/25, q0=3/10, k=169/3000, H=1/100,
               b=11/200, c=3., abar=2/25)
ZERO_DELTA = dict(gamma=0., q0=3/10, k=2/25, H=1/100,
                  b=11/200, c=10., abar=2/25)


def market(gamma):
    # Solve 2*x_i + gamma*x_j = 1. Revenue is p_i*x_i.
    quantities = np.linalg.solve(np.array([[2., gamma], [gamma, 2.]]), [1., 1.])
    prices = 1 - quantities - gamma*quantities[::-1]
    profits = quantities*prices
    cs = .5*(quantities @ quantities + 2*gamma*np.prod(quantities))
    mono_q = .5
    mono_p = 1-mono_q
    mono_cs = .5*mono_q**2
    return dict(pd=profits[0], pm=mono_q*mono_p, csd=cs,
                td=cs+sum(profits), tmon=mono_cs+mono_q*mono_p,
                delta=mono_q*mono_p-profits[0])


def states(s1, s2, joint, r1, r2):
    """Enumerate primary-failure vectors and conditional backup draws.

    Indices (0,0),(1,0),(0,1),(1,1) mean final AVAILABILITY.
    """
    primary = {(0,0): 1-s1-s2+joint, (1,0): s1-joint,
               (0,1): s2-joint, (1,1): joint}
    out = {z: 0 for z in ((0,0),(1,0),(0,1),(1,1))}
    for (f1,f2), prob in primary.items():
        for h1,h2 in itertools.product((0,1), repeat=2):
            bprob = (r1 if h1 else 1-r1)*(r2 if h2 else 1-r2)
            out[(int(not f1) or h1, int(not f2) or h2)] += prob*bprob
    return out


def clipped_backup_response(s1, joint, rival, par=WITNESS):
    """Global quadratic optimum, including the two feasibility boundaries."""
    m = market(par['gamma'])
    return np.clip((m['pd']*s1+m['delta']*joint*(1-rival))/par['k'],0,1)


def clipped_backup_fixed_point(s1,s2,joint,initial=(0.,1.),par=WITNESS):
    """Full feasible map; never assumes its entire range is interior."""
    m = market(par['gamma'])
    if m['delta']*joint/par['k'] >= 1:
        raise ValueError('No contraction certificate for these primitives')
    r = np.array(initial,dtype=float)
    for _ in range(1000):
        new = np.array([clipped_backup_response(s1,joint,r[1],par),
                        clipped_backup_response(s2,joint,r[0],par)])
        if max(abs(new-r))<2e-14:
            return new
        r = new
    raise RuntimeError('Full clipped backup iteration did not converge')


def continuation(aA, aB, loc, par=WITNESS, nonlinear=False, fixed_readiness=None):
    aA, aB = np.broadcast_arrays(np.asarray(aA), np.asarray(aB))
    qa = par['q0']*np.exp(-aA/par['q0']) if nonlinear else par['q0']-aA
    qb = par['q0']*np.exp(-aB/par['q0']) if nonlinear else par['q0']-aB
    si = qa if loc[0] == 0 else qb
    sj = qa if loc[1] == 0 else qb
    joint = si if loc[0] == loc[1] else qa*qb
    m = market(par['gamma'])
    shape = si.shape
    matrix = np.empty(shape+(2,2), dtype=np.result_type(si,sj,float))
    matrix[...,0,0] = matrix[...,1,1] = par['k']
    matrix[...,0,1] = matrix[...,1,0] = m['delta']*joint
    rhs = np.stack([m['pd']*si+m['delta']*joint,
                    m['pd']*sj+m['delta']*joint], axis=-1)
    if fixed_readiness is None:
        rr = np.linalg.solve(matrix, rhs[...,None])[...,0]
        r1, r2 = rr[...,0], rr[...,1]
    else:
        r1, r2 = fixed_readiness
    if np.any(np.real(r1)<=0) or np.any(np.real(r1)>=1) or np.any(np.real(r2)<=0) or np.any(np.real(r2)>=1):
        raise ValueError('Independent interior evaluator outside its certified branch')
    z = states(si,sj,joint,r1,r2)
    pi1 = z[(1,1)]*m['pd'] + z[(1,0)]*m['pm'] - par['k']*r1*r1/2
    pi2 = z[(1,1)]*m['pd'] + z[(0,1)]*m['pm'] - par['k']*r2*r2/2
    surplus = z[(1,1)]*m['td'] + (z[(1,0)]+z[(0,1)])*m['tmon'] - par['k']*(r1*r1+r2*r2)/2
    return dict(profit1=pi1,profit2=pi2,S=surplus,r1=r1,r2=r2,
                states=z,joint=joint,s1=si,s2=sj)


def policies(aA, aB, par=WITNESS, nonlinear=False, logistic=False):
    aA, aB = np.broadcast_arrays(np.asarray(aA), np.asarray(aB))
    profiles = {loc:continuation(aA,aB,loc,par,nonlinear) for loc in itertools.product((0,1),repeat=2)}
    da = profiles[(0,0)]['profit1']-profiles[(1,0)]['profit1']
    db = profiles[(0,1)]['profit1']-profiles[(1,1)]['profit1']
    u0, u1 = .5+db/(2*par['H']), .5+da/(2*par['H'])
    slope = (da-db)/(2*par['H'])
    if not logistic:
        # Solve both firms' probability equations, not just a symmetric guess.
        mat = np.empty(aA.shape+(2,2),dtype=np.result_type(aA,aB,float))
        mat[...,0,0] = mat[...,1,1] = 1
        mat[...,0,1] = mat[...,1,0] = -slope
        rhs = np.stack([u0,u0],axis=-1)
        if np.any(np.real(u0)<=0) or np.any(np.real(u0)>=1) or np.any(np.real(u1)<=0) or np.any(np.real(u1)>=1):
            raise ValueError('Location endpoints require clipping: fail closed')
        pp = np.linalg.solve(mat,rhs[...,None])[...,0]
        p = pp[...,0]
        assert np.max(np.abs(pp[...,0]-pp[...,1])) < 5e-13
    else:
        if np.max(np.abs(np.real(slope))) >= 1:
            raise ValueError('Logistic global contraction bound not satisfied')
        p = np.full(aA.shape,.5,dtype=np.result_type(aA,aB,float))
        for _ in range(1000):
            pn = 1/(1+np.exp(-2*(db+(da-db)*p)/par['H']))
            difference=pn-p
            error=max(float(np.max(np.abs(np.real(difference)))),
                      float(np.max(np.abs(np.imag(difference))))/1e-24
                      if np.iscomplexobj(p) else 0.)
            if error<2e-14:
                p = pn
                break
            p = pn
        else:
            raise RuntimeError('Logistic probability solve failed')
    weights = {(0,0):p*p,(0,1):p*(1-p),(1,0):(1-p)*p,(1,1):(1-p)**2}
    S = sum(weights[z]*profiles[z]['S'] for z in weights)
    GA = S/2 + 2*par['b']*p-par['c']*aA*aA/2
    GB = S/2 + 2*par['b']*(1-p)-par['c']*aB*aB/2
    W = S+2*par['b']-par['c']*(aA*aA+aB*aB)/2
    return dict(W=W,GA=GA,GB=GB,S=S,p=p,u0=u0,u1=u1,slope=slope,profiles=profiles)


def derivative(aA,aB,which='GA',coord=0,par=WITNESS,**kwargs):
    h = 1e-24
    args = [np.asarray(aA,dtype=complex),np.asarray(aB,dtype=complex)]
    args[coord] = args[coord]+h*1j
    return np.imag(policies(*args,par,**kwargs)[which])/h


def best_response(rival,par=WITNESS,**kwargs):
    # Inspect ALL grid peaks, refine each, and include both boundaries.
    grid = np.linspace(0,par['abar'],401)
    val = policies(grid,rival,par,**kwargs)['GA']
    candidates = [(0.,float(val[0])),(par['abar'],float(val[-1]))]
    for i in range(1,len(grid)-1):
        if val[i] >= val[i-1] and val[i] >= val[i+1]:
            sol = minimize_scalar(lambda z:-float(policies(z,rival,par,**kwargs)['GA']),
                                  bounds=(grid[i-1],grid[i+1]),method='bounded',
                                  options=dict(xatol=2e-14))
            if not sol.success:
                raise RuntimeError('Best-response refinement failed')
            candidates.append((float(sol.x),float(-sol.fun)))
    return max(candidates,key=lambda z:z[1])


def audit():
    rng = np.random.default_rng(20261003)
    par = WITNESS
    alpha = brentq(lambda a:float(derivative(a,a)),0,par['abar'],xtol=2e-15)
    grid = np.linspace(0,par['abar'],301)
    xx,yy = np.meshgrid(grid,grid,indexing='ij')
    ev = policies(xx,yy)
    origin = float(policies(0,0)['W'])
    max_idx = np.unravel_index(np.argmax(ev['W']),ev['W'].shape)
    assert max_idx == (0,0)
    max_random_gain = -np.inf
    for _ in range(5):
        rpoints = rng.uniform(0,par['abar'],(10000,2))
        gains = policies(rpoints[:,0],rpoints[:,1])['W']-origin
        max_random_gain = max(max_random_gain,float(max(gains)))
    assert max_random_gain<0
    optima=[]
    for z in itertools.product(np.linspace(0,par['abar'],5),repeat=2):
        sol = minimize(lambda v:-float(policies(*v)['W']),z,bounds=[(0,par['abar'])]*2,
                       jac=lambda v:-np.array([derivative(*v,'W',0),derivative(*v,'W',1)]),
                       method='L-BFGS-B',options=dict(ftol=1e-14,gtol=1e-11))
        if not sol.success:
            raise RuntimeError('Planner multistart failure: '+str(sol.message))
        optima.append(sol.x.tolist())
        assert np.max(np.abs(sol.x))<1e-10
    de = differential_evolution(lambda v:-float(policies(*v)['W']),[(0,par['abar'])]*2,
                                rng=rng,tol=1e-10,atol=1e-12,popsize=12,maxiter=500,polish=True)
    assert de.success and abs(-de.fun-origin)<1e-10
    own = np.linspace(0,par['abar'],4001)
    f = derivative(own,alpha)
    roots=[]
    for i in range(len(own)-1):
        if f[i]*f[i+1]<0:
            roots.append(brentq(lambda z:float(derivative(z,alpha)),own[i],own[i+1],xtol=2e-15))
    assert len(roots)==1 and abs(roots[0]-alpha)<1e-12
    opt,brval = best_response(alpha)
    base = float(policies(alpha,alpha)['GA'])
    assert abs(opt-alpha)<3e-8 and brval-base<1e-12
    own_curvature=(derivative(own,alpha+0)-derivative(own-1e-6,alpha))/1e-6
    assert max(own_curvature)<0
    h = 1e-5
    aa=(derivative(alpha+h,alpha)-derivative(alpha-h,alpha))/(2*h)
    ab=(derivative(alpha,alpha+h)-derivative(alpha,alpha-h))/(2*h)
    diag=(derivative(alpha+h,alpha+h)-derivative(alpha-h,alpha-h))/(2*h)
    assert abs(aa+ab-diag)<2e-8 and diag<0
    equilibria=[]
    rejected_roots=[]
    for z in itertools.product(np.linspace(0,par['abar'],7),repeat=2):
        sol=least_squares(lambda v:[derivative(*v),derivative(v[1],v[0])],z,
                          bounds=([0,0],[par['abar'],par['abar']]),
                          xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=400)
        res=max(abs(sol.fun))
        if sol.success and res<1e-9 and np.all(sol.x>=0) and np.all(sol.x<=par['abar']):
            if not any(np.max(abs(sol.x-np.array(z)))<1e-7 for z in equilibria):
                for i in range(2):
                    _,vmax=best_response(sol.x[1-i])
                    assert vmax-float(policies(sol.x[i],sol.x[1-i])['GA'])<1e-10
                equilibria.append(sol.x.tolist())
        else:
            rejected_roots.append(dict(start=list(z),success=bool(sol.success),residual=float(res)))
    dynamics=[]
    for z in itertools.product(np.linspace(0,par['abar'],3),repeat=2):
        v=np.array(z)
        for it in range(150):
            nv=np.array([best_response(v[1])[0],best_response(v[0])[0]])
            if max(abs(nv-v))<1e-8:
                break
            v=.5*(nv+v)
        else:
            raise RuntimeError('Best-response dynamics did not converge')
        dynamics.append(dict(start=list(z),end=nv.tolist(),iterations=it+1))
    boundary_kkt=[]
    for r in (0.,par['abar']):
        ownbr,val=best_response(r)
        # For a boundary equilibrium, the boundary player's return deviation must not be profitable.
        rivalbr,rval=best_response(ownbr)
        boundary_kkt.append(dict(rival=r,ownBR=ownbr,rivalBR=rivalbr,
                                 boundary_gain=rval-float(policies(r,ownbr)['GA'])))
        assert abs(rivalbr-r)>1e-4
    zeropar=ZERO_DELTA
    az=brentq(lambda a:float(derivative(a,a,par=zeropar)),0,zeropar['abar'],xtol=2e-15)
    assert abs(az-1/126)<2e-14
    dz=policies(xx,yy,zeropar)
    assert np.unravel_index(np.argmax(dz['W']),dz['W'].shape)==(0,0)
    thresholds={}
    for name,kind in [('gamma_S','W'),('gamma_L','GA')]:
        thresholds[name]=brentq(lambda g:float((2 if kind=='W' else 1)*derivative(0,0,kind,par={**par,'gamma':g})),.44,.54,xtol=2e-15)
    # Independently compute the engineering derivative with readiness fixed.
    hs=1e-24
    eng=0
    for loc in itertools.product((0,1),repeat=2):
        z=continuation(0,0,loc)
        eng+=np.imag(continuation(hs*1j,hs*1j,loc,fixed_readiness=(z['r1'],z['r2']))['S'])/hs/4
    ms=float(2*derivative(0,0,'W'))
    ml=float(derivative(0,0))
    lam=float(derivative(0,0,'p'))
    assert abs(ml-ms/4-2*par['b']*lam)<2e-14
    assert np.max(abs(ev['GA']+ev['GB']-ev['W']))<2e-15
    # Attack clipping independently of the linear-system formula.
    clipped_checks=0
    for aA,aB in itertools.product(np.linspace(0,par['abar'],9),repeat=2):
        for loc in itertools.product((0,1),repeat=2):
            cp=continuation(aA,aB,loc)
            for initial in itertools.product((0.,.5,1.),repeat=2):
                rr=clipped_backup_fixed_point(cp['s1'],cp['s2'],cp['joint'],initial)
                assert max(abs(rr-np.array([cp['r1'],cp['r2']])))<1e-12
                clipped_checks+=1
    # The co-located BR at rival readiness zero DOES clip at the witness.
    unclipped_zero=market(par['gamma'])['pm']*par['q0']/par['k']
    assert unclipped_zero>1 and clipped_backup_response(par['q0'],par['q0'],0.)==1.
    # All figure points are reconstructed from primitive policy derivatives.
    figure_errors=[]
    with (ROOT/'tables/policy_marginals.csv').open() as stream:
        exported=list(csv.DictReader(stream))
    assert len(exported)==101
    for i,row in enumerate(exported):
        gamma=float(Fraction(row['gamma']))
        assert gamma==(440+i)/1000
        params={**par,'gamma':gamma}
        figure_values={'MS':float(2*derivative(0,0,'W',par=params)),
             'ML':float(derivative(0,0,par=params)),
             'lambda':float(derivative(0,0,'p',par=params))}
        for name,val in figure_values.items():
            error=abs(val-float(Fraction(row[name])))
            assert error<3e-12
            figure_errors.append(error)
    with (ROOT/'tables/channel_decomposition.csv').open() as stream:
        exported_channels=list(csv.DictReader(stream))
    independent_channels=[eng,ms-eng,ms,ml]
    assert len(exported_channels)==len(independent_channels)
    for row,val in zip(exported_channels,independent_channels):
        assert abs(float(Fraction(row['exact_value']))-val)<3e-13
    alt={}
    for name,kw in [('nonlinear_risk',dict(nonlinear=True)),('logistic_fit',dict(logistic=True))]:
        ax=brentq(lambda a:float(derivative(a,a,**kw)),0,par['abar'],xtol=2e-15)
        brp,brv=best_response(ax,**kw)
        ag=policies(xx,yy,**kw)
        assert np.unravel_index(np.argmax(ag['W']),ag['W'].shape)==(0,0)
        assert brv-float(policies(ax,ax,**kw)['GA'])<1e-11
        alt[name]=dict(alpha=ax,BR=brp,planner_grid_max_location=[0,0],
                      origin_MS=float(2*derivative(0,0,'W',**kw)),
                      origin_ML=float(derivative(0,0,**kw)),
                      deviation_gain=brv-float(policies(ax,ax,**kw)['GA']))
    # A local perturbation attack supplements, but never replaces, compactness
    # and IFT. Both jurisdictions share each perturbed primitive vector.
    persistence=[]
    small=np.linspace(0,1,31)
    gx,gy=np.meshgrid(small,small,indexing='ij')
    for _ in range(100):
        theta={name:value*(1+rng.uniform(-1e-5,1e-5)) for name,value in par.items()}
        root=brentq(lambda a:float(derivative(a,a,par=theta)),0,theta['abar'],xtol=2e-15)
        pe=policies(theta['abar']*gx,theta['abar']*gy,theta)
        assert np.unravel_index(np.argmax(pe['W']),pe['W'].shape)==(0,0)
        best,bval=best_response(root,theta)
        assert abs(best-root)<4e-8 and bval-float(policies(root,root,theta)['GA'])<1e-11
        contraction=market(theta['gamma'])['delta']*theta['q0']/theta['k']
        assert contraction<1
        persistence.append(dict(alpha=root,backup_contraction=contraction))
    result=dict(seed=20261003,parameters=par,alpha=alpha,planner_W_origin=origin,
                planner_grid_shape=list(ev['W'].shape),random_points=50000,
                max_random_gain=max_random_gain,planner_multistart=optima,
                differential_evolution=dict(success=bool(de.success),argmax=de.x.tolist(),max_gain=float(-de.fun-origin)),
                own_stationary_points=roots,own_grid_points=len(own),ownBR=opt,
                own_boundary_gaps={str(z):float(policies(z,alpha)['GA'])-base for z in (0,par['abar'])},
                own_second_derivative_range=[float(min(own_curvature)),float(max(own_curvature))],
                F_a=float(diag),G_A_AA=float(aa),G_A_AB=float(ab),
                found_policy_equilibria=equilibria,root_initial_conditions=49,
                rejected_root_searches=rejected_roots,best_response_dynamics=dynamics,
                boundary_search=boundary_kkt,location_endpoint_range=[float(min(np.min(ev['u0']),np.min(ev['u1']))),float(max(np.max(ev['u0']),np.max(ev['u1'])))],
                location_contraction_grid_max=float(np.max(abs(ev['slope']))),
                backup_range=[float(min(np.min(v['r1']) for v in ev['profiles'].values())),float(max(np.max(v['r1']) for v in ev['profiles'].values()))],
                clipped_backup=dict(fixed_point_checks=clipped_checks,unclipped_BR_at_rival_zero=float(unclipped_zero)),
                figure_points_checked=len(exported),figure_max_abs_error=max(figure_errors),
                table_rows_checked=len(exported_channels),
                thresholds=thresholds,channels=dict(direct=float(eng),induced=float(ms-eng),MS=ms,ML=ml,attraction=2*par['b']*lam,lambda0=lam),
                zero_delta=dict(alpha=az,MS=float(2*derivative(0,0,'W',par=zeropar)),ML=float(derivative(0,0,par=zeropar))),
                portability_diagnostics=alt,scope='Falsification searches; do not establish policy uniqueness or alternative-family global theorem')
    result['nearby_symmetric_primitive_search']=dict(vectors=len(persistence),relative_radius=1e-5,
        alpha_range=[min(z['alpha'] for z in persistence),max(z['alpha'] for z in persistence)],
        largest_backup_contraction=max(z['backup_contraction'] for z in persistence),
        scope='Numerical attack only; no certified neighborhood radius')
    out=ROOT/'dist'/'independent_numerical_audit_2026-10-03.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('alpha','channels','F_a','found_policy_equilibria','thresholds','zero_delta','portability_diagnostics')},indent=2))


if __name__ == '__main__':
    audit()
