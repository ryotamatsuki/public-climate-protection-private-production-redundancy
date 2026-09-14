# Provenance and Change Control

## Canonical history

The theory originated in a local reproducibility package before the GitHub repository was created. The first GitHub import therefore represents migration of an already-developed mathematical object rather than the origin of the theory.

Historical theory freeze:

`PCPPR-THEORY-FREEZE-2026-09-06-v1`

After the Stage 12 independent Astra audit, the intended backup-success joint law was made explicit and the theory record was superseded by:

`PCPPR-THEORY-FREEZE-2026-09-14-v2`

The v2 freeze does not change the canonical parameter witness or the central Protection–Attraction Conflict theorem. It makes explicit the conditional-independence probability primitive required by the expected-profit formula, narrows one comparative-static empirical claim, and records the scope of the open-set result.

## Reproducibility milestones

- Stage 10 imported the local reproducibility baseline into GitHub and re-ran the validation stack.
- Stage 11A replaced numerical global-policy evidence with exact whole-domain certificates.
- Stage 11C closed the location-equilibrium no-clipping/uniqueness gap and added the general marginal decomposition.
- Stage 12 selected RAND as a one-shot stretch target, with JEEM as the immediate fallback.
- Stage 12R responds to an independent mathematical audit that reconstructed the model before reading the author verification code.

The Stage 12R audit preserved the central theorem but required three substantive repairs before submission:

1. make the conditional joint distribution of backup success explicit;
2. correct the sign interpretation of the product-substitutability × policy-response interaction;
3. record and verify the non-unit scaling factors in the auxiliary coefficient archive.

It also required the manuscript proof appendix to be rewritten as mathematical lemmas and exact certificates rather than an internal verification log.

## Theory change control

No theorem, parameter domain, equilibrium concept, welfare statement, benchmark definition, or novelty boundary may change silently.

A proposed change is classified as one of:

1. **No theory change** — formatting, exposition, reproducibility plumbing, or verification code that leaves the mathematical object unchanged.
2. **Verification repair** — fixes or strengthens a verifier without changing the theoretical claim. The repaired verifier must reproduce the mathematical result from the stated primitives.
3. **Primitive clarification / scoped repair** — makes an intended primitive or claim scope explicit when a prior manuscript formula already relied on it. This requires an independent re-audit and a new freeze, even when the canonical equilibrium formulas are unchanged.
4. **Theory reopening** — changes a primitive in a way that changes equilibrium objects, welfare definitions, the canonical witness, or the theorem architecture. This requires reopening all dependent gates.

Stage 12R is classified as **primitive clarification / scoped repair** because conditional independence of backup success is now explicit. The repair is admissible only because the independent audit reconstructed and re-certified the central theorem under that explicit law.

## Auxiliary certificate normalization

`docs/certificate_polynomials.json` stores algebraic numerator/denominator pairs used for exact root isolation. Some pairs are scaled versions of the economic functions rather than identically normalized representations. The mapping is recorded in `docs/certificate_normalization.json` and checked by `scripts/verify_normalization.py` against a primitive symbolic reconstruction. Roots are invariant to the nonzero scaling factors, but signs must never be inferred from the stored coefficients without applying the recorded normalization.

## Canonical validation

The repository is canonical only at an explicitly frozen commit for which the full command

```bash
make verify
```

passes, including symbolic identities, auxiliary normalization identities, exact policy and whole-domain certificates, numerical stress tests, benchmark checks, regression tests, deterministic object generation, and a clean manuscript build.
