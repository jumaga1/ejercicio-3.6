# -*-coding: utf-8-*-
"""
Created on Fri Sep 12:22:24 2017
@autor: juan manuel garcia ayala
"""
#PROBLEMA 3.6 INGENIERIA DE CALOR
import numpy as np
import scipy as sp
import pandas as pd 
#PROPIEDADES DEL FLUIDO
data1={'propiedad':['densidad','viscocidad','temperatura','conductividad termica','capacidad calorifica'],'valor':[990,0.00044,65,0.5816,4187],'unidad':['kg/m3','N.s/m2','°C','W/m.°C','J/kg.°C']}
df1= pd.DataFrame(data1,columns=['propiedad','valor','unidad'])
b='PROPIEDADES DEL FLUIDO'
print (b)
print (df1)
#PROPIEDADES DEL RECIPIENTE
data2={'.':['Da','Di','l'],'longitud':[0.18,0.305,0.25],'unidad':['m','m','m']}
df2=pd.DataFrame(data2,columns=['.','longitud','unidad'])
c='PROPIEDADES DEL RECIPIENTE'
print (c)
print (df2)
"""
PLANTEAMIENTO
calor ganado = calor perdido
Qp=(Mvapor)*(\DeltaT_2-\DeltaT_1)
Qg=U*A*(\DeltaT_2-\DeltaT_1)
COEFICIENTES
para el interior(con agitacion)
Nu=alpha*(Re**0.66)*(Pr**0.33)*((mus/mu)**0.14)
para el exterior(vapor condensandose)
ho=11915/(l**0.25)*(DeltaT**0.33)
DeltaT=Tv-Ts/2
"""
#CALCULOS
a='CALCULOS'
print (a)
#Numero de Reynolds
ni=2.08 #rps velocidad del agitador
da=0.18 #m diametro agitador
liquid_density=990
mu_liquid=0.00044
re= (da**2)*ni*liquid_density/mu_liquid
print ('NUMERO DE REYNOLDS=',re)
#NUMERO DE PRANDTL
c_p_liquid=4187
conduct_liquid=0.5815
pr=c_p_liquid*mu_liquid/conduct_liquid
print ('NUMERO DE PRANDTL=',pr)
#NUMERO DE NUSSELT
alpha=0.36
nu=alpha*(re**0.66)*(pr**0.33)
print ('NUMERO DE NUSSELT=',nu)
#CALCULO DE hi
di=0.305 #ancho del recipiente 
hi=nu*conduct_liquid/di
print ('hi=',hi)
#COEFICIENTE DEL LADO DEL VAPOR
