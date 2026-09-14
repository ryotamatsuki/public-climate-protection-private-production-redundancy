import PCPPR.Bernstein

open Set

namespace PCPPR.GlobalPlanner

/-- A strictly negative derivative on the interior of a closed interval implies
strict decrease on the full interval, including comparison with boundaries. -/
theorem strictAntiOn_Icc_of_deriv_neg
    {f : ℝ → ℝ} {lo hi : ℝ}
    (hf : ContinuousOn f (Icc lo hi))
    (hderiv : ∀ x ∈ interior (Icc lo hi), deriv f x < 0) :
    StrictAntiOn f (Icc lo hi) := by
  exact strictAntiOn_of_deriv_neg (convex_Icc lo hi) hf hderiv

/-- T11 implication layer: if welfare is strictly decreasing in each policy
coordinate throughout the full square, every non-origin feasible policy has
strictly lower welfare than the origin. -/
theorem origin_strictly_dominates
    {W : ℝ → ℝ → ℝ} {abar a b : ℝ}
    (habar : 0 < abar)
    (hA : ∀ y ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun x => W x y) (Icc (0 : ℝ) abar))
    (hB : ∀ x ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun y => W x y) (Icc (0 : ℝ) abar))
    (ha : a ∈ Icc (0 : ℝ) abar)
    (hb : b ∈ Icc (0 : ℝ) abar)
    (hne : (a, b) ≠ (0, 0)) :
    W a b < W 0 0 := by
  have h0 : (0 : ℝ) ∈ Icc (0 : ℝ) abar := ⟨le_rfl, le_of_lt habar⟩
  by_cases ha0 : a = 0
  · subst a
    have hb0 : b ≠ 0 := by
      intro hbzero
      apply hne
      simp [hbzero]
    have hbpos : 0 < b := lt_of_le_of_ne hb.1 (Ne.symm hb0)
    exact (hB 0 h0) h0 hb hbpos
  · have hapos : 0 < a := lt_of_le_of_ne ha.1 (Ne.symm ha0)
    have hfirst : W a b < W 0 b := (hA b hb) h0 ha hapos
    by_cases hb0 : b = 0
    · simpa [hb0] using hfirst
    · have hbpos : 0 < b := lt_of_le_of_ne hb.1 (Ne.symm hb0)
      have hsecond : W 0 b < W 0 0 := (hB 0 h0) h0 hb hbpos
      exact hfirst.trans hsecond

/-- Equivalent uniqueness formulation: the origin is the unique feasible
maximizer whenever the coordinatewise strict-decrease hypotheses hold. -/
theorem origin_unique_global_maximizer
    {W : ℝ → ℝ → ℝ} {abar a b : ℝ}
    (habar : 0 < abar)
    (hA : ∀ y ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun x => W x y) (Icc (0 : ℝ) abar))
    (hB : ∀ x ∈ Icc (0 : ℝ) abar,
      StrictAntiOn (fun y => W x y) (Icc (0 : ℝ) abar))
    (ha : a ∈ Icc (0 : ℝ) abar)
    (hb : b ∈ Icc (0 : ℝ) abar)
    (hmax : W 0 0 ≤ W a b) :
    a = 0 ∧ b = 0 := by
  by_contra hne
  have hp : (a, b) ≠ (0, 0) := by
    simpa [Prod.ext_iff] using hne
  have hlt := origin_strictly_dominates habar hA hB ha hb hp
  linarith

end PCPPR.GlobalPlanner
