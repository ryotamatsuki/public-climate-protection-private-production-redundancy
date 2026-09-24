import PCPPR.Primitives

namespace PCPPR.ProductMarket

noncomputable section

/-- Symmetric Cournot quantity/price when both products are available. -/
def xD (γ : ℝ) : ℝ := 1 / (2 + γ)

def pD (γ : ℝ) : ℝ := xD γ

def piD (γ : ℝ) : ℝ := 1 / (2 + γ)^2

/-- Monopoly quantity, price, and profit. -/
def xM : ℝ := 1 / 2

def pM : ℝ := 1 / 2

def piM : ℝ := 1 / 4

/-- Disaster-state scarcity-rent wedge. -/
def delta (γ : ℝ) : ℝ := piM - piD γ

/-- Total product-market surplus in the duopoly state. -/
def TD (γ : ℝ) : ℝ := (3 + γ) / (2 + γ)^2

/-- Total product-market surplus in the monopoly state. -/
def TM : ℝ := 3 / 8

/-- The symmetric Cournot first-order condition pins down the paper's x_D. -/
theorem symmetric_cournot_foc_solution {γ x : ℝ} (hden : 2 + γ ≠ 0)
    (hfoc : 1 - (2 + γ) * x = 0) : x = xD γ := by
  unfold xD
  apply (eq_div_iff hden).2
  linarith

/-- Paper equation (6): exact closed form for Delta. -/
theorem delta_identity (γ : ℝ) (hden : 2 + γ ≠ 0) :
    delta γ = γ * (γ + 4) / (4 * (γ + 2)^2) := by
  unfold delta piM piD
  have hden' : γ + 2 ≠ 0 := by linarith
  field_simp [hden, hden']
  ring

/-- Delta is strictly positive for positive product substitutability. -/
theorem delta_pos {γ : ℝ} (hγ : 0 < γ) : 0 < delta γ := by
  have hden : 2 + γ ≠ 0 := by linarith
  rw [delta_identity γ hden]
  have hn : 0 < γ * (γ + 4) := mul_pos hγ (by linarith)
  have hd : 0 < 4 * (γ + 2)^2 := by positivity
  exact div_pos hn hd

/-- The algebraic derivative expression reported in equation (7) is positive
on the maintained domain.  The actual calculus derivative is not needed by the
headline theorem; this lemma kernel-checks the sign of the reported expression. -/
theorem delta_derivative_expression_pos {γ : ℝ} (hγ : 0 ≤ γ) :
    0 < 2 / (γ + 2)^3 := by
  positivity

end

end PCPPR.ProductMarket
