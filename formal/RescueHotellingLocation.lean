import Mathlib
import RescueHotellingCore
import RescueHotellingModelCheck

/-!
Exact polynomial identities and strict global same-side bounds for
contract and non-contract continuations. Unlike a purely conditional
quadratic-envelope lemma, these statements use the actual location
payoff functions of the paper.
-/
noncomputable section
namespace RescueHotellingLocation
open RescueHotelling RescueHotellingModelCheck

def revenueL (t b s : ℝ) : ℝ := 2*t*s*(1+b-s/2)^2/9
def revenueR (t b s : ℝ) : ℝ := 2*t*s*(2-b+s/2)^2/9
def symmetricRivalPosition (d : ℝ) : ℝ := (1+d)/2

def agreementPayoff (r A t c V F b s : ℝ) : ℝ :=
  r*revenueL t b s-c*(b-s-1/2)^2/2
  +A*s*(1-s)*((revenueL t b s+revenueR t b s)/2+V)-F
def disagreementPayoff (r t c b s : ℝ) : ℝ :=
  r*revenueL t b s-c*(b-s-1/2)^2/2

def G0 (r t c d : ℝ) : ℝ := c*d/2-r*t*(1/2-d/3)
def G (r A t c V d : ℝ) : ℝ :=
  G0 r t c d-A*(1-2*d)*(t*d/2+V)-A*t*d*(1-d)/2

def contractRemainder (r A t c V d s : ℝ) : ℝ :=
  -A*V-A*d*t+A*t*(1-s)*(s*s+9)/18-c/2+r*t*(s-6)/18
def noContractRemainder (r t c s : ℝ) : ℝ :=
  -c/2+r*t*(s-6)/18

theorem agreement_payoff_gap_exact (r A t c V F d s : ℝ) :
    agreementPayoff r A t c V F (symmetricRivalPosition d) s -
    agreementPayoff r A t c V F (symmetricRivalPosition d) d +
    (s-d)*G r A t c V d =
    (s-d)^2*contractRemainder r A t c V d s := by
  unfold agreementPayoff symmetricRivalPosition revenueL revenueR
    G G0 contractRemainder
  ring

theorem disagreement_payoff_gap_exact (r t c d s : ℝ) :
    disagreementPayoff r t c (symmetricRivalPosition d) s -
    disagreementPayoff r t c (symmetricRivalPosition d) d +
    (s-d)*G0 r t c d =
    (s-d)^2*noContractRemainder r t c s := by
  unfold disagreementPayoff symmetricRivalPosition revenueL
    G0 noContractRemainder
  ring

theorem contractRemainder_negative
    (r A t c V d s : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t) (hV : 0 ≤ V)
    (hd : 0 ≤ d) (hs0 : 0 ≤ s) (hs1 : s ≤ 1)
    (hc : A*t < c) : contractRemainder r A t c V d s < 0 := by
  have hS1 : 0 ≤ 1-s := by linarith
  have hSproduct : s*(1-s) ≤ 1 := calc
    s*(1-s) ≤ s*1 := mul_le_mul_of_nonneg_left (by linarith : 1-s ≤ 1) hs0
    _ = s := by ring
    _ ≤ 1 := hs1
  have h9 : 0 ≤ s*(9-s*(1-s)) :=
    mul_nonneg hs0 (by linarith)
  have hPoly : (1-s)*(s*s+9) ≤ 9 := by nlinarith [h9]
  have hAt : 0 ≤ A*t := mul_nonneg hA ht
  have hTerm : A*t*((1-s)*(s*s+9)) ≤ A*t*9 :=
    mul_le_mul_of_nonneg_left hPoly hAt
  have hAV : 0 ≤ A*V := mul_nonneg hA hV
  have hAdt : 0 ≤ A*d*t := mul_nonneg (mul_nonneg hA hd) ht
  have hrtNeg : r*t*(s-6) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hr ht) (by linarith)
  unfold contractRemainder
  nlinarith

theorem agreement_same_side_global_optimum
    (r A t c V F d s : ℝ)
    (hr : 0 ≤ r) (hA : 0 ≤ A) (ht : 0 ≤ t) (hV : 0 ≤ V)
    (hd : 0 ≤ d) (hs0 : 0 ≤ s) (hs1 : s ≤ 1)
    (hc : A*t < c) (hFOC : G r A t c V d = 0) :
    agreementPayoff r A t c V F (symmetricRivalPosition d) s ≤
    agreementPayoff r A t c V F (symmetricRivalPosition d) d := by
  have hGap := agreement_payoff_gap_exact r A t c V F d s
  rw [hFOC] at hGap
  have hSq : 0 ≤ (s-d)^2 := sq_nonneg _
  have hK : contractRemainder r A t c V d s < 0 :=
    contractRemainder_negative r A t c V d s hr hA ht hV hd hs0 hs1 hc
  have hProd : (s-d)^2*contractRemainder r A t c V d s ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hSq (le_of_lt hK)
  nlinarith

theorem noContractRemainder_negative (r t c s : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hc : 0 < c) (hs : s ≤ 1) :
    noContractRemainder r t c s < 0 := by
  have hterm : r*t*(s-6) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hr ht) (by linarith)
  unfold noContractRemainder
  linarith

theorem no_contract_same_side_global_optimum
    (r t c d s : ℝ)
    (hr : 0 ≤ r) (ht : 0 ≤ t) (hc : 0 < c)
    (hs : s ≤ 1) (hFOC : G0 r t c d = 0) :
    disagreementPayoff r t c (symmetricRivalPosition d) s ≤
    disagreementPayoff r t c (symmetricRivalPosition d) d := by
  have hgap := disagreement_payoff_gap_exact r t c d s
  rw [hFOC] at hgap
  have hK := noContractRemainder_negative r t c s hr ht hc hs
  have hSq : 0 ≤ (s-d)^2 := sq_nonneg _
  have hprod : (s-d)^2 * noContractRemainder r t c s ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hSq (le_of_lt hK)
  nlinarith

theorem agreement_symmetric_payoff (r A t c V F d : ℝ) :
    agreementPayoff r A t c V F (symmetricRivalPosition d) d =
      r*t*d/2-c*d*d/8+
      A*d*(1-d)*(t*d/2+V)-F := by
  unfold agreementPayoff symmetricRivalPosition revenueL revenueR
  ring

theorem disagreement_symmetric_payoff (r t c d : ℝ) :
    disagreementPayoff r t c (symmetricRivalPosition d) d =
      r*t*d/2-c*d*d/8 := by
  unfold disagreementPayoff symmetricRivalPosition revenueL
  ring

end RescueHotellingLocation

#print axioms RescueHotellingLocation.agreement_same_side_global_optimum
#print axioms RescueHotellingLocation.no_contract_same_side_global_optimum
