# Stage 11A — Rigorous Global-Certificate Repair

Project: **Public Climate Protection and Private Production Redundancy**  
Frozen input: `62a3a4444783828dc313e974b5e798e30f1fe5a2`  
Repair branch: `repair/stage11a-global-certificate`  
Trigger: Stage 11 hostile-audit verdict `REPAIR`

## Verdict

**PASS — the Stage 11 globality proof gap is repaired without changing the economic mechanism or the canonical parameter witness.**

## Exact certificate

`scripts/verify_global_certificate.py` reconstructs the canonical model over the exact rational-function field `QQ(a_A,a_B)`. It uses tensor-product Bernstein coefficients after affine mapping of the relevant rectangles to `[0,1]^2`. No floating-point arithmetic enters the certificate.

The script certifies:

1. **Continuation regularity on the full policy square.** For every `(a_A,a_B) in [0,2/25]^2`, all backup-system denominators and the location fixed-point denominator are nonzero with certified sign, every backup readiness lies strictly in `(0,1)`, and the equilibrium location probability lies strictly in `(0,1)`.

2. **Global coordinated optimum.** Exact Bernstein signs establish
   `dW/da_A < 0` and `dW/da_B < 0` everywhere on `[0,2/25]^2`. Therefore `W` is strictly decreasing in each coordinate and `(0,0)` is the unique global coordinated optimum.

3. **Exact positive local-policy root.** The diagonal first-order condition `partial G_A(a,a)/partial a_A = 0` has exactly one root on `[0,2/25]`. Exact real-root isolation places it in

   `1649737/71666359 < alpha < 380091/16511564`,

   i.e. approximately `0.0230196848705541 < alpha < 0.0230196848705550`.

4. **Global best response.** For every rival action in the exact isolating interval containing `alpha`, exact Bernstein signs establish
   `partial^2 G_A / partial a_A^2 < 0`
   for every own action in `[0,2/25]`. Hence at `a_B=alpha`, the local objective is strictly concave on the entire feasible interval. Since the exact FOC vanishes at `(alpha,alpha)`, `alpha` is the unique global best response to `alpha`. Symmetry yields the same result for jurisdiction B.

Together these statements replace the former finite-grid/Nelder–Mead evidence for the theorem's global quantifiers with a machine-checkable exact certificate. The legacy numerical routines remain as independent stress tests only.

## Welfare-convention repair

The location shock is now stated explicitly as a Harsanyi-style non-welfare purification device for the discrete location rule, rather than a consumption, profit, or real-resource term. The material welfare criterion therefore integrates over the location distribution induced by the perturbation without assigning welfare weight to the perturbation draw itself. This resolves the Stage 11 convention ambiguity without changing equations or the theorem.

## Theory-change ledger

- Product-market primitives: unchanged.
- Disaster technology: unchanged.
- Backup technology and FOC: unchanged.
- Location probability equation: unchanged.
- Government objectives: unchanged.
- Planner objective: unchanged.
- Canonical witness: unchanged.
- Main theorem statement: unchanged.
- Proof technology: strengthened from numerical global checks to exact Bernstein/root-isolation certification.

## Gate

Stage 11A is complete only when the repository CI runs the new global certificate together with the pre-existing symbolic, policy, numerical, benchmark, pytest, deterministic-object, and LaTeX checks and returns green.
