import PCPPR.MarginalDecomposition

namespace PCPPR.CanonicalWitness

/-- Exact rational canonical parameter vector from paper equation (24). -/
def gamma0 : ℚ := 12 / 25
def q0 : ℚ := 3 / 10
def k0 : ℚ := 169 / 3000
def H0 : ℚ := 1 / 100
def b0 : ℚ := 11 / 200
def c0 : ℚ := 3
def abar0 : ℚ := 2 / 25

/-- Independently reconstructed exact planner common-policy marginal at the origin. -/
def MS0 : ℚ :=
  -10651615424202276975145722347598033 /
    1643142955852817767935206845318567220

/-- Independently reconstructed exact local unilateral marginal at the origin. -/
def ML0 : ℚ :=
  717004319683029789719275067656347639039338956556328208736741107 /
    371338299758534039173259783433492599466444392472176495572868210320

/-- Exact plant-attraction response at the symmetric origin. -/
def lambda0 : ℚ :=
  434154857586848106411014309280220 /
    13447073651202386523890945009299301

/-- T9: exact rational sign of the planner marginal. -/
theorem canonical_MS_negative : MS0 < 0 := by
  norm_num [MS0]

/-- T9: exact rational sign of the local-government marginal. -/
theorem canonical_ML_positive : 0 < ML0 := by
  norm_num [ML0]

/-- Exact rational sign of the plant-attraction response. -/
theorem canonical_lambda_positive : 0 < lambda0 := by
  norm_num [lambda0]

/-- The independently reconstructed exact values satisfy the paper's central
marginal decomposition identically. -/
theorem canonical_marginal_decomposition :
    ML0 = MS0 / 4 + 2 * b0 * lambda0 := by
  norm_num [ML0, MS0, b0, lambda0]

/-- Rational endpoints of the local-government FOC isolating interval. -/
def alphaL : ℚ := 1649737 / 71666359
def alphaU : ℚ := 380091 / 16511564

/-- T12 arithmetic layer: the isolating interval is nonempty, positive, and
strictly inside the canonical policy interval. -/
theorem alpha_interval_inside_policy_domain :
    0 < alphaL ∧ alphaL < alphaU ∧ alphaU < abar0 := by
  norm_num [alphaL, alphaU, abar0]

end PCPPR.CanonicalWitness
