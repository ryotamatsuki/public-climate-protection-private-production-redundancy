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

#check ProductMarket.delta_identity
#check Availability.state_probabilities_sum_one
#check Backup.expectedProfit_state_eq_closed
#check Backup.strict_global_backup_optimum
#check Location.endpoint_interior_implies_contraction
#check Location.no_asymmetric_probability_fixed_point
#check Welfare.surplus_state_eq_closed
#check MarginalDecomposition.plant_attraction_decomposition
#check CanonicalWitness.canonical_MS_negative
#check CanonicalWitness.canonical_ML_positive
#check Bernstein.tensor_weighted_sum_negative
#check GlobalPlanner.origin_unique_global_maximizer
#check GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
#check TheoremCore.canonical_witness_core

#print axioms ProductMarket.delta_identity
#print axioms Backup.expectedProfit_state_eq_closed
#print axioms Location.no_asymmetric_probability_fixed_point
#print axioms MarginalDecomposition.plant_attraction_decomposition
#print axioms CanonicalWitness.canonical_MS_negative
#print axioms Bernstein.tensor_weighted_sum_negative
#print axioms GlobalPlanner.origin_unique_global_maximizer
#print axioms GlobalLocalGovernment.second_deriv_negative_stationary_unique_global_max
#print axioms TheoremCore.canonical_witness_core

def main : IO Unit := do
  IO.println "PCPPR formal verification core loaded."
