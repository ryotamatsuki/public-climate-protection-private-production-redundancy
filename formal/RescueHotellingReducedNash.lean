import Mathlib
import RescueHotellingCore
import RescueHotellingLocation
import RescueHotellingRefusal
import RescueHotellingCrossing

/-!
Theorem: at the constructed symmetric distance, each firm is a global
best responder in the *reduced location game*, including contract refusal
and crossing the rival. Assumes candidate stationarity and R1/R2 inequalities
as explicit hypotheses; does not claim those inequalities hold for a full
open parameter region, and does not formalize the full extensive form SPNE.
-/
noncomputable section
namespace RescueHotellingReducedNash
open RescueHotelling RescueHotellingLocation
  RescueHotellingRefusal RescueHotellingCrossing

def payoffLeftAfterLocation (r A t c V F d y : ℝ) : ℝ :=
  if y ≤ symmetricRivalPosition d then
    max
      (disagreementPayoff r t c (symmetricRivalPosition d)
        (symmetricRivalPosition d-y))
      (agreementPayoff r A t c V F (symmetricRivalPosition d)
        (symmetricRivalPosition d-y))
  else
    crossingPayoff r A t c V F d (y-symmetricRivalPosition d)

def candidateLeft (d : ℝ) : ℝ := (1-d)/2

theorem candidate_payoff_is_agreement
    (r A t c V F d : ℝ) (hc : 0 < c) (hd : 0 ≤ d)
    (hR1 : (g A t V d)^2/(2*c) < H A t V F d) :
    payoffLeftAfterLocation r A t c V F d (candidateLeft d) =
      agreementPayoff r A t c V F (symmetricRivalPosition d) d := by
  have hPos : 0 ≤ (g A t V d)^2/(2*c) := by
    exact div_nonneg (sq_nonneg _) (le_of_lt (by positivity : 0 < 2*c))
  have hH : 0 ≤ H A t V F d := by linarith
  have hCandidate : candidateLeft d ≤ symmetricRivalPosition d := by
    unfold candidateLeft symmetricRivalPosition
    linarith
  have hSep : symmetricRivalPosition d-candidateLeft d = d := by
    unfold symmetricRivalPosition candidateLeft
    ring
  have hGain := agreement_at_candidate_equals_disagreement_plus_H
    r A t c V F d
  have hCmp : disagreementPayoff r t c (symmetricRivalPosition d) d ≤
      agreementPayoff r A t c V F (symmetricRivalPosition d) d := by
    linarith
  unfold payoffLeftAfterLocation
  rw [if_pos hCandidate]
  rw [hSep]
  exact max_eq_right hCmp

theorem global_left_location_best_response
    (r A t c V F d : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t)
    (hc : 0 < c) (hV : 0 ≤ V) (hF : 0 ≤ F)
    (hd0 : 0 ≤ d) (hd1 : d ≤ 1/2)
    (hCost : A*t < c)
    (hFOC : G r A t c V d = 0)
    (hR1 : (g A t V d)^2/(2*c) < H A t V F d)
    (hK : 0 < crossingK A t c)
    (hR2 : (crossingL r A t c V d)^2/(2*crossingK A t c) <
        r*t*d/2+H A t V F d) :
    ∀ y : ℝ, 0 ≤ y → y ≤ 1 →
      payoffLeftAfterLocation r A t c V F d y ≤
      payoffLeftAfterLocation r A t c V F d (candidateLeft d) := by
  intro y hy0 hy1
  have hSelf := candidate_payoff_is_agreement r A t c V F d hc hd0 hR1
  rw [hSelf]
  by_cases hLeft : y ≤ symmetricRivalPosition d
  · have hs0 : 0 ≤ symmetricRivalPosition d-y := by linarith
    have hs1 : symmetricRivalPosition d-y ≤ 1 := by
      unfold symmetricRivalPosition
      linarith
    have hAopt := agreement_same_side_global_optimum r A t c V F d
      (symmetricRivalPosition d-y) hr hA ht hV hd0 hs0 hs1
      hCost hFOC
    have hNopt := R1_rules_out_every_same_side_refusal r A t c V F d
      (symmetricRivalPosition d-y) hr ht hc hs1 hFOC hR1
    unfold payoffLeftAfterLocation
    rw [if_pos hLeft]
    exact max_le (le_of_lt hNopt) hAopt
  · have hyGreater : symmetricRivalPosition d < y := lt_of_not_ge hLeft
    have hu : 0 ≤ y-symmetricRivalPosition d := by linarith
    have hur : y-symmetricRivalPosition d ≤ (1-d)/2 := by
      unfold symmetricRivalPosition
      linarith
    have hCross := R2_rules_out_all_crossing_deviations r A t c V F d
      (y-symmetricRivalPosition d) hr hA ht hc hV hF hd0
      (by linarith : d ≤ 1) hu hur hK hR2
    unfold payoffLeftAfterLocation
    rw [if_neg (not_le.mpr hyGreater)]
    exact le_of_lt hCross

def payoffRightByReflection (r A t c V F d y : ℝ) : ℝ :=
  payoffLeftAfterLocation r A t c V F d (1-y)

theorem globally_symmetric_reduced_location_nash
    (r A t c V F d : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t)
    (hc : 0 < c) (hV : 0 ≤ V) (hF : 0 ≤ F)
    (hd0 : 0 ≤ d) (hd1 : d ≤ 1/2)
    (hCost : A*t < c)
    (hFOC : G r A t c V d = 0)
    (hR1 : (g A t V d)^2/(2*c) < H A t V F d)
    (hK : 0 < crossingK A t c)
    (hR2 : (crossingL r A t c V d)^2/(2*crossingK A t c) <
        r*t*d/2+H A t V F d) :
    (∀ y : ℝ, 0 ≤ y → y ≤ 1 →
        payoffLeftAfterLocation r A t c V F d y ≤
        payoffLeftAfterLocation r A t c V F d (candidateLeft d)) ∧
    (∀ y : ℝ, 0 ≤ y → y ≤ 1 →
        payoffRightByReflection r A t c V F d y ≤
        payoffRightByReflection r A t c V F d (symmetricRivalPosition d)) := by
  have hLeft := global_left_location_best_response r A t c V F d
    hr hA ht hc hV hF hd0 hd1 hCost hFOC hR1 hK hR2
  constructor
  · exact hLeft
  · intro y hy0 hy1
    unfold payoffRightByReflection
    have hCandidate : 1-symmetricRivalPosition d = candidateLeft d := by
      unfold symmetricRivalPosition candidateLeft
      ring
    rw [hCandidate]
    exact hLeft (1-y) (by linarith) (by linarith)

end RescueHotellingReducedNash
#print axioms RescueHotellingReducedNash.globally_symmetric_reduced_location_nash
