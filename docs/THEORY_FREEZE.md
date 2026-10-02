# Canonical Theory Freeze

Freeze ID: `PCPPR-THEORY-FREEZE-2026-10-02-v3`

Freeze date: **2026-10-02**

Supersedes:
- `PCPPR-THEORY-FREEZE-2026-09-14-v2`, which was reopened by the independent pre-submission audit after discovery of an invalid policy-equilibrium exhibit and proof gaps in backup-game uniqueness and open-set persistence;
- `PCPPR-THEORY-FREEZE-2026-09-06-v1`.

Version 3 retains the canonical primitive vector and baseline Protection--Attraction Conflict ranking, but freezes the repaired proof architecture: clipped-backup contraction for global continuation uniqueness, the full diagonal FOC derivative for open-set persistence, the exact origin-marginal exhibit, the narrowed mechanism/novelty claims, and the explicit formalization boundary.

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
