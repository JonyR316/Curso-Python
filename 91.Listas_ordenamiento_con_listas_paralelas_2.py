"""
Crear y cargar en una lista los nombres de 5 paises y en otra lista paralela la cantidad de habitantes
del mismo. Ordenar alfabeticamente e imprimir los resultados. Por ultimo ordenar con respecto a la cantidad
de  habiatantes (de mayor a menor) e imprimir nuevamente. 
"""
paises=[]
habitantes=[]

for x in range(5):
    pais= input("Ingrese el nombre del pais: ")
    paises.append(pais)
    habitante=int(input("Ingrese el numero de habitantes: "))
    habitantes.append(habitante)
for x in range(4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
print("Ordenado alfabetico")
for x in range(5):
    print(paises[x], habitantes[x])
for x in range(4):
    for x in range(4):
        if habitantes[x]<habitantes[x+1]:
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2
print("Cantidad de Habitantes de mayor a menor")
for x in range(5):
    print(paises[x], habitantes[x])