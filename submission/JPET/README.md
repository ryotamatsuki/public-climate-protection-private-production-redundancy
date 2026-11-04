# Journal of Public Economic Theory (JPET) submission overlay

**Status:** editorial candidate, **not submitted**.  
**Base:** the already frozen ERE v4 science; original `paper/`, `references/`, mathematical code, and frozen proof assets are unchanged.  
**Target:** `Journal of Public Economic Theory` (JPET), Original Article.

## What changed

- Journal-facing title, identified author (JPET uses single-anonymized review), structured abstract, JEL and keywords: `submission/JPET/main.tex`.
- Public-economic theory framing and explicit non-novelty of generic public-input overprovision: `sections/01_introduction.tex`.
- Relevant prior literature added and positioned without claiming theorem absorption has been conclusively excluded: `sections/08_literature.tex` and `references.tex`. New references: Bayindir-Upmann (1998); Billon (2023); Morita and Okoshi (2025).
- More bounded public-economics conclusion: `sections/10_conclusion.tex`.
- Journal-specific editorial cover letter and preflight checklist.

**Current PR #41, Round 2 (2026-11-05):** Three simulated reviewer lenses now conditionally favor Major R&R on the basis of a new global primitive region, a positive-gamma open-neighborhood result, and an exact new response-interaction comparative static: the slope of the overprovision gap with respect to a common direct protection benefit is +16/189 when private readiness and location are endogenous, 0 when readiness is fixed, and -16/1593 when location is fixed. These are fully re-solved policy games, not independent publication claims. The published Bayindir-Upmann full theorem comparison remains unfinished. All Round 0 and Round 1 adverse verdicts are archived and remain unaltered.

**Current PR #41 amendment:** The original ERE v4 model, theorem, proofs, certificates and source code remain unchanged. On this separate JPET revision branch, an **additional scientific result** has been inserted in `submission/JPET/sections/06_benchmarks.tex`: a gamma=0 augmented-welfare positive-planner-optimum benchmark with exact, globally certified overprovision. The independent SymPy script is `submission/JPET/review_cycles/positive_optimum_exact.py`. This scientific addition is **not approved by the author** and is NOT part of the historical ERE freeze. The main differentiated-product theorem is unchanged, and this addition does not prove the same positive-optimum result for gamma>0. Retain the submission HOLD until scientific review, revised proof-package creation, and author approval.

**Major R&R resolution audit (Rounds 3–4, 2026-11-05):** The prior Round-2 simulated R&R verdict is not a proof of mathematical correctness. The new global primitive-region proof was found to omit a positive boundary derivative term; it is now replaced by a strictly stronger supporting-hyperplane argument requiring **fewer** primitive assumptions. A second rational parameter witness demonstrates why the removed condition was redundant. See `review_cycles/ROUND_3_MATHEMATICAL_CORRECTION.md`.

The newest candidate additionally relaxes the fixed 1/2 local surplus incidence and fully state-independent hosting benefits, while tying any state-contingent local return to **the primary plant actually operating in that region**, not geographically separate backup production. Exact bivariate Bernstein bounds independently certify an explicit nonzero-perturbation example. The full game's policy reaction to positive product substitutability is derived exactly at the separable limit: both planner and local protection rise, but local protection increases more. The five new full proofs are located in `appendix/additional_proofs.tex`; main propositions remain in `sections/06b_analytic_region.tex`. New checks: `incidence_robustness_exact.py` and `gamma_policy_derivative_exact.py`.

The separate JPET workflow now builds a PDF and a complete tracked-source reproducibility archive with checkout provenance and SHA-256 checksums; old ERE attestation remains immutable. No genuine journal R&R, independent human review, actual acceptance or scientific author approval has occurred.

## Compile

Run from repository root:

```bash
python -m pip install -r requirements.txt
python scripts/generate_objects.py
mkdir -p dist/JPET
cd paper
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -jobname=JPET_manuscript -output-directory=../dist/JPET ../submission/JPET/main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -jobname=JPET_manuscript -output-directory=../dist/JPET ../submission/JPET/main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -jobname=JPET_manuscript -output-directory=../dist/JPET ../submission/JPET/main.tex
```

Result: `dist/JPET/JPET_manuscript.pdf`. The build depends on the original repo's `paper/sections/` and `figures/`.

## Freeze-governance caveat

The historical `scripts/verify_final_audit_freeze.py` verifies the **exact** ERE audited descendant and explicitly rejects any new tracked file. A branch containing this overlay will therefore fail that **historical ERE exact-file-set check by construction**, even though the ERE scientific files remain untouched. Do not weaken or silently update the historical lock to claim that it validates a new journal candidate. Review the JPET overlay independently and implement a new, author-approved JPET freeze/attestation before any merge, if needed. Other verification outcomes must be read separately.

## Journal guidance checked on 2026-11-05

Current Wiley author guidelines (prefer these over legacy ScholarOne-era pages):
- https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html
- https://onlinelibrary.wiley.com/page/journal/14679779/homepage/productinformation.html
- Submission: https://submission.wiley.com/journal/JPET

Journal currently indicates free-format initial submission, no submission fees, max 250-word abstract, up to seven keywords, required ORCID, single-anonymized peer review, and upload of both LaTeX and a peer-review PDF when submitting LaTeX through Research Exchange. Recheck the portal at the actual time of submission.

## Scientific limitations and novelty checks outstanding

1. Bayindir-Upmann (1998) publisher full text is restricted in the sources inspected. Its abstract confirms public-good overprovision but **does not suffice to certify a theorem-level non-absorption**.
2. Billon (2023) full online exposition concerns tax competition, jurisdictional market power and a productive public input; it should not be represented as proving the same private-readiness policy ranking.
3. Morita and Okoshi (2025) links transport investment, firm attraction and welfare under fiscal competition; the welfare mechanism is different, but no general novelty proof is claimed.
4. A targeted theorem-level parent-result check and author signoff remain necessary. The journal-specific positioning is improved, **not an acceptance guarantee**.
