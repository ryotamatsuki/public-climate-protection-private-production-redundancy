# Stage 12R — Independent Astra mathematical-audit repair

**Date:** 2026-09-14  
**Input Stage 12 freeze:** `134ff145a89afb78c587d10081caf1a4bdb1601f`  
**Input freeze branch:** `freeze/pcppr-stage12-2026-09-14`  
**Repair branch:** `repair/stage12r-astra-audit`

## Verdict

**PASS / AUTHORIZE STAGE 13 after merge and refreeze.**

The independent Astra audit returned `REPAIR BEFORE SUBMISSION`, but did not overturn the central Protection–Attraction Conflict theorem. The audit independently reconstructed the model before reading the author verification code and confirmed the canonical planner optimum, the positive decentralized equilibrium, the marginal decomposition, and the exact whole-domain certificate. Its three substantive objections have now been repaired: the joint backup-success probability law is explicit, the incorrect empirical interaction prediction has been corrected, and the auxiliary coefficient normalizations are recorded and verified from primitives.

## 1. Probability primitive repair

The model now states the joint law required by the expected-profit and welfare formulas. Conditional on public policies, primary locations, and the realized primary-failure vector:

- firm `i`'s backup succeeds with probability `r_i` when its primary production fails;
- backup-success draws are independent across firms;
- conditional backup success has no additional dependence on the regional shock beyond the realized primary-failure vector;
- location-fit shocks are independent of primary-disaster and backup-success draws.

Hence firm `i` is finally unavailable with probability `s_i(1-r_i)` and joint final unavailability is

`J(1-r_1)(1-r_2)`.

The manuscript derives the four final production-availability states from this law before deriving expected profit. It also makes explicit the no-capacity-constraint assumption for available primary/backup production, the ex-ante state-independent readiness cost, and the equal-share local incidence rule for national product-market surplus.

The theory record is superseded by `PCPPR-THEORY-FREEZE-2026-09-14-v2`. The canonical parameter witness and central theorem architecture are unchanged.

## 2. Comparative-static repair

The maintained level result remains:

- on the symmetric interior branch, higher product substitutability lowers equilibrium backup readiness.

The manuscript no longer claims that higher substitutability strengthens the marginal crowd-out of readiness by public protection. At the canonical co-located symmetric origin,

`r^C_{q gamma} = -26550065039062500 / 13482801445834729 < 0`.

Since `q=q0-a`, the readiness reduction caused by an incremental increase in protection is locally **weaker**, not stronger, at higher substitutability at this point. The empirical-predictions section now separates the readiness-level comparative static from this policy-interaction comparative static and assigns no global sign to the latter.

A regression test checks the exact rational cross-partial and its sign.

## 3. Auxiliary certificate normalization repair

`docs/certificate_polynomials.json` contains scaled numerator/denominator representations. The new `docs/certificate_normalization.json` records the exact convention

`stored_rational = normalization_factor * economic_object`.

The factors confirmed by the independent audit and now checked by the repository are:

| Object | Normalization factor |
|---|---:|
| `MS` | `-80/3` |
| `ML` | `320` |
| `F` | `-76880` |
| `W` | `-19220/3` |

Roots are invariant to these nonzero factors, but signs are not interpreted without applying the factor. `scripts/verify_normalization.py` independently reconstructs the four economic functions from the primitives using exact forward-mode differentiation and verifies the complete rational-function identities. This check is part of `make verify`.

## 4. Proof-presentation repair

Appendix A has been reorganized as a mathematical proof rather than a development/verification log. Its dependency structure is now:

1. **Unique interior continuation lemma:** global backup concavity/interiority and unique Bayesian location continuation, including no clipping and no asymmetric probability fixed point.
2. **Global planner monotonicity lemma:** exact Bernstein certificates prove `W_{a_A}<0` and `W_{a_B}<0` on the entire policy rectangle, giving the unique planner optimum `(0,0)`.
3. **Global local-government best-response lemma:** exact root isolation plus whole-interval strict concavity makes the isolated positive root the unique global best response to itself, including boundary deviations.
4. **Main theorem proof:** combines the continuation, planner, and local-government lemmas.
5. **Open-set persistence lemma:** normalizes the policy domain to a fixed compact square, uses uniform strict margins from the exact certificates, and applies the implicit-function theorem to the simple government root.

The appendix states the tensor-product Bernstein transformation, the nonnegative-basis sign principle, the policy domain normalization, separate denominator-sign checks, and a table mapping each certificate to the lemma it proves. Internal terms such as `Stage 11C certificate`, `frozen model`, and `verification record` have been removed from the submission manuscript.

## 5. Theorem scope and benchmarks

The theorem now states explicitly that the nonempty open set is within the maintained symmetric primitive family. The marginal inequalities derived from

`M_L = M_S/4 + 2 b lambda_0`

are identified as a characterization of the **marginal** sign conflict, not by themselves as sufficient conditions for the global equilibrium theorem.

The fixed-location and fixed-redundancy benchmarks now specify exactly which choices are held exogenous under policy deviations and which downstream games are re-solved. They are presented as mechanism-identification exercises rather than separate global-equilibrium certificates.

## 6. Canonical mathematical results retained

Under the explicit conditional-independence probability primitive, the independent audit and the repository certificates agree on the central results:

- unique planner optimum: `(a_A,a_B)=(0,0)`;
- positive symmetric local-government equilibrium:
  `a^LG = 0.023019684870554434657337382232045620...`;
- exact isolating interval:
  `1649737/71666359 < a^LG < 380091/16511564`;
- general marginal identity:
  `M_L = M_S/4 + 2 b lambda_0`;
- canonical marginal values:
  `M_S<0<M_L`;
- the nonempty-open-set extension persists within the maintained symmetric primitive family.

No canonical witness value was changed in Stage 12R.

## 7. Verification gate

GitHub Actions run `34805445924` at branch head `20cae1da2a297c9cf9344548104a8f88aeb7e089` completed successfully before this report-only commit. The full `make verify` gate passed, including:

- symbolic threshold certificate;
- **new primitive-to-auxiliary-normalization exact identities**;
- exact policy-root certificate;
- exact whole-domain planner/continuation/local-best-response certificate;
- numerical global-deviation stress test;
- nested benchmark recovery;
- regression tests including the conditional-independence state law and corrected cross-partial;
- deterministic object generation;
- three-pass LaTeX manuscript build.

A final report-inclusive CI run is required before merge.

## 8. Submission consequence

The independent audit's `REPAIR BEFORE SUBMISSION` blocker has been addressed. Stage 13 remains blocked only until this repair branch is merged, a new Stage 12R freeze is created, and Issue #9 is updated to use that freeze.

The editorial sequencing from Stage 12 is otherwise unchanged: RAND remains a one-shot stretch submission with JEEM as the immediate fallback. Stage 13 may perform submission formatting and editorial compression, but it may not alter the Stage 12R probability law, canonical witness, theorem architecture, or repaired comparative-static scope without reopening the theory gate.
