import PCPPR.CanonicalWitness
import Mathlib.Analysis.Convex.Deriv

open Set

namespace PCPPR.GlobalLocalGovernment

/-- A stationary interior point of a strictly concave objective is its unique
global maximizer on the whole policy interval. -/
theorem strictConcave_stationary_unique_global_max
    {G : ℝ → ℝ} {abar α : ℝ}
    (habar : 0 < abar)
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hconc : StrictConcaveOn ℝ (Icc (0 : ℝ) abar) G)
    (hstat : HasDerivAt G 0 α) :
    ∀ x ∈ Icc (0 : ℝ) abar, x ≠ α → G x < G α := by
  let S : Set ℝ := Icc (0 : ℝ) abar
  have hαS : α ∈ S := ⟨le_of_lt hα.1, le_of_lt hα.2⟩
  have hαint : α ∈ interior S := by
    simpa [S, interior_Icc, habar.ne'] using hα
  have hnegStrict : StrictConvexOn ℝ S (fun x => -G x) := by
    simpa [S] using hconc.neg
  have hnegStat : HasDerivAt (fun x => -G x) 0 α := by
    simpa using hstat.neg
  have hright : derivWithin (fun x => -G x) (Ioi α) α = 0 := by
    exact hnegStat.hasDerivWithinAt.derivWithin (uniqueDiffWithinAt_Ioi α)
  have hmin : IsMinOn (fun x => -G x) S α :=
    hnegStrict.convexOn.isMinOn_of_rightDeriv_eq_zero hαint hright
  have hmax : IsMaxOn G S α := by
    intro x hx
    have h := hmin hx
    linarith
  intro x hx hne
  have hle : G x ≤ G α := hmax hx
  have hneq : G x ≠ G α := by
    intro heq
    have hmaxx : IsMaxOn G S x := by
      intro y hy
      have hymax := hmax hy
      linarith
    have hxeq : x = α := hconc.eq_of_isMaxOn hmaxx hmax hx hαS
    exact hne hxeq
  exact lt_of_le_of_ne hle hneq

/-- T13: the paper's certificate premise G''<0 on the full feasible interval,
together with an interior stationary point, implies a unique global best
response.  This theorem separates the generic implication from the exact
certificate supplying the second-derivative sign. -/
theorem second_deriv_negative_stationary_unique_global_max
    {G : ℝ → ℝ} {abar α : ℝ}
    (habar : 0 < abar)
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hcont : ContinuousOn G (Icc (0 : ℝ) abar))
    (hsecond : ∀ x ∈ interior (Icc (0 : ℝ) abar), (deriv^[2] G) x < 0)
    (hstat : HasDerivAt G 0 α) :
    ∀ x ∈ Icc (0 : ℝ) abar, x ≠ α → G x < G α := by
  have hconc : StrictConcaveOn ℝ (Icc (0 : ℝ) abar) G :=
    strictConcaveOn_of_deriv2_neg' (convex_Icc (0 : ℝ) abar) hcont hsecond
  exact strictConcave_stationary_unique_global_max habar hα hconc hstat

/-- Symmetric best-response implication: if the same strictly positive alpha
is the unique global best response of each jurisdiction to alpha, then the
symmetric profile is a positive Nash equilibrium.  No uniqueness claim for
the entire policy-game equilibrium correspondence is made. -/
theorem symmetric_positive_nash_of_unique_best_responses
    {GA GB : ℝ → ℝ → ℝ} {abar α : ℝ}
    (hα : α ∈ Ioo (0 : ℝ) abar)
    (hA : ∀ x ∈ Icc (0 : ℝ) abar, GA x α ≤ GA α α)
    (hB : ∀ y ∈ Icc (0 : ℝ) abar, GB α y ≤ GB α α) :
    0 < α ∧
      (∀ x ∈ Icc (0 : ℝ) abar, GA x α ≤ GA α α) ∧
      (∀ y ∈ Icc (0 : ℝ) abar, GB α y ≤ GB α α) := by
  exact ⟨hα.1, hA, hB⟩

end PCPPR.GlobalLocalGovernment
