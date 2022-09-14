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

# Para dos puntos

raices_2=listaraiceslegendre[1]
pesos_2=[]
fd_2, funcion=obtenerderivadapolinomio(2)

for r in raices_2:
    pesos_2.append( 2/(( 1- (r**2) )*(fd_2(r)**2) ))
    
a = 1
b = 2
f_2= lambda x : 1/(x**2)
t = 0.5*((b-a)*raices_2 + a + b)
Integral_2 = 0.5*(b-a)*np.sum( pesos_2*f_2(t) )

print("La cuadratura de Gauss-Legendre con dos puntos es: "+ str(np.round(Integral_2,6)))

# Para tres puntos

raices_3=listaraiceslegendre[2]
pesos_3=[]
fd_3, funcion=obtenerderivadapolinomio(3)

for r in raices_3:
    pesos_3.append( 2/(( 1- (r**2) )*(fd_3(r)**2) ))
    
a = 1
b = 2
f_3= lambda x : 1/(x**2)
t = 0.5*((b-a)*raices_3 + a + b)
Integral_3= 0.5*(b-a)*np.sum( pesos_3*f_3(t) )

print("La cuadratura de Gauss-Legendre con tres puntos es: "+ str(np.round(Integral_3,6)))

            


