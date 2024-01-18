"""
Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron.
Imprimir un mensaje que gano si la suma de los mismos es igual a 7.

Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio entre 1 y 6. 
Como la generacion de valores aleatorios es un tema muy frecuente la biblioteca standar de Python incluye 
un modulo que nos resuelve la generacion de valores aleatorios.
"""

import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dado:",dado2)
suma=dado1+dado2
if suma ==7:
    print("Ganaste")
else:
    print("Perdiste")