import PCPPR.GlobalPlanner
import PCPPR.GlobalLocalGovernment

open Set

namespace PCPPR.TheoremCore

/-- T14: statement-faithful implication layer for the canonical-witness part of
Theorem 1.  The assumptions are certificate-level local facts (full-domain
planner derivative signs and full-own-domain local concavity), not the desired
global conclusions themselves.

The open-neighborhood persistence claim is intentionally absent from this theorem. -/
theorem canonical_witness_core
    {W GA GB : ℝ → ℝ → ℝ}
    {abar alpha L U : ℝ}
    (habar : 0 < abar)
    (halpha : alpha ∈ Ioo (0 : ℝ) abar)
    (hinterval : alpha ∈ Ioo L U)
    (hWcontA : ∀ y ∈ Icc (0 : ℝ) abar,
      ContinuousOn (fun x => W x y) (Icc (0 : ℝ) abar))
    (hWcontB : ∀ x ∈ Icc (0 : ℝ) abar,
      ContinuousOn (fun y => W x y) (Icc (0 : ℝ) abar))
    (hWderivA : ∀ y ∈ Icc (0 : ℝ) abar,
      ∀ x ∈ interior (Icc (0 : ℝ) abar), deriv (fun t => W t y) x < 0)
    (hWderivB : ∀ x ∈ Icc (0 : ℝ) abar,
      ∀ y ∈ interior (Icc (0 : ℝ) abar), deriv (fun t => W x t) y < 0)
    (hGAcont : ContinuousOn (fun x => GA x alpha) (Icc (0 : ℝ) abar))
    (hGAsecond : ∀ x ∈ interior (Icc (0 : ℝ) abar),
      (deriv^[2] (fun t => GA t alpha)) x < 0)
    (hGAstationary : HasDerivAt (fun x => GA x alpha) 0 alpha)
    (hsym : ∀ x y, GB x y = GA y x) :
    (∀ a ∈ Icc (0 : ℝ) abar, ∀ b ∈ Icc (0 : ℝ) abar,
      W 0 0 ≤ W a b → a = 0 ∧ b = 0) ∧
    alpha ∈ Ioo L U ∧
    0 < alpha ∧
    (∀ x ∈ Icc (0 : ℝ) abar, GA x alpha ≤ GA alpha alpha) ∧
    (∀ y ∈ Icc (0 : ℝ) abar, GB alpha y ≤ GB alpha alpha) := by
  have hAanti : ∀ y ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun x => W x y) (Icc (0 : ℝ) abar) := by
    intro y hy
    exact GlobalPlanner.strictAntiOn_Icc_of_deriv_neg (hWcontA y hy) (hWderivA y hy)
  have hBanti : ∀ x ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun y => W x y) (Icc (0 : ℝ) abar) := by
    intro x hx
    exact GlobalPlanner.strictAntiOn_Icc_of_deriv_neg (hWcontB x hx) (hWderivB x hx)
  have hplanner : ∀ a ∈ Icc (0 : ℝ) abar, ∀ b ∈ Icc (0 : ℝ) abar,
      W 0 0 ≤ W a b → a = 0 ∧ b = 0 := by
    intro a ha b hb hmax
    exact GlobalPlanner.origin_unique_global_maximizer habar hAanti hBanti ha hb hmax
  have hlocalStrict :=
    GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
      habar halpha hGAcont hGAsecond hGAstationary
  have halphaS : alpha ∈ Icc (0 : ℝ) abar := ⟨le_of_lt halpha.1, le_of_lt halpha.2⟩
  have hA : ∀ x ∈ Icc (0 : ℝ) abar, GA x alpha ≤ GA alpha alpha := by
    intro x hx
    by_cases heq : x = alpha
    · simp [heq]
    · exact le_of_lt (hlocalStrict x hx heq)
  have hB : ∀ y ∈ Icc (0 : ℝ) abar, GB alpha y ≤ GB alpha alpha := by
    intro y hy
    rw [hsym alpha y, hsym alpha alpha]
    exact hA y hy
  exact ⟨hplanner, hinterval, halpha.1, hA, hB⟩

end PCPPR.TheoremCore
