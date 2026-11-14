import Mathlib
import RescueHotellingCore

/-!
The no-contract constrained welfare optimum from Proposition 6:
A global, unique maximizer proof for the actual welfareNoContract
polynomial (not merely a first-order identity).
-/
noncomputable section
namespace RescueHotellingWelfareGlobal
open RescueHotelling

def welfareNoContractSlope (q t c d : ℝ) : ℝ :=
  survival q*t*(1-2*d)/4-c*d/2

theorem welfareNoContractDifference
    (q t c v Lambda d s : ℝ) :
    welfareNoContract q t c v Lambda d -
      welfareNoContract q t c v Lambda s =
    (d-s)*welfareNoContractSlope q t c s -
      (survival q*t+c)*(d-s)^2/4 := by
  unfold welfareNoContract welfareNoContractSlope mismatch survival
  ring

theorem no_contract_planner_stationary (q t c : ℝ)
    (hc : 0 < c) (hrt : 0 < survival q*t) :
    welfareNoContractSlope q t c (noContractSocialDistance q t c) = 0 := by
  have hden : c+survival q*t ≠ 0 := ne_of_gt (by linarith)
  unfold welfareNoContractSlope noContractSocialDistance
  field_simp [hden]
  ring

theorem no_contract_planner_global_unique (q t c v Lambda d : ℝ)
    (hc : 0 < c) (hrt : 0 < survival q*t) :
    welfareNoContract q t c v Lambda d ≤
      welfareNoContract q t c v Lambda (noContractSocialDistance q t c) ∧
      (welfareNoContract q t c v Lambda d =
         welfareNoContract q t c v Lambda (noContractSocialDistance q t c) →
       d = noContractSocialDistance q t c) := by
  let target := noContractSocialDistance q t c
  have hstation : welfareNoContractSlope q t c target = 0 :=
    no_contract_planner_stationary q t c hc hrt
  have hgap := welfareNoContractDifference q t c v Lambda d target
  rw [hstation] at hgap
  have hC : 0 < survival q*t+c := by linarith
  have hs : 0 ≤ (d-target)^2 := sq_nonneg _
  have hproduct : 0 ≤ (survival q*t+c)*(d-target)^2 :=
    mul_nonneg (le_of_lt hC) hs
  constructor
  · nlinarith
  · intro heq
    have hzero : (survival q*t+c)*(d-target)^2 = 0 := by
      linarith
    rcases mul_eq_zero.mp hzero with hcoeff | hsq
    · linarith
    · have hx : d-target = 0 := (sq_eq_zero_iff).mp hsq
      dsimp [target] at *
      linarith

theorem no_contract_planner_distance_interior (q t c : ℝ)
    (hc : 0 < c) (hrt : 0 < survival q*t) :
    0 < noContractSocialDistance q t c ∧
      noContractSocialDistance q t c < 1/2 := by
  have hden : 0 < 2*(c+survival q*t) := by linarith
  unfold noContractSocialDistance
  constructor
  · exact div_pos hrt hden
  · apply (div_lt_iff₀ hden).2
    linarith

end RescueHotellingWelfareGlobal
#print axioms RescueHotellingWelfareGlobal.no_contract_planner_global_unique
