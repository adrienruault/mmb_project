# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov  7 17:26:30 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.678396,-10000,10000,0,'ASC_CAR' )

Beta_Time_CAR = Beta('Beta_Time_CAR',-0.0489551,-10000,10000,0,'Beta_Time_CAR' )

Beta_Cost_CAR = Beta('Beta_Cost_CAR',0.0120835,-10000,10000,0,'Beta_Cost_CAR' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_Time_PT = Beta('Beta_Time_PT',-0.0112902,-10000,10000,0,'Beta_Time_PT' )

Beta_Cost_PT = Beta('Beta_Cost_PT',-0.0720801,-10000,10000,0,'Beta_Cost_PT' )

Beta_freq = Beta('Beta_freq',0.10613,-10000,10000,0,'Beta_freq' )

ASC_SM = Beta('ASC_SM',0.56923,-10000,10000,0,'ASC_SM' )

Beta_DistanceSM = Beta('Beta_DistanceSM',-0.325349,-10000,10000,0,'Beta_DistanceSM' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Cost_CAR','Beta_Cost_PT','Beta_DistanceSM','Beta_Time_CAR','Beta_Time_PT','Beta_freq']
values = [[0.039468,0.03363,0.00190628,0.000200152,0.000513205,-0.00011692,9.59453e-05,0.00891463],[0.03363,0.105263,0.00149829,0.00028853,-0.0135861,-9.68425e-06,7.80728e-05,0.00867752],[0.00190628,0.00149829,0.00279041,-0.000163128,-0.000481731,-0.000564973,-2.92362e-05,4.87917e-05],[0.000200152,0.00028853,-0.000163128,0.000146172,0.00011196,8.84492e-05,1.02704e-05,1.10734e-05],[0.000513205,-0.0135861,-0.000481731,0.00011196,0.0033258,0.000165624,2.22459e-05,4.21551e-05],[-0.00011692,-9.68425e-06,-0.000564973,8.84492e-05,0.000165624,0.000155603,1.46101e-05,2.03825e-05],[9.59453e-05,7.80728e-05,-2.92362e-05,1.02704e-05,2.22459e-05,1.46101e-05,2.72933e-06,7.4159e-06],[0.00891463,0.00867752,4.87917e-05,1.10734e-05,4.21551e-05,2.03825e-05,7.4159e-06,0.00294589]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
