/-!
# RescueHotellingCore — Lean 4 + mathlib formalization draft

IMPORTANT: SOURCE SUBMITTED FOR KERNEL VERIFICATION VIA GITHUB ACTIONS.
Formal verification status is recorded in the CI logs.
There are no intentional unproved placeholder declarations in the executable
proof sections. This is NOT proof of successful compilation. Statements below formalize ALGEBRAIC
cores or conditional implications, NOT the full extensive-form SPNE theorem.
See FORMALIZATION_STATUS.md for the precise proof coverage.
-/
import Mathlib

noncomputable section
namespace RescueHotelling

def survival (q : ℝ) : ℝ := 1 - q
def intensity (q : ℝ) : ℝ := q * (1 - q)
def rescue (q d : ℝ) : ℝ := intensity q * d * (1 - d)
def rescuePrime (q d : ℝ) : ℝ := intensity q * (1 - 2*d)
def mismatch (d : ℝ) : ℝ := (1 - 3*d + 3*d*d) / 12

def quadratic (T B C d : ℝ) : ℝ := T*d*d + B*d - C

def tCoeff (q t : ℝ) : ℝ := 3 * intensity q * t / 2
def bCoeff (q t c V : ℝ) : ℝ := c/2 + survival q*t/3 - intensity q*t + 2*intensity q*V
def cCoeff (q t V : ℝ) : ℝ := survival q*t/2 + intensity q*V

def contractFOC (q t c V d : ℝ) : ℝ :=
  quadratic (tCoeff q t) (bCoeff q t c V) (cCoeff q t V) d

def noContractFOC (q t c d : ℝ) : ℝ :=
  c*d/2 - survival q*t*(1/2-d/3)

def contractMarginal (q t V d : ℝ) : ℝ :=
  rescuePrime q d * (t*d/2+V) + t*rescue q d/2

def noContractDistance (q t c : ℝ) : ℝ :=
  3*survival q*t/(3*c+2*survival q*t)

def noContractSocialDistance (q t c : ℝ) : ℝ :=
  survival q*t/(2*(c+survival q*t))

-- B1: rescue kernel positivity, the economic "surviving partner" condition.
theorem rescue_pos {q d : ℝ} (hq0 : 0 < q) (hq1 : q < 1)
    (hd0 : 0 < d) (hd1 : d < 1) : 0 < rescue q d := by
  unfold rescue intensity
  exact mul_pos (mul_pos (mul_pos hq0 (sub_pos.mpr hq1)) hd0)
    (sub_pos.mpr hd1)

-- B2: exact polynomial identity from differentiated contract profit.
theorem contract_FOC_decomposition (q t c V d : ℝ) :
    contractFOC q t c V d =
      noContractFOC q t c d - contractMarginal q t V d := by
  unfold contractFOC noContractFOC contractMarginal quadratic
    tCoeff bCoeff cCoeff rescue rescuePrime intensity survival
  ring

-- B3: a quadratic is strictly increasing on the nonnegative ray
-- when the quadratic coefficient is nonnegative and its linear coefficient positive.
theorem quadratic_strict_increase {T B C x y : ℝ}
    (hT : 0 ≤ T) (hB : 0 < B) (hx : 0 ≤ x) (hxy : x < y) :
    quadratic T B C x < quadratic T B C y := by
  have hsum : 0 ≤ x+y := by linarith
  have hfactor : 0 < T*(x+y)+B :=
    add_pos_of_nonneg_of_pos (mul_nonneg hT hsum) hB
  have hdiff : quadratic T B C y - quadratic T B C x =
      (y-x)*(T*(y+x)+B) := by
    unfold quadratic
    ring
  have hprod : 0 < (y-x)*(T*(y+x)+B) :=
    mul_pos (sub_pos.mpr hxy) (by simpa [add_comm] using hfactor)
  linarith

-- B4: negative value at a candidate smaller than the unique nonnegative root.
theorem quadratic_root_order {T B C x y : ℝ}
    (hT : 0 ≤ T) (hB : 0 < B) (hx : 0 ≤ x) (hy : 0 ≤ y)
    (hneg : quadratic T B C x < 0)
    (hroot : quadratic T B C y = 0) : x < y := by
  by_contra h
  have hyx : y ≤ x := le_of_not_gt h
  rcases eq_or_lt_of_le hyx with heq | hlt
  · rw [heq] at hroot
    linarith
  · have hh := quadratic_strict_increase hT hB hy hlt
    linarith

