import pathlib,sys
from scipy.optimize import minimize_scalar
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from core_model import Params, profile, primitives, national_welfare

par=Params(); piD,piM,delta,TD,TM=primitives(par)
q=par.q0
# Closed-form recovery of symmetric backup levels.
rC=q*piM/(par.k+q*delta)
rD=q*(piD+q*delta)/(par.k+q*q*delta)
AA=profile(0,0,'A','A',par); AB=profile(0,0,'A','B',par)
assert abs(AA['r1']-rC)<1e-12
assert abs(AB['r1']-rD)<1e-12
assert rC>rD

# Fixed-location benchmark removes the plant-attraction term by construction.
# The check records that the full model location probability is exactly 1/2 at symmetric policies.
from core_model import location_probability
p,_=location_probability(0,0,par)
assert abs(p-.5)<1e-14

print({'r_co_located':rC,'r_dispersed':rD,'symmetric_location_probability':p})
print('PASS nested benchmark recovery')
