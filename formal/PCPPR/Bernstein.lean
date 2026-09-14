import Mathlib

open scoped unitInterval

namespace PCPPR.Bernstein

/-- A finite nonnegative partition of unity has at least one strictly positive weight. -/
theorem exists_positive_weight
    {ι : Type*} [Fintype ι] [Nonempty ι]
    (w : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i)
    (hsum : ∑ i, w i = 1) :
    ∃ i, 0 < w i := by
  by_contra h
  simp only [not_exists, not_lt] at h
  have hz : ∀ i, w i = 0 := by
    intro i
    exact le_antisymm (h i) (hw i)
  have hzero : (∑ i, w i) = 0 := by
    simp [hz]
  linarith

/-- T10: generic finite convex-combination certificate logic. If basis weights
are nonnegative and sum to one, and every coefficient is strictly negative,
the weighted value is strictly negative. -/
theorem weighted_sum_negative
    {ι : Type*} [Fintype ι] [Nonempty ι]
    (w β : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i)
    (hsum : ∑ i, w i = 1)
    (hβ : ∀ i, β i < 0) :
    (∑ i, w i * β i) < 0 := by
  obtain ⟨i, hi⟩ := exists_positive_weight w hw hsum
  refine Finset.sum_neg' (fun j _ => ?_) ?_
  · exact mul_nonpos_of_nonneg_of_nonpos (hw j) (le_of_lt (hβ j))
  · exact ⟨i, Finset.mem_univ i, mul_neg_of_pos_of_neg hi (hβ i)⟩

/-- Positive-coefficient counterpart of `weighted_sum_negative`. -/
theorem weighted_sum_positive
    {ι : Type*} [Fintype ι] [Nonempty ι]
    (w β : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i)
    (hsum : ∑ i, w i = 1)
    (hβ : ∀ i, 0 < β i) :
    0 < (∑ i, w i * β i) := by
  obtain ⟨i, hi⟩ := exists_positive_weight w hw hsum
  refine Finset.sum_pos' (fun j _ => ?_) ?_
  · exact mul_nonneg (hw j) (le_of_lt (hβ j))
  · exact ⟨i, Finset.mem_univ i, mul_pos hi (hβ i)⟩

/-- Tensor-product specialization used by bivariate certificates. The proof is
performed as two successive finite convex combinations, avoiding any dependence
on a particular product-Fintype enumeration identity. -/
theorem tensor_weighted_sum_negative
    {ι κ : Type*} [Fintype ι] [Fintype κ] [Nonempty ι] [Nonempty κ]
    (wx : ι → ℝ) (wy : κ → ℝ) (β : ι → κ → ℝ)
    (hx : ∀ i, 0 ≤ wx i) (hy : ∀ j, 0 ≤ wy j)
    (hsx : ∑ i, wx i = 1) (hsy : ∑ j, wy j = 1)
    (hβ : ∀ i j, β i j < 0) :
    (∑ i, ∑ j, (wx i * wy j) * β i j) < 0 := by
  have hinner : ∀ i : ι, (∑ j : κ, wy j * β i j) < 0 := by
    intro i
    exact weighted_sum_negative wy (β i) hy hsy (hβ i)
  have houter :
      (∑ i : ι, wx i * (∑ j : κ, wy j * β i j)) < 0 := by
    exact weighted_sum_negative wx
      (fun i : ι => ∑ j : κ, wy j * β i j) hx hsx hinner
  simpa [Finset.mul_sum, mul_assoc] using houter

/-- T10: specialization to mathlib's actual univariate Bernstein basis on the
unit interval. Nonnegativity and partition of unity are discharged by
`bernstein_nonneg` and `bernstein.probability`, not left as caller hypotheses. -/
theorem bernstein_sum_negative
    (n : ℕ) (x : I) (β : Fin (n + 1) → ℝ)
    (hβ : ∀ k, β k < 0) :
    (∑ k : Fin (n + 1), bernstein n k x * β k) < 0 := by
  exact weighted_sum_negative
    (fun k : Fin (n + 1) => bernstein n k x) β
    (fun _ => bernstein_nonneg)
    (bernstein.probability n x) hβ

/-- T10: actual tensor-product Bernstein basis used by the bivariate global
certificates. The only remaining hypothesis is strict negativity of the
coefficient array. -/
theorem tensor_bernstein_sum_negative
    (nx ny : ℕ) (x y : I)
    (β : Fin (nx + 1) → Fin (ny + 1) → ℝ)
    (hβ : ∀ i j, β i j < 0) :
    (∑ i : Fin (nx + 1), ∑ j : Fin (ny + 1),
      (bernstein nx i x * bernstein ny j y) * β i j) < 0 := by
  exact tensor_weighted_sum_negative
    (fun i : Fin (nx + 1) => bernstein nx i x)
    (fun j : Fin (ny + 1) => bernstein ny j y)
    β
    (fun _ => bernstein_nonneg)
    (fun _ => bernstein_nonneg)
    (bernstein.probability nx x)
    (bernstein.probability ny y)
    hβ

end PCPPR.Bernstein
