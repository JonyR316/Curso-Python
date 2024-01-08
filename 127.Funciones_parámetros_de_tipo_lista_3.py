"""
Crear una lista de entros por asignacion. Definir una funcion que reciba una lista de enteros y un segundo 
parametro de tipo entero. Dentro de la funcion mostrar cada elemento de la lista multiplicado por el valor 
entero enviado
"""

def multiplicar(lista, valor):
    for x in range(len(lista)):
        multiplicar=lista[x] * valor
        print(multiplicar)
    

lista=[3,7,8,10,2]
print("Lista original")
print(lista)
print("Lista de los elementos multiplicados por 3")
multiplicar(lista,3)