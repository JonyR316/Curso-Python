"""
Realizar un programa que pida la carga de dos listas numericas enteras de 4 elementos cada una.
Generar una tercer lista que surja de la suma de los elementos de la misma posicion de cada lista.
Mostrar esta tercer lista.
"""
lista1=[]
print("Elementos de la primer lista")
for x in range(4):
    valor=int(input("Ingrese el valor: "))
    lista1.append(valor)

lista2=[]
print("Elementos de la segunda lista")
for x in range(4):
    valor=int(input("Ingrese el valor: "))
    lista2.append(valor)

lista_suma=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista_suma.append(suma)

print("Primera Lista")
print(lista1)
print("Segunda Lista")
print(lista2)
print("Tercer Lista")
print(lista_suma)