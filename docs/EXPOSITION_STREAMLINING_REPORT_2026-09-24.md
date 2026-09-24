# v2.5 Exposition Streamlining Report — 2026-09-24

## Executive verdict

**CONDITIONAL PASS — CI PAGE-ARRIVAL AUDIT PENDING**

Primary exposition profile: **GENERAL THEORY / THEORY-FIRST**

Target article: full-length theory article for Environmental and Resource Economics.

The integrated manuscript already had a coherent theory-first architecture. The v2.5 retrofit therefore uses bounded streamlining rather than substantive rewriting. No theorem, equilibrium concept, welfare definition, numerical certificate, portability classification, or literature-positioning conclusion is changed.

## 1. Reader objective

The paper should move the reader through this sequence with minimum search cost:

1. climate protection changes both hazard exposure and firms' private resilience choices;
2. decentralized governments additionally value plant attraction;
3. the model formalizes those two margins;
4. the main theorem establishes planner-zero / decentralized-positive protection on a nonempty open set;
5. welfare decomposition explains the sign reversal;
6. benchmarks identify which endogenous margin carries which mechanism;
7. institutional and literature sections delimit interpretation and novelty;
8. discussion states portability and limitations.

## 2. Introduction compression audit

PASS after bounded edit.

The Introduction already delivers, in order: question; mechanism; headline result; essential model structure; nested-benchmark intuition; closest-literature positioning; policy interpretation; roadmap.

The only clear redundancy was a paragraph listing Japanese institutional examples that are developed again in Section 7. It was removed from the Introduction and retained in the dedicated institutional section.

No derivation, robustness calculation, or appendix-level proof material remains in the Introduction.

## 3. Section-purity map

| Section | Primary role | Classification | v2.5 decision |
|---|---|---|---|
| Introduction | question, finding, mechanism, novelty | CORE | retain; remove duplicated institutional paragraph |
| Model | primitives, timing, strategies, objectives | CORE | retain |
| Equilibrium Characterization | solve product, backup, location continuations | CORE | retain |
| Protection–Attraction Conflict | headline propositions and theorem | CORE | retain |
| Welfare | surplus accounting and channel decomposition | CORE | retain |
| Nested Benchmarks | mechanism identification | HELPFUL | retain table; compress three repetitive subsections |
| Institutional Interpretation | map primitives to real decisions; empirical implications | HELPFUL | retain; move giant exact fraction back to Appendix |
| Related Literature | novelty boundary | HELPFUL | retain because v2.2 absorption audit makes positioning substantive |
| Discussion | limitations, portability, scope | HELPFUL | retain; remove internal workflow/journal-positioning phrasing |
| Conclusion | answer question; no new claims | CORE | retain |
| Proofs and Computer-Assisted Certificates | proof detail, exact certificates, reproducibility | APPENDIX | retain in appendix |

No main-text section is classified DELETE after the bounded edits.

## 4. CORE / HELPFUL / APPENDIX / DELETE ledger

### CORE

- research question and headline policy conflict;
- all material model primitives and timing;
- backup strategic-substitution mechanism;
- location continuation and plant-attraction response;
- headline global theorem;
- welfare sign decomposition;
- concise statement of theorem scope;
- final conclusion.

### HELPFUL

- benchmark summary table and one compressed explanatory paragraph;
- institutional mapping to Japanese adaptation/BCP/plant-attraction practice;
- empirical predictions;
- focused related-literature section;
- conditional-portability discussion.

These items remain because each changes reader interpretation of mechanism, scope, or novelty.

### APPENDIX

- exact global Bernstein certificates;
- exact normalization factors;
- exact root-isolation details;
- exact cross-partial magnitude;
- detailed numerical stress-test provenance;
- robustness to counting selected location-fit payoff.

### DELETE / removed in v2.5

- duplicated Japanese-policy paragraph from Introduction;
- duplicated benchmark subsections that repeated the benchmark table;
- giant exact rational cross-partial from the empirical-predictions flow;
- internal phrase “For journal positioning” from Discussion.

## 5. Main-text exhibit scarcity

The manuscript has only three main-text exhibits:

1. **Figure: Public protection and product substitutability** — CORE. It visualizes the two exact gamma thresholds and the conflict region, which is materially harder to parse from the root intervals alone.
2. **Table: Marginal welfare channels at the canonical witness** — CORE. It makes the direct engineering effect, endogenous private-response effect, and net sign immediately visible.
3. **Table: Nested benchmark logic** — HELPFUL/near-CORE. It replaces several paragraphs and identifies which margin each restricted game removes.

Five-exhibit thought experiment: all three survive. There are no fourth or fifth main-text exhibits to defend.

## 6. Redundancy audit

Resolved:

- Introduction ↔ Institutional duplication: removed from Introduction.
- Benchmark table ↔ benchmark subsections duplication: subsections compressed to one paragraph.
- Institutional exact cross-partial ↔ Appendix duplication: exact magnitude retained only in Appendix.
- Discussion internal workflow language: removed.

Not removed:

- brief restatement of the headline result in Conclusion;
- brief statement of theorem scope in Discussion;
- related-literature positioning in both Introduction and dedicated literature section.

These repetitions serve different reader functions and are not avoidable duplication.

## 7. Compression-without-damage audit

The v2.5 edits do **not** remove or alter:

- any model primitive;
- any equilibrium concept;
- any theorem hypothesis or quantifier;
- any welfare definition;
- any exact certificate;
- any citation supporting a retained factual/literature claim;
- any v2.2 novelty limitation;
- any v2.4 portability limitation;
- any formal-verification statement.

The exact cross-partial remains auditable in Appendix. Institutional citations removed from Introduction remain in Section 7 and the reference list.

## 8. Reader-arrival budget

The repository now contains scripts/verify_exposition_v25.py, invoked by make verify after the paper build.

The automated audit extracts actual section page numbers from paper/main.aux, verifies monotone section order, applies the workflow's soft Introduction heuristic, checks the main-text exhibit inventory, and blocks known exposition regressions.

**Actual page landmarks will be recorded here after the first green CI run on this branch.**

## 9. v2.5 regression guard

make verify now includes the exposition audit. It fails if:

- the internal phrase “For journal positioning” returns;
- the duplicated Japanese institutional paragraph returns to the Introduction;
- the giant exact cross-partial returns to the main empirical-predictions section;
- main-text figures or tables unexpectedly expand beyond the current low-exhibit architecture;
- section labels are missing or nonmonotone;
- the Introduction exceeds the v2.5 soft five-page diagnostic without an explicit workflow change.

## 10. Stage-13-equivalent streamlining verdict

**PASS subject only to actual-page CI confirmation.**

No Stage-10 architecture failure was found. No substantive research rollback is required.

## 11. Routing

After green page-arrival/verify/Lean regression evidence:

**v2.5 CLOSED → proceed to refreshed Stage 14 QA and freeze.**