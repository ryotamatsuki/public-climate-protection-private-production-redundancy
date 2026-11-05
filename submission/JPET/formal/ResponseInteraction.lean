import Mathlib

/-!
# JPET Proposition 8 — exact response-interaction certificate

This module strengthens the *bounded*, model-specific parts of Proposition 8:
* expands the gamma=0 private-continuation surplus and location probabilities
  into exact public policy payoffs, then checks the first-order coefficients;
* verifies primitive coefficients and all six interior policy levels;
* proves positive / zero / negative response-gap increments;
* proves global planner and unilateral best-response inequalities in all
  three policy games, including the fully endogenous benchmark;
* reconstructs gamma=0 primitive payoffs, optimal private readiness,
  Bayesian location cutoff and national surplus from the original primitives;
* checks all three reduced policy games against their primitive objectives.

The uniform-fit cutoff interpretation and the stochastic independence law
remain economic assumptions; positive-gamma/open-set results are not proved
in Lean. This is not a closed formalization of every stage of the full paper.
No sorry, admit, axiom, or native_decide is used.
-/

namespace JPET.ResponseInteraction

private noncomputable def q0 : ℝ := 3 / 10
private noncomputable def k : ℝ := 2 / 25
private noncomputable def H : ℝ := 1 / 100
private noncomputable def b : ℝ := 11 / 200
private noncomputable def c : ℝ := 10

noncomputable def mu0 : ℝ := (q0 - 3 * k) / (8 * k)
noncomputable def tc : ℝ := c - 1 / (8 * k)
noncomputable def s : ℝ := c - (H + b) / (16 * H * k)
noncomputable def m : ℝ := (H * (3 * k - q0) + b * (4 * k - q0)) / (16 * H * k)

theorem coefficient_values :
    mu0 = 3 / 32 ∧ tc = 135 / 16 ∧ s = 315 / 64 ∧ m = 5 / 128 := by
  norm_num [mu0, tc, s, m, q0, k, H, b, c]

noncomputable def qbar (x y : ℝ) : ℝ := q0 - (x + y) / 2
noncomputable def t (q : ℝ) : ℝ := 3 * (1 - q) / 8 + q ^ 2 / (16 * k)
noncomputable def U (q : ℝ) : ℝ := 1 / (32 * k) + (4 * k - q) * (3 * k - q) / (128 * H * k ^ 2)
noncomputable def h (q : ℝ) : ℝ := (4 * k - q) / (16 * k)
noncomputable def fullSurplus (x y : ℝ) : ℝ :=
  2 * t (qbar x y) + U (qbar x y) * (x - y) ^ 2
noncomputable def locationProb (x y : ℝ) : ℝ :=
  1 / 2 + h (qbar x y) * (x - y) / (2 * H)
noncomputable def fullPlannerPayoff (μ x y : ℝ) : ℝ :=
  fullSurplus x y + 2 * b - c * (x ^ 2 + y ^ 2) / 2 + μ * (x + y)
noncomputable def fullLocalPayoff (μ x y : ℝ) : ℝ :=
  fullSurplus x y / 2 + 2 * b * locationProb x y - c * x ^ 2 / 2 + μ * x

/-! Exact deviations retain all higher-order terms. In particular, the linear
    d coefficient is the public-policy FOC, NOT a global-optimality proof. -/
theorem full_planner_deviation (μ a d : ℝ) :
    fullPlannerPayoff μ (a + d) a - fullPlannerPayoff μ a a =
      d * (μ - 3 / 32 - 135 * a / 16) +
      d ^ 2 * (5 * (12500 * a ^ 2 + 12500 * a * d - 500 * a +
                    3125 * d ^ 2 - 250 * d - 447) / 512) := by
  norm_num [fullPlannerPayoff, fullSurplus, qbar, t, U, q0, k, H, b, c] <;> ring

theorem full_local_deviation (μ a d : ℝ) :
    fullLocalPayoff μ (a + d) a - fullLocalPayoff μ a a =
      d * (μ + 5 / 128 - 315 * a / 64) +
      d ^ 2 * (5 * (12500 * a ^ 2 + 12500 * a * d - 500 * a +
                    3125 * d ^ 2 - 250 * d - 519) / 1024) := by
  norm_num [fullLocalPayoff, fullSurplus, locationProb, qbar, t, U, h, q0, k, H, b, c] <;> ring

