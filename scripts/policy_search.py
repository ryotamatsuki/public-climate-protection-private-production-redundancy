"""Numerical counterexample searches, never whole-domain equilibrium proofs.

Candidates are zeros of the continuous diagonal FOC, not sign changes of a
potentially discontinuous best-response selection. Every returned candidate
passes residual and boundary-inclusive multipeak deviation checks.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar


def maximize_interval(payoff, upper, *, grid_size=1001):
    xs = np.linspace(0.0, upper, grid_size)
    values = [float(payoff(float(x))) for x in xs]
    if not all(map(math.isfinite, values)):
        raise ValueError('nonfinite payoff in deviation search')
    candidates = [(float(x), value) for x,value in zip(xs,values)]
    # Refine every grid-detected peak, and explicitly retain both boundaries.
    for i in range(1,len(xs)-1):
        if values[i] >= values[i-1] and values[i] >= values[i+1]:
            z = minimize_scalar(lambda x:-payoff(float(x)),
                                bounds=(float(xs[i-1]),float(xs[i+1])), method='bounded',
                                options={'xatol':1e-13,'maxiter':1000})
            if not z.success or not math.isfinite(z.fun):
                raise RuntimeError('local peak refinement failed')
            candidates.append((float(z.x),float(-z.fun)))
    return max(candidates,key=lambda z:z[1])


def own_derivative(payoff, x, y, upper):
    # Fourth-order finite differences, with explicit one-sided boundary stencils.
    h = min(2e-6,upper/1000)
    if x < 2*h:
        f = [payoff(x+i*h,y) for i in range(5)]
        return (-25*f[0]+48*f[1]-36*f[2]+16*f[3]-3*f[4])/(12*h)
    if x > upper-2*h:
        f = [payoff(x-i*h,y) for i in range(5)]
        return (25*f[0]-48*f[1]+36*f[2]-16*f[3]+3*f[4])/(12*h)
    return (payoff(x-2*h,y)-8*payoff(x-h,y)+8*payoff(x+h,y)-payoff(x+2*h,y))/(12*h)


def symmetric_candidates(payoff, upper, *, scan_size=401, gain_tolerance=1e-10):
    def foc(a): return own_derivative(payoff,a,a,upper)
    scan = np.linspace(0.0,upper,scan_size)
    vals = [foc(float(x)) for x in scan]
    if not all(map(math.isfinite,vals)):
        raise ValueError('nonfinite diagonal FOC')
    candidates = [0.0,upper]
    for lo,hi,flo,fhi in zip(scan[:-1],scan[1:],vals[:-1],vals[1:]):
        if flo == 0:
            candidates.append(float(lo))
        if flo*fhi < 0:
            root = brentq(foc,float(lo),float(hi),xtol=1e-12)
            # A converged bracket alone is insufficient; check the actual residual.
            if abs(foc(root)) <= 1e-7:
                candidates.append(float(root))
    accepted = []
    for a in sorted(candidates):
        if accepted and abs(a-accepted[-1]['policy']) < 1e-7:
            continue
        best_x,best_value = maximize_interval(lambda x:payoff(x,a),upper)
        gain = best_value-payoff(a,a)
        if gain <= gain_tolerance:
            accepted.append({'policy':a,'foc_residual':foc(a),
                             'best_deviation_policy':best_x,'max_deviation_gain':gain})
    return accepted
