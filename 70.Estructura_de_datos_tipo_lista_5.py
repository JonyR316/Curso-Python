"""
Definir una lista por asignacioncon 5 enteros. Mostar por pantalla solo los elementos con valor iguales
o superores a 7.
"""

lista=[6, 12, 18, 9, 7, 3, 1]
x=0

print(lista)
print("los elementos con valor iguales o superores a 7 son: ")

while x <len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1

