# Stage 11 — Independent Hostile Full-Manuscript Referee Gate

**Audit date:** 2026-09-13  
**Frozen target:** `62a3a4444783828dc313e974b5e798e30f1fe5a2`  
**Frozen ref:** `freeze/pcppr-stage10-2026-09-13`  
**Theory freeze:** `PCPPR-THEORY-FREEZE-2026-09-06-v1`

## Executive verdict

**REPAIR — the core mechanism survives, but Theorem 1 is not yet supported by a proof-grade global certificate.**

No counterexample to the Protection–Attraction Conflict was found. A clean-room reconstruction reproduces the product-market, backup, location, welfare, and local-policy objects. Independent global numerical attacks strongly support the canonical witness. The material defect is evidentiary: the manuscript calls Theorem 1 computer-assisted, but the decisive global claims are currently certified by finite grids and non-rigorous numerical optimizers rather than interval/exact global verification.

This is **not** a rollback to the research question and **not** a STOP verdict. It is a theorem-certification repair gate.

## 1. Independent mathematical reconstruction

The audit did not import `scripts/core_model.py`. Starting from the manuscript primitives it recovered:

- duopoly profit `pi_D = 1/(2+gamma)^2`;
- monopoly profit `pi_M = 1/4`;
- scarcity-rent wedge `Delta = pi_M-pi_D = gamma(gamma+4)/(4(gamma+2)^2)`;
- `Delta'(gamma)=2/(gamma+2)^3>0`;
- backup FOC `k r_i = pi_D s_i + Delta J(1-r_j)`;
- the linear location-probability fixed point;
- state-enumerated product-market surplus and private backup costs;
- the government and coordinated objectives printed in the manuscript.

At the canonical witness the backup best-response absolute slope is bounded by

`Delta*q0/k = 75600/162409 ≈ 0.46549144 < 1`,

so the interior backup fixed point is a contraction throughout the maintained risk domain. No alternative backup Nash equilibrium was found.

## 2. Global-deviation and boundary audit

The independent script `audit/stage11_independent_audit.py` reconstructs the model from primitives and does not call the author's model code.

At the witness:

- differential evolution selects the planner solution numerically at `(0,0)` (up to ~1e-11 search noise);
- `W(0,0)=0.6183204099408616`;
- on a `201 x 201` full policy grid, complex-step partial derivatives satisfy
  - `dW/da_A in [-0.2020107732, -0.0032412321]`,
  - `dW/da_B in [-0.2020107732, -0.0032412321]`;
- on the same full square, equilibrium location probability remains in `[0.42043150, 0.57956850]`;
- backup readiness remains in `[0.64498382, 0.90847405]`;
- the untruncated location best-response endpoint probabilities remain in `[0.32245937, 0.67754063]`;
- the location best-response slope is in `[-0.24571968, -0.08404296]`, so the sampled location game stays interior and its affine best-response system is uniquely pinned down;
- against the exact policy-root interval midpoint, an independent global optimizer returns a best response `0.0230196819`, numerically indistinguishable from the certified candidate `0.0230196849` in payoff;
- the independent derivative of the local payoff has exactly one sign change on a 1,001-point policy grid.

No boundary continuation, solver failure, or profitable deviation was found.

## 3. Major finding: globality is not rigorously certified

The frozen verifier `scripts/verify_numerical.py` uses:

1. an `81 x 81` planner grid;
2. six Nelder–Mead starts;
3. `scipy.optimize.minimize_scalar(method='bounded')` for the local best response;
4. a 2,001-point deviation grid with tolerance.

These are strong numerical diagnostics but are not a mathematical certificate over a continuum. In particular:

- the exact polynomial certificate proves the marginal signs and the symmetric FOC/root statements;
- it does **not** prove `W(a_A,a_B) <= W(0,0)` for every point of the full two-dimensional policy rectangle;
- it does **not** prove that the symmetric algebraic policy root is a global best response against the rival's algebraic root for every unilateral deviation.

Therefore the sentence that Theorem 1 is proved by a computer-assisted global certification currently overstates what the stored certificate establishes. Since global planner optimality and Nash best response are quantifiers inside the theorem, this is a material proof gap even though all numerical attacks support the claim.

### Required repair gate

Before a GO verdict, add a rigorous certificate, for example:

- exact/interval branch-and-bound for `W(0,0)-W(a_A,a_B)` on `[0,2/25]^2`;
- Bernstein-polynomial positivity or another certified multivariate inequality proof for the planner block;
- exact algebraic-number/interval verification that `G_A(a*,a*)-G_A(a_A,a*) >= 0` for all `a_A in [0,2/25]`;
- certified denominator positivity and continuation interiority on every branch used by those inequalities.

A denser grid is not a sufficient repair.

