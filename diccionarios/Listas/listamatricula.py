from ast import While


ta = []
"""
Matricula Nombre ex1 ex2 ex3"""
def Agregaralumnos():
    print("Escribe el nombre del alumno:")
    nom = input()
    print("Escribe la matricula")
    mat = input()
    ta.append([nom,mat])
    print(ta)

def AgregarCalificaciones():
    print("¿Cual es tu matricula")
    mat = input()
    for i in range(len(ta)):
        print(i)
        for j in range(len(ta[i])):
            print(j)
            if mat == ta[i][j]:
                print("Si esta la matricula")
                for k in range(5):
                    print("Escribe calificacion: ")
                    cal = int(input())
                    ta[i].append(cal)
def Consultas():
    print("Escribe la matricula del alumno")
    mat = input()
    for i in range(len(ta)):
        print(i)
        for j in range(len(ta[i])):
            print(j)
            if mat == ta[i][j]:
                print(ta[i])

def ReporteCalificaciones():
    print("¿Cual es tu matricula")
    mat = input()
    for i in range(len(ta)):
        print(i)
        for j in range(len(ta[i])):
            print(j)
            if mat == ta[i][j]:
                cal = 0
                m=2
                for k in range(5):
                    print("Calificaciones")
                    print(ta[i][m])
                    cal = cal + ta[i][m]
                    m=m+1
                promedio = cal/5
                print("Su promedio es" + promedio)

                



while True:
    print("MENU\n1-. Agregar Alumnos\n2-. Agregar Calificacion\n3-. Consultas\n4-. Reporte de calificaciones con promedio final\n5-. Finalizar\nEscribe una opcion")
    op = int(input())
    if (op == 1):
        if(len(ta)==10):
            print("Limite de alumnos")
        else:
            Agregaralumnos()
    elif(op == 2):
        AgregarCalificaciones()
    elif( op == 3):
        Consultas()
    elif( op == 4):
        ReporteCalificaciones()
    elif( op == 5):
        break

