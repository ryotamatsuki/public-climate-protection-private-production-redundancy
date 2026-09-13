# Public Climate Protection and Private Production Redundancy

Reproducibility and manuscript repository for the theory project **Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power**.

## Research status

- Theory freeze: `PCPPR-THEORY-FREEZE-2026-09-06-v1`
- Stage 10 reproducibility freeze commit: `62a3a4444783828dc313e974b5e798e30f1fe5a2`
- Frozen ref: `freeze/pcppr-stage10-2026-09-13`
- Stage 10 GitHub Actions validation: PASS
- Manuscript status: Stage 10 complete; Stage 11 hostile referee gate in progress
- Current target: *RAND Journal of Economics*

## Core result

The model combines decentralized place-based climate protection, endogenous primary plant location, costly geographic backup readiness, localized disaster risk, and differentiated-product oligopoly.

The main result is a **Protection–Attraction Conflict**: there exists a nonempty open set of primitives in which coordinated welfare is maximized by zero additional local protection while the decentralized jurisdictional game has a strictly positive symmetric protection equilibrium. Public protection directly lowers disruption risk but can crowd out firms' private geographic redundancy; local governments may nevertheless continue protection because it attracts mobile primary production.

## Repository governance

The frozen Stage 10 commit is the authoritative pre-audit baseline. Verification and audit code may test that baseline but must not silently modify it.

Any change affecting equilibrium correctness, the policy-ranking theorem, parameter domains, welfare accounting, or the claim boundary must explicitly reopen the relevant research stage before being merged.

## Reproducibility layout

```text
.
├── README.md
├── docs/
│   ├── THEORY_FREEZE.md
│   ├── STAGE_10_REPORT.md
│   └── PROVENANCE.md
├── paper/
│   ├── main.tex
│   └── sections/
├── scripts/
│   ├── core_model.py
│   ├── verify_symbolic.py
│   ├── verify_policy_certificate.py
│   ├── verify_numerical.py
│   ├── verify_benchmarks.py
│   └── generate_objects.py
├── tests/
├── figures/
├── tables/
└── references/
```

Generated figure/table objects and the manuscript PDF are rebuilt deterministically by the verification pipeline rather than treated as independent theory sources.

## Canonical environment

- Python 3.13+
- SymPy 1.14.0
- NumPy 2.3.5
- SciPy 1.17.0
- Matplotlib 3.10.8
- pytest
- pdfLaTeX

Canonical validation entry point:

```bash
make verify
```

It runs symbolic identities and threshold certificates, the policy-root certificate, numerical global-deviation and planner audits, nested-benchmark checks, regression tests, deterministic exposition-object generation, and the manuscript build.
