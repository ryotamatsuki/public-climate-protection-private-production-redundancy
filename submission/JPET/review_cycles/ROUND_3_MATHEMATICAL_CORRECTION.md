# Round 3 — Genuine mathematical defect, correction, and falsification audit

**Date:** 2026-11-05. **Classification:** critical self-audit finding in the *new JPET primitive-band proof*, not in the frozen ERE baseline.

## Defect found

The Round 2 supporting proof wrote the planner policy derivative at (x,y)=(0,y) as
```
W_x(0,y) = -mu0 - U'(q0-y/2)*y^2/2 - 2 U(q0-y/2)*y
```
but the complete exact derivative is
```
W_x(0,y) = -mu0 + y/(16k)
           - U'(q0-y/2)*y^2/2 - 2 U(q0-y/2)*y.
```
The omitted `+y/(16k)` means the earlier off-axis boundary argument was invalid. The earlier unqualified simulation had rated mathematical correctness highly but **did not detect this error**; this should lower confidence in self-evaluation and precludes using the earlier simulated editor decision as a mathematical attestation.

## Better global proof (does not strengthen primitives)

The planner `W(x,y)` is strictly concave on the **entire convex policy square** under the original global Hessian/cost inequalities. At the zero-policy corner, `nabla W(0,0)=(-mu0,-mu0)` with `mu0=(q0-3k)/(8k)>0`.

For every nonzero feasible `(x,y)>=0`, strict concavity and differentiability give:
```
W(x,y) < W(0,0) + nabla W(0,0)·(x,y)
       = W(0,0) - mu0*(x+y) < W(0,0).
```
Therefore `(0,0)` is the *unique global* planner optimum without requiring ANY bound on `W_x(0,y)` for unequal policies. The entire erroneous line is removed from the paper proof. No extra cost or restriction is needed beyond strict global concavity and `3k<q0<4k`.

## Additional falsification of unnecessary condition

There is a second strict primitive witness
`(q0,k,H,b,c,a_bar)=(49/200, 2/25, 1/100, 11/200, 20, 2/25)`
that satisfies all retained interiority, Hessian, attraction, positive Nash and cost inequalities, **but fails the previously imposed overstrong off-axis boundary condition**. This proves that the corrective supporting-hyperplane argument materially enlarges the theorem's admissible region, rather than merely manipulating a benchmark already passing an unnecessarily strong restriction.

An independent new exact script `analytic_region_exact.py` verifies the complete boundary derivative, both origin gradient components, all strict rational conditions at the second witness, and that the discarded condition is not satisfied there.

## Status

- [x] Identified omitted mathematical term using independent SymPy differentiation.
- [x] Replaced source proof by strict-concavity supporting-hyperplane argument.
- [x] Removed the unnecessary extra condition from the proposition.
- [x] Added exact regression checks and an additional strict primitive witness.
- [ ] CI results at the final last scientific commit; see GitHub Actions.
- [ ] Independent human mathematical proof read-through remains prudent.

**Main ERE v4 theory files, frozen proof certificates and original source are unchanged.**