## 4. Government objective and location-fit perturbation

The location-fit shock `epsilon_i` is payoff-relevant for firm location choice but explicitly excluded from the social objective. This is not literally welfare-consistent unless the shock is microfounded as a non-welfare purification/selection device or a transfer-like payoff component.

The audit tested the natural alternative in which the selected location-fit payoff is included in welfare. For the manuscript's uniform shock, the expected selected contribution of the two firms is

`H/2 - D^2/(2H)`, where equilibrium `D=2H(p-1/2)`.

Numerically adding this term leaves the canonical ranking intact: the planner remains at zero and the local best response remains at the positive candidate to numerical precision. Thus this issue does not generate a counterexample, but the manuscript must either (a) microfound the exclusion cleanly or (b) include the term and re-certify the theorem.

## 5. Welfare-accounting audit

The state-by-state surplus accounting is internally consistent. The direct public-protection effect at the witness is positive, while the endogenous private-redundancy response is larger and negative. The local-government payoff additionally values expected plant attraction. No double counting of private backup cost or public protection cost was found.

Also, `G_A+G_B=W` for the printed government objectives when local plant benefits sum to the constant national `2b`, so the decentralization wedge is a distributional/strategic plant-attraction wedge rather than an accounting error.

## 6. Closest-literature re-kill

The closest families remain distinct from the full-game theorem:

| Literature | Overlap | Missing relative to PCPPR |
|---|---|---|
| Markusen, Morey & Olewiler (1993) | environmental policy, endogenous plant number/location, imperfect competition | endogenous private geographic backup and local protection competition |
| Markusen, Morey & Olewiler (1995) | regional environmental-policy competition, endogenous plant location | public-protection/private-redundancy substitution |
| Walz & Wellisch (1996); Maurer & Walz (2000) | local public inputs, mobile oligopolistic firms, regional competition | disaster risk and endogenous private redundancy |
| Otazawa et al. (2016) | disaster risk, industrial agglomeration, mitigation policy | firm-level backup readiness and plant-attraction protection game |
| Eisenack (2014) | private adaptation with endogenous market structure | mobile production and decentralized place-based protection |
| Capponi, Du & Stiglitz (2024/25) | market power and inefficient resilience investment | location-specific public protection and jurisdictional competition |
| Castro-Vincenzi et al. (2024/25) | geographic diversification under climate risk | public-protection crowd-out and local policy competition |
| Zhao, Yang & Zhang (2026) | direct evidence that public flood protection crowds out private defenses and raises tail-risk losses | strategic competition among jurisdictions for mobile oligopolistic production |

Zhao, Yang & Zhang (2026) materially narrows the novelty claim: public/private resilience substitution cannot be presented as new. The manuscript already acknowledges this. The surviving contribution is the joint policy-ranking result created by combining crowd-out with plant attraction in a decentralized oligopoly/location game.

## 7. Claim-boundary audit

The Introduction and Discussion are mostly disciplined: they explicitly deny a general claim that climate protection is excessive and do not claim that the causal plant-attraction channel has already been identified empirically.

One claim must be weakened until the repair gate is passed: references to a proof-grade 'whole-domain' or 'global' computer-assisted certification should distinguish exact certificates from non-rigorous numerical stress tests.

## 8. RAND-level importance gate

The mechanism is economically coherent and timely, and the 2026 flood-protection evidence increases its policy relevance. The novelty re-kill did not find an existing paper that combines all of the relevant margins into the same policy-ranking theorem.

However, the current RAND case is not yet secure. After stripping away known components, the paper's structural contribution is an existence result built around one rational witness and a deliberately minimal two-region/two-firm environment. A rigorous global certificate is necessary but may not be sufficient for RAND; the referee may still ask whether the interaction yields a broader analytical condition or robust comparative-static insight rather than a verified existence region.

This is an importance risk, not a mathematical counterexample.

## 9. Solver-failure ledger

- clean-room primitive reconstruction: PASS
- independent planner global numerical attack: PASS (no counterexample)
- full-square continuation stress grid: PASS
- local-government global numerical attack: PASS (no counterexample)
- boundary backup equilibrium search: no alternative equilibrium found; contraction bound < 1
- location mixed-choice boundary search: no boundary equilibrium found on stress domain
- location-fit-inclusive welfare variant: headline ranking survives numerically
- independent numerical exceptions: 0
- rigorous bivariate global certificate: **MISSING**
- rigorous algebraic unilateral-deviation certificate: **MISSING**

## Final routing

**REPAIR.** Keep the frozen Stage 10 commit unchanged. Do not reopen the economic mechanism unless the rigorous global certificate fails. The next authorized task is a narrow Stage-11A global-certificate repair on a new branch, followed by re-running this hostile gate against the repaired freeze.
