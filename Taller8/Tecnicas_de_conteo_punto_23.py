import numpy as np 


n=3 # numero de colores 
r=4 # numero de llaves que se van a escoger 

numerador = np.math.factorial(n+r-1)
denominador = (np.math.factorial(r))*(np.math.factorial(n-1))

resultado = numerador / denominador

print(int(resultado - 3 ))

# Al resultado toca restarle 3 porque dentro de los resultados posibles, las 4 llaves 
# escogidas pueden ser todas del mismo color. Sin embargo, de cada color solo hay 3 llaves
# entonces los casos en los que las 4 son del mismo color son imposibles y no se deben tener 
# en cuenta. 





