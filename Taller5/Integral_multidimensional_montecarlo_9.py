import numpy as np 

def funcion(x1,x2,x3,x4,x5,x6,x7,x8):
    resultado=(x1+x2+x3+x4+x5+x6+x7+x8)**2/(2**7)
    return resultado

N=int(1e6)
f=[]
for i in range(N):
    
    x1=np.random.uniform(0,1)
    x2=np.random.uniform(0,1)
    x3=np.random.uniform(0,1)
    x4=np.random.uniform(0,1)
    x5=np.random.uniform(0,1)
    x6=np.random.uniform(0,1)
    x7=np.random.uniform(0,1)
    x8=np.random.uniform(0,1)
    
    f.append(funcion(x1,x2,x3,x4,x5,x6,x7,x8))
    
suma=np.average(f)
print(suma, 25/192)
    
    