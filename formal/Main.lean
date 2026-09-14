import PCPPR.Primitives
import PCPPR.ProductMarket
import PCPPR.Availability
import PCPPR.Backup
import PCPPR.Location
import PCPPR.Welfare
import PCPPR.MarginalDecomposition
import PCPPR.Bernstein
import PCPPR.CanonicalWitness
import PCPPR.GeneratedCertificates
import PCPPR.GlobalPlanner
import PCPPR.GlobalLocalGovernment
import PCPPR.TheoremCore

open PCPPR

-- T1-T14 theorem inventory.
#check ProductMarket.delta_identity
#check Availability.state_probabilities_sum_one
#check Backup.expectedProfit_state_eq_closed
#check Backup.strict_global_backup_optimum
#check Backup.interior_linear_system_unique
#check Backup.strategic_substitution_expression_neg
#check Backup.rC_solves_symmetric_foc
#check Backup.rD_solves_symmetric_foc
#check Location.endpoint_interior_implies_no_clipping
#check Location.endpoint_interior_implies_contraction
#check Location.no_asymmetric_probability_fixed_point
#check Location.affine_pair_unique
#check Welfare.surplus_state_eq_closed
#check MarginalDecomposition.plant_attraction_decomposition
#check CanonicalWitness.canonical_MS_negative
#check CanonicalWitness.canonical_ML_positive
#check CanonicalWitness.canonical_lambda_positive
#check CanonicalWitness.canonical_marginal_decomposition
#check CanonicalWitness.alpha_interval_inside_policy_domain
#check Bernstein.bernstein_sum_negative
#check Bernstein.tensor_bernstein_sum_negative
#check GlobalPlanner.strictAntiOn_Icc_of_deriv_neg
#check GlobalPlanner.origin_strictly_dominates
#check GlobalPlanner.origin_unique_global_maximizer
#check GlobalLocalGovernment.generated_diagonal_FOC_unique_root
#check GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
#check GlobalLocalGovernment.symmetric_positive_nash_of_unique_best_responses
#check TheoremCore.canonical_witness_core
#check TheoremCore.canonical_witness_from_generated_certificates

-- T15 proof-critical axiom audit.  CI also rejects source-level sorry/admit and
-- custom `axiom` declarations before this file is elaborated.
#print axioms ProductMarket.delta_identity
#print axioms Backup.expectedProfit_state_eq_closed
#print axioms Backup.strict_global_backup_optimum
#print axioms Location.endpoint_interior_implies_no_clipping
#print axioms Location.no_asymmetric_probability_fixed_point
#print axioms MarginalDecomposition.plant_attraction_decomposition
#print axioms CanonicalWitness.canonical_MS_negative
#print axioms CanonicalWitness.canonical_ML_positive
#print axioms CanonicalWitness.canonical_marginal_decomposition
#print axioms Bernstein.bernstein_sum_negative
#print axioms Bernstein.tensor_bernstein_sum_negative
#print axioms GlobalPlanner.origin_unique_global_maximizer
#print axioms GlobalLocalGovernment.generated_diagonal_FOC_unique_root
#print axioms GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
#print axioms TheoremCore.canonical_witness_from_generated_certificates

def main : IO Unit := do
  IO.println "PCPPR formal verification core loaded."
