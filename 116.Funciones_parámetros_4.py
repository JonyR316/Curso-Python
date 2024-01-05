"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
llamarla desde el bloque principal del programa 3 veces con string distintos.
"""

def contar_vocales(cadena):
    contador=0
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u":
            contador = contador + 1
    print("Cantidad de vocales de la palabra:",cadena,"es",contador)

for x in range(3):
    cadena=input("Ingresar la palabra: ")
    contar_vocales(cadena)