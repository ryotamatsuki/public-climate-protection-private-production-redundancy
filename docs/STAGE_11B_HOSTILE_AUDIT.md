# Stage 11B — Post-Repair Adversarial Re-Audit

**Audit date:** 2026-09-13  
**Frozen target:** `2a6f5b2519acfbbe1d4e7afcf536baad839830c0`  
**Frozen ref:** `freeze/pcppr-stage11a-2026-09-13`

## Executive verdict

**REPAIR — Stage 11A successfully repaired the main global-policy proof gap, but the new certificate still omits an exact uniqueness/no-clipping certificate for the location subgame, and the literature positioning misses a materially close flood-location/adaptation paper.**

No counterexample to Theorem 1 was found. An independent reconstruction using a separately coded direct affine-expansion/tensor-Bernstein conversion reproduces the Stage 11A global planner signs, the exact local-policy root, and global own-policy concavity. The missing location-subgame conditions also hold exactly at the canonical witness and can be added without changing the theory.

## 1. Independent validation of the Bernstein proof technology

The audit script `audit/stage11b_independent_certificate_audit.py` does not import either `scripts/verify_global_certificate.py` or `scripts/core_model.py`. It reconstructs the model from the primitive formulas and uses a different Bernstein conversion: every monomial is directly expanded under the affine rectangle map and then converted to tensor Bernstein coefficients with the closed-form power-to-Bernstein formula.

The independent calculation reproduces:

- strict positivity and interiority of the stored backup continuations on the full policy square;
- strict negativity of `dW/da_A` and `dW/da_B` on `[0,2/25]^2`;
- the same unique diagonal local-government root interval;
- strict negativity of `d^2 G_A / da_A^2` on the full own-policy interval for every rival action in the exact root enclosure.

The Stage 11A convex-hull argument is therefore not an artifact of the particular implementation of the Bernstein converter.

## 2. Remaining proof omission: location-subgame global validity

The repaired Stage 11A certificate proves that the **symmetric fixed-point probability** `p` lies in `(0,1)` and that its denominator has fixed sign. This is not, by itself, a complete certificate that the underlying Bayesian location best-response map is globally untruncated and has a unique equilibrium.

With

`D(z)=z d_A+(1-z)d_B`,

an interior location best response is

`BR(z)=1/2 + D(z)/(2H)`.

To justify that formula for every rival probability `z in [0,1]`, it is sufficient to prove that the endpoint probabilities

`u_0=(H+d_B)/(2H)` and `u_1=(H+d_A)/(2H)`

both lie in `(0,1)` throughout the complete first-stage policy square. To establish uniqueness of the simultaneous location-probability equilibrium it is sufficient here to certify

`|B|<1`, where `B=(d_A-d_B)/(2H)`.

The independent exact Bernstein audit proves all four missing inequalities on `[0,2/25]^2`:

- `0<u_0<1`;
- `0<u_1<1`;
- `1-B>0`;
- `1+B>0`.

Thus the theorem survives the attack. The defect is that these exact checks are not yet part of the canonical Stage 11A certificate or proof appendix. They should be promoted into `scripts/verify_global_certificate.py` and the location subsection should state explicitly that the shocks are privately observed before simultaneous location choice. This is a verification/exposition repair, not a theory reopening.

## 3. Open-set quantifier audit

The open-set step is defensible once the location conditions above are included. The exact Bernstein certificates give uniform strict margins on compact policy rectangles, the local-policy root is interior and simple because own-policy curvature is strictly negative, and all continuation denominators and interiority inequalities have strict margins. After normalizing the moving upper policy bound to a unit interval (or taking a slightly larger common rectangle around the witness), continuity in primitives and the implicit-function theorem yield persistence in a neighborhood of the witness.

The appendix should make that compactness/IFT step explicit rather than relying only on an informal appeal to continuity.

## 4. Location-fit shock and welfare convention

Stage 11A now describes the location shock as a non-welfare purification device. This produces a coherent reduced-form decision rule if the distinction between decision perturbations and material surplus is taken as primitive, but the phrase “Harsanyi-style” may invite a reviewer to object that Harsanyi purification normally perturbs payoffs.

The result is nevertheless robust to the natural alternative of counting the selected location-fit payoff in welfare. Under the manuscript's one-dimensional uniform perturbation, the expected selected contribution of the two firms is

`R(D)=H/2-D^2/(2H) <= H/2`,

with equality at `D=0`. At every symmetric policy profile, including `(0,0)` and `(alpha,alpha)`, symmetry gives `D=0`. Since the baseline planner objective is globally maximized at `(0,0)`, adding `R(D)` cannot overturn the planner result. Against rival policy `alpha`, the baseline local payoff is globally maximized at `alpha`, and the additional half-share `R(D)/2` is also maximized at `D=0`, which occurs at the symmetric action. Hence the positive local equilibrium also survives this welfare convention exactly.

Recommended repair: state the private-information/purification convention precisely and add this robustness argument as a short remark or appendix result.

## 5. Closest-literature re-kill

One materially close paper is missing from the current literature section:

- Grames, Grass, Kort, Prskawetz et al., “Optimal investment and location decisions of a firm in a flood risk area using impulse control theory,” *Central European Journal of Operations Research* 27 (2019), 1051–1077, DOI `10.1007/s10100-018-0532-0`.

That paper jointly studies flood-risk location and private flood-protection investment and explicitly reports that when government flood defense is already present, firms move closer to the water and invest less in their own flood defense. Thus **public protection -> riskier/more concentrated location plus lower private protection** is prior art and should not be implied to be new.

A second nearby paper, Meng, Ding & Wang, “Urban resilience under local government competition: A new perspective on industrial resilience,” *Cities* 155 (2024), studies local-government competition and industrial resilience empirically/theoretically, although through market segmentation and industrial-structure distortion rather than endogenous firm-level backup readiness.

The surviving novelty is narrower but still distinct: decentralized governments use protection to attract mobile oligopolistic primary production, while that same protection changes endogenous geographic redundancy, producing a local-versus-coordinated **policy-ranking reversal** in a single solved game.

## 6. RAND-level importance

Correctness is now substantially stronger than at Stage 10. The remaining concern is contribution scale, not validity. Several ingredients are individually established in prior work: local-public-input competition for mobile oligopolistic firms, policy-induced plant location, disaster/agglomeration vulnerability, public/private protection substitution, and geographic diversification under climate risk. The manuscript's incremental contribution is their interaction and the resulting policy-ranking reversal.

For *RAND Journal of Economics*, an existence theorem supported by one canonical rational witness may still be viewed as too example-specific unless the paper extracts a broader analytical condition or economically transparent sufficient-statistic characterization. The most valuable strengthening would be a proposition expressing the conflict in terms of three interpretable margins: the direct engineering protection benefit, the induced-redundancy response, and the plant-attraction externality. This is an importance/positioning repair, not a correctness repair.

## Required repair before GO

1. Add exact endpoint/no-clipping and `|B|<1` location-map checks to the canonical global certificate.
2. State the private-information structure of the location shocks explicitly.
3. Add the exact welfare-robustness argument for counting selected fit payoff, or replace “Harsanyi-style” with a less contestable decision-noise interpretation.
4. Add Grames et al. (2019) and Meng et al. (2024) to the closest-literature matrix and narrow the novelty wording accordingly.
5. Before committing to RAND as first submission, either derive a more general sufficient-condition result or explicitly accept that target fit remains borderline.

**Verdict: REPAIR. No rollback of the core theorem is warranted.**
