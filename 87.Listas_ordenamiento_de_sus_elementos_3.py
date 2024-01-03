"""
Crear una lista y almacenar los nombres de 5 paises. Ordenar alfabeticamente la lista e imprimirla.
"""

paises=[]

for x in range(5):
    pais=input("Ingresar el nombre del pais: ")
    paises.append(pais)
for x in range(4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("Lista de paises odenados alfabeticamente")
print(paises)

#----------------------------------------------

paises=[]

for x in range(5):
    pais=input("Ingresar el nombre del pais: ")
    paises.append(pais)
for k in range(4):
    for x in range(4-k):
        if paises[x]>paises[x+1]:
            aux=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux
print("Lista de paises odenados alfabeticamente")
print(paises)