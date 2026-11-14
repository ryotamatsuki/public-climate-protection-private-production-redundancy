import Mathlib
import RescueHotellingCore

/-!
Exact rescue-value comparative statics as a strict ORDERING of
selected regular contracted stationarity roots. This avoids
pretending that a proof of a derivative has been completed.
-/
noncomputable section
namespace RescueHotellingValue
open RescueHotelling

theorem contractFOC_value_difference (q t c V₁ V₂ d : ℝ) :
    contractFOC q t c V₂ d =
      contractFOC q t c V₁ d -
      intensity q*(V₂-V₁)*(1-2*d) := by
  unfold contractFOC quadratic tCoeff bCoeff cCoeff intensity survival
  ring

theorem higher_rescue_value_increases_selected_root
    (q t c V₁ V₂ d₁ d₂ : ℝ)
    (hq0 : 0 < q) (hq1 : q < 1) (ht : 0 < t)
    (hV : V₁ < V₂)
    (hd10 : 0 ≤ d₁) (hd1half : d₁ < 1/2) (hd20 : 0 ≤ d₂)
    (hB : 0 < bCoeff q t c V₂)
    (hG1 : contractFOC q t c V₁ d₁ = 0)
    (hG2 : contractFOC q t c V₂ d₂ = 0) :
    d₁ < d₂ := by
  have hA : 0 < intensity q := by
    unfold intensity
    exact mul_pos hq0 (by linarith)
  have hGain : 0 < intensity q*(V₂-V₁)*(1-2*d₁) := by
    exact mul_pos (mul_pos hA (by linarith)) (by linarith)
  have hdiff := contractFOC_value_difference q t c V₁ V₂ d₁
  have hneg : contractFOC q t c V₂ d₁ < 0 := by
    rw [hdiff,hG1]
    linarith
  have hT : 0 ≤ tCoeff q t := by
    unfold tCoeff
    positivity
  change quadratic (tCoeff q t) (bCoeff q t c V₂)
      (cCoeff q t V₂) d₁ < 0 at hneg
  change quadratic (tCoeff q t) (bCoeff q t c V₂)
      (cCoeff q t V₂) d₂ = 0 at hG2
  exact quadratic_root_order hT hB hd10 hd20 hneg hG2

end RescueHotellingValue
#print axioms RescueHotellingValue.higher_rescue_value_increases_selected_root
