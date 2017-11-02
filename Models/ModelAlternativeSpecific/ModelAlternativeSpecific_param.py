# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Thu Nov  2 15:31:16 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.363779,-10000,10000,0,'ASC_CAR' )

Beta_Time_CAR = Beta('Beta_Time_CAR',-0.0488894,-10000,10000,0,'Beta_Time_CAR' )

Beta_Cost_CAR = Beta('Beta_Cost_CAR',0.00833465,-10000,10000,0,'Beta_Cost_CAR' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_Time_PT = Beta('Beta_Time_PT',-0.0114119,-10000,10000,0,'Beta_Time_PT' )

Beta_Cost_PT = Beta('Beta_Cost_PT',-0.0727175,-10000,10000,0,'Beta_Cost_PT' )

ASC_SM = Beta('ASC_SM',0.258167,-10000,10000,0,'ASC_SM' )

Beta_DistanceSM = Beta('Beta_DistanceSM',-0.326435,-10000,10000,0,'Beta_DistanceSM' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Cost_CAR','Beta_Cost_PT','Beta_DistanceSM','Beta_Time_CAR','Beta_Time_PT']
values = [[0.0124959,0.00721452,0.00174281,0.000170522,0.000420513,-0.000171668,7.44064e-05],[0.00721452,0.0797329,0.00132723,0.000261266,-0.0137609,-6.22071e-05,5.58083e-05],[0.00174281,0.00132723,0.00281532,-0.000167892,-0.000477435,-0.000566703,-2.87236e-05],[0.000170522,0.000261266,-0.000167892,0.000145694,0.000113619,8.98962e-05,1.05241e-05],[0.000420513,-0.0137609,-0.000477435,0.000113619,0.00334582,0.000164884,2.23112e-05],[-0.000171668,-6.22071e-05,-0.000566703,8.98962e-05,0.000164884,0.000155477,1.44571e-05],[7.44064e-05,5.58083e-05,-2.87236e-05,1.05241e-05,2.23112e-05,1.44571e-05,2.68937e-06]]
vc = bioMatrix(7,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
