
contador = 0
for i in range(0,11):
    for j in range(0,11):
        for k in range(0,11):
            
            suma = i+j+k
            
            if suma ==10:
                contador +=1
                
print(contador)

