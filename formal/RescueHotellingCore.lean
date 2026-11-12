import Mathlib

/-!
# RescueHotellingCore — Lean 4 + mathlib formalization draft

IMPORTANT: SOURCE SUBMITTED FOR KERNEL VERIFICATION VIA GITHUB ACTIONS.
Formal verification status is recorded in the CI logs.
There are no intentional unproved placeholder declarations in the executable
proof sections. This is NOT proof of successful compilation. Statements below formalize ALGEBRAIC
cores or conditional implications, NOT the full extensive-form SPNE theorem.
See FORMALIZATION_STATUS.md for the precise proof coverage.
-/

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
  · have hh : quadratic T B C y < quadratic T B C x :=
      @quadratic_strict_increase T B C y x hT hB hy hlt
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
  let S : ℝ := Real.sqrt (B*B+4*T*C)
  have hrad : 0 ≤ B*B+4*T*C := by positivity
  have hs : S*S = B*B+4*T*C := by
    dsimp [S]
    nlinarith [Real.sq_sqrt hrad]
  have hdenpos : 0 < B+S := add_pos_of_pos_of_nonneg hB (by
    dsimp [S]
    exact Real.sqrt_nonneg _)
  have hden : B+S ≠ 0 := ne_of_gt hdenpos
  have hrel : 4*T*C+2*B*(B+S)-(B+S)^2 = 0 := by
    nlinarith [hs]
  have hrelC : C*(4*T*C+2*B*(B+S)-(B+S)^2) = 0 := by
    rw [hrel]
    ring
  change T*(2*C/(B+S))*(2*C/(B+S)) + B*(2*C/(B+S)) - C = 0
  field_simp [hden]
  nlinarith [hrelC]

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
  have hp1 : 0 < 3*c+4*survival q*t := by linarith
  have hp2 : 0 < c+survival q*t := by linarith
  have hp3 : 0 < 3*c+2*survival q*t := by linarith
  have hn : 0 < survival q*t*(3*c+4*survival q*t) := mul_pos hrt hp1
  have hd : 0 < 2*(c+survival q*t)*(3*c+2*survival q*t) :=
    mul_pos (mul_pos (by norm_num) hp2) hp3
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
  dsimp [welfareSlope, cutoffNumerator, contractFOC, quadratic,
    rescuePrime, rescue, mismatch, intensity, survival, tCoeff, bCoeff, cCoeff]
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
#print axioms RescueHotelling.contract_FOC_decomposition
#print axioms RescueHotelling.contract_distance_gt_no_contract
#print axioms RescueHotelling.no_contract_excessive_distance
#print axioms RescueHotelling.welfare_cutoff_at_private_FOC



/-!
## v0.4.2 extension: global deviation envelopes and risk response

These results are kernel-checkable algebraic implications. Analytical derivation
of the envelope premises from the extensive-form game and a full formal proof
of the SPNE remain outside this module. See the coverage ledger.
-/

namespace RescueHotelling

-- Appendix B, R1: refusal after a same-side relocation is strictly inferior
-- when a strong-concavity envelope holds and H exceeds g²/(2c).
theorem R1_excludes_contract_refusal
    (c g H N0 Ndeviate z : ℝ)
    (hc : 0 < c)
    (henv : Ndeviate ≤ N0 - g*z - c*z*z/2)
    (hR1 : g*g/(2*c) < H) :
    Ndeviate < N0+H := by
  have hquadratic := strong_concavity_quadratic_bound c (-g) z hc
  have hsign : (-g)*(-g) = g*g := by ring
  rw [hsign] at hquadratic
  linarith

-- Appendix B and H: optimize an unbounded quadratic superset of all
-- feasible crossing relocations, including the zero-distance boundary.
theorem quadratic_crossing_upper_bound
    (K B u : ℝ) (hK : 0 < K) (hu : 0 ≤ u) :
    B*u-K*u*u/2 ≤
      (max 0 B)*(max 0 B)/(2*K) := by
  have hBl : B ≤ max 0 B := le_max_right 0 B
  have hlin : B*u ≤ (max 0 B)*u :=
    mul_le_mul_of_nonneg_right hBl hu
  have hquad := strong_concavity_quadratic_bound K (max 0 B) u hK
  linarith

-- Appendix B, R2: conditional global crossing-deviation exclusion.
-- The crossing payoff envelope and the primitive bound K>0 are explicit inputs.
theorem R2_excludes_all_crossing_relocations
    (c r t d H K B u Udeviate : ℝ)
    (hK : 0 < K) (hu : 0 ≤ u)
    (henv : Udeviate ≤
      -c*d*d/8 + B*u-K*u*u/2)
    (hR2 : (max 0 B)*(max 0 B)/(2*K) < r*t*d/2+H) :
    Udeviate < r*t*d/2-c*d*d/8+H := by
  have hb := quadratic_crossing_upper_bound K B u hK hu
  linarith

