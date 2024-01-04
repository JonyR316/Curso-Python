"""
Solicitar por teclado dos enteros.El primer valor indica la cantidad de elementos que crearemos en
la lista. El segundo valor indica la cantidad de elementos que tendra cada una de las listas internas a 
la lista principal.
Mostrar la lista y la suma de todos sus elementos.

Por ejemplo si el operador carga un 2 y un 4 significa que debemos creaer una lista similar a:
"""

lista=[]
elementos=int(input("Ingrese la cantidad de elementos:  "))
sublista=int(input("Elementos de la listas internas :  "))
for k in range(elementos):
    lista.append([])
    for x in range(sublista):
        valor= int(input("Ingrese el valor: "))
        lista[k].append(valor)
print(lista)
suma=0
for k in range(len(lista)):
    for x in range(len(lista[k])):
        suma = suma + lista[k][x]
print("suma de todos los elementos es: ", suma)