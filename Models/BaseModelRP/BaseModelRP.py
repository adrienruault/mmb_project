from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed

### ASC ###
ASC_PT	 = Beta('ASC_PT',0,-10000,10000,1)
ASC_CAR	 = Beta('ASC_CAR',0,-10000,10000,0)
ASC_SM	 = Beta('ASC_SM',0,-10000,10000,0)

### Beta ###
Beta_Time = Beta('Beta_Time',0,-10000,10000,0)
Beta_Cost = Beta('Beta_Cost',0,-10000,10000,0)
Beta_Distance = Beta('Beta_Distance',0,-10000,10000,0)

# Define here arithmetic expressions for name that are not directly available from the data

one  = DefineVariable('one',1)
TotalTimePT = DefineVariable('TotalTimePT', TimePT + WalkingTimePT + WaitingTimePT )


#### UTILITIES #####

PT = ASC_PT + Beta_Time*TotalTimePT+Beta_Cost*MarginalCostPT
CAR = ASC_CAR + Beta_Time*TimeCar+Beta_Cost*CostCarCHF
SM = ASC_SM + Beta_Distance*distance_km


V = {0: PT, 1: CAR, 2: SM}
av = {0: one, 1: one, 2: one}

# Exclude SP data (responses to the hypothetical scenarios)
BIOGEME_OBJECT.EXCLUDE = (Choice == -1 )

# Loglikelihood
loglik = bioLogLogit(V,av,Choice)

# Defines an itertor on the data
rowIterator('obsIter')

# Defines the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(loglik,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"

#Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [0,1,2]
cteLoglikelihood(choiceSet,Choice,'obsIter')
availabilityStatistics(av,'obsIter')
BIOGEME_OBJECT.FORMULAS['Car utility'] = CAR
BIOGEME_OBJECT.FORMULAS['PT utility'] = PT
BIOGEME_OBJECT.FORMULAS['Soft mode utility'] = SM