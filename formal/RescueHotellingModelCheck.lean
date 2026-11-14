import Mathlib
import RescueHotellingCore

/-!
# RescueHotellingModelCheck — additional scoped formal proofs
Prices and interior profits, bargaining-transfer feasibility, monotone risk
response without contracts, and algebraic R1/R2 envelopes.
This file does NOT formalize the full SPNE or full risk interval certificate.
-/

noncomputable section
namespace RescueHotellingModelCheck
open RescueHotelling

def priceLeft (td m : ℝ) : ℝ := 2 * td * (1 + m) / 3
def priceRight (td m : ℝ) : ℝ := 2 * td * (2 - m) / 3
def indifferentConsumer (td m pLeft pRight : ℝ) : ℝ :=
  m + (pRight - pLeft) / (2 * td)
def conditionalShareLeft (m : ℝ) : ℝ := (1 + m) / 3
def conditionalShareRight (m : ℝ) : ℝ := (2 - m) / 3

theorem price_left_reaction (td m : ℝ) :
    2 * priceLeft td m = priceRight td m + 2 * td * m := by
  unfold priceLeft priceRight
  ring

theorem price_right_reaction (td m : ℝ) :
    2 * priceRight td m = priceLeft td m + 2 * td * (1 - m) := by
  unfold priceLeft priceRight
  ring

theorem price_share_left (td m : ℝ) (htd : td ≠ 0) :
    indifferentConsumer td m (priceLeft td m) (priceRight td m) =
      conditionalShareLeft m := by
  unfold indifferentConsumer priceLeft priceRight conditionalShareLeft
  field_simp [htd]
  ring

theorem price_share_right (td m : ℝ) (htd : td ≠ 0) :
    1 - indifferentConsumer td m (priceLeft td m) (priceRight td m) =
      conditionalShareRight m := by
  rw [price_share_left td m htd]
  unfold conditionalShareLeft conditionalShareRight
  ring

theorem candidate_conditional_revenue_left (td m : ℝ) :
    priceLeft td m * conditionalShareLeft m =
      2 * td * (1 + m) ^ 2 / 9 := by
  unfold priceLeft conditionalShareLeft
  ring

theorem candidate_conditional_revenue_right (td m : ℝ) :
    priceRight td m * conditionalShareRight m =
      2 * td * (2 - m) ^ 2 / 9 := by
  unfold priceRight conditionalShareRight
  ring

theorem symmetric_price (td : ℝ) :
    priceLeft td (1/2) = td ∧ priceRight td (1/2) = td := by
  constructor <;> dsimp [priceLeft, priceRight] <;> ring

def linearDemandRevenue (td m pOther p : ℝ) : ℝ :=
  p * (m + (pOther - p) / (2 * td))
def optimalInteriorPrice (td m pOther : ℝ) : ℝ :=
  (pOther + 2 * td * m) / 2

theorem interior_revenue_square_identity (td m pOther p : ℝ) (htd : td ≠ 0) :
    2 * td * (linearDemandRevenue td m pOther (optimalInteriorPrice td m pOther)
      - linearDemandRevenue td m pOther p)
    = (p - optimalInteriorPrice td m pOther) ^ 2 := by
  unfold linearDemandRevenue optimalInteriorPrice
  field_simp [htd]
  ring

theorem interior_revenue_best_response (td m pOther p : ℝ) (htd : 0 < td) :
    linearDemandRevenue td m pOther p ≤
      linearDemandRevenue td m pOther (optimalInteriorPrice td m pOther) := by
  have hId := interior_revenue_square_identity td m pOther p (ne_of_gt htd)
  have hsq : 0 ≤ (p - optimalInteriorPrice td m pOther) ^ 2 := sq_nonneg _
  nlinarith

theorem bilateral_transfer_feasible_iff (gainLeft gainRight : ℝ) :
    (∃ transfer : ℝ, 0 ≤ gainLeft - transfer ∧ 0 ≤ gainRight + transfer) ↔
      0 ≤ gainLeft + gainRight := by
  constructor
  · rintro ⟨transfer, hLeft, hRight⟩
    linarith
  · intro hTotal
    refine ⟨gainLeft, ?_, ?_⟩ <;> linarith

theorem random_proposer_expected_gain (gain : ℝ) :
    (1 / 2 : ℝ) * gain + (1 / 2 : ℝ) * 0 = gain / 2 := by
  ring

theorem no_contract_distance_strictly_decreases
    (q₁ q₂ t c : ℝ)
    (hq₁ : 0 < q₁) (hq₂ : q₁ < q₂) (hq₂one : q₂ < 1)
    (ht : 0 < t) (hc : 0 < c) :
    noContractDistance q₂ t c < noContractDistance q₁ t c := by
  have hr₁ : 0 < survival q₁ := by unfold survival; linarith
  have hr₂ : 0 < survival q₂ := by unfold survival; linarith
  have hden₁ : 0 < 3 * c + 2 * survival q₁ * t := by positivity
  have hden₂ : 0 < 3 * c + 2 * survival q₂ * t := by positivity
  unfold noContractDistance
  apply (div_lt_div_iff₀ hden₂ hden₁).2
  have hpos : 0 < c * t * (q₂ - q₁) := by positivity
  unfold survival at *
  nlinarith

theorem refusal_envelope_bridge (c g z H : ℝ)
    (hc : 0 < c) (hR1 : g * g / (2*c) < H) :
    -g*z-c*z*z/2 < H := by
  have h := RescueHotelling.strong_concavity_quadratic_bound c (-g) z hc
  have hsq : (-g)*(-g) = g*g := by ring
  rw [hsq] at h
  linarith

theorem across_envelope_bridge (K L u benefit : ℝ)
    (hK : 0 < K) (hR2 : L * L / (2*K) < benefit) :
    L*u-K*u*u/2 < benefit := by
  have h := RescueHotelling.strong_concavity_quadratic_bound K L u hK
  linarith

end RescueHotellingModelCheck

#print axioms RescueHotellingModelCheck.interior_revenue_best_response
#print axioms RescueHotellingModelCheck.bilateral_transfer_feasible_iff
#print axioms RescueHotellingModelCheck.no_contract_distance_strictly_decreases
#print axioms RescueHotellingModelCheck.refusal_envelope_bridge
