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


def failureCovariance (q rho : ℝ) : ℝ :=
  bothFail q rho-q*q

theorem failure_covariance_identity (q rho : ℝ) :
    failureCovariance q rho = q*(1-q)*rho := by
  unfold failureCovariance bothFail
  ring

theorem failure_correlation_exact (q rho : ℝ)
    (hq0 : 0 < q) (hq1 : q < 1) :
    failureCovariance q rho/(q*(1-q)) = rho := by
  have hden : q*(1-q) ≠ 0 :=
    ne_of_gt (mul_pos hq0 (by linarith))
  rw [failure_covariance_identity]
  field_simp [hden]

def individualExpectedContractGain
    (q rho s revenue V F : ℝ) : ℝ :=
  (deliveryLeftProbability q rho s - (1-q))*(revenue+V)-F

theorem per_firm_contract_gain_from_state_weights
    (q rho s revenue V F : ℝ) :
    individualExpectedContractGain q rho s revenue V F =
      q*(1-q)*(1-rho)*s*(revenue+V)-F := by
  unfold individualExpectedContractGain
  rw [deliveryLeft_formula]
  ring

theorem total_contract_surplus_from_state_weights
    (q rho s revenueA revenueB V F : ℝ) :
    individualExpectedContractGain q rho s revenueA V F +
      individualExpectedContractGain q rho s revenueB V F =
      q*(1-q)*(1-rho)*s*(revenueA+revenueB+2*V)-2*F := by
  rw [per_firm_contract_gain_from_state_weights,
    per_firm_contract_gain_from_state_weights]
  ring

theorem total_contract_surplus_for_linear_geography
    (q d revenueA revenueB V F : ℝ) :
    individualExpectedContractGain q (1-d) (1-d) revenueA V F +
      individualExpectedContractGain q (1-d) (1-d) revenueB V F =
      jointSurplus q 0 V F d revenueA revenueB := by
  rw [total_contract_surplus_from_state_weights]
  unfold jointSurplus rescue intensity
  ring

end RescueHotellingDelivery
#print axioms RescueHotellingDelivery.totalProbability_eq_one
#print axioms RescueHotellingDelivery.linear_geography_delivered_probability
