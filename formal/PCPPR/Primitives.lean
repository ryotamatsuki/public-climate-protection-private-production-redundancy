import Mathlib

namespace PCPPR

noncomputable section

/-- Primitive parameter vector used by the paper.  The formal development keeps
parameter restrictions separate from the raw record so that every theorem makes
its own assumptions explicit. -/
structure Params where
  gamma : ℝ
  q0 : ℝ
  k : ℝ
  H : ℝ
  b : ℝ
  c : ℝ
  abar : ℝ

/-- The paper's baseline parameter domain. -/
def Admissible (p : Params) : Prop :=
  0 ≤ p.gamma ∧ p.gamma < 1 ∧
  0 < p.abar ∧ p.abar < p.q0 ∧ p.q0 < 1 ∧
  0 < p.k ∧ 0 < p.H ∧ 0 < p.c ∧ 0 < p.b

/-- Public protection translates into primary-failure risk by q = q0-a. -/
def risk (q0 a : ℝ) : ℝ := q0 - a

/-- Backup-readiness resource cost. -/
def backupCost (k r : ℝ) : ℝ := k * r^2 / 2

/-- Public-protection resource cost. -/
def protectionCost (c a : ℝ) : ℝ := c * a^2 / 2

end

end PCPPR
