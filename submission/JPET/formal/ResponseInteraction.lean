import Mathlib

/-!
# JPET Proposition 8 — exact response-interaction certificate

This module strengthens the *bounded*, model-specific parts of Proposition 8:
* expands the gamma=0 private-continuation surplus and location probabilities
  into exact public policy payoffs, then checks the first-order coefficients;
* verifies primitive coefficients and all six interior policy levels;
* proves positive / zero / negative response-gap increments;
* proves GLOBAL planner and unilateral best-response inequalities in the
  fixed-readiness and fixed-location counterfactual games.

The full endogenous policy game's global inequalities and the identity linking
its private equilibrium to the analytically reduced surplus and probabilities
remain external mathematical/Python obligations. This file is NOT a closed
Lean proof of Proposition 8 or of positive-gamma/open-set results.
No sorry, admit, axiom, or native_decide is used.
-/

namespace JPET.ResponseInteraction

private def q0 : ℚ := 3 / 10
private def k : ℚ := 2 / 25
private def H : ℚ := 1 / 100
private def b : ℚ := 11 / 200
private def c : ℚ := 10

def mu0 : ℚ := (q0 - 3 * k) / (8 * k)
def tc : ℚ := c - 1 / (8 * k)
def s : ℚ := c - (H + b) / (16 * H * k)
def m : ℚ := (H * (3 * k - q0) + b * (4 * k - q0)) / (16 * H * k)

theorem coefficient_values :
    mu0 = 3 / 32 ∧ tc = 135 / 16 ∧ s = 315 / 64 ∧ m = 5 / 128 := by
  norm_num [mu0, tc, s, m, q0, k, H, b, c]

def qbar (x y : ℚ) : ℚ := q0 - (x + y) / 2
def t (q : ℚ) : ℚ := 3 * (1 - q) / 8 + q ^ 2 / (16 * k)
def U (q : ℚ) : ℚ := 1 / (32 * k) + (4 * k - q) * (3 * k - q) / (128 * H * k ^ 2)
def h (q : ℚ) : ℚ := (4 * k - q) / (16 * k)
def fullSurplus (x y : ℚ) : ℚ :=
  2 * t (qbar x y) + U (qbar x y) * (x - y) ^ 2
def locationProb (x y : ℚ) : ℚ :=
  1 / 2 + h (qbar x y) * (x - y) / (2 * H)
def fullPlannerPayoff (μ x y : ℚ) : ℚ :=
  fullSurplus x y + 2 * b - c * (x ^ 2 + y ^ 2) / 2 + μ * (x + y)
def fullLocalPayoff (μ x y : ℚ) : ℚ :=
  fullSurplus x y / 2 + 2 * b * locationProb x y - c * x ^ 2 / 2 + μ * x

/-! Exact deviations retain all higher-order terms. In particular, the linear
    d coefficient is the public-policy FOC, NOT a global-optimality proof. -/
theorem full_planner_deviation (μ a d : ℚ) :
    fullPlannerPayoff μ (a + d) a - fullPlannerPayoff μ a a =
      d * (μ - 3 / 32 - 135 * a / 16) +
      d ^ 2 * (5 * (12500 * a ^ 2 + 12500 * a * d - 500 * a +
                    3125 * d ^ 2 - 250 * d - 447) / 512) := by
  norm_num [fullPlannerPayoff, fullSurplus, qbar, t, U, q0, k, H, b, c]
  <;> ring

theorem full_local_deviation (μ a d : ℚ) :
    fullLocalPayoff μ (a + d) a - fullLocalPayoff μ a a =
      d * (μ + 5 / 128 - 315 * a / 64) +
      d ^ 2 * (5 * (12500 * a ^ 2 + 12500 * a * d - 500 * a +
                    3125 * d ^ 2 - 250 * d - 519) / 1024) := by
  norm_num [fullLocalPayoff, fullSurplus, locationProb, qbar, t, U, h, q0, k, H, b, c]
  <;> ring

def fullP (μ : ℚ) : ℚ := (32 * μ - 3) / 270
def fullN (μ : ℚ) : ℚ := (128 * μ + 5) / 630
def readyP (μ : ℚ) : ℚ := (μ + 3 / 128) / 10
def readyN (μ : ℚ) : ℚ := (μ + 25 / 256) / 10
def locP (μ : ℚ) : ℚ := 16 / 135 * (μ - 3 / 32)
def locN (μ : ℚ) : ℚ := 32 / 295 * (μ - 3 / 64)

theorem full_stationarity (μ : ℚ) :
    (μ - mu0 - tc * fullP μ = 0) ∧ (μ + m - s * fullN μ = 0) := by
  constructor
  · norm_num [mu0, tc, fullP, q0, k, c] <;> ring
  · norm_num [m, s, fullN, q0, k, H, b, c] <;> ring

theorem fixed_readiness_stationarity (μ : ℚ) :
    μ + 3 / 128 - 10 * readyP μ = 0 ∧
    μ + 25 / 256 - 10 * readyN μ = 0 := by
  constructor <;> norm_num [readyP, readyN] <;> ring

theorem fixed_location_stationarity (μ : ℚ) :
    μ - 3 / 32 - 135 / 16 * locP μ = 0 ∧
    μ - 3 / 64 - 295 / 32 * locN μ = 0 := by
  constructor <;> norm_num [locP, locN] <;> ring

theorem all_six_interior (μ : ℚ) (hlo : (3 : ℚ) / 32 < μ)
    (hhi : μ < (1 : ℚ) / 8) :
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

def gapFull (μ : ℚ) : ℚ := fullN μ - fullP μ
def gapReady (μ : ℚ) : ℚ := readyN μ - readyP μ
def gapLoc (μ : ℚ) : ℚ := locN μ - locP μ

