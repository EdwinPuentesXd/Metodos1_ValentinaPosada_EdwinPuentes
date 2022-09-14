import numpy as np
from scipy import integrate

class Integrator:
    
    def __init__(self, x,y):
        
        self.x = x
        self.y = y
        self.h = self.x[1] - self.x[0]
        
        self.integral = 0.
        
    def trapecio(self):
        
        self.integral = 0.
        
        self.integral += 0.5*(self.y[0] + self.y[-1])
        
        self.integral += np.sum( self.y[1:-1] )
        
        return self.integral*self.h
    
    def calcular_error(self,f):
        
        d = (f( self.x + self.h ) - 2*f(self.x) + f( self.x - self.h))/self.h**2 
             
        max_ = np.max(np.abs(d))
        
        self.error = (max_* (self.x[-1]-self.x[0])**3 )/(12*(len(self.x)-1)**2)
        
        return self.error

funcion= lambda x: np.exp(-(x**2))
n=1

error=1
while error > 0.005:
    n+=1
    x=np.linspace(0,1,n+1)
    y=funcion(x)
    resultado_0= Integrator(x,y)
    resultado=resultado_0.trapecio()
    error1=resultado_0.calcular_error(funcion)
    error=error1

print("El error es: " + str(error) )
print("El resultado de la integral es: " +str( resultado))
print("El numero de puntos es: " + str(n))