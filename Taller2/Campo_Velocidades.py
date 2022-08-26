# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:27:56 2022

@author: 57305
"""

import numpy as np 
import matplotlib.pyplot as plt

    
def potencial(x,y):
    
    potencial= 2*x*(1-(2**2/(x**2+y**2)))
    
    return potencial

def cilindro(n):
    
    Q = np.zeros(n)
    r = np.zeros((n,2))
    
    Q[0] = 2
    Q[1] = -2
     
    for i in range(n):
        r[i] = [ 2*np.cos( 2*np.pi*i/n ), 2*np.sin( 2*np.pi*i/n ) ] 
        
    return Q,r

    
xi,xf,N= -4, 4, 25
x= np.linspace(xi,xf,N)
y=x.copy()

X,Y=np.meshgrid(x,y)

v_x=np.zeros((25,25))
v_y=np.zeros((25,25))

R=2
h=0.001
for i in range(25):
    for j in range(25):
        x=X[i,j]
        y=Y[i,j]
        r=np.sqrt((x**2)+(y**2))
        if r >= R:
            v_x[i,j]=(potencial(x+h,y)-potencial(x-h,y))/2*h
            v_y[i,j]=-(potencial(x,y+h)-potencial(x,y-h))/2*h
            
Q,rq=cilindro(2000)

plt.scatter(rq[:,0],rq[:,1],color='red',s=1)

plt.quiver(X,Y,v_x,v_y,color='blue')