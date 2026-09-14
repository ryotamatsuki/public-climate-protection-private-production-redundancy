# Public Climate Protection and Private Production Redundancy

Reproducibility and manuscript repository for the theory project **Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power**.

## Research status

- Current theory freeze record: `PCPPR-THEORY-FREEZE-2026-09-14-v2`
- Historical Stage 12 freeze commit: `134ff145a89afb78c587d10081caf1a4bdb1601f`
- Current repair: Stage 12R independent-mathematical-audit repair
- Stage 12 editorial verdict: RAND as a one-shot stretch, JEEM as the immediate fallback
- Stage 13 submission formatting remains blocked until Stage 12R is merged, fully verified, and refrozen

## Core result

The model combines decentralized place-based climate protection, endogenous primary plant location, costly geographic backup readiness, localized disaster risk, and differentiated-product oligopoly.

The main result is a **Protection–Attraction Conflict**: within the maintained symmetric primitive family, there exists a nonempty open set in which coordinated welfare is maximized by zero additional local protection while the decentralized jurisdictional game has a strictly positive symmetric protection equilibrium. Public protection directly lowers disruption risk but can crowd out firms' private geographic redundancy; local governments may nevertheless continue protection because it attracts mobile primary production.

The baseline probability law is explicit. Conditional on realized primary failures, backup-success draws are independent across firms, with success probability `r_i` for firm `i` when its primary plant fails. Hence joint final unavailability is `J(1-r_1)(1-r_2)`. This law is a primitive of the model rather than an implication of the marginal readiness probabilities alone.

## Repository governance

Every submission candidate must point to an explicit freeze commit. Any change affecting probability primitives, equilibrium correctness, the policy-ranking theorem, parameter domains, welfare accounting, benchmark definitions, or the claim boundary reopens the relevant research gate.

The auxiliary coefficient archive contains scaled rational-function representations. `docs/certificate_normalization.json` records the exact factors and `scripts/verify_normalization.py` reconstructs the corresponding economic functions from primitives to verify the identities.

## Reproducibility layout

```text
.
├── README.md
├── docs/
│   ├── THEORY_FREEZE.md
│   ├── PROVENANCE.md
│   ├── STAGE_10_REPORT.md
│   ├── STAGE_11A_REPORT.md
│   ├── STAGE_11C_REPORT.md
│   ├── STAGE_12_REPORT.md
│   ├── certificate_polynomials.json
│   └── certificate_normalization.json
├── paper/
│   ├── main.tex
│   └── sections/
├── scripts/
│   ├── core_model.py
│   ├── direct_evaluator.py
│   ├── verify_symbolic.py
│   ├── verify_normalization.py
│   ├── verify_policy_certificate.py
│   ├── verify_global_certificate.py
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

It runs symbolic identities and threshold certificates, primitive-to-certificate normalization identities, the policy-root certificate, the exact whole-domain certificate, numerical global-deviation and planner stress tests, nested-benchmark checks, regression tests, deterministic exposition-object generation, and the manuscript build.
