import numpy as np
from scipy.signal import argrelextrema

def funcion(x):
    return (3*(x**5))+(5*(x**4))-(x**3)

def derivada(x):
    return (15*(x**4))+(20*(x**3))-(3*(x**2))

def newton(f,xn):
    d=1
    while d > 1e-11:
        
        d= f(xn)/derivada(xn)
        xn1= xn-d
        xn=xn1
    
    return xn

tolerancia=6
listaraices=[]  
x=np.arange(-2,2,0.01)   
for n in range(1):
    y=funcion(x)
    y_abs=np.abs(y)
    minimos=x[argrelextrema(y_abs, np.less)]
    for i in range(len(minimos)):
        minimos[i]=newton(funcion,minimos[i])
    listaraices.append(np.round(minimos,tolerancia))
    
print(listaraices)


      
    