-- B5: the technology gain from additional distance is positive for d<1/2.
theorem contractMarginal_pos {q t V d : ℝ}
    (hq0 : 0 < q) (hq1 : q < 1) (ht : 0 < t)
    (hV : 0 < V) (hd0 : 0 < d) (hdh : d < 1/2) :
    0 < contractMarginal q t V d := by
  have hA : 0 < intensity q := mul_pos hq0 (sub_pos.mpr hq1)
  have hap : 0 < rescuePrime q d := by
    unfold rescuePrime
    exact mul_pos hA (by linarith)
  have ha : 0 < rescue q d :=
    rescue_pos hq0 hq1 hd0 (by linarith)
  have hvalue : 0 < t*d/2+V := by positivity
  unfold contractMarginal
  have h1 : 0 < rescuePrime q d*(t*d/2+V) := mul_pos hap hvalue
  have h2 : 0 < t*rescue q d/2 := by positivity
  linarith

-- B6: CONDITIONAL root comparison. Assumptions explicitly include
-- positivity/regularity of both quadratic root problems.
theorem contract_distance_gt_no_contract
    {q t c V d0 dC : ℝ}
    (hT : 0 ≤ tCoeff q t) (hB : 0 < bCoeff q t c V)
    (hd0 : 0 ≤ d0) (hdC : 0 ≤ dC)
    (hG0 : noContractFOC q t c d0 = 0)
    (hg : 0 < contractMarginal q t V d0)
    (hGC : contractFOC q t c V dC = 0) : d0 < dC := by
  have hid := contract_FOC_decomposition q t c V d0
  have hneg : contractFOC q t c V d0 < 0 := by linarith
  exact quadratic_root_order hT hB hd0 hdC hneg hGC

-- B7: closed-form root, given the standard positive denominator conditions.
theorem quadratic_closed_form_root {T B C : ℝ}
    (hT : 0 < T) (hB : 0 < B) (hC : 0 < C) :
    quadratic T B C (2*C/(B+Real.sqrt (B*B+4*T*C))) = 0 := by
  have hrad : 0 ≤ B*B+4*T*C := by positivity
  have hsq := Real.sq_sqrt hrad
  have hdenpos : 0 < B+Real.sqrt (B*B+4*T*C) :=
    add_pos_of_pos_of_nonneg hB (Real.sqrt_nonneg _)
  have hden : B+Real.sqrt (B*B+4*T*C) ≠ 0 := ne_of_gt hdenpos
  have hmult := congrArg (fun z : ℝ => C*z) hsq
  unfold quadratic
  field_simp [hden]
  nlinarith [hmult]

-- B7a: the closed-form no-contract location satisfies its own private FOC.
theorem no_contract_distance_solves_FOC (q t c : ℝ)
    (hc : 0 < c) (hrt : 0 < survival q*t) :
    noContractFOC q t c (noContractDistance q t c) = 0 := by
  have hden : 3*c+2*survival q*t ≠ 0 := ne_of_gt (by linarith)
  unfold noContractFOC noContractDistance
  field_simp [hden]
  ring

-- B7b: under the strong hub-cost inequality the no-contract root is interior.
theorem no_contract_distance_lt_half (q t c : ℝ)
    (hrt : 0 < survival q*t) (hc : 4*survival q*t < 3*c) :
    noContractDistance q t c < 1/2 := by
  have hden : 0 < 3*c+2*survival q*t := by linarith
  unfold noContractDistance
  apply (div_lt_iff₀ hden).2
  nlinarith

-- B8: the social mismatch integral as a closed-form (the integral
-- evaluation itself is NOT kernel-verified in this file).
def mismatchFull (d m : ℝ) : ℝ :=
  mismatch d+(9-5*d)*(m-1/2)*(m-1/2)/9

theorem mismatch_midpoint_comparison (d m : ℝ) (hd0 : 0 ≤ d)
    (hd1 : d ≤ 1) : mismatch d ≤ mismatchFull d m := by
  have hcoef : 0 ≤ (9-5*d)/9 := by
    have hh : 0 ≤ 9-5*d := by linarith
    exact div_nonneg hh (by norm_num)
  have hs : 0 ≤ (m-1/2)*(m-1/2) := mul_self_nonneg _
  unfold mismatchFull
  nlinarith [mul_nonneg hcoef hs]

-- B9: conditional branch gains of negotiated production agreements.
def jointSurplus (q t V F d RA RB : ℝ) : ℝ :=
  rescue q d*(RA+RB+2*V)-2*F

def individualContractGain (q t V F d RA RB : ℝ) : ℝ :=
  rescue q d*((RA+RB)/2+V)-F

theorem contract_surplus_split (q t V F d RA RB : ℝ) :
    jointSurplus q t V F d RA RB =
    2*individualContractGain q t V F d RA RB := by
  unfold jointSurplus individualContractGain
  ring

-- B10: PRIVATE versus SOCIAL payoff, in both contract regimes.
def welfareNoContract (q t c v Lambda d : ℝ) : ℝ :=
  survival q*(v-t*mismatch d)-c*d*d/4-2*q*Lambda

def welfareContract (q t c v Lambda V F d : ℝ) : ℝ :=
  (survival q+rescue q d)*(v-t*mismatch d)
  +2*rescue q d*V-2*F-c*d*d/4-2*q*Lambda

