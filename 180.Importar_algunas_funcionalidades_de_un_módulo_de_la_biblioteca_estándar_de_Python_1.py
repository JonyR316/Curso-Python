"""
Confeccionar un programa que solicite la carga de un valor entero por teclado y luego nos muestre 
la raiz cuadrada del numero y el valor elevado al cubo.

Para resolver este problema utilizaremos dos funcionalidades que nos provee el modulo math de la 
biblioteca estandar de Python.
"""

from math import sqrt, pow

valor=int(input("Ingrese el numero: "))
valor1=sqrt(valor)
print("La raiz cuadrada es:",valor1)
valor2=pow(valor,3)
print("La raiz cubica es:",valor2)