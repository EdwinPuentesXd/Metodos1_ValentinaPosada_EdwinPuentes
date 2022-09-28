import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm 

def esfera(N,R):
    
    X=np.zeros(N)
    Y=np.zeros_like(X)
    Z=np.zeros_like(X)
    
    for i in tqdm(range(N)):
        
        u = np.random.rand()
        r = R*u**(1/3)
        
        phi = np.random.uniform(0,2*np.pi)
        theta=np.random.uniform(0,np.pi)
        
        X[i]= r*np.cos(phi)*np.sin(theta)
        Y[i]= r*np.sin(phi)*np.sin(theta)
        Z[i]= r*np.cos(theta)
        
    return X,Y,Z

def funcion(x,y,z):
    return np.exp(np.sqrt((x**2)+(y**2)+(z**2)))


N=int(1e6) 

X,Y,Z = esfera(N,1)
fig = plt.figure(figsize=(8,8))
ax=fig.add_subplot(1,1,1, projection ="3d")

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.view_init(10, 60)

ax.scatter(X,Y,Z,color='b')

resultado=np.zeros(N)
for i in range(N):
     
     x=X[i]
     y=Y[i]
     z=Z[i]
     
     resultado[i]= funcion(x,y,z)
     
integral=(4*np.pi/3)*np.average(resultado)

print(integral, 4*np.pi*((np.exp(1)-2)))
         






        
    
    

    
    
    
