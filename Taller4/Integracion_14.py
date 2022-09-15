import numpy as np
import sympy as sym
from scipy.signal import argrelextrema

def legendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)   
    y = (x**2-1)**n
    polinomio = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    return polinomio

Legendre=[]
derivada_legendre=[]
n=20
for i in range(n+1):
    Legendre.append(legendre(i))
    derivada_legendre.append(sym.diff(legendre(i)))
    
def derivada(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def obtenerpolinomio(n):
    
    x = sym.Symbol('x',Real=True)
    funcion=Legendre[n]
    f=sym.lambdify(x,funcion)  
    return f, funcion

def newton(f,xn):
    d=1
    while d > 1e-5:
        
        d= f(xn)/derivada(f,xn)
        xn1= xn-d
        xn=xn1
    
    return xn

def obtenerderivadapolinomio(n):
    
    x = sym.Symbol('x',Real=True)
    funcion=derivada_legendre[n]
    fd=sym.lambdify(x,funcion)  
    return fd, funcion


tolerancia=6
listaraiceslegendre=[]  
x=np.arange(-1,1,0.001)   
for n in range(1, 21):
    f, funcion=obtenerpolinomio(n)
    y=f(x)
    y_abs=np.abs(y)
    minimos=x[argrelextrema(y_abs, np.less)[0]]
    for i in range(len(minimos)):
        minimos[i]=newton(f,minimos[i])       
    listaraiceslegendre.append(np.round(minimos, tolerancia))
    
pesos=[]
for i in range(len(listaraiceslegendre)):
    raices=listaraiceslegendre[i] 
    fd, funcion=obtenerderivadapolinomio(i+1)
    poly=[]
    for r in raices:
        poly.append( 2/(( 1- (r**2) )*(fd(r)**2) ))
    pesos.append(np.round(poly,tolerancia))
        
print("Los pesos de ponderacion para los primeros 20 polinomios de Legendre son: " +str(pesos))
# Empieza con los pesos de ponderacion del polinomio de grado 1