"""
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
"""

lista=[1,2,3,4,5]
x=0
suma=0

while x<len(lista):
    suma=suma +lista[x]
    x=x+1
print("Los elementos d ela lista: ")
print(lista)
print("La suma de todos los elementos es: ")
print(suma)