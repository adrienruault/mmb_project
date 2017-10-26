#BL_NL_generic.py

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


# Choice
# 0 -> public transports
# 1 -> private modes
# 2 -> soft modes

#Parameters to be estimated
# Arguments:
#   1  Name for report; typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR	 = Beta('ASC_CAR',0,-100,100,0)
ASC_RAIL	 = Beta('ASC_RAIL',0,-100,100,1)
BETA_COST	 = Beta('BETA_COST',0,-100,100,0)
BETA_TIME	 = Beta('BETA_TIME',0,-100,100,0)

# Define here arithmetic expressions for variables that are not directly available in the data
one  = DefineVariable('one',1)
rail_time = DefineVariable('rail_time',( rail_ivtt + rail_acc_time ) + rail_egr_time )
car_time = DefineVariable('car_time', car_ivtt + car_walk_time )
rate_G2E = DefineVariable('rate_G2E', 0.44378022)
car_cost_euro = DefineVariable('car_cost_euro', car_cost * rate_G2E)
rail_cost_euro = DefineVariable('rail_cost_euro', rail_cost * rate_G2E)


# Utilities
Car = ASC_CAR * one + BETA_COST * car_cost_euro + BETA_TIME * car_time
Rail = ASC_RAIL * one + BETA_COST * rail_cost_euro + BETA_TIME * rail_time

V = {0: Car, 1: Rail}
av = {0: one, 1: one}

# Exclude SP data (responses to the hypothetical scenarios)
BIOGEME_OBJECT.EXCLUDE = sp != 0

# Loglikelihood
loglik = bioLogLogit(V,av,choice)

# Defines an itertor on the data
rowIterator('obsIter') 

# Defines the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(loglik,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"

#Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [0,1]
cteLoglikelihood(choiceSet,choice,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Car utility'] = Car
BIOGEME_OBJECT.FORMULAS['Rail utility'] = Rail