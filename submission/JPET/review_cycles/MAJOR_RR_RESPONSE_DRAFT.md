# Major R&R response dossier — simulated reviewer comments only

**Not a response to genuine JPET referees.** These comments summarize the project's Round 2 simulated Major R&R assessment and are answered as an adversarial R&R-resolution test. Date 2026-11-05. No journal submission or merge is authorized.

## Editor: "The research must show a public-economics contribution beyond combining old overprovision and self-protection results."

**Response.** Revised theoretical contribution is a *policy comparative-static interaction*, not generic overinvestment. With a common local nonindustrial protection benefit mu, the derivative of the local-versus-social provision gap is **+16/189** under endogenous private backup and mobility; **0** when backup is frozen and locations re-optimized; and **−16/1593** when locations are frozen but private backup re-optimized. All three are globally solved policy games. The analytic primitive region provides strict interpretable sufficient conditions; a continuity proposition extends the positive-gap comparative static to a nonempty open subset with `gamma>0`. Manuscript: Proposition `benefit-gap-response-interaction`, `global-primitive-band`, `positive-gamma-extension`.

**Residual limitation.** Not proved for all gamma. Parent paper Bayindir-Upmann (1998) full theorem text was not available; literature nonabsorption is conditional on accessible material, **not exhaustively certified**.

## Referee 1: "Public-input overprovision is old; how is this not mechanically anticipated by Bayindir-Upmann, Keen–Marchand, Billon, Walz–Wellisch?"

**Response.** The Introduction and Literature section now concede productive public-input overprovision and generic firm attraction are old, explicitly add Keen and Marchand (1997), Matsumoto (1998), Pauser (2026, JPET), and explain different choice variables and policy instruments. The new full-equilibrium sign pattern for *the benefit response of the provision gap* is not asserted as a universal novelty claim, and has not been demonstrated as a corollary of the published parent theorems. Restricted access to Bayindir-Upmann's actual 1998 proof is disclosed.

**Required external confirmation.** The theorem-by-theorem mapping remains open, subject to obtaining legitimate access to that original article. Do not fabricate page or proposition numbers.

## Referee 2: "Do the global claims actually follow from the equations, not merely on-path policy FOCs?"

**Response.** New exact standalone SymPy scripts rederive primitive profit/availability/market surplus and include bivariate Bernstein certificates for full-domain negative-definite planner Hessians and strictly negative local own-policy curvature. New restricted policy games re-solve all first-stage deviations. Positive-gamma continuation follows from uniform private cutoffs, nonsingular backup system, compact-domain Hessian strictness and IFT. ERE frozen source remains immutable and the JPET-specific workflow re-runs original model tests without bypassing old tracked-set attestations.

**Crucial discovered error and correction.** The Round 2 primitive-region proof omitted a positive `y/(16k)` term in a boundary derivative. The incorrect proof was removed. A stronger, cleaner strict-concavity supporting-hyperplane argument establishes planner global optimality **with weaker primitive assumptions**, as recorded in `ROUND_3_MATHEMATICAL_CORRECTION.md`. The error is not concealed or rebranded as cosmetic. Proofs of the new propositions were moved to `submission/JPET/appendix/additional_proofs.tex`.

## Referee 3: "Exact half-incidence of national surplus and state-independent plant hosting are ad hoc."

**Response.** New Proposition `incidence-robustness` allows a location-dependent national industrial-surplus allocation `theta_A(p)=1/2+eta*(p-1/2)` and a fraction rho of hosting benefits conditional on the *primary plant itself operating in the hosting region*. The latter no longer credits a host for geographically separate backup operations. The coordinated welfare objective sums these regional objectives and is unaffected by the national surplus redistribution. Compactness and strict nondegenerate continuations show persistence of the positive social optimum, excessive local Nash provision, and positive common-benefit gap slope for small `gamma>0`, `eta`, `rho` and `mu-1/10`. At gamma=rho=eta=0, the local policy response to strengthening location-linked income incidence is the exact positive rational `19956004/78764805`.

**Independent numeric/example evidence.** `incidence_robustness_exact.py` reconstructs the revised gamma=0 primary-hosting model from primitives, tests surplus conservation, verifies the exact incidence derivative, and certifies global two-dimensional Hessian signs at `eta=rho=1/100,mu=1/10`. This is a concrete finite-perturbation witness in addition to the analytic open-neighborhood proof.

**Residual limitation.** Neither income incidence nor hosting is fully microfounded in a labor/ownership/capital-budget economy. The model is a disciplined reduced-form policy game, not an exhaustive local government finance model.

## Presentation: "A theory article should distinguish novelty, intuition and technical proof."

**Response.** Main text contains the economic conditions, proposition statements, and globally solved counterfactual results. Four full new proofs were relocated, unchanged in substance, to the new dedicated mathematical Appendix. The structured abstract matches Wiley's Background/Methods/Results/Conclusions guidance and remains within 250 words. Journal-specific bibliography adds the 2026 JPET contribution by Pauser.

## Reproducibility: "Can reviewers rerun the *current* paper?"

**Response.** Dedicated `jpet-candidate.yml` verifies unmodified ERE scientific source against an archival reference, executes old symbolic/global/numerical/test stages, executes all new standalone exact scripts, compiles the JPET PDF, then produces a complete tracked-source `tar.gz` with checksums and checkout SHA. Old ERE historical tracked-file-set CI remains untouched and is not renamed as a success.

## Additional mathematical finding: product substitutability directly amplifies the fiscal distortion

**Response.** A fifth new proposition now differentiates the entire state-contingent oligopoly continuation at the separable-product boundary. It differentiates private backup best responses, firm-level disaster-state profits, the Bayesian primary-location probability, and national expected market surplus *before* taking the local government's unilateral policy derivative. At the augmented optimum, the exact right derivatives are `daP/dgamma=29820457/354294000>0` and `daN/dgamma=3355337640241/15630875552250>0`. Their difference is `16317660285149/125047004418000>0`. Thus stronger product substitutability raises both socially coordinated and decentralized protection at these primitives, but **magnifies the excess local level**. This gives differentiated Cournot competition a concrete equilibrium role beyond the existence of disaster-state monopoly rents. A separate exact script `gamma_policy_derivative_exact.py` reconstructs profile-specific first-order profit and welfare responses and cross-checks directly against full gamma-dependent Cournot formulas.

**Scope:** A one-sided derivative at gamma=0 with local persistence for small gamma>0. It is not a monotonicity claim across all gamma values or all economic primitives.

## Source and editorial completeness

Four full newly proposed proofs were moved from the main text to a labeled additional-theory appendix; a fifth complete gamma-policy-comparative-static proof is included there. The updated author cover letter identifies the genuinely new comparative-static result rather than relying on generic local-public-input overprovision. A reproducible source tarball and SHA-256 checksums are generated by the JPET GitHub workflow, subject to the final run's successful artifact and independent extraction check.

## Scope of final judgment

**This is a response dossier, not acceptance.** A final independent re-review should veto ACCEPT-CALIBER if the new source code fails, the math proof is contradicted, or an important parent theorem demonstrably absorbs the interaction result. Without a real editor and two independent external experts, all conclusions are internal and conditional.

The author must independently review and authorize scientific changes and any actual submission.
