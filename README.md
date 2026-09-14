# Public Climate Protection and Private Production Redundancy

Reproducibility and manuscript repository for the theory project **Public Climate Protection and Private Production Redundancy: Local Resilience Competition, Plant Location, and Disaster-State Market Power**.

## Research status

- Current theory freeze record: `PCPPR-THEORY-FREEZE-2026-09-14-v2`
- Stage 12R merged checkpoint: `7a02e1b8558d8059c72287f2e226b74161ce36b3`
- Stage 13 ERE submission package merged through PR #12
- Current journal target: *Environmental and Resource Economics (ERE)*
- Current phase: final ERE submission freeze / administrative metadata completion

## Core result

The model combines decentralized place-based climate protection, endogenous primary plant location, costly geographic backup readiness, localized disaster risk, and differentiated-product oligopoly.

The main result is a **Protection–Attraction Conflict**: within the maintained symmetric primitive family, there exists a nonempty open set in which coordinated welfare is maximized by zero additional local protection while the decentralized jurisdictional game has a strictly positive symmetric protection equilibrium. Public protection directly lowers disruption risk but can crowd out firms' private geographic redundancy; local governments may nevertheless continue protection because it attracts mobile primary production.

The baseline probability law is explicit. Conditional on realized primary failures, backup-success draws are independent across firms, with success probability `r_i` for firm `i` when its primary plant fails. Hence joint final unavailability is `J(1-r_1)(1-r_2)`. This law is a primitive of the model rather than an implication of the marginal readiness probabilities alone.

## Repository governance

Every submission candidate must point to an explicit freeze commit. Any change affecting probability primitives, equilibrium correctness, the policy-ranking theorem, parameter domains, welfare accounting, benchmark definitions, or the claim boundary reopens the relevant research gate.

The auxiliary coefficient archive contains scaled rational-function representations. `docs/certificate_normalization.json` records the exact factors and `scripts/verify_normalization.py` reconstructs the corresponding economic functions from primitives to verify the identities.

## ERE submission architecture

The journal-facing package separates double-anonymous reviewer materials from non-anonymous editorial materials.

- Anonymous manuscript source: `paper/main.tex`
- Stage 13 report: `STAGE_13_REPORT.md`
- Title page: `submission/ERE_title_page.tex`
- Cover letter: `submission/ERE_cover_letter.md`
- Submission checklist: `submission/ERE_submission_checklist.md`
- Anonymous replication README: `submission/ERE_replication_README.md`
- Review-only Makefile: `submission/ERE_review_Makefile`
- Anonymous archive builder: `scripts/build_ere_review_package.py`
- ERE format/anonymity verifier: `scripts/verify_ere_submission.py`

`make verify` generates `dist/ERE_anonymous_replication.zip`. GitHub Actions uploads the same anonymous archive as the `ERE-anonymous-replication` workflow artifact after a successful verification run.

## Reproducibility layout

```text
.
├── README.md
├── STAGE_13_REPORT.md
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
├── submission/
├── scripts/
├── tests/
├── figures/
├── tables/
└── references/
```

Generated figure/table objects, manuscript PDFs, and the anonymous review archive are rebuilt deterministically by the verification pipeline rather than treated as independent theory sources.

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

It runs symbolic identities and threshold certificates, primitive-to-certificate normalization identities, the policy-root certificate, the exact whole-domain certificate, numerical global-deviation and planner stress tests, nested-benchmark checks, regression tests, deterministic exposition-object generation, ERE format/anonymity checks, the manuscript build, the separate title-page build, and anonymous review-package generation.
