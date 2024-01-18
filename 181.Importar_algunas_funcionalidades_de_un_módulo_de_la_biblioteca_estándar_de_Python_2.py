"""
Confecionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre 
la raiz cuadrada del numero y el valor elvado al cubo.
"""

from math import sqrt as cuadrada, pow as cubica

valor=int(input("Ingrese el valor: "))
print("La Raiz Cudrada es:",cuadrada(valor))
print("La Raiz cubica es:",cubica(valor,3))
