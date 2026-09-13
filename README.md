# Public Climate Protection and Private Production Redundancy

Reproducibility and manuscript repository for the theory project **Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power**.

## Research status

- Theory freeze: `PCPPR-THEORY-FREEZE-2026-09-06-v1`
- Manuscript status: Stage 10 complete; draft prepared for hostile referee gate
- Next gate: Stage 11 — hostile full-manuscript referee audit
- Current target: *RAND Journal of Economics*

## Core result

The model combines decentralized place-based climate protection, endogenous primary plant location, costly geographic backup readiness, localized disaster risk, and differentiated-product oligopoly.

The main result is a **Protection–Attraction Conflict**: there exists a nonempty open set of primitives in which coordinated welfare is maximized by zero additional local protection while the decentralized jurisdictional game has a strictly positive symmetric protection equilibrium. Public protection directly lowers disruption risk but can crowd out firms' private geographic redundancy; local governments may nevertheless continue protection because it attracts mobile primary production.

## Repository governance

The frozen theory is authoritative. Verification code may test the frozen model but must not silently modify it.

Any change affecting equilibrium correctness, the policy-ranking theorem, parameter domains, welfare accounting, or the claim boundary must explicitly reopen the relevant research stage before being merged.

## Planned reproducibility layout

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

The Stage 10 local reproducibility package remains the canonical source until all frozen files are imported and checked against this repository.

## Canonical environment

- Python 3.13+
- SymPy 1.14.0
- NumPy 2.3.5
- SciPy 1.17.0
- pytest
- pdfLaTeX

Once the frozen reproducibility package has been imported, the canonical validation entry point will be:

```bash
make verify
```

It must run symbolic identities and threshold certificates, the policy-root certificate, numerical global-deviation and planner audits, nested-benchmark checks, regression tests, deterministic exposition-object generation, and the manuscript build.
