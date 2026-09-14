# Canonical Theory Freeze

Freeze ID: `PCPPR-THEORY-FREEZE-2026-09-14-v2`

Supersedes: `PCPPR-THEORY-FREEZE-2026-09-06-v1` by making the intended backup-success joint probability law explicit. The canonical parameter witness and central theorem architecture are unchanged.

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
