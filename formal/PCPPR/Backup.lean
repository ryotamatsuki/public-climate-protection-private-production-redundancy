import PCPPR.Availability
import PCPPR.ProductMarket

namespace PCPPR.Backup

noncomputable section

open PCPPR.Availability

/-- Expected profit obtained by enumerating final availability states. -/
def expectedProfitByStates
    (πD πM si sj J k ri rj : ℝ) : ℝ :=
  p11 si sj J ri rj * πD + p10 si sj J ri rj * πM - k * ri^2 / 2

/-- Closed-form expected profit used in paper equation (7). -/
def expectedProfitClosed
    (πD Δ si sj J k ri rj : ℝ) : ℝ :=
  πD - πD * si * (1 - ri) + Δ * sj * (1 - rj)
    - Δ * J * (1 - ri) * (1 - rj) - k * ri^2 / 2

/-- T3: the state-enumerated payoff is exactly the paper's closed form.
The closed form is therefore not inserted as its own proof hypothesis. -/
theorem expectedProfit_state_eq_closed
    (πD πM Δ si sj J k ri rj : ℝ)
    (hΔ : Δ = πM - πD) :
    expectedProfitByStates πD πM si sj J k ri rj =
      expectedProfitClosed πD Δ si sj J k ri rj := by
  subst Δ
  unfold expectedProfitByStates expectedProfitClosed
  unfold p11 p10 m z
  ring

/-- The affine first derivative expression in paper equation (9). -/
def backupMarginal (πD Δ si J k ri rj : ℝ) : ℝ :=
  πD * si + Δ * J * (1 - rj) - k * ri

/-- The paper's unclipped interior best response. -/
def unclippedBR (πD Δ si J k rj : ℝ) : ℝ :=
  (πD * si + Δ * J * (1 - rj)) / k

/-- The unclipped expression solves the interior FOC whenever k is nonzero. -/
theorem unclippedBR_solves_foc
    (πD Δ si J k rj : ℝ) (hk : k ≠ 0) :
    k * unclippedBR πD Δ si J k rj =
      πD * si + Δ * J * (1 - rj) := by
  unfold unclippedBR
  field_simp [hk]

/-- Exact quadratic difference identity behind global optimality of an
interior backup FOC. -/
theorem profit_difference_at_foc
    (πD Δ si sj J k rj r rStar : ℝ)
    (hfoc : k * rStar = πD * si + Δ * J * (1 - rj)) :
    expectedProfitClosed πD Δ si sj J k r rj -
      expectedProfitClosed πD Δ si sj J k rStar rj =
        -(k / 2) * (r - rStar)^2 := by
  unfold expectedProfitClosed
  linear_combination (r - rStar) * hfoc

/-- T4: because the objective is a quadratic with curvature -k, any
interior FOC solution is the unique global maximizer on every subset that
contains it.  Feasibility/interiority itself is a separate obligation. -/
theorem strict_global_backup_optimum
    (πD Δ si sj J k rj r rStar : ℝ)
    (hk : 0 < k)
    (hfoc : k * rStar = πD * si + Δ * J * (1 - rj))
    (hne : r ≠ rStar) :
    expectedProfitClosed πD Δ si sj J k r rj <
      expectedProfitClosed πD Δ si sj J k rStar rj := by
  have hdiff := profit_difference_at_foc πD Δ si sj J k rj r rStar hfoc
  have hne' : r - rStar ≠ 0 := sub_ne_zero.mpr hne
  have hsquare : 0 < (r - rStar) * (r - rStar) := mul_self_pos.mpr hne'
  rw [pow_two] at hdiff
  nlinarith

/-- T4: uniqueness of the two-firm interior linear-system solution under
nonzero determinant k^2-h^2.  This theorem deliberately says nothing about
whether the solution lies in [0,1]. -/
theorem interior_linear_system_unique
    (k h a1 a2 r1 r2 r1' r2' : ℝ)
    (hdet : k^2 - h^2 ≠ 0)
    (h1 : k * r1 = a1 + h * (1 - r2))
    (h2 : k * r2 = a2 + h * (1 - r1))
    (h1' : k * r1' = a1 + h * (1 - r2'))
    (h2' : k * r2' = a2 + h * (1 - r1')) :
    r1 = r1' ∧ r2 = r2' := by
  have e1 : k * (r1 - r1') + h * (r2 - r2') = 0 := by
    linear_combination h1 - h1'
  have e2 : h * (r1 - r1') + k * (r2 - r2') = 0 := by
    linear_combination h2 - h2'
  have d1 : (k^2 - h^2) * (r1 - r1') = 0 := by
    linear_combination k * e1 - h * e2
  have d2 : (k^2 - h^2) * (r2 - r2') = 0 := by
    linear_combination k * e2 - h * e1
  constructor
  · have : r1 - r1' = 0 := (mul_eq_zero.mp d1).resolve_left hdet
    linarith
  · have : r2 - r2' = 0 := (mul_eq_zero.mp d2).resolve_left hdet
    linarith

/-- T5: the slope of the affine interior backup best response with respect
to rival readiness is -Delta*J/k. -/
theorem strategic_substitution_expression_neg
    {Δ J k : ℝ} (hΔ : 0 < Δ) (hJ : 0 < J) (hk : 0 < k) :
    -(Δ * J) / k < 0 := by
  exact div_neg_of_neg_of_pos (neg_lt_zero.mpr (mul_pos hΔ hJ)) hk

/-- Symmetric co-location readiness, paper equation (12). -/
def rC (q πM k Δ : ℝ) : ℝ := q * πM / (k + q * Δ)

/-- Symmetric dispersed-location readiness, paper equation (13). -/
def rD (q πD k Δ : ℝ) : ℝ := q * (πD + q * Δ) / (k + q^2 * Δ)

/-- The co-location closed form solves the symmetric backup FOC. -/
theorem rC_solves_symmetric_foc
    (q πD πM k Δ : ℝ)
    (hΔ : Δ = πM - πD)
    (hden : k + q * Δ ≠ 0) :
    k * rC q πM k Δ = πD * q + Δ * q * (1 - rC q πM k Δ) := by
  unfold rC
  field_simp [hden]
  subst Δ
  ring

/-- The dispersed-location closed form solves the symmetric backup FOC. -/
theorem rD_solves_symmetric_foc
    (q πD k Δ : ℝ)
    (hden : k + q^2 * Δ ≠ 0) :
    k * rD q πD k Δ = πD * q + Δ * q^2 * (1 - rD q πD k Δ) := by
  unfold rD
  field_simp [hden]
  ring

end

end PCPPR.Backup
