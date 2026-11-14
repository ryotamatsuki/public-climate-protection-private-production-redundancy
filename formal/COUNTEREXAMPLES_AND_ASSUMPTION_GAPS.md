# Counterexamples and assumption gaps — v0.4.2
Checked: 2026-11-14. No mathematical counterexample has yet been established by this audit. Do not treat 'unproved' as 'false'.

## Mathematical and interpretation gaps
1. The existing `globally_symmetric_reduced_location_nash` statement uses a reduced location payoff and assumes G=0 plus R1/R2/K>0. Its proof does **not** establish existence of the required d, validity of the inequalities over an open parameter box, or equilibrium in every extensive-form subgame.
2. The 800-cell q-interval risk-reversal certificate and the 400-cell imperfect-correlation certificate are presently external Python rational checks, not Lean-certified proof objects.
3. The manuscript's full-coverage assumption `v>3t` concerns candidate prices; full off-path demand with outside-option choices is not explicitly compiled into the older price game's `clippedProfit`. Existing global-price proof uses an upper-envelope demand argument.
4. The manuscript's payoffs exclude a location-independent `-qΛ` constant; formalized expected payoff must include it or explicitly prove that dropping it preserves best responses.
5. The chosen offer protocol accepts at responder indifference; at zero joint surplus the proposer is also indifferent between an accepted zero gain and a rejected offer. If exact signing at S=0 is part of the intended equilibrium selection, add the proposer's tie-breaking convention explicitly, or prove it irrelevant to the location payoffs.
6. The geometry's 'plant distance' and 'consumer differentiation distance' are the same reduced-form coordinate. This is not an algebraic inconsistency but it is a substantive economic restriction.
7. Exact parameter witnesses involve `v>3t`, `Λ>V` and `F>0`; all quantifier conditions must remain explicit in formal theorems.
8. For welfare, `Λ` must be real unfulfilled-order loss avoided by rescue, not a transfer or physical damage already realized. Otherwise welfare accounting changes.
9. Absence of consumer switching and unlimited emergency spare capacity are primitives, not derivable equilibrium consequences.
10. A pure reduced payoff must use `max 0 S/2`, including all off-path contracting refusals, and not an unconditional contracted payoff.

## Disposition
- Counterexample confirmed: **NONE SO FAR**.
- Incomplete proof obligations: see `FORMAL_PROOF_OBLIGATIONS.md`.
- If a theorem fails after exact manuscript translation, distinguish a Lean tactic failure from a mathematical counterexample. Supply an explicit rational witness or constructed admissible strategy deviation for the latter.