noncomputable def fullP (μ : ℝ) : ℝ := (32 * μ - 3) / 270
noncomputable def fullN (μ : ℝ) : ℝ := (128 * μ + 5) / 630
noncomputable def readyP (μ : ℝ) : ℝ := (μ + 3 / 128) / 10
noncomputable def readyN (μ : ℝ) : ℝ := (μ + 25 / 256) / 10
noncomputable def locP (μ : ℝ) : ℝ := 16 / 135 * (μ - 3 / 32)
noncomputable def locN (μ : ℝ) : ℝ := 32 / 295 * (μ - 3 / 64)

theorem full_stationarity (μ : ℝ) :
    (μ - mu0 - tc * fullP μ = 0) ∧ (μ + m - s * fullN μ = 0) := by
  constructor
  · norm_num [mu0, tc, fullP, q0, k, c] <;> ring
  · norm_num [m, s, fullN, q0, k, H, b, c] <;> ring

theorem fixed_readiness_stationarity (μ : ℝ) :
    μ + 3 / 128 - 10 * readyP μ = 0 ∧
    μ + 25 / 256 - 10 * readyN μ = 0 := by
  constructor <;> norm_num [readyP, readyN] <;> ring

theorem fixed_location_stationarity (μ : ℝ) :
    μ - 3 / 32 - 135 / 16 * locP μ = 0 ∧
    μ - 3 / 64 - 295 / 32 * locN μ = 0 := by
  constructor <;> norm_num [locP, locN] <;> ring

theorem all_six_interior (μ : ℝ) (hlo : (3 : ℝ) / 32 < μ)
    (hhi : μ < (1 : ℝ) / 8) :
    (0 < fullP μ ∧ fullP μ < 2 / 25) ∧
    (0 < fullN μ ∧ fullN μ < 2 / 25) ∧
    (0 < readyP μ ∧ readyP μ < 2 / 25) ∧
    (0 < readyN μ ∧ readyN μ < 2 / 25) ∧
    (0 < locP μ ∧ locP μ < 2 / 25) ∧
    (0 < locN μ ∧ locN μ < 2 / 25) := by
  constructor
  · constructor <;> dsimp [fullP] <;> linarith
  constructor
  · constructor <;> dsimp [fullN] <;> linarith
  constructor
  · constructor <;> dsimp [readyP] <;> linarith
  constructor
  · constructor <;> dsimp [readyN] <;> linarith
  constructor
  · constructor <;> dsimp [locP] <;> linarith
  · constructor <;> dsimp [locN] <;> linarith

noncomputable def gapFull (μ : ℝ) : ℝ := fullN μ - fullP μ
noncomputable def gapReady (μ : ℝ) : ℝ := readyN μ - readyP μ
noncomputable def gapLoc (μ : ℝ) : ℝ := locN μ - locP μ

theorem gap_full_increment (μ ν : ℝ) :
    gapFull ν - gapFull μ = (16 / 189 : ℝ) * (ν - μ) := by
  norm_num [gapFull, fullN, fullP] <;> ring

theorem gap_readiness_increment (μ ν : ℝ) :
    gapReady ν - gapReady μ = 0 := by
  norm_num [gapReady, readyN, readyP] <;> ring

theorem gap_location_increment (μ ν : ℝ) :
    gapLoc ν - gapLoc μ = -(16 / 1593 : ℝ) * (ν - μ) := by
  norm_num [gapLoc, locN, locP] <;> ring

theorem response_interaction_signs (μ ν : ℝ) (h : μ < ν) :
    gapFull μ < gapFull ν ∧
    gapReady μ = gapReady ν ∧
    gapLoc ν < gapLoc μ := by
  have hd : (0 : ℝ) < ν - μ := sub_pos.mpr h
  constructor
  · have heq := gap_full_increment μ ν
    have hmul : (0 : ℝ) < (16 / 189 : ℝ) * (ν - μ) :=
      mul_pos (by norm_num) hd
    linarith
  constructor
  · have hz := gap_readiness_increment μ ν
    linarith
  · have heq := gap_location_increment μ ν
    have hmul : (0 : ℝ) < (16 / 1593 : ℝ) * (ν - μ) :=
      mul_pos (by norm_num) hd
    linarith

/-! Fixed-readiness exact objectives, after dropping terms constant in policy. -/
noncomputable def readyPlannerPayoff (μ x y : ℝ) : ℝ :=
    (μ + 3 / 128) * (x + y) + 75 / 2048 * (x - y) ^ 2 -
      5 * (x ^ 2 + y ^ 2)
noncomputable def readyLocalPayoff (μ x y : ℝ) : ℝ :=
    μ * x + 3 / 256 * (x + y) + 75 / 4096 * (x - y) ^ 2 +
      11 / 128 * (x - y) - 5 * x ^ 2

theorem ready_planner_global (μ x y : ℝ) :
    readyPlannerPayoff μ x y ≤
      readyPlannerPayoff μ (readyP μ) (readyP μ) := by
  have hs := (fixed_readiness_stationarity μ).1
  have hmu : μ = 10 * readyP μ - 3 / 128 := by linarith
  have hidentity :
      readyPlannerPayoff μ (readyP μ) (readyP μ) -
      readyPlannerPayoff μ x y =
        (5 / 2 : ℝ) * (x + y - 2 * readyP μ) ^ 2 +
        (5045 / 2048 : ℝ) * (x - y) ^ 2 := by
    dsimp [readyPlannerPayoff]
    linear_combination (2 * readyP μ - x - y) * hmu
  have h1 : (0 : ℝ) ≤ (5 / 2 : ℝ) * (x + y - 2 * readyP μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  have h2 : (0 : ℝ) ≤ (5045 / 2048 : ℝ) * (x - y) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith

theorem ready_local_global (μ x : ℝ) :
    readyLocalPayoff μ x (readyN μ) ≤
      readyLocalPayoff μ (readyN μ) (readyN μ) := by
  have hs := (fixed_readiness_stationarity μ).2
  have hmu : μ = 10 * readyN μ - 25 / 256 := by linarith
  have hidentity :
      readyLocalPayoff μ (readyN μ) (readyN μ) -
      readyLocalPayoff μ x (readyN μ) =
        (20405 / 4096 : ℝ) * (x - readyN μ) ^ 2 := by
    dsimp [readyLocalPayoff]
    linear_combination (readyN μ - x) * hmu
  have hnonneg : (0 : ℝ) ≤ (20405 / 4096 : ℝ) * (x - readyN μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith

/-! Fixed-location reduced objectives with backup reoptimized and p = 1/2. -/
noncomputable def locPlannerPayoff (μ x y : ℝ) : ℝ :=
  (μ - 3 / 32) * (x + y) - 135 / 32 * (x ^ 2 + y ^ 2)
noncomputable def locLocalPayoff (μ x : ℝ) : ℝ :=
  (μ - 3 / 64) * x - 295 / 64 * x ^ 2

theorem loc_planner_global (μ x y : ℝ) :
    locPlannerPayoff μ x y ≤ locPlannerPayoff μ (locP μ) (locP μ) := by
  have hs := (fixed_location_stationarity μ).1
  have hmu : μ = 3 / 32 + 135 / 16 * locP μ := by linarith
  have hidentity :
      locPlannerPayoff μ (locP μ) (locP μ) - locPlannerPayoff μ x y =
        (135 / 32 : ℝ) * ((x - locP μ) ^ 2 + (y - locP μ) ^ 2) := by
    dsimp [locPlannerPayoff]
    linear_combination (2 * locP μ - x - y) * hmu
  have hnonneg : (0 : ℝ) ≤
      (135 / 32 : ℝ) * ((x - locP μ) ^ 2 + (y - locP μ) ^ 2) :=
    mul_nonneg (by norm_num) (add_nonneg (sq_nonneg _) (sq_nonneg _))
  linarith

theorem loc_local_global (μ x : ℝ) :
    locLocalPayoff μ x ≤ locLocalPayoff μ (locN μ) := by
  have hs := (fixed_location_stationarity μ).2
  have hmu : μ = 3 / 64 + 295 / 32 * locN μ := by linarith
  have hidentity :
      locLocalPayoff μ (locN μ) - locLocalPayoff μ x =
        (295 / 64 : ℝ) * (x - locN μ) ^ 2 := by
    dsimp [locLocalPayoff]
    linear_combination (locN μ - x) * hmu
  have hnonneg : (0 : ℝ) ≤ (295 / 64 : ℝ) * (x - locN μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith


/-! The full endogenous gamma=0 planner game admits an exact decomposition
    around the symmetrical optimum. This is a *new Lean globality bridge*.
    It uses the already-reduced private surplus identity, not a derivation
    of that identity from the preceding private-game stages. -/
theorem full_planner_global (μ x y : ℝ)
    (hx0 : 0 ≤ x) (hxbar : x ≤ 2 / 25)
    (hy0 : 0 ≤ y) (hybar : y ≤ 2 / 25) :
    fullPlannerPayoff μ x y ≤ fullPlannerPayoff μ (fullP μ) (fullP μ) := by
  have hmu : μ = (3 : ℝ) / 32 + (135 / 16 : ℝ) * fullP μ := by
    norm_num [fullP] <;> ring
  have hm0 : (0 : ℝ) ≤ (x + y) / 2 := by linarith
  have hmbar : (x + y) / 2 ≤ (2 : ℝ) / 25 := by linarith
  have hbound : (0 : ℝ) ≤
      ((x + y) / 2) * ((2 : ℝ) / 25 - (x + y) / 2) :=
    mul_nonneg hm0 (sub_nonneg.mpr hmbar)
  have hub : U (qbar x y) ≤ (325 : ℝ) / 512 := by
    norm_num [U, qbar, q0, k, H] <;> nlinarith [hbound]
  have hidentity :
      fullPlannerPayoff μ (fullP μ) (fullP μ) - fullPlannerPayoff μ x y =
      tc * ((x + y) / 2 - fullP μ) ^ 2 +
        (c / 4 - U (qbar x y)) * (x - y) ^ 2 := by
    dsimp [fullPlannerPayoff, fullSurplus, qbar, t, U, tc, q0, k, H, b, c]
    linear_combination (2 * fullP μ - x - y) * hmu
  have htc : (0 : ℝ) ≤ tc := by norm_num [tc, c, k]
  have hU : (0 : ℝ) ≤ c / 4 - U (qbar x y) := by
    norm_num [c] at *
    linarith
  have h1 : (0 : ℝ) ≤ tc * ((x + y) / 2 - fullP μ) ^ 2 :=
    mul_nonneg htc (sq_nonneg _)
  have h2 : (0 : ℝ) ≤ (c / 4 - U (qbar x y)) * (x - y) ^ 2 :=
    mul_nonneg hU (sq_nonneg _)
  linarith

/-! Full-endogenous unilateral deviations are also globally dominated on
    the WHOLE policy interval. Strict negativity of the quartic remainder
    follows from a simple interval square bound, rather than just the FOC. -/
theorem full_local_global (μ x : ℝ)
    (hlo : (3 : ℝ) / 32 < μ) (hhi : μ < (1 : ℝ) / 8)
    (hx0 : 0 ≤ x) (hxbar : x ≤ 2 / 25) :
    fullLocalPayoff μ x (fullN μ) ≤
      fullLocalPayoff μ (fullN μ) (fullN μ) := by
  have ha0 : (0 : ℝ) ≤ fullN μ := by dsimp [fullN]; linarith
  have habar : fullN μ ≤ (2 : ℝ) / 25 := by dsimp [fullN]; linarith
  have hz0 : (0 : ℝ) ≤ x + fullN μ := by linarith
  have hzbar : x + fullN μ ≤ (4 : ℝ) / 25 := by linarith
  have hbound : (0 : ℝ) ≤
      (x + fullN μ) * ((4 : ℝ) / 25 - (x + fullN μ)) :=
    mul_nonneg hz0 (sub_nonneg.mpr hzbar)
  have hP : (3125 : ℝ) * (x + fullN μ) ^ 2 -
      250 * (x + fullN μ) - 519 < 0 := by
    nlinarith [hbound]
  have hmu : μ = (315 / 64 : ℝ) * fullN μ - 5 / 128 := by
    norm_num [fullN] <;> ring
  have hidentity :
      fullLocalPayoff μ x (fullN μ) -
        fullLocalPayoff μ (fullN μ) (fullN μ) =
      (5 / 1024 : ℝ) * (x - fullN μ) ^ 2 *
        (3125 * (x + fullN μ) ^ 2 -
          250 * (x + fullN μ) - 519) := by
    dsimp [fullLocalPayoff, fullSurplus, locationProb, qbar, t, U, h,
      q0, k, H, b, c]
    linear_combination (x - fullN μ) * hmu
  have hnonneg : (0 : ℝ) ≤ (5 / 1024 : ℝ) * (x - fullN μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  have hnonpos :
      (5 / 1024 : ℝ) * (x - fullN μ) ^ 2 *
        (3125 * (x + fullN μ) ^ 2 - 250 * (x + fullN μ) - 519) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hnonneg (le_of_lt hP)
  linarith


/-!
## Primitive-to-reduced-form bridge at gamma = 0

The product-market monopoly/Cournot payoff, endogenous private readiness,
location cutoff, national material surplus and government policy objectives
are reconstructed from the model's state-contingent primitives. Fixed-readiness
and fixed-location counterfactual objectives are likewise checked against their
reduced-form counterparts.

The economic interpretation of the uniform location-fit distribution and the
probabilistic independence of disaster/backup draws remains a mathematical
model assumption, rather than a measure-theoretic Lean construction.
-/

-- With separable products, each surviving firm maximizes z * (1-z).
theorem separable_cournot_global (z : ℝ) :
    z * (1 - z) ≤ (1 / 4 : ℝ) := by
  nlinarith [sq_nonneg (z - 1 / 2)]

theorem separable_market_surplus :
    (1 / 2 : ℝ) - (1 / 2 : ℝ) ^ 2 / 2 = 3 / 8 := by
  norm_num

-- Independent backup success conditional on a primary failure.
-- The incremental sole-survivor rent is zero in this benchmark.
noncomputable def primitiveProfit (q r : ℝ) : ℝ :=
  (1 - q * (1 - r)) / 4 - k * r ^ 2 / 2

noncomputable def privateReadiness (q : ℝ) : ℝ := q / (4 * k)
noncomputable def continuationProfit (q : ℝ) : ℝ :=
  (1 - q) / 4 + q ^ 2 / (32 * k)

theorem readiness_square_identity (q r : ℝ) :
    primitiveProfit q (privateReadiness q) - primitiveProfit q r =
      (k / 2) * (r - privateReadiness q) ^ 2 := by
  norm_num [primitiveProfit, privateReadiness, k] <;> ring

theorem readiness_global_best_response (q r : ℝ) :
    primitiveProfit q r ≤ primitiveProfit q (privateReadiness q) := by
  have h := readiness_square_identity q r
  have hn : (0 : ℝ) ≤ (k / 2) * (r - privateReadiness q) ^ 2 :=
    mul_nonneg (by norm_num [k]) (sq_nonneg _)
  linarith

theorem readiness_unique_best_response (q r : ℝ)
    (h : primitiveProfit q r = primitiveProfit q (privateReadiness q)) :
    r = privateReadiness q := by
  have hs := readiness_square_identity q r
  have hk : (0 : ℝ) < k / 2 := by norm_num [k]
  have hz : (r - privateReadiness q) ^ 2 = 0 := by
    have hm := mul_pos_of_pos_of_pos hk
    nlinarith [sq_nonneg (r - privateReadiness q)]
  nlinarith [sq_nonneg (r - privateReadiness q)]

theorem readiness_policy_bounds (x : ℝ)
    (hx0 : 0 ≤ x) (hxbar : x ≤ 2 / 25) :
    (11 / 16 : ℝ) ≤ privateReadiness (q0 - x) ∧
      privateReadiness (q0 - x) ≤ 15 / 16 := by
  have heq : privateReadiness (q0 - x) =
      (15 / 16 : ℝ) - 25 * x / 8 := by
    norm_num [privateReadiness, q0, k] <;> ring
  rw [heq]
  constructor <;> linarith

theorem continuation_profit_formula (q : ℝ) :
    primitiveProfit q (privateReadiness q) = continuationProfit q := by
  norm_num [primitiveProfit, privateReadiness, continuationProfit, k] <;> ring

noncomputable def primitiveMaterialSurplus (q r : ℝ) : ℝ :=
  (3 / 8) * (1 - q * (1 - r)) - k * r ^ 2 / 2

theorem continuation_surplus_formula (q : ℝ) :
    primitiveMaterialSurplus q (privateReadiness q) = t q := by
  norm_num [primitiveMaterialSurplus, privateReadiness, t, k] <;> ring

-- At gamma=0 the deterministic A-minus-B location advantage is
-- independent of the rival's location, and the interior uniform-fit cutoff
-- is (H + f(q_A) - f(q_B)) / (2H).
noncomputable def primitiveLocationCutoff (x y : ℝ) : ℝ :=
  1 / 2 +
    (continuationProfit (q0 - x) - continuationProfit (q0 - y)) / (2 * H)

theorem primitive_location_equals_reduced (x y : ℝ) :
    primitiveLocationCutoff x y = locationProb x y := by
  norm_num [primitiveLocationCutoff, continuationProfit, locationProb,
    qbar, h, q0, k, H] <;> ring

theorem primitive_location_bounds (x y : ℝ)
    (hx0 : 0 ≤ x) (hxbar : x ≤ 2 / 25)
    (hy0 : 0 ≤ y) (hybar : y ≤ 2 / 25) :
    (5 / 16 : ℝ) ≤ primitiveLocationCutoff x y ∧
      primitiveLocationCutoff x y ≤ 11 / 16 := by
  have hxprod : (0 : ℝ) ≤ x * (2 / 25 - x) :=
    mul_nonneg hx0 (sub_nonneg.mpr hxbar)
  have hyprod : (0 : ℝ) ≤ y * (2 / 25 - y) :=
    mul_nonneg hy0 (sub_nonneg.mpr hybar)
  have hx2 : x ^ 2 ≤ (4 / 625 : ℝ) := by nlinarith
  have hy2 : y ^ 2 ≤ (4 / 625 : ℝ) := by nlinarith
  have heq : primitiveLocationCutoff x y =
      (1 / 2 : ℝ) + 25 / 32 * (x - y) +
      625 / 32 * (x ^ 2 - y ^ 2) := by
    norm_num [primitiveLocationCutoff, continuationProfit, q0, k, H] <;> ring
  rw [heq]
  constructor <;> nlinarith [sq_nonneg x, sq_nonneg y]

noncomputable def primitiveNationalSurplus (x y : ℝ) : ℝ :=
  2 * (primitiveLocationCutoff x y *
        primitiveMaterialSurplus (q0 - x) (privateReadiness (q0 - x)) +
      (1 - primitiveLocationCutoff x y) *
        primitiveMaterialSurplus (q0 - y) (privateReadiness (q0 - y)))

theorem primitive_surplus_equals_reduced (x y : ℝ) :
    primitiveNationalSurplus x y = fullSurplus x y := by
  norm_num [primitiveNationalSurplus, primitiveLocationCutoff,
    primitiveMaterialSurplus, privateReadiness, continuationProfit,
    fullSurplus, t, U, qbar, q0, k, H] <;> ring

theorem primitive_planner_equals_reduced (μ x y : ℝ) :
    primitiveNationalSurplus x y + 2 * b - c * (x ^ 2 + y ^ 2) / 2 +
      μ * (x + y) = fullPlannerPayoff μ x y := by
  rw [primitive_surplus_equals_reduced]
  rfl

theorem primitive_local_equals_reduced (μ x y : ℝ) :
    primitiveNationalSurplus x y / 2 + 2 * b * primitiveLocationCutoff x y -
      c * x ^ 2 / 2 + μ * x = fullLocalPayoff μ x y := by
  rw [primitive_surplus_equals_reduced, primitive_location_equals_reduced]
  rfl

-- The restricted games must be re-solved from their own primitives:
-- fixed readiness is r*=15/16, whereas fixed location is p=1/2.
noncomputable def fixedReadiness : ℝ := 15 / 16
noncomputable def fixedReadinessLocation (x y : ℝ) : ℝ :=
  1 / 2 +
    (primitiveProfit (q0 - x) fixedReadiness -
      primitiveProfit (q0 - y) fixedReadiness) / (2 * H)
noncomputable def fixedReadinessSurplus (x y : ℝ) : ℝ :=
  2 * (fixedReadinessLocation x y *
        primitiveMaterialSurplus (q0 - x) fixedReadiness +
    (1 - fixedReadinessLocation x y) *
        primitiveMaterialSurplus (q0 - y) fixedReadiness)
noncomputable def primitiveReadyPlanner (μ x y : ℝ) : ℝ :=
  fixedReadinessSurplus x y + 2 * b -
    c * (x ^ 2 + y ^ 2) / 2 + μ * (x + y)
noncomputable def primitiveReadyLocal (μ x y : ℝ) : ℝ :=
  fixedReadinessSurplus x y / 2 + 2 * b * fixedReadinessLocation x y -
    c * x ^ 2 / 2 + μ * x

theorem primitive_fixed_readiness_planner (μ x y : ℝ) :
    primitiveReadyPlanner μ x y =
      readyPlannerPayoff μ x y + (1241 / 1600 : ℝ) := by
  norm_num [primitiveReadyPlanner, fixedReadinessSurplus,
    fixedReadinessLocation, primitiveMaterialSurplus, primitiveProfit,
    fixedReadiness, readyPlannerPayoff, q0, k, H, b, c] <;> ring

theorem primitive_fixed_readiness_local (μ x y : ℝ) :
    primitiveReadyLocal μ x y =
      readyLocalPayoff μ x y + (1241 / 3200 : ℝ) := by
  norm_num [primitiveReadyLocal, fixedReadinessSurplus,
    fixedReadinessLocation, primitiveMaterialSurplus, primitiveProfit,
    fixedReadiness, readyLocalPayoff, q0, k, H, b, c] <;> ring

noncomputable def primitiveFixedLocationSurplus (x y : ℝ) : ℝ :=
  (primitiveMaterialSurplus (q0 - x) (privateReadiness (q0 - x)) +
    primitiveMaterialSurplus (q0 - y) (privateReadiness (q0 - y)))
noncomputable def primitiveLocPlanner (μ x y : ℝ) : ℝ :=
  primitiveFixedLocationSurplus x y + 2 * b -
    c * (x ^ 2 + y ^ 2) / 2 + μ * (x + y)
noncomputable def primitiveLocLocal (μ x y : ℝ) : ℝ :=
  primitiveFixedLocationSurplus x y / 2 + b - c * x ^ 2 / 2 + μ * x

theorem primitive_fixed_location_planner (μ x y : ℝ) :
    primitiveLocPlanner μ x y =
      locPlannerPayoff μ x y + (1241 / 1600 : ℝ) := by
  norm_num [primitiveLocPlanner, primitiveFixedLocationSurplus,
    primitiveMaterialSurplus, privateReadiness,
    locPlannerPayoff, q0, k, b, c] <;> ring

theorem primitive_fixed_location_local (μ x y : ℝ) :
    primitiveLocLocal μ x y =
      locLocalPayoff μ x + 25 / 64 * y ^ 2 - 3 / 64 * y +
        (1241 / 3200 : ℝ) := by
  norm_num [primitiveLocLocal, primitiveFixedLocationSurplus,
    primitiveMaterialSurplus, privateReadiness,
    locLocalPayoff, q0, k, b, c] <;> ring

end JPET.ResponseInteraction

-- Explicit kernel-dependency audit for the new (real-valued) JPET certificates.
#print axioms JPET.ResponseInteraction.response_interaction_signs
#print axioms JPET.ResponseInteraction.full_planner_global
#print axioms JPET.ResponseInteraction.full_local_global
#print axioms JPET.ResponseInteraction.ready_planner_global
#print axioms JPET.ResponseInteraction.ready_local_global
#print axioms JPET.ResponseInteraction.loc_planner_global
#print axioms JPET.ResponseInteraction.loc_local_global
