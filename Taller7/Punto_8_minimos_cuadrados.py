import numpy as np

B=np.array([[3,1,0,1],[1,2,1,1],[-1,0,2,-1]])
A = np.transpose(B)
b = np.array([-3,-3,8,9])
Bb= B@b
BA= B@A
xsol = np.linalg.solve(BA,Bb)
solucion = A@xsol

S=np.array([0,0,0,0])
for i in range(0,len(solucion)):
    S[i]= np.round(solucion[i],1)
    
print("La proyeccion ortogonal de b por el metodo de minimos cuadrados es: "  + str(S))

# SEGUNDA PARTE 

m,n=B.shape
U=np.zeros((m,n))
U[0]=B[0]

for i in range(1,m):
    U[i]=B[i]
    for j in range(i):
        U[i]=U[i]-((np.dot(B[i],U[j])/np.dot(U[j],U[j]))*U[j])
        
M = np.zeros((m,n))
for i in range(0,m):
    norma = np.sqrt(np.dot(U[i],U[i]))
    M[i] = U[i]/norma

A1 = np.transpose(M)
Mb = M@b
MA1 = M@A1
xsol2 = np.linalg.solve(MA1, Mb)
solucion1 = A1@xsol2

K=np.array([0,0,0,0])
for i in range(0,len(solucion1)):
    K[i]= np.round(solucion1[i],1)

print("La proyeccion de b por el metodo de Gram-Schmidt es: " +str(K))


