# This file has automatically been generated
# biogeme 2.6a [Mon Apr 24 10:21:29 BST 2017]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Wed Nov  1 16:16:29 2017</p>
#
ASC_CAR = Beta('ASC_CAR',0.09876,-10000,10000,0,'ASC_CAR' )

Beta_Time = Beta('Beta_Time',-0.00392793,-10000,10000,0,'Beta_Time' )

Beta_Cost = Beta('Beta_Cost',-0.0589883,-10000,10000,0,'Beta_Cost' )

ASC_PT = Beta('ASC_PT',0,-10000,10000,1,'ASC_PT' )

ASC_SM = Beta('ASC_SM',0.184444,-10000,10000,0,'ASC_SM' )

Beta_Distance = Beta('Beta_Distance',-0.2729,-10000,10000,0,'Beta_Distance' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_SM','Beta_Cost','Beta_Distance','Beta_Time']
values = [[0.0100583,0.00373393,0.000318582,0.000700729,5.72003e-05],[0.00373393,0.0740237,0.000311985,-0.0131938,1.75592e-05],[0.000318582,0.000311985,0.000212214,2.59733e-05,-3.13636e-06],[0.000700729,-0.0131938,2.59733e-05,0.00304502,5.01856e-06],[5.72003e-05,1.75592e-05,-3.13636e-06,5.01856e-06,6.26109e-07]]
vc = bioMatrix(5,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
