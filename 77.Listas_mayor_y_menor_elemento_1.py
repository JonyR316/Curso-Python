"""
Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista
"""

lista=[]

for x in range(5):
    valor=int(input("Ingrese el valor: " ))
    lista.append(valor)
mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print("La lista completa es: ")
print(lista)
print("El numero mayor es: ")
print(mayor)