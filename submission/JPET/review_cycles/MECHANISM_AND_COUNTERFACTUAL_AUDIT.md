# Exact mechanism and counterfactual audit — 2026-11-05

**Classification:** New, author-unapproved JPET scientific extensions in PR #41. Not part of historic ERE theorem freeze. Reproducibility files: `positive_optimum_exact.py`, `restricted_games_exact.py`. Exact checks were run locally, independent of archived production certificates; the JPET CI is required to rerun both.

## Baseline separable-product primitives
Gamma=0, q0=3/10, k=2/25, H=1/100, b=11/200, c=10, policy interval [0,2/25]. The private backup response is r(q)=q/(4k); private continuation profit f(q)=(1-q)/4+q^2/(32k), and social contribution t(q)=3(1-q)/8+q^2/(16k). Location p=1/2+[f(qA)-f(qB)]/(2H); national industrial surplus S=2[p t(qA)+(1-p)t(qB)].

At any symmetric origin with gamma=0 and private readiness interior:
- national common-policy origin marginal `MS=(3k-q0)/(4k)`;
- engineering effect holding readiness fixed `E0=3/4(1-q0/(4k))`;
- endogenous-readiness effect `R0=-q0/(16k)`;
- one-jurisdiction attraction response `lambda0=(4k-q0)/(32Hk)`;
- local marginal `ML=[H(3k-q0)+b(4k-q0)]/(16Hk)`.

Thus in the interior band `3k<q0<4k`, the common industrial marginal is negative although engineering direct effects are positive, and `ML>0` precisely if `b>H(q0-3k)/(4k-q0)`. This is a **marginal identity**, not a global-equilibrium theorem or original fiscal-competition law. The baseline global exact result already established planner zero/local positive at the stated rational witness.

## New exact augmented-benefit robustness
Define `G_tilde_j=G_j+mu*a_j` and `W_tilde=W+mu*(aA+aB)`, modeling direct local protection benefits valued by both. For `3/32<mu<227/640`, exact formulas give:
- unique full-square coordinated optimum `aP=(32mu-3)/270>0`;
- positive symmetric Nash equilibrium `aN=(128mu+5)/630>0` and `aN>aP`.
- difference `aN-aP=2(40mu+9)/945>0`.

Full-square exact two-dimensional Bernstein ranges:
- each planner diagonal Hessian entry in `[-2485/256,-1885/256]`;
- determinant in `[128925/2048,2607175/32768]`;
- local-government own-policy second derivative in `[-2845/512,-2245/512]`.
Thus the planner Hessian is everywhere negative definite and each local best response is globally strictly concave. At mu=1/10: `aP=1/1350`, `aN=89/3150`. With b set to zero at that same mu, a positive local Nash level `17/2950` persists; its own-policy Hessian is in `[-5045/512,-4445/512]`. **The augmented case does not make plant attraction necessary for generic overprovision.**

## Exact restricted policy games (unaugmented mu=0)
The two restrictions must each be analyzed as a complete new game, not by setting an on-path derivative to zero.

| Game | Private resilience | Locations | Planner optimum | Symmetric local Nash | Fully solved globally? |
|---|---|---|---|---|---|
| Original exact gamma=0 benchmark | Endogenous r(q) | Endogenous p | (0,0) | (1/126,1/126) | Original Proposition 3, exact certificates |
| Fixed-readiness r*=15/16 | Fixed for all deviations | Re-solved | (3/1280,3/1280) | (5/512,5/512) | Yes: strictly negative planner Hessian; local own Hessian -20405/2048 |
| Fixed-location p=1/2 | Re-solved r(q) | Fixed for all deviations | (0,0) | (0,0) | Yes: both own-policy derivatives negative on full interval |

Fixed-readiness gives location probabilities in [7/16,9/16] and planner Hessian diagonal entries `-10165/1024`, cross `-75/1024` (strictly negative definite). At equal policies the planner derivative is `3/128-10a`, local derivative is `25/256-10a`.

Fixed-location leaves each firm's readiness reoptimized, but p=1/2 and the hosting benefit becomes constant. The global planner derivative is `-3/32-135aA/16<0`, while the local derivative is `-3/64-295aA/32<0`, similarly for B.

**Interpretation:** Readiness crowd-out can overturn the *social industrial* marginal and push optimal protection to zero; attracting mobile production is responsible for positive local investment in this particular planner-zero/local-positive witness. Neither force is universally necessary for all forms of public-input overprovision. This distinction should be a central claim boundary in JPET.

## Limits
This exact audit covers gamma=0 and stated parameters, plus the origin primitive band; it does not prove a fully generalized gamma>0 global theorem or universal necessity/sufficiency statements. An exploratory symbolic differentiation of the gamma=12/25 full policy Hessian exceeded local execution limits, so no new such claim was added.