theorem welfare_contract_increment (q t c v Lambda V F d : ℝ) :
    welfareContract q t c v Lambda V F d -
    welfareNoContract q t c v Lambda d =
    rescue q d*(v-t*mismatch d+2*V)-2*F := by
  unfold welfareContract welfareNoContract
  ring

-- B11: the no-contract "excessive differentiation" distance gap.
theorem no_contract_distance_gap (q t c : ℝ)
    (hct : 0 < c) (hrt : 0 < survival q*t) :
    noContractDistance q t c - noContractSocialDistance q t c =
    survival q*t*(3*c+4*survival q*t) /
     (2*(c+survival q*t)*(3*c+2*survival q*t)) := by
  have hden1 : c+survival q*t ≠ 0 := ne_of_gt (by linarith)
  have hden2 : 3*c+2*survival q*t ≠ 0 := ne_of_gt (by linarith)
  unfold noContractDistance noContractSocialDistance
  field_simp [hden1,hden2]
  ring

-- B11a: the private no-contract distance is strictly more dispersed
-- than the social no-contract distance, assuming positive primitives.
theorem no_contract_excessive_distance (q t c : ℝ)
    (hc : 0 < c) (hrt : 0 < survival q*t) :
    noContractSocialDistance q t c < noContractDistance q t c := by
  have hgap := no_contract_distance_gap q t c hc hrt
  have hn : 0 < survival q*t*(3*c+4*survival q*t) := by positivity
  have hd : 0 < 2*(c+survival q*t)*(3*c+2*survival q*t) := by positivity
  have hratio : 0 < survival q*t*(3*c+4*survival q*t) /
      (2*(c+survival q*t)*(3*c+2*survival q*t)) := div_pos hn hd
  linarith

-- B11b: the reduced mismatch term is bounded on the unit interval.
theorem mismatch_upper_bound {d : ℝ} (h0 : 0 ≤ d) (h1 : d ≤ 1) :
    mismatch d ≤ 1/12 := by
  have hprod : 0 ≤ d*(1-d) := mul_nonneg h0 (sub_nonneg.mpr h1)
  unfold mismatch
  nlinarith

-- B12: welfare first-order expression and exact private-social wedge.
def welfareSlope (q t c v V d : ℝ) : ℝ :=
  rescuePrime q d*(v-t*mismatch d+2*V)
  +(survival q+rescue q d)*t*(1-2*d)/4-c*d/2

def cutoffNumerator (q t V d : ℝ) : ℝ :=
  rescuePrime q d*(t*mismatch d-V+t*d/2)
  +survival q*t*(1/4+d/6)
  +rescue q d*t*(1/4+d/2)

def valuationCutoff (q t V d : ℝ) : ℝ :=
  cutoffNumerator q t V d / rescuePrime q d

theorem welfare_cutoff_polynomial_identity (q t c v V d : ℝ) :
    welfareSlope q t c v V d -
    (rescuePrime q d*v-cutoffNumerator q t V d) =
    -contractFOC q t c V d := by
  unfold welfareSlope cutoffNumerator contractFOC quadratic
    rescuePrime rescue mismatch intensity survival tCoeff bCoeff cCoeff
  ring

theorem welfare_cutoff_at_private_FOC (q t c v V d : ℝ)
    (hFOC : contractFOC q t c V d = 0)
    (hap : rescuePrime q d ≠ 0) :
    welfareSlope q t c v V d =
      rescuePrime q d*(v-valuationCutoff q t V d) := by
  have hId := welfare_cutoff_polynomial_identity q t c v V d
  have hmul : rescuePrime q d * valuationCutoff q t V d =
      cutoffNumerator q t V d := by
    unfold valuationCutoff
    field_simp [hap]
  rw [mul_sub, hmul]
  linarith

-- B13: the economic direction of welfare at a private equilibrium.
theorem welfare_slope_sign_above_cutoff (q t c v V d : ℝ)
    (hFOC : contractFOC q t c V d = 0)
    (hap : 0 < rescuePrime q d)
    (hv : valuationCutoff q t V d < v) :
    0 < welfareSlope q t c v V d := by
  rw [welfare_cutoff_at_private_FOC q t c v V d hFOC (ne_of_gt hap)]
  exact mul_pos hap (sub_pos.mpr hv)

-- B14: a generic global-deviation certificate building block.
-- If a payoff function has a strongly-concave tangent upper bound,
-- the maximum gain above its tangent is at most g^2/(2*c).
theorem strong_concavity_quadratic_bound (c g z : ℝ) (hc : 0 < c) :
    g*z-c*z*z/2 ≤ g*g/(2*c) := by
  have hs := sq_nonneg (c*z-g)
  apply (le_div_iff₀ (by positivity : 0 < 2*c)).2
  nlinarith [hs]

end RescueHotelling