theorem gap_full_increment (μ ν : ℚ) :
    gapFull ν - gapFull μ = (16 / 189 : ℚ) * (ν - μ) := by
  norm_num [gapFull, fullN, fullP] <;> ring

theorem gap_readiness_increment (μ ν : ℚ) :
    gapReady ν - gapReady μ = 0 := by
  norm_num [gapReady, readyN, readyP] <;> ring

theorem gap_location_increment (μ ν : ℚ) :
    gapLoc ν - gapLoc μ = -(16 / 1593 : ℚ) * (ν - μ) := by
  norm_num [gapLoc, locN, locP] <;> ring

theorem response_interaction_signs (μ ν : ℚ) (h : μ < ν) :
    gapFull μ < gapFull ν ∧
    gapReady μ = gapReady ν ∧
    gapLoc ν < gapLoc μ := by
  have hd : (0 : ℚ) < ν - μ := sub_pos.mpr h
  constructor
  · have heq := gap_full_increment μ ν
    have hmul : (0 : ℚ) < (16 / 189 : ℚ) * (ν - μ) :=
      mul_pos (by norm_num) hd
    linarith
  constructor
  · have hz := gap_readiness_increment μ ν
    linarith
  · have heq := gap_location_increment μ ν
    have hmul : (0 : ℚ) < (16 / 1593 : ℚ) * (ν - μ) :=
      mul_pos (by norm_num) hd
    linarith

/-! Fixed-readiness exact objectives, after dropping terms constant in policy. -/
def readyPlannerPayoff (μ x y : ℚ) : ℚ :=
    (μ + 3 / 128) * (x + y) + 75 / 2048 * (x - y) ^ 2 -
      5 * (x ^ 2 + y ^ 2)
def readyLocalPayoff (μ x y : ℚ) : ℚ :=
    μ * x + 3 / 256 * (x + y) + 75 / 4096 * (x - y) ^ 2 +
      11 / 128 * (x - y) - 5 * x ^ 2

theorem ready_planner_global (μ x y : ℚ) :
    readyPlannerPayoff μ x y ≤
      readyPlannerPayoff μ (readyP μ) (readyP μ) := by
  have hs := (fixed_readiness_stationarity μ).1
  have hmu : μ = 10 * readyP μ - 3 / 128 := by linarith
  have hidentity :
      readyPlannerPayoff μ (readyP μ) (readyP μ) -
      readyPlannerPayoff μ x y =
        (5 / 2 : ℚ) * (x + y - 2 * readyP μ) ^ 2 +
        (5045 / 2048 : ℚ) * (x - y) ^ 2 := by
    rw [hmu]
    dsimp [readyPlannerPayoff]
    ring
  have h1 : (0 : ℚ) ≤ (5 / 2 : ℚ) * (x + y - 2 * readyP μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  have h2 : (0 : ℚ) ≤ (5045 / 2048 : ℚ) * (x - y) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith

theorem ready_local_global (μ x : ℚ) :
    readyLocalPayoff μ x (readyN μ) ≤
      readyLocalPayoff μ (readyN μ) (readyN μ) := by
  have hs := (fixed_readiness_stationarity μ).2
  have hmu : μ = 10 * readyN μ - 25 / 256 := by linarith
  have hidentity :
      readyLocalPayoff μ (readyN μ) (readyN μ) -
      readyLocalPayoff μ x (readyN μ) =
        (20405 / 4096 : ℚ) * (x - readyN μ) ^ 2 := by
    rw [hmu]
    dsimp [readyLocalPayoff]
    ring
  have hnonneg : (0 : ℚ) ≤ (20405 / 4096 : ℚ) * (x - readyN μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith

/-! Fixed-location reduced objectives with backup reoptimized and p = 1/2. -/
def locPlannerPayoff (μ x y : ℚ) : ℚ :=
  (μ - 3 / 32) * (x + y) - 135 / 32 * (x ^ 2 + y ^ 2)
def locLocalPayoff (μ x : ℚ) : ℚ :=
  (μ - 3 / 64) * x - 295 / 64 * x ^ 2

theorem loc_planner_global (μ x y : ℚ) :
    locPlannerPayoff μ x y ≤ locPlannerPayoff μ (locP μ) (locP μ) := by
  have hs := (fixed_location_stationarity μ).1
  have hmu : μ = 3 / 32 + 135 / 16 * locP μ := by linarith
  have hidentity :
      locPlannerPayoff μ (locP μ) (locP μ) - locPlannerPayoff μ x y =
        (135 / 32 : ℚ) * ((x - locP μ) ^ 2 + (y - locP μ) ^ 2) := by
    rw [hmu]
    dsimp [locPlannerPayoff]
    ring
  have hnonneg : (0 : ℚ) ≤
      (135 / 32 : ℚ) * ((x - locP μ) ^ 2 + (y - locP μ) ^ 2) :=
    mul_nonneg (by norm_num) (add_nonneg (sq_nonneg _) (sq_nonneg _))
  linarith

theorem loc_local_global (μ x : ℚ) :
    locLocalPayoff μ x ≤ locLocalPayoff μ (locN μ) := by
  have hs := (fixed_location_stationarity μ).2
  have hmu : μ = 3 / 64 + 295 / 32 * locN μ := by linarith
  have hidentity :
      locLocalPayoff μ (locN μ) - locLocalPayoff μ x =
        (295 / 64 : ℚ) * (x - locN μ) ^ 2 := by
    rw [hmu]
    dsimp [locLocalPayoff]
    ring
  have hnonneg : (0 : ℚ) ≤ (295 / 64 : ℚ) * (x - locN μ) ^ 2 :=
    mul_nonneg (by norm_num) (sq_nonneg _)
  linarith

end JPET.ResponseInteraction
