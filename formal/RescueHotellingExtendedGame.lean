import Mathlib
import RescueHotellingCore
import RescueHotellingModelCheck

/-!
# RescueHotellingExtendedGame: price-game and failure-distribution kernel checks

These theorems strengthen the price verification from *interior* to
nonnegative prices and demand clipped into [0,1], and reconstruct a
symmetric correlated Bernoulli failure distribution. The outside option,
the full contract-contingent extensive form, and SPNE are not certified.
-/
noncomputable section
namespace RescueHotellingExtendedGame
open RescueHotelling RescueHotellingModelCheck

def clipDemand (z : ℝ) : ℝ :=
  if z ≤ 0 then 0 else if 1 ≤ z then 1 else z

theorem clip_zero (z : ℝ) (hz : z ≤ 0) : clipDemand z = 0 := by
  simp [clipDemand, hz]

theorem clip_identity (z : ℝ) (h0 : 0 < z) (h1 : z < 1) :
    clipDemand z = z := by
  simp [clipDemand, not_le.mpr h0, not_le.mpr h1]

theorem clip_le_original (z : ℝ) (hz : 0 ≤ z) :
    clipDemand z ≤ z := by
  by_cases h0 : z ≤ 0
  · have heq : z = 0 := le_antisymm h0 hz
    simp [heq, clipDemand]
  · by_cases h1 : 1 ≤ z
    · simp [clipDemand, h0, h1]
      linarith
    · simp [clipDemand, h0, h1]

def clippedProfit (td m pOther p : ℝ) : ℝ :=
  p * clipDemand (indifferentConsumer td m p pOther)

theorem clipping_price_best_reply (td m pOther : ℝ)
    (htd : 0 < td)
    (hpositive : 0 ≤ optimalInteriorPrice td m pOther)
    (hshareLo : 0 < indifferentConsumer td m (optimalInteriorPrice td m pOther) pOther)
    (hshareHi : indifferentConsumer td m (optimalInteriorPrice td m pOther) pOther < 1) :
    ∀ p : ℝ, 0 ≤ p →
      clippedProfit td m pOther p ≤
        clippedProfit td m pOther (optimalInteriorPrice td m pOther) := by
  intro p hp
  let star := optimalInteriorPrice td m pOther
  let zstar := indifferentConsumer td m star pOther
  have hstar : clipDemand zstar = zstar :=
    clip_identity zstar hshareLo hshareHi
  have hvstar : clippedProfit td m pOther star = linearDemandRevenue td m pOther star := by
    simp only [clippedProfit]
    rw [show clipDemand (indifferentConsumer td m star pOther) = zstar from hstar]
    rfl
  have hnonneg : 0 ≤ clippedProfit td m pOther star := by
    rw [hvstar]
    change 0 ≤ star * zstar
    exact mul_nonneg hpositive (le_of_lt hshareLo)
  let z := indifferentConsumer td m p pOther
  by_cases hz : z ≤ 0
  · have heq : clippedProfit td m pOther p = 0 := by
      unfold clippedProfit
      change p * clipDemand z = 0
      rw [clip_zero z hz]
      ring
    rw [heq]
    exact hnonneg
  · have hzpos : 0 ≤ z := le_of_lt (lt_of_not_ge hz)
    have hClip : clippedProfit td m pOther p ≤
        linearDemandRevenue td m pOther p := by
      unfold clippedProfit linearDemandRevenue
      change p * clipDemand z ≤ p * z
      exact mul_le_mul_of_nonneg_left (clip_le_original z hzpos) hp
    calc
      clippedProfit td m pOther p ≤ linearDemandRevenue td m pOther p := hClip
      _ ≤ linearDemandRevenue td m pOther star := interior_revenue_best_response td m pOther p htd
      _ = clippedProfit td m pOther star := hvstar.symm

theorem priceLeft_is_optimal (td m : ℝ) :
    optimalInteriorPrice td m (priceRight td m) = priceLeft td m := by
  unfold optimalInteriorPrice priceRight priceLeft
  ring

theorem priceRight_is_optimal (td m : ℝ) :
    optimalInteriorPrice td (1-m) (priceLeft td m) = priceRight td m := by
  unfold optimalInteriorPrice priceRight priceLeft
  ring

