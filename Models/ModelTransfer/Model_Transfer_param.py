# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov  7 17:14:20 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.367045,-10000,10000,0,'ASC_CAR' )

Beta_Time_CAR = Beta('Beta_Time_CAR',-0.0489998,-10000,10000,0,'Beta_Time_CAR' )

Beta_Cost_CAR = Beta('Beta_Cost_CAR',0.00839198,-10000,10000,0,'Beta_Cost_CAR' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

Beta_Time_PT = Beta('Beta_Time_PT',-0.0113009,-10000,10000,0,'Beta_Time_PT' )

Beta_Cost_PT = Beta('Beta_Cost_PT',-0.0728761,-10000,10000,0,'Beta_Cost_PT' )

Beta_NbTransfer = Beta('Beta_NbTransfer',-0.00816447,-10000,10000,0,'Beta_NbTransfer' )

ASC_SM = Beta('ASC_SM',0.261384,-10000,10000,0,'ASC_SM' )

Beta_DistanceSM = Beta('Beta_DistanceSM',-0.326541,-10000,10000,0,'Beta_DistanceSM' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Cost_CAR','Beta_Cost_PT','Beta_DistanceSM','Beta_NbTransfer','Beta_Time_CAR','Beta_Time_PT']
values = [[0.0129333,0.00746515,0.00198617,9.30096e-05,0.000348992,-0.00120092,-0.000264513,8.18386e-05],[0.00746515,0.0797963,0.00156328,0.00019475,-0.013823,-0.000730715,-0.000147137,5.69898e-05],[0.00198617,0.00156328,0.00282722,-0.000182231,-0.000485368,-0.000608255,-0.000576191,-2.04004e-05],[9.30096e-05,0.00019475,-0.000182231,0.000152092,0.000119475,0.000195141,9.6823e-05,8.38935e-06],[0.000348992,-0.013823,-0.000485368,0.000119475,0.00334961,0.000182159,0.000169781,2.0117e-05],[-0.00120092,-0.000730715,-0.000608255,0.000195141,0.000182159,0.00325678,0.000235695,-2.17375e-05],[-0.000264513,-0.000147137,-0.000576191,9.6823e-05,0.000169781,0.000235695,0.000161247,1.15287e-05],[8.18386e-05,5.69898e-05,-2.04004e-05,8.38935e-06,2.0117e-05,-2.17375e-05,1.15287e-05,2.67432e-06]]
vc = bioMatrix(8,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
