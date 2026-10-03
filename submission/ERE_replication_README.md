# Anonymized replication package

This archive supplies the source, exact certificates and numerical diagnostics
for a theoretical manuscript. It omits editorial identity files and Git metadata.

## Environment

Use Python 3.13 and install the pinned direct dependencies:

```bash
python -m pip install -r requirements.txt
```

The requirements specify SymPy 1.14.0, NumPy 2.3.5, SciPy 1.17.0,
Matplotlib 3.10.8 and pytest 9.1.1. GNU Make is needed to run the targets.
A standard LaTeX distribution with
`amsmath`, `amsthm`, `mathtools`, `booktabs`, `natbib`, `microtype`, `setspace`,
`hyperref`, `xurl`, `enumitem`, `caption` and `geometry` is required. Debian/Ubuntu's
`texlive-latex-base`, `texlive-latex-recommended` and `texlive-latex-extra`
provide these packages. Exact arithmetic is independent of floating-point
library behavior; numerical optimization and layout may vary by platform.

## Reproduction

From the archive root:

```bash
make verify
```

This runs symbolic and normalization identities, exact root isolation,
whole-domain backup/location/planner and local-best-response certificates,
the full diagonal-FOC derivative needed for the open-set proof, numerical
counterexample searches, the two portability diagnostics, the exact Delta=0
mechanism benchmark, regression tests, exact marginal exhibit generation and
verification, anonymous manuscript checks and a three-pass LaTeX build. It also
regenerates the finite Lean certificate source and large JSON archive.
No title page, author record, submission folder, repository access or Git
checkout is required. Results are mathematical and implementation checks, not
journal-readiness decisions.

The independent audit target reconstructs consumer demand, availability
states, backup and location choices, and welfare without production imports.
It uses a separately implemented Bernstein basis conversion and Sturm root
counts. Only after constructing and certifying those objects does it compare
the production expressions and generated Lean payload. Its numerical grid,
multistart, random and asymmetric-equilibrium searches are falsification
exercises; they do not prove full policy-game uniqueness or an alternative
functional-form theorem. Numerical JSON last digits can vary by platform.

## Formal verification

Install the toolchain declared in `formal/lean-toolchain` using elan and the
Git command for fetching pinned external Lean dependencies. Ensure `lake`
and `git` are on PATH, and run:

```bash
make formal-verify
```

The target explicitly regenerates its certificate dependencies, obtains the
pinned mathlib cache (network access is needed on first installation), runs
the build of all thirteen proof modules, and writes
`formal/FORMAL_AXIOM_REPORT.txt` by checking `Main.lean` with Lean. Linking the
optional native executable is not part of proof reproduction; it would also
compile mathlib C object files absent from the proof cache. Full assumptions,
unformalized bridges, and the `native_decide` extended trust boundary are
listed in `formal/README.md` and in the manuscript appendix. The final Lean
theorem is a conditional implication, not a closed verification of the whole
economic model or its open-set extension.

## Main mathematical objects

- `scripts/verify_global_certificate.py`: whole-policy-domain signs, exact
  symmetric FOC root, own-policy global concavity, clipped-backup contraction,
  and diagonal-FOC derivative.
- `scripts/independent_model_audit.py`: primitive state enumeration, full
  clipped backup map, downstream re-solutions, global numerical searches,
  all 101 figure points and every channel-table row.
- `scripts/independent_exact_audit.py`: separate economic reconstruction,
  triangular Bernstein conversion, Sturm counting, strict rational signs,
  and independent comparison of all eight generated bivariate coefficient
  vectors, endpoint values and the 52 structural Lean rational encodings.
- `scripts/verify_normalization.py`: primitive-to-archive scaling identities.
- `scripts/exact_marginals.py` and `scripts/verify_marginal_exhibits.py`: state
  enumeration with exact forward differentiation, all 101 marginal-figure
  points, both gamma thresholds, readiness wedge and channel decomposition.
- `scripts/verify_benchmarks.py`: exact global Delta=0 witness. Its separate
  canonical continuation recoveries do not solve fixed-location or
  fixed-readiness policy games.
- `scripts/policy_search.py`: numerical FOC candidates with residual checks
  and boundary-inclusive multipeak deviation searches. Finite grids and
  refinements are falsification searches, not whole-domain proofs.
- `scripts/verify_portability_v24.py`: numerical alternatives. Matched-density
  logistic agreement on the symmetric FOC and matched-slope risk agreement
  at the origin are constructional; off-diagonal checks are the additional
  diagnostic evidence.

The permanent public repository and archival citation will be supplied before
final acceptance. The appendix explains the proof; neither a recorded PASS
nor a successful Lean build substitutes for reading its assumptions.
