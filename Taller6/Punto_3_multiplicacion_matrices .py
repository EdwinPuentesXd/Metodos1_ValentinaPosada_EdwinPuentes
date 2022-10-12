import numpy as np

A = np.array([[1,0,0],[5,1,0],[-2,3,1]])

B = np.array([[4,-2,1],[0,3,7],[0,0,2]])

def multiplicacion(A,B):
      
    M,N = A.shape
    R,T = B.shape

    C = np.zeros((N,R))
    
    if N==R:

        for i in range(N):
            for j in range(N):
                for k in range(N):
                        
                    C[i][j] += A[i][k]*(B[k][j])
        
        return C
