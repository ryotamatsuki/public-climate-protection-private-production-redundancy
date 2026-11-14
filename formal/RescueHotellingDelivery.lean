import Mathlib
import RescueHotellingCore
import RescueHotellingExtendedGame

/-!
A six-element *outcome enumeration* of the paper's two-factory failure
and conditional rescue technology. All probability weights are explicit.
This verifies the reduced-form stochastic kernel without assuming
independent plant failures. It is not yet a complete extensive game.
-/
noncomputable section
namespace RescueHotellingDelivery
open RescueHotelling RescueHotellingExtendedGame

inductive Outcome
  | neither | leftRescued | leftUnrescued
  | rightRescued | rightUnrescued | both
  deriving DecidableEq

def probability (q rho s : ℝ) : Outcome → ℝ
  | .neither => neitherFail q rho
  | .leftRescued => onlyLeftFail q rho*s
  | .leftUnrescued => onlyLeftFail q rho*(1-s)
  | .rightRescued => onlyRightFail q rho*s
  | .rightUnrescued => onlyRightFail q rho*(1-s)
  | .both => bothFail q rho

def totalProbability (q rho s : ℝ) : ℝ :=
  probability q rho s .neither
  + probability q rho s .leftRescued
  + probability q rho s .leftUnrescued
  + probability q rho s .rightRescued
  + probability q rho s .rightUnrescued
  + probability q rho s .both

theorem totalProbability_eq_one (q rho s : ℝ) :
    totalProbability q rho s = 1 := by
  unfold totalProbability probability onlyLeftFail onlyRightFail
    neitherFail bothFail
  ring

theorem probabilities_nonnegative (q rho s : ℝ)
    (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hrho0 : 0 ≤ rho) (hrho1 : rho ≤ 1)
    (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    0 ≤ probability q rho s .neither ∧
    0 ≤ probability q rho s .leftRescued ∧
    0 ≤ probability q rho s .leftUnrescued ∧
    0 ≤ probability q rho s .rightRescued ∧
    0 ≤ probability q rho s .rightUnrescued ∧
    0 ≤ probability q rho s .both := by
  have hfail := joint_failures_nonnegative q rho hq0 hq1 hrho0 hrho1
  obtain ⟨hNeither,hLeft,hRight,hBoth⟩ := hfail
  have hsrest : 0 ≤ 1-s := by linarith
  unfold probability
  exact ⟨hNeither,mul_nonneg hLeft hs0,
    mul_nonneg hLeft hsrest,mul_nonneg hRight hs0,
    mul_nonneg hRight hsrest,hBoth⟩

def deliveryLeftProbability (q rho s : ℝ) : ℝ :=
  probability q rho s .neither
  + probability q rho s .leftRescued
  + probability q rho s .rightRescued
  + probability q rho s .rightUnrescued

def deliveryRightProbability (q rho s : ℝ) : ℝ :=
  probability q rho s .neither
  + probability q rho s .rightRescued
  + probability q rho s .leftRescued
  + probability q rho s .leftUnrescued

theorem both_brands_same_delivery_probability (q rho s : ℝ) :
    deliveryLeftProbability q rho s =
      deliveryRightProbability q rho s := by
  unfold deliveryLeftProbability deliveryRightProbability probability
    neitherFail onlyLeftFail onlyRightFail
  ring

theorem deliveryLeft_formula (q rho s : ℝ) :
    deliveryLeftProbability q rho s =
      (1-q)+q*(1-q)*(1-rho)*s := by
  unfold deliveryLeftProbability probability neitherFail onlyLeftFail
    onlyRightFail bothFail
  ring

theorem deliveryRight_formula (q rho s : ℝ) :
    deliveryRightProbability q rho s =
      (1-q)+q*(1-q)*(1-rho)*s := by
  unfold deliveryRightProbability probability neitherFail onlyLeftFail
    onlyRightFail bothFail
  ring

theorem linear_geography_delivered_probability (q d : ℝ) :
    deliveryLeftProbability q (1-d) (1-d) = survival q+rescue q d ∧
    deliveryRightProbability q (1-d) (1-d) = survival q+rescue q d := by
  constructor
  · rw [deliveryLeft_formula]
    unfold survival rescue intensity
    ring
  · rw [deliveryRight_formula]
    unfold survival rescue intensity
    ring

end RescueHotellingDelivery
#print axioms RescueHotellingDelivery.totalProbability_eq_one
#print axioms RescueHotellingDelivery.linear_geography_delivered_probability
