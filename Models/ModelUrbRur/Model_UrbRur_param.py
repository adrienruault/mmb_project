# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov  7 17:49:31 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.499714,-10000,10000,0,'ASC_CAR' )

Beta_Time_CAR = Beta('Beta_Time_CAR',-0.0490963,-10000,10000,0,'Beta_Time_CAR' )

Beta_Cost_CAR = Beta('Beta_Cost_CAR',0.00920395,-10000,10000,0,'Beta_Cost_CAR' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_Time_PT = Beta('Beta_Time_PT',-0.0113952,-10000,10000,0,'Beta_Time_PT' )

Beta_Cost_PT = Beta('Beta_Cost_PT',-0.072968,-10000,10000,0,'Beta_Cost_PT' )

Beta_UrbRur = Beta('Beta_UrbRur',0.0877489,-10000,10000,0,'Beta_UrbRur' )

ASC_SM = Beta('ASC_SM',0.392516,-10000,10000,0,'ASC_SM' )

Beta_DistanceSM = Beta('Beta_DistanceSM',-0.326224,-10000,10000,0,'Beta_DistanceSM' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Cost_CAR','Beta_Cost_PT','Beta_DistanceSM','Beta_Time_CAR','Beta_Time_PT','Beta_UrbRur']
values = [[0.0443357,0.0362154,0.0029615,-0.000172726,0.000444321,-0.000546147,4.22467e-05,0.0209368],[0.0362154,0.105757,0.00251346,-6.94081e-05,-0.0136885,-0.000425716,2.44365e-05,0.0190651],[0.0029615,0.00251346,0.00284422,-0.000175673,-0.000476548,-0.000573098,-2.86523e-05,0.00078058],[-0.000172726,-6.94081e-05,-0.000175673,0.000147961,0.000113986,9.22794e-05,1.06782e-05,-0.000220826],[0.000444321,-0.0136885,-0.000476548,0.000113986,0.00333465,0.000164797,2.22196e-05,2.44624e-05],[-0.000546147,-0.000425716,-0.000573098,9.22794e-05,0.000164797,0.000157345,1.44929e-05,-0.000240047],[4.22467e-05,2.44365e-05,-2.86523e-05,1.06782e-05,2.22196e-05,1.44929e-05,2.68335e-06,-2.04831e-05],[0.0209368,0.0190651,0.00078058,-0.000220826,2.44624e-05,-0.000240047,-2.04831e-05,0.0137513]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
