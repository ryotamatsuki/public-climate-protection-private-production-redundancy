# JPET scientific replication: exact formulas, policy games, and provenance

**Revision date:** 2026-11-05. **Status:** revised theoretical candidate; not submitted or author-approved.

## Objective

The JPET draft preserves the canonical ERE v4 source `paper/`, `references/`, `formal/`, `scripts/`, and archived proof assets. All new theoretical statements are in the separate JPET overlay under `submission/JPET/`. The historical ERE immutable tracked-file-set validation is not modified.

A successful **dedicated JPET workflow** checks source identity against the historical ERE reference, re-runs the existing symbolic/global/numerical/independent-exact/test stages, independently checks all new gamma=0 and gamma-derivative assertions, compiles the paper, and uploads a candidate PDF and an independently extractable archive with a SHA-256 manifest.

**Latest relevant CI:** https://github.com/ryotamatsuki/public-climate-protection-private-production-redundancy/actions/workflows/jpet-candidate.yml

## Independent exact scientific checks

Run at the extracted repository root, in a Python environment with `sympy`:

```bash
python submission/JPET/review_cycles/positive_optimum_exact.py
python submission/JPET/review_cycles/restricted_games_exact.py
python submission/JPET/review_cycles/analytic_region_exact.py
python submission/JPET/review_cycles/incidence_robustness_exact.py
python submission/JPET/review_cycles/gamma_policy_derivative_exact.py
```

Scope:
- `positive_optimum_exact.py`: exact welfare/Nash roots and two-dimensional Bernstein Hessian certificates for direct-benefit augmented game.
- `restricted_games_exact.py`: re-optimized full policy games with fixed readiness and fixed location, and exact positive/zero/negative benefit-gap slope signs.
- `analytic_region_exact.py`: symbolic primitive sufficient conditions, strict cost and continuation-interiority inequalities, exact origin planner gradient, and a second witness that contradicts an unnecessary historical restriction. The full global proof uses strict planner concavity and a supporting hyperplane, not an off-axis derivative bound.
- `incidence_robustness_exact.py`: national-surplus share conservation, primary-site-operation-related hosting, a nonzero \(\eta=\rho=1/100\) exact perturbation and bivariate planner/local Hessian certificates.
- `gamma_policy_derivative_exact.py`: first-order derivatives at \(\gamma=0^+\) from complete two-firm Cournot states, private backup readiness and Bayesian location. Exact policy derivative numerators and denominators are checked, plus direct differentiation of the full \(\gamma\)-dependent equations at a separate off-symmetric rational state.

The tests verify mathematical consequences of the stated model, but do **not** constitute a separately published independent proof or a complete Lean formalization of every source-to-certificate bridge.

## Rebuild from downloaded GitHub Actions artifact

Download the `JPET-editorial-candidate` ZIP from the successful workflow for the desired exact commit.

It includes:
- `JPET_manuscript.pdf`
- `JPET_manuscript.txt`
- `JPET_source_bundle.tar.gz` — complete tracked repository state used by the workflow
- `build_commit.txt` — the build checkout commit, which may be a GitHub PR synthetic merge commit
- `SHA256SUMS.txt` — checksums of the candidate PDF and source bundle

```bash
unzip JPET-editorial-candidate.zip -d jpetaudit
cd jpetaudit
sha256sum -c SHA256SUMS.txt
mkdir source
tar xzf JPET_source_bundle.tar.gz -C source
cd source
python -m pip install -r requirements.txt
python scripts/generate_objects.py
mkdir -p dist/JPET
cd paper
for pass in 1 2 3; do
  pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error \
    -jobname=JPET_manuscript -output-directory=../dist/JPET \
    ../submission/JPET/main.tex
done
```

The clean-room workflow was actually reproduced against the downloaded earlier Round-4 artifact on 2026-11-05: all five independent exact tests passed, and the rebuilt 48-page PDF had the same extracted text on every page as the GitHub Actions original. The manifest check initially required path-prefix normalization because the archive flattened stored files; the workflow has since been amended to make the manifest directly usable after unzip. The **corrected manifest** still requires its final successful action run before it can be independently verified from a newly downloaded ZIP.

## Limits

- The Bayindir-Upmann (1998) published full theorem/proof text was not accessible at the public URLs checked, so complete theorem-level absorption has not been certified.
- The direct protection benefit \(\mu\), local surplus incidence and hosting values are stylized economic primitives, not empirically calibrated values.
- The original theorem's full formal-verification trust boundary and partial Lean status are disclosed in the paper.
- All new scientific content requires human author verification and explicit final submission approval.

No action in this document submits a manuscript, modifies the official ERE archive, or merges the draft into the default branch.
