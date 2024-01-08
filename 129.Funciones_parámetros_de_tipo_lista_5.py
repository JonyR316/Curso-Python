"""
Definir una lista de enteros por asignacion en el bloque principal. Llamar a una funcion que reciba la 
lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto e el bloque principal de 
nuestro programa.
"""

def retornar_enteros(lista):
    producto=1
    for x in range(len(lista)):
        producto=producto*lista[x]
    return producto


lista=[1,3,6,9,12]
print(lista)
print("El resultado de la multiplicacion de estos elementos es:",retornar_enteros(lista) )