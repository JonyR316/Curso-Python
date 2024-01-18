"""
Calcular el factorial de un numero ingresado por teclado.
El factorial de un numero es la cantidad que resulta de la multiplicacion de determinado numero 
natural por todos los numeros naturales que le anteceden excluyendo el cero. Por ejemplo el
factorial de 4 es 24, resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha 
funcionalidad del modulo math.
El modulo math tiene una funcion llamada factorial que recibe como parametro un entero del que 
necesitamos que nos retorne el factorial.
Solo importar la funcionalidad factorial del modulo math de la biblioteca estandar de Python.
"""

from math import factorial 

valor=int(input("Ingrese un numero: "))
print("El factorial de:",valor,"es:",factorial(valor))

