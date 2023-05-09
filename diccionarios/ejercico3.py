def lista():
    print("codigo de for con listas")
    ta = []
    h = 8
    j = 3
    r = 0
    for i in range (5,9,1):
        ta.append([i,h,j])
        print(ta[r])
        h -=1
        j +=3
        r +=1

def bucle():
    nom = "nadie"
    edad = "0"
    while (nom != "juan"):
        nom = input("n")
        edad = input ("")

while True:
    opcion = int(input("Elige una opcion"))
    print("Funcion for --- 1")
    print("Funcion while --- 2")
    if(opcion==1):
        print(lista())
    elif (opcion==2):
        bucle()
    elif (opcion==0):
        break
    else:
        print("Ingresa un valor")        