-- The positive-intercept rescue technology in Appendix H.
def rhoRescuePoly (A rho e k u : ℝ) : ℝ :=
  A*(e+k*u-rho*u*u)

-- Unlike the baseline a(0)=0, this holds when rho<1 and e=1-rho.
theorem rhoRescue_upper_affine
    (A rho e k u : ℝ)
    (hA : 0 ≤ A) (hrho : 0 ≤ rho) :
    rhoRescuePoly A rho e k u ≤ A*(e+k*u) := by
  have hn : 0 ≤ A*rho*(u*u) :=
    mul_nonneg (mul_nonneg hA hrho) (mul_self_nonneg u)
  unfold rhoRescuePoly
  nlinarith

-- Exact expansion used in the post-crossing contracting-option envelope.
theorem rho_contract_option_upper
    (A rho e k u t V F rev : ℝ)
    (hA : 0 ≤ A) (hrho : 0 ≤ rho)
    (hu : 0 ≤ u) (ht : 0 ≤ t)
    (hV : 0 ≤ V) (hF : 0 ≤ F)
    (hrev : 0 ≤ rev) (hrevBound : rev ≤ 5*t*u/9)
    (ha : 0 ≤ rhoRescuePoly A rho e k u) :
    max 0 (rhoRescuePoly A rho e k u*(rev+V)-F) ≤
      A*e*V+A*(k*V+5*e*t/9)*u+5*A*k*t*u*u/9 := by
  let a := rhoRescuePoly A rho e k u
  have hAup : a ≤ A*(e+k*u) :=
    rhoRescue_upper_affine A rho e k u hA hrho
  have hsum : 0 ≤ rev+V := add_nonneg hrev hV
  have hsum2 : 0 ≤ 5*t*u/9+V := by positivity
  have hopen : max 0 (a*(rev+V)-F) ≤ a*(rev+V) := by
    apply max_le
    · exact mul_nonneg ha hsum
    · linarith
  have hstep : a*(rev+V) ≤ a*(5*t*u/9+V) :=
    mul_le_mul_of_nonneg_left (by linarith) ha
  have hstep2 : a*(5*t*u/9+V) ≤
      A*(e+k*u)*(5*t*u/9+V) :=
    mul_le_mul_of_nonneg_right hAup hsum2
  calc
    max 0 (a*(rev+V)-F)
        ≤ a*(rev+V) := hopen
    _ ≤ a*(5*t*u/9+V) := hstep
    _ ≤ A*(e+k*u)*(5*t*u/9+V) := hstep2
    _ = A*e*V+A*(k*V+5*e*t/9)*u+5*A*k*t*u*u/9 := by ring

-- Appendix H, R2_rho: the positive rescue intercept AeV remains on
-- the deviation side of the comparison, unlike the baseline model.
theorem R2rho_excludes_all_crossing_relocations
    (c r t d H K B A e V u Udeviate : ℝ)
    (hK : 0 < K) (hu : 0 ≤ u)
    (henv : Udeviate ≤
      -c*d*d/8 + A*e*V+B*u-K*u*u/2)
    (hR2rho : A*e*V+
      (max 0 B)*(max 0 B)/(2*K) < r*t*d/2+H) :
    Udeviate < r*t*d/2-c*d*d/8+H := by
  have hb := quadratic_crossing_upper_bound K B u hK hu
  linarith

-- The sufficient conditions K>0 and R2rho are not merely labels:
-- the following coefficients coincide with Appendix H (60)-(62).
def rhoCrossingK (A k t c : ℝ) : ℝ := c-10*A*k*t/9
def rhoCrossingB (A e k r t c V d : ℝ) : ℝ :=
  r*t/2-c*d/2+A*(k*V+5*e*t/9)

theorem R2rho_from_paper_envelope
    (A e k r t c V d H u Udeviate : ℝ)
    (hK : 0 < rhoCrossingK A k t c) (hu : 0 ≤ u)
    (henv : Udeviate ≤
      -c*d*d/8+A*e*V+
      rhoCrossingB A e k r t c V d*u-
      rhoCrossingK A k t c*u*u/2)
    (hR2rho : A*e*V+
      (max 0 (rhoCrossingB A e k r t c V d))*
      (max 0 (rhoCrossingB A e k r t c V d))/
      (2*rhoCrossingK A k t c) < r*t*d/2+H) :
    Udeviate < r*t*d/2-c*d*d/8+H := by
  exact R2rho_excludes_all_crossing_relocations c r t d H
    (rhoCrossingK A k t c)
    (rhoCrossingB A e k r t c V d) A e V u Udeviate
    hK hu henv hR2rho

-- Proposition 4, analytic risk-response numerator: D=-partial_q G.
def riskKernel (t V d : ℝ) : ℝ :=
  (1-2*d)*V+t*d*(1-3*d/2)

def riskResponseNumerator (q t V d : ℝ) : ℝ :=
  (1-2*q)*riskKernel t V d-t*(1/2-d/3)

def contractedGd (q t c V d : ℝ) : ℝ :=
  3*intensity q*t*d+bCoeff q t c V

theorem contracted_G_risk_decomposition (q t c V d : ℝ) :
    contractFOC q t c V d =
      noContractFOC q t c d - intensity q*riskKernel t V d := by
  unfold contractFOC noContractFOC quadratic tCoeff bCoeff cCoeff
    riskKernel intensity survival
  ring

-- Exact polynomial difference yields the partial-q derivative numerator.
theorem contracted_G_q_increment (q t c V d h : ℝ) :
    contractFOC (q+h) t c V d-contractFOC q t c V d =
      -riskResponseNumerator q t V d*h+
      h*h*riskKernel t V d := by
  unfold riskResponseNumerator riskKernel
    contractFOC quadratic tCoeff bCoeff cCoeff intensity survival
  ring

-- Exact polynomial difference yields the partial-d derivative denominator.
theorem contracted_G_d_increment (q t c V d h : ℝ) :
    contractFOC q t c V (d+h)-contractFOC q t c V d =
      contractedGd q t c V d*h+tCoeff q t*h*h := by
  unfold contractFOC contractedGd quadratic tCoeff bCoeff cCoeff
  ring

-- Under the implicit derivative identity G_d * d' = D, regularity
-- turns the algebraic numerator into the economic direction of relocation.
theorem positive_contract_risk_response
    (q t c V d dprime : ℝ)
    (hregular : 0 < contractedGd q t c V d)
    (himplicit : contractedGd q t c V d*dprime =
      riskResponseNumerator q t V d)
    (hD : 0 < riskResponseNumerator q t V d) :
    0 < dprime := by
  by_contra hn
  have hnonpos : dprime ≤ 0 := le_of_not_gt hn
  have hprod : contractedGd q t c V d*dprime ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (le_of_lt hregular) hnonpos
  linarith

-- The negative benchmark slope, conditional on c,t>0 and q<1.
def noContractRiskSlope (q t c : ℝ) : ℝ :=
  -(9*c*t)/(3*c+2*survival q*t)^2

theorem no_contract_risk_slope_negative
    (q t c : ℝ) (hc : 0 < c) (ht : 0 < t)
    (hq : q < 1) :
    noContractRiskSlope q t c < 0 := by
  have hr : 0 < survival q := by
    unfold survival
    linarith
  have hden : 0 < 3*c+2*survival q*t := by positivity
  have hn : 0 < 9*c*t := by positivity
  have hdiv : 0 < (9*c*t)/(3*c+2*survival q*t)^2 :=
    div_pos hn (pow_pos hden 2)
  have hEq : -(9*c*t)/(3*c+2*survival q*t)^2 =
      -((9*c*t)/(3*c+2*survival q*t)^2) := by ring
  unfold noContractRiskSlope
  rw [hEq]
  linarith

-- Proposition 4's local reversal from the two formulae.
theorem risk_response_reversal
    (q t c V d dprime : ℝ)
    (hc : 0 < c) (ht : 0 < t) (hq : q < 1)
    (hregular : 0 < contractedGd q t c V d)
    (himplicit : contractedGd q t c V d*dprime =
      riskResponseNumerator q t V d)
    (hD : 0 < riskResponseNumerator q t V d) :
    0 < dprime ∧ noContractRiskSlope q t c < 0 := by
  exact ⟨positive_contract_risk_response q t c V d dprime
    hregular himplicit hD,
    no_contract_risk_slope_negative q t c hc ht hq⟩

end RescueHotelling

#print axioms RescueHotelling.R1_excludes_contract_refusal
#print axioms RescueHotelling.R2_excludes_all_crossing_relocations
#print axioms RescueHotelling.rho_contract_option_upper
#print axioms RescueHotelling.R2rho_from_paper_envelope
#print axioms RescueHotelling.contracted_G_q_increment
#print axioms RescueHotelling.contracted_G_d_increment
#print axioms RescueHotelling.risk_response_reversal
