# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov  7 17:55:21 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.0613004,-10000,10000,0,'ASC_CAR' )

Beta_Time_CAR = Beta('Beta_Time_CAR',-0.0487663,-10000,10000,0,'Beta_Time_CAR' )

Beta_Cost_CAR = Beta('Beta_Cost_CAR',0.00489442,-10000,10000,0,'Beta_Cost_CAR' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_Time_PT = Beta('Beta_Time_PT',-0.0115101,-10000,10000,0,'Beta_Time_PT' )

Beta_Cost_PT = Beta('Beta_Cost_PT',-0.073784,-10000,10000,0,'Beta_Cost_PT' )

Beta_Age = Beta('Beta_Age',-0.00632425,-10000,10000,0,'Beta_Age' )

ASC_SM = Beta('ASC_SM',-0.0510355,-10000,10000,0,'ASC_SM' )

Beta_DistanceSM = Beta('Beta_DistanceSM',-0.326283,-10000,10000,0,'Beta_DistanceSM' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Age','Beta_Cost_CAR','Beta_Cost_PT','Beta_DistanceSM','Beta_Time_CAR','Beta_Time_PT']
values = [[0.0363058,0.03238,0.000500041,0.00202325,0.000343063,0.00038292,-0.000133175,9.08706e-05],[0.03238,0.106321,0.000526676,0.00164479,0.000441399,-0.0138111,-2.71162e-05,7.29086e-05],[0.000500041,0.000526676,1.0556e-05,6.40504e-06,3.40115e-06,-9.11244e-07,6.10063e-07,3.09522e-07],[0.00202325,0.00164479,6.40504e-06,0.00288721,-0.000165127,-0.000484044,-0.000575878,-2.90176e-05],[0.000343063,0.000441399,3.40115e-06,-0.000165127,0.000146425,0.000114051,9.06047e-05,1.08606e-05],[0.00038292,-0.0138111,-9.11244e-07,-0.000484044,0.000114051,0.00334935,0.000166111,2.24416e-05],[-0.000133175,-2.71162e-05,6.10063e-07,-0.000575878,9.06047e-05,0.000166111,0.000157017,1.4596e-05],[9.08706e-05,7.29086e-05,3.09522e-07,-2.90176e-05,1.08606e-05,2.24416e-05,1.4596e-05,2.71356e-06]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
