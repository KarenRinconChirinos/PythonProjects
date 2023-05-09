dictionary = { 'one':'two','three':'one','two':'three'}  #Se asigna el diccionario
v = dictionary['three']                                    #le asigna la variable  v l valor que esta en la clave one
print(v)
for k in range(len(dictionary)):                         #Ciclo que va del rango de dictionario
    v=dictionary[v]                                      #Se le asigna a v el valor de diccionario en v osea two

print(v)