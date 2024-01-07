"""
Definir por asignacion una lista de enteros en el bloque principal del programa. Elabore tres funciones 
la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna 
el mayor y la ultima recibe la lista y retorna el menor.
"""

def cargar_suma(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    return suma

def cargar_mayor(lista):
    mayor =lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor= lista[x]
    return mayor        

def cargar_menor(lista):
    menor =lista[0]
    for x in range(1,len(lista)):
        if lista[x]<menor:
            menor= lista[x]
    return menor

listavalores=[1,3,6,9,12]
print("lista completa")
print(listavalores)
print("la suma completa de los numeros es:",cargar_suma(listavalores))

print("El numero mayor es:",cargar_mayor(listavalores))

print("El numero menor es:",cargar_menor(listavalores))
