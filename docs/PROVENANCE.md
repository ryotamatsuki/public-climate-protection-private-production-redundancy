# Provenance and Change Control

## Canonical baseline

The authoritative pre-GitHub baseline is the local Stage 10 reproducibility package associated with theory freeze:

`PCPPR-THEORY-FREEZE-2026-09-06-v1`

The GitHub repository was created only after Stage 10 was completed. Therefore the first GitHub commits are a migration/bootstrap layer, not the origin of the theory.

## Stage 10 status carried into GitHub

The pre-GitHub baseline records the following as passing:

- exact symbolic identities and threshold/root-isolation certificates;
- exact policy-root certificate at the canonical rational witness;
- numerical global-deviation and planner audits;
- nested-benchmark recovery;
- pytest regression suite (4/4);
- deterministic figure/table generation;
- clean LaTeX build and PDF preflight.

Until the frozen Stage 10 source package is fully imported and re-run from GitHub, these PASS statements describe the local canonical baseline rather than the current GitHub checkout.

## Theory change control

The theory freeze is authoritative. No theorem, parameter domain, equilibrium concept, welfare statement, benchmark label, or novelty boundary may change silently.

A proposed change must be classified as one of:

1. **No theory change** — formatting, exposition, reproducibility plumbing, or verification code that leaves the frozen mathematical object unchanged.
2. **Verification repair** — fixes a verifier without changing the frozen theoretical claim. The repaired verifier must reproduce the frozen results.
3. **Theory reopening** — changes a primitive, equilibrium object, welfare definition, theorem, scope, or claim boundary. This requires reopening the relevant research stage and all downstream dependent gates.

## Immediate migration task

The next repository operation is to import the exact frozen Stage 10 files (paper sources, scripts, tests, references, generated objects, and theory-freeze record), then run the complete validation stack before declaring the GitHub checkout canonical.
