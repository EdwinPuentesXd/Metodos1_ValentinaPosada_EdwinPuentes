import numpy as np 
import matplotlib.pyplot as plt

def funcion1(x):
    return 2*x -2

def funcion2(x):
    return (1-x)/2

def funcion3(x):
    return 4-x

x = range(-10,10)

plt.plot(x,[funcion1(i) for i in x], color="purple")
plt.plot(x,[funcion2(i) for i in x], color="blue")
plt.plot(x,[funcion3(i) for i in x], color="green")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlim(-11,11)
plt.ylim(-11,11)

A=[[2,-1],[1,2],[1,1]]
B= []

for i in range(len(A[0])):
    B.append([])
    for j in range(len(A)):
        B[i].append(A[j][i])
        
A = np.array(A)
B = np.array(B)
b = np.array([[2],[1],[4]])
AB= B@b
AA= B@A

xsol = np.linalg.solve(AA,AB)
print("La solucion es el punto: " + "(" +str(np.round(xsol[0][0],3))+ " , " +str(np.round(xsol[1][0],3))+")")
solucion=np.linalg.norm((A@xsol)-b)
print("La distancia obtenida con el punto encontrado es: " +str(np.round(solucion,3)))

plt.scatter(xsol[0], xsol[1], color='orange')
plt.show()

x = np.arange(-5,5,0.03)
y = np.arange(-5,5,0.03)        

X,Y= np.meshgrid(x,y)
Z= np.zeros(X.shape)

for i in range(X.shape[0]):
    for j in range(Y.shape[1]):
        
        xi=X[i][j]
        yi=Y[i][j]
        x_vec=np.array([[xi],[yi]])
   
        resultado1 = np.dot(A, x_vec)
        resultado = resultado1 - b
        resultado_norma= np.linalg.norm(resultado)
        Z[i][j]= resultado_norma

print("La distancia minima es: " +str(np.round(np.min(Z),3)))

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1, projection = '3d')

ax.set_xlim3d(-5, 5)
ax.set_ylim3d(-5, 5)
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel('$d(x^*)$')
ax.view_init(25, 45)
ax.plot_surface(X,Y,Z,cmap='coolwarm')

plt.show()

