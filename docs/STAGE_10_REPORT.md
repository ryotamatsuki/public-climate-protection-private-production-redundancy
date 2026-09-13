# Stage 10 — Section-by-Section Paper Construction Report

Project: **Public Climate Protection and Private Production Redundancy**  
Freeze: `PCPPR-THEORY-FREEZE-2026-09-06-v1`  
Target: *RAND Journal of Economics*  
Repository status at Stage 10: deferred by user; local reproducibility package used as authoritative working copy.

## Construction order and section audit

### 2. Model
- File: `paper/sections/02_model.tex`
- Frozen inputs: two jurisdictions, two differentiated firms, linear local protection technology, endogenous primary location, quadratic backup readiness, localized disaster correlation, government and planner objectives.
- Key equations: utility/inverse demand; `q_j=q0-a_j`; backup cost; joint-failure rule; government and national welfare objectives; timing.
- Verification: text compared against `docs/THEORY_FREEZE.md` and `scripts/core_model.py`; no theory changes.
- Unresolved: none.

### 3. Equilibrium Characterization
- File: `paper/sections/03_equilibrium.tex`
- Frozen inputs: Cournot/monopoly continuation payoffs; scarcity-rent wedge; backup FOC; symmetric co-location/dispersed readiness; smooth location fixed point.
- Key results: `Delta'(gamma)>0`; backup choices strategic substitutes; `r^C`, `r^D`; both fall with product substitutability; location probability formula.
- Verification: exact symbolic scripts PASS; benchmark recovery PASS.
- Unresolved: none.

### 4. Main Results
- File: `paper/sections/04_main_results.tex`
- Frozen inputs: exact rational witness; marginal sign certificates; root isolation; decentralized policy root; continuation audit.
- Main claim: Protection–Attraction Conflict — a nonempty open set supports positive decentralized protection while the coordinated optimum is zero.
- Verification: `verify_symbolic.py`, `verify_policy_certificate.py`, and `verify_numerical.py` all PASS.
- Scope discipline: explicitly labels the main theorem as computer-assisted; threshold figure is exposition rather than proof.
- Unresolved: no theoretical blocker; Stage 11 should attack the computer-assisted global-equilibrium certification.

### 5. Welfare
- File: `paper/sections/05_welfare.tex`
- Frozen inputs: exact consumer surplus and total-surplus identities; real backup/public protection costs.
- Generated object: `tables/channel_decomposition.tex` from `scripts/generate_objects.py`.
- Canonical decomposition: direct protection effect positive; endogenous redundancy response larger and negative; total coordinated marginal effect negative; local unilateral marginal payoff positive.
- Verification: generated directly from frozen model; no manual quantitative entries.
- Unresolved: none.

### 6. Nested Benchmarks
- File: `paper/sections/06_benchmarks.tex`
- Frozen inputs: fixed-location and fixed-redundancy benchmarks retained from novelty gate.
- Function: shows that the headline policy regime is full-game-only rather than a claim that each component is new.
- Verification: `verify_benchmarks.py` PASS; benchmark table contains qualitative model logic only.
- Unresolved: none.

### 7. Institutional Interpretation and Empirical Implications
- File: `paper/sections/07_institutional.tex`
- Evidence: Japan Ministry of the Environment local adaptation planning; SME Agency BCP alternatives; METI industrial-location policy; Ehime business-attraction policy.
- Scope: evidence validates primitives but does not claim causal evidence that protection is chosen to attract firms.
- Unresolved: none.

### 8. Related Literature
- File: `paper/sections/08_literature.tex`
- Verified families: regional competition/local public inputs; environmental policy with endogenous plant location; disaster/agglomeration; private adaptation and resilient supply networks; 2026 public-protection/private-defense crowd-out evidence.
- Claim boundary: no novelty claim for adaptation crowd-out, public-input overprovision, capacity strategic substitution, or geographic diversification under risk.
- Unresolved: Stage 11 should re-kill the full-game theorem against any missed closest paper.

### 1. Introduction
- File: `paper/sections/01_introduction.tex`
- Written after the mathematical sections.
- Main framing: public protection changes both local physical risk and private production architecture; jurisdictional competition can keep protection positive after the national marginal value becomes negative.
- Scope: RAND-level big question without claiming general inefficiency of climate protection.
- Unresolved: none.

### 9. Discussion
- File: `paper/sections/09_discussion.tex`
- Function: states policy limits, tractability choices, excluded extensions, and generality conditions.
- Theory drift: none.

### 10. Conclusion
- File: `paper/sections/10_conclusion.tex`
- Function: restates full-game interaction and benchmark distinction without adding claims.

### Appendix
- File: `paper/sections/A_proofs_verification.tex`
- Contents: analytical identities, exact threshold certificates, whole-domain continuation audit, independent evaluator, open-set argument.
- Verification: aligned with Stage 9 artifacts and solver-failure ledger.

## Generated exposition objects
- `figures/policy_regime.pdf`
- `tables/policy_regime.csv`
- `tables/channel_decomposition.csv`
- `tables/channel_decomposition.tex`

All are generated by `scripts/generate_objects.py`.

## Build / verification status

`make verify` passes all theory gates through pytest and object generation in the Stage 10 local reproducibility package. The local TeX distribution lacked the `bibtex` executable, so the draft used a deterministic `references/references.tex` bibliography generated from the maintained `references/references.bib` metadata. The manuscript compiled cleanly with repeated `pdflatex` passes. The final PDF had no unresolved citations/cross-references and no overfull boxes.

- symbolic threshold certificate: PASS
- exact policy certificate: PASS
- numerical/global-deviation audit: PASS
- nested benchmark recovery: PASS
- pytest: 4/4 PASS
- deterministic figure/table generation: PASS
- LaTeX build: PASS
- PDF preflight/render inspection: PASS
- material unresolved continuations: 0
- numerical failures: 0

## Current manuscript at Stage 10

- `paper/main.pdf`
- 17 pages including appendix and references.

## Repository / PR status at Stage 10

No GitHub repository commit or PR was created in Stage 10 because repository creation was explicitly deferred. This was an operational provenance gap only; the local build and verification baseline were complete.

## Stage 11 contract

Stage 11 should conduct a hostile full-manuscript referee gate, with particular attention to:
1. whether the computer-assisted main theorem overstates the strength of the global certification;
2. whether the full-game policy conflict is genuinely non-absorbed by the closest regional-competition and resilience literatures;
3. whether the government objective and the treatment of the location-fit perturbation are welfare-consistent;
4. whether the RAND-level importance claim survives after stripping away known component results;
5. whether any sentence in the Introduction or Discussion exceeds the frozen claim boundary.
