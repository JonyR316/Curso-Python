"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.
"""

sueldos=[]
for x in range(5):
    valor=int(input("Ingresar el valor del sueldo: "))
    sueldos.append(valor)
print("Lista de Sueldos Original")
print(sueldos)
for x in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
print("Lista de sueldos Ordenada")
print(sueldos)





#-----------------------------------------
sueldos=[]

for x in range(5):
    valor=int(input("Ingresar el valor del sueldo: "))
    sueldos.append(valor)
print("Lista de Sueldos Original")
print(sueldos)
for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
    for x in range(3):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
            for x in range(2):
                if sueldos[x]>sueldos[x+1]:
                    aux=sueldos[x]
                    sueldos[x]=sueldos[x+1]
                    sueldos[x+1]=aux
                for x in range(1):
                    if sueldos[x]>sueldos[x+1]:
                        aux=sueldos[x]
                        sueldos[x]=sueldos[x+1]
                        sueldos[x+1]=aux
print("Lista tiene el ultimo elemento ordenado")
print(sueldos)
