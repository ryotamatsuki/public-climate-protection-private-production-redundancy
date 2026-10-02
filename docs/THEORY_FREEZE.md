# Canonical Theory Freeze

Freeze ID: `PCPPR-THEORY-FREEZE-2026-10-03-v4`

Freeze date: **2026-10-03**

Supersedes:
- `PCPPR-THEORY-FREEZE-2026-10-02-v3`, reopened by the workflow-v2.5 hostile re-certification because Stage-6 prior-art coverage and Stage-7.5A portability/human-accountability certification were stale after the independent audit repair;
- `PCPPR-THEORY-FREEZE-2026-09-14-v2`;
- `PCPPR-THEORY-FREEZE-2026-09-06-v1`.

Version 4 retains the v3 canonical primitive vector, welfare formulas, and repaired proof architecture. It additionally freezes the refreshed Stage-6 theorem-absorption map, the corrected Stage-7.5A portability interpretation, the bounded formal-verification scope, and the author's explicit 2026-10-03 scientific reconfirmation.

Working title: **Public Climate Protection and Private Production Redundancy**

## Research question

Can competition among local governments for mobile production induce public climate protection even when additional protection is socially undesirable because it crowds out firms' geographic production redundancy?

## Timing

1. Jurisdictions A and B choose public climate protection `a_A, a_B in [0, abar]`.
2. Firms privately observe independent location-fit shocks and simultaneously choose primary production locations.
3. Firms choose geographic backup readiness `r_i in [0,1]`.
4. Localized primary-disaster states realize.
5. Conditional on primary failures, backup success realizes.
6. Available firms compete in a differentiated Cournot market.

## Probability law

Let `F_i` denote failure of firm `i`'s primary production, with marginal probability `s_i` and joint primary-failure probability `J` determined by the primary-location configuration.

Conditional on public policies, primary locations, and the realized primary-failure vector:

- if `F_i=1`, firm `i`'s backup is available with probability `r_i`;
- backup-success draws are conditionally independent across firms;
- the backup-success law has no additional dependence on the regional shock beyond the realized primary-failure vector;
- location-fit shocks are independent of primary-disaster and backup-success draws.

Hence firm `i` is finally unavailable with probability `s_i(1-r_i)`, and both firms are finally unavailable with probability `J(1-r_1)(1-r_2)`.

This conditional-independence law is a primitive of the baseline model. Marginal backup-success probabilities alone are not sufficient to determine expected profits.

## Other maintained baseline assumptions

- Available primary or backup production can supply the unconstrained Cournot quantity at the same zero marginal production cost.
- Backup-readiness cost `k r_i^2/2` is paid ex ante and does not vary by realized state.
- Each local government receives one half of national product-market surplus plus its local plant-attraction benefit and pays its own protection cost; this is a reduced-form incidence rule.
- The nonempty-open-set result is taken within the maintained symmetric primitive family.

## Headline theorem

There exists a nonempty open set within the maintained symmetric primitive family for which coordinated welfare is maximized by zero additional local climate protection, while the decentralized jurisdictional game has a positive symmetric protection equilibrium.

Canonical rational witness:

- gamma = 12/25
- q0 = 3/10
- k = 169/3000
- H = 1/100
- b = 11/200
- c = 3
- abar = 2/25

## Claim boundary

The paper does **not** claim novelty for public/private adaptation crowd-out, local-public-input overprovision, resilience underinvestment under market power, geographic diversification under disaster risk, or strategic substitutability of capacity investment. Novelty is restricted to the full-game policy-ranking conflict.

The level result that higher product substitutability lowers backup readiness on the maintained symmetric interior branch is retained. No general claim is made that higher substitutability strengthens the marginal crowd-out response of readiness to public protection; at the canonical co-located origin the relevant cross-partial has the opposite sign.

## Independent-audit repair and v3 re-freeze, 2026-10-02

The independent audit reopened version 2 for proof correctness, plotted
quantities, mechanism benchmarks, novelty positioning, formal-scope disclosure,
and package execution. Version 3 closes that scientific repair cycle.

The canonical primitive vector and material welfare formulas are retained.
The own-policy concavity argument is distinguished from the full diagonal
FOC derivative; uniqueness of backup is proved for the clipped game and the
strict contraction margin is carried explicitly into the open-set persistence
argument. The former non-Nash policy-equilibrium figure is permanently
withdrawn and replaced by an exact origin-marginal exhibit.

The current contribution boundary explicitly permits the policy ranking at
Delta=0: incremental sole-survivor rents are not a necessary mechanism. The
new exact benchmark does not substitute for comparison with prior theory.
The planner is protection-policy constrained and industrial-surplus specific.
The current repair and evidence are described in
`INDEPENDENT_AUDIT_REPAIRS_2026-10-02.md`.

This v3 freeze covers the scientific object only. Live journal-portal fields,
the portal-generated review PDF, and final submission authorization remain
separate operational gates.


## Workflow-v2.5 re-certification and v4 freeze, 2026-10-03

The v3 scientific object was re-opened for certification rather than because a
new mathematical defect was found.

Stage 6 was re-run after locating closer parent literature, especially
Kousky, Luttmer and Zeckhauser (2006), together with Mahmud and Barbier (2016)
and application-neutral public/private prevention models. These papers absorb
broad claims for protection-induced investment/location responses and
public/private protection interaction. They do not supply a parent theorem
from which the full planner-zero / local-positive policy ranking follows by
direct specialization. Novelty therefore remains restricted to the coupled
global policy-ranking result.

Stage 7.5A was re-run with the diagnostic evidence narrowed. The nonlinear-risk
diagnostic matches the baseline origin slope by construction; the logistic
diagnostic matches the symmetric density response by construction. Their
informative content is off-origin/off-diagonal continuation and deviation
behavior. The exact theorem remains baseline-family-specific and the final
classification remains **CONDITIONALLY PORTABLE**.

The formal-verification state is **PASS / PROOF-CRITICAL CORE** with explicit
generated-certificate premises, clipped-backup uniqueness and open-set
persistence outside the final Lean theorem, and native-computation trust
disclosed.

On 2026-10-03 the author explicitly confirmed the current mechanism, repaired
proof/equilibrium logic, Delta=0 benchmark interpretation, prior-art/limitation
boundary, and maximum defensible claim, and explicitly approved the v4 freeze.

Current recertification evidence:
- `docs/STAGE_6_RECERTIFICATION_2026-10-03.md`
- `docs/STAGE_7_5A_RECERTIFICATION_2026-10-03.md`
- `docs/FORMAL_VERIFICATION_GATE_ADDENDUM_2026-10-03.md`
- `docs/INDEPENDENT_SCIENTIFIC_CONFIRMATION_2026-10-03.md`
- `docs/AUTHOR_INTELLECTUAL_CONTRIBUTION_RECORD.md`

Live journal-portal fields, portal-generated review PDF inspection, and final
submission authorization remain separate operational gates.
