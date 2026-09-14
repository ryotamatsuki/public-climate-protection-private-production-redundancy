import Mathlib

namespace PCPPR.Bernstein

/-- A finite nonnegative partition of unity has at least one strictly positive weight. -/
theorem exists_positive_weight
    {ι : Type*} [Fintype ι] [Nonempty ι]
    (w : ι → ℝ)
    (hw : ∀ i, 0 ≤ w i)
    (hsum : ∑ i, w i = 1) :
    ∃ i, 0 < w i := by
  by_contra h
  push_neg at h
  have hz : ∀ i, w i = 0 := by
    intro i
    exact le_antisymm (h i) (hw i)
  have hzero : (∑ i, w i) = 0 := by
    simp [hz]
  linarith

/-- T10: generic finite Bernstein/convex-combination certificate logic.
If basis weights are nonnegative and sum to one, and every coefficient is
strictly negative, the weighted polynomial value is strictly negative. -/
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

/-- Tensor-product specialization used by bivariate Bernstein certificates.
The theorem is basis-agnostic: callers supply nonnegativity and partition-of-
unity properties for the actual Bernstein basis values at a point. -/
theorem tensor_weighted_sum_negative
    {ι κ : Type*} [Fintype ι] [Fintype κ] [Nonempty ι] [Nonempty κ]
    (wx : ι → ℝ) (wy : κ → ℝ) (β : ι → κ → ℝ)
    (hx : ∀ i, 0 ≤ wx i) (hy : ∀ j, 0 ≤ wy j)
    (hsx : ∑ i, wx i = 1) (hsy : ∑ j, wy j = 1)
    (hβ : ∀ i j, β i j < 0) :
    (∑ i, ∑ j, (wx i * wy j) * β i j) < 0 := by
  let w : ι × κ → ℝ := fun ij => wx ij.1 * wy ij.2
  let c : ι × κ → ℝ := fun ij => β ij.1 ij.2
  have hw : ∀ ij, 0 ≤ w ij := by
    intro ij
    exact mul_nonneg (hx ij.1) (hy ij.2)
  have hsum : ∑ ij, w ij = 1 := by
    simp [w, Finset.sum_mul, Finset.mul_sum, hsx, hsy]
  have hc : ∀ ij, c ij < 0 := by
    intro ij
    exact hβ ij.1 ij.2
  have h := weighted_sum_negative w c hw hsum hc
  simpa [w, c, Finset.sum_product] using h

end PCPPR.Bernstein