theorem right_is_left_after_reflection (td m : ℝ) :
    priceRight td m = priceLeft td (1-m) := by
  unfold priceRight priceLeft
  ring

theorem price_competition_nash (td m : ℝ)
    (htd : 0 < td) (hm0 : 0 ≤ m) (hm1 : m ≤ 1) :
    (∀ p : ℝ, 0 ≤ p →
       clippedProfit td m (priceRight td m) p ≤
       clippedProfit td m (priceRight td m) (priceLeft td m)) ∧
    (∀ p : ℝ, 0 ≤ p →
       clippedProfit td (1-m) (priceLeft td m) p ≤
       clippedProfit td (1-m) (priceLeft td m) (priceRight td m)) := by
  have hLPrice : 0 ≤ priceLeft td m := by
    unfold priceLeft
    positivity
  have hRPrice : 0 ≤ priceRight td m := by
    unfold priceRight
    have h : 0 ≤ 2-m := by linarith
    positivity
  constructor
  · rw [← priceLeft_is_optimal td m]
    have hShare : indifferentConsumer td m (optimalInteriorPrice td m (priceRight td m))
       (priceRight td m) = conditionalShareLeft m := by
      rw [priceLeft_is_optimal]
      exact price_share_left td m (ne_of_gt htd)
    apply clipping_price_best_reply td m (priceRight td m) htd
      (by rw [priceLeft_is_optimal]; exact hLPrice)
      (by rw [hShare]; unfold conditionalShareLeft; linarith)
      (by rw [hShare]; unfold conditionalShareLeft; linarith)
  · rw [← priceRight_is_optimal td m]
    have hReflect : indifferentConsumer td (1-m) (priceRight td m)
       (priceLeft td m) = conditionalShareLeft (1-m) := by
      rw [right_is_left_after_reflection]
      exact price_share_left td (1-m) (ne_of_gt htd)
    apply clipping_price_best_reply td (1-m) (priceLeft td m) htd
      (by rw [priceRight_is_optimal]; exact hRPrice)
      (by rw [priceRight_is_optimal, hReflect]; unfold conditionalShareLeft; linarith)
      (by rw [priceRight_is_optimal, hReflect]; unfold conditionalShareLeft; linarith)

/- Failure-state probabilities for the joint Bernoulli model: none,
   only left, only right, and both. No independence is assumed. -/
def bothFail (q rho : ℝ) : ℝ := q*q + q*(1-q)*rho
def onlyLeftFail (q rho : ℝ) : ℝ := q*(1-q)*(1-rho)
def onlyRightFail (q rho : ℝ) : ℝ := q*(1-q)*(1-rho)
def neitherFail (q rho : ℝ) : ℝ := (1-q)*(1-q)+q*(1-q)*rho

theorem joint_failures_sum_one (q rho : ℝ) :
    neitherFail q rho + onlyLeftFail q rho +
      onlyRightFail q rho + bothFail q rho = 1 := by
  unfold neitherFail onlyLeftFail onlyRightFail bothFail
  ring

theorem joint_failures_left_marginal (q rho : ℝ) :
    bothFail q rho + onlyLeftFail q rho = q := by
  unfold bothFail onlyLeftFail
  ring

theorem joint_failures_right_marginal (q rho : ℝ) :
    bothFail q rho + onlyRightFail q rho = q := by
  unfold bothFail onlyRightFail
  ring

theorem joint_failures_nonnegative (q rho : ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hrho0 : 0 ≤ rho) (hrho1 : rho ≤ 1) :
    0 ≤ neitherFail q rho ∧ 0 ≤ onlyLeftFail q rho ∧
    0 ≤ onlyRightFail q rho ∧ 0 ≤ bothFail q rho := by
  have hqone : 0 ≤ 1-q := by linarith
  have hrhoone : 0 ≤ 1-rho := by linarith
  unfold neitherFail onlyLeftFail onlyRightFail bothFail
  constructor
  · positivity
  constructor
  · positivity
  constructor
  · positivity
  · positivity

theorem geographic_rescue_probability_identity (q d : ℝ) :
    onlyLeftFail q (1-d) * (1-d) = rescue q d := by
  unfold onlyLeftFail rescue intensity
  ring

end RescueHotellingExtendedGame

#print axioms RescueHotellingExtendedGame.price_competition_nash
#print axioms RescueHotellingExtendedGame.joint_failures_nonnegative
