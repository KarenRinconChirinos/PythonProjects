calif = {}
calif["X02"] =["Karen",4,3,2,1,3]
calif["X03"] =["Maria",1,2,3,4,5]
m = input("Que matricula buscas?")
for mat in calif:
    if mat == m:
        print("matricula encontrada")
        print(calif[mat])
        calif[m][1]=[10]
print(calif)