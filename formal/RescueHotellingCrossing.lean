import Mathlib
import RescueHotellingCore
import RescueHotellingLocation
import RescueHotellingRefusal

/-!
R2 across-rival location deviations, including endogenous refusal.
The theorem uses the exact conditional price revenues from the paper,
the positive-part contracting option, and the quadratic R2 upper bound.
-/
noncomputable section
namespace RescueHotellingCrossing
open RescueHotelling RescueHotellingLocation RescueHotellingRefusal

def crossingMidpoint (d u : ℝ) : ℝ := (1+d+u)/2
def crossingRivalRevenue (t d u : ℝ) : ℝ :=
  2*t*u*(1+crossingMidpoint d u)^2/9
def crossingDeviatorRevenue (t d u : ℝ) : ℝ :=
  2*t*u*(2-crossingMidpoint d u)^2/9
def crossingRescue (A u : ℝ) : ℝ := A*u*(1-u)
def crossingMeanRevenue (t d u : ℝ) : ℝ :=
  (crossingDeviatorRevenue t d u + crossingRivalRevenue t d u)/2
def crossingPayoff (r A t c V F d u : ℝ) : ℝ :=
  r*crossingDeviatorRevenue t d u-c*(d/2+u)^2/2+
  max 0 (crossingRescue A u*(crossingMeanRevenue t d u+V)-F)

theorem crossing_midpoint_range (d u : ℝ)
    (hd : 0 ≤ d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2) :
    1/2 ≤ crossingMidpoint d u ∧ crossingMidpoint d u ≤ 1 := by
  unfold crossingMidpoint
  constructor <;> linarith

theorem crossing_revenue_upper_bounds (t d u : ℝ)
    (ht : 0 ≤ t) (hd : 0 ≤ d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2) :
    crossingDeviatorRevenue t d u ≤ t*u/2 ∧
    crossingMeanRevenue t d u ≤ 5*t*u/9 := by
  obtain ⟨hm0,hm1⟩ :=
    crossing_midpoint_range d u hd hd1 hu hur
  let m := crossingMidpoint d u
  have hOne : 0 ≤ 1-m := by linarith
  have hTwo : 0 ≤ 2-m := by linarith
  have hNine : (2-m)^2 ≤ (3/2 : ℝ)^2 := by nlinarith
  have hFive : (1+m)^2 + (2-m)^2 ≤ (5:ℝ) := by
    have hm : 0 ≤ m*(1-m) := mul_nonneg (by linarith) hOne
    nlinarith
  have hScale : 0 ≤ 2*t*u/9 := by positivity
  have hScaleMean : 0 ≤ t*u/9 := by positivity
  have hR : 2*t*u*(2-m)^2/9 ≤ t*u/2 := by
    have hMul := mul_le_mul_of_nonneg_left hNine hScale
    nlinarith
  have hM : t*u*((1+m)^2+(2-m)^2)/9 ≤ 5*t*u/9 := by
    have hMul := mul_le_mul_of_nonneg_left hFive hScaleMean
    nlinarith
  constructor
  · unfold crossingDeviatorRevenue
    change 2*t*u*(2-m)^2/9 ≤ t*u/2
    exact hR
  · unfold crossingMeanRevenue crossingDeviatorRevenue
      crossingRivalRevenue
    change (2*t*u*(2-m)^2/9+2*t*u*(1+m)^2/9)/2 ≤ 5*t*u/9
    nlinarith [hM]

theorem crossing_rescue_bound (A u : ℝ)
    (hA : 0 ≤ A) (hu : 0 ≤ u) (hu1 : u ≤ 1) :
    0 ≤ crossingRescue A u ∧ crossingRescue A u ≤ A*u := by
  have h1 : 0 ≤ 1-u := by linarith
  have hAu : 0 ≤ A*u := mul_nonneg hA hu
  unfold crossingRescue
  constructor
  · exact mul_nonneg hAu h1
  · have hn : 0 ≤ A*u*u := mul_nonneg hAu hu
    nlinarith

theorem crossing_payoff_upper_envelope
    (r A t c V F d u : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t)
    (hc : 0 ≤ c) (hV : 0 ≤ V) (hF : 0 ≤ F)
    (hd : 0 ≤ d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2) :
    crossingPayoff r A t c V F d u ≤
      -c*d*d/8+(r*t/2+A*V-c*d/2)*u
        -(c-10*A*t/9)*u*u/2 := by
  obtain ⟨hRev,hMean⟩ :=
    crossing_revenue_upper_bounds t d u ht hd hd1 hu hur
  have hu1 : u ≤ 1 := by linarith
  obtain ⟨hRescuePos,hRescueBound⟩ :=
    crossing_rescue_bound A u hA hu hu1
  have hMeanPos : 0 ≤ crossingMeanRevenue t d u := by
    unfold crossingMeanRevenue crossingRivalRevenue crossingDeviatorRevenue
    positivity
  have hMuV : 0 ≤ crossingMeanRevenue t d u+V := by linarith
  have hAu : 0 ≤ A*u := mul_nonneg hA hu
  have hGross : 0 ≤ crossingRescue A u *
      (crossingMeanRevenue t d u+V) := mul_nonneg hRescuePos hMuV
  have hOption : max 0 (crossingRescue A u *
      (crossingMeanRevenue t d u+V)-F) ≤
      crossingRescue A u*(crossingMeanRevenue t d u+V) := by
    apply max_le hGross
    linarith
  have hGross1 := mul_le_mul_of_nonneg_right hRescueBound hMuV
  have hGross2 := mul_le_mul_of_nonneg_left
    (show crossingMeanRevenue t d u+V ≤ 5*t*u/9+V by linarith) hAu
  have hGrossUpper :
      max 0 (crossingRescue A u*(crossingMeanRevenue t d u+V)-F)
        ≤ A*u*(5*t*u/9+V) := by
    exact le_trans hOption (le_trans hGross1 hGross2)
  have hRevUpper := mul_le_mul_of_nonneg_left hRev hr
  have hTotal : crossingPayoff r A t c V F d u ≤
      r*t*u/2-c*(d/2+u)^2/2+A*u*(5*t*u/9+V) := by
    unfold crossingPayoff
    linarith
  have hIdentity :
      r*t*u/2-c*(d/2+u)^2/2+A*u*(5*t*u/9+V) =
      -c*d*d/8+(r*t/2+A*V-c*d/2)*u-(c-10*A*t/9)*u*u/2 := by
    ring
  linarith

def acrossQuadratic (r A t c V d u : ℝ) : ℝ :=
  -c*d*d/8+(r*t/2+A*V-c*d/2)*u-(c-10*A*t/9)*u*u/2
def crossingLinear (r A t c V d : ℝ) : ℝ :=
  r*t/2+A*V-c*d/2
def crossingL (r A t c V d : ℝ) : ℝ :=
  max 0 (crossingLinear r A t c V d)
def crossingK (A t c : ℝ) : ℝ := c-10*A*t/9

theorem R2_rules_out_all_crossing_deviations
    (r A t c V F d u : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t)
    (hc : 0 < c) (hV : 0 ≤ V) (hF : 0 ≤ F)
    (hd : 0 ≤ d) (hd1 : d ≤ 1)
    (hu : 0 ≤ u) (hur : u ≤ (1-d)/2)
    (hK : 0 < crossingK A t c)
    (hR2 : (crossingL r A t c V d)^2 /
        (2*crossingK A t c) <
        r*t*d/2+H A t V F d) :
    crossingPayoff r A t c V F d u <
      agreementPayoff r A t c V F (symmetricRivalPosition d) d := by
  have hActual := crossing_payoff_upper_envelope r A t c V F d u
    hr hA ht (le_of_lt hc) hV hF hd hd1 hu hur
  have hMax : crossingLinear r A t c V d ≤ crossingL r A t c V d :=
    le_max_right 0 _
  have hMul := mul_le_mul_of_nonneg_right hMax hu
  have hQuad := RescueHotelling.strong_concavity_quadratic_bound
    (crossingK A t c) (crossingL r A t c V d) u hK
  have hOn := agreement_at_candidate_equals_disagreement_plus_H
    r A t c V F d
  rw [disagreement_symmetric_payoff] at hOn
  unfold crossingK crossingL crossingLinear acrossQuadratic at *
  nlinarith

end RescueHotellingCrossing
#print axioms RescueHotellingCrossing.R2_rules_out_all_crossing_deviations
