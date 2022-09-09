import numpy as np
import sympy as sym
from scipy.signal import argrelextrema

def laguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = sym.exp(-x)*x**n
    
    polinomio = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    
    return polinomio

Laguerre=[]
n=20
for i in range(n+1):
    Laguerre.append(laguerre(i))
    
def derivada(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def obtenerpolinomio(n):
    
    x = sym.Symbol('x',Real=True)
    funcion=Laguerre[n]
    f=sym.lambdify(x,funcion)  
    return f, funcion

def newton(f,xn):
    d=1
    while d > 1e-6:
        
        d= f(xn)/derivada(f,xn)
        xn1= xn-d
        xn=xn1
    
    return xn

tolerancia=5
listaraiceslaguerre=[]
g=100
x=np.arange(0,g,0.001)   
for n in range(1, 21):
    f, funcion=obtenerpolinomio(n)
    y=f(x)
    y_abs=np.abs(y)
    minimos=x[argrelextrema(y_abs, np.less)[0]]
    for i in range(len(minimos)):
        minimos[i]=newton(f,minimos[i])
    listaraiceslaguerre.append(np.round(minimos,tolerancia))

print(listaraiceslaguerre)
