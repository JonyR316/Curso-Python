"""
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla,
luego ordenar de mayor a menor e imprimir nuevamente.
"""

lista=[]

for x in range(5):
    valor= int(input("Ingresar el valor:"))
    lista.append(valor)
for x in range(4):
    for x in range(4):
        if lista[x]>lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]= aux
print("Lista ordenada de menor a mayor")
print(lista)
for x in range(4):
    for x in range(4):
        if lista[x]<lista[x+1]:
            aux=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]= aux
print("Lista ordenada de mayor a menor")
print(lista)
