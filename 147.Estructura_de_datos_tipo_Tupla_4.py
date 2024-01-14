"""
Confeccionar un programa co las siguientes funciones:
1) Cargar una lista de 5 enteros.
2) Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en ele bloque principal y mostrar el mayor y menor.
"""

def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingresar el valor entero: "))
        lista.append(valor)
    return lista

def mayormenor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    return [menor, mayor]

lista=cargar()
menor,mayor=mayormenor(lista)
print("El menor elemento en la lista es:", menor)
print("El mayor elemento en la lista es:", mayor)