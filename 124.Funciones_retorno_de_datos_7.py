"""
Plantear una funcion que recibe un string en mayusculas o minusculas 
y retorne la cantidad de letras "a" o "A".
"""

def retornar_vocales(cadena):
    contador=0
    for x in range(len(cadena)):
        if cadena[x] == "a" or cadena[x] == "e" or cadena[x] == "i" or cadena[x] == "o" or cadena[x] == "u" or cadena[x] == "A" or cadena[x] == "E" or cadena[x] == "I" or cadena[x] == "O" or cadena[x] == "U": 
            contador = contador + 1
    return contador

cadena=input("Ingrese la palabra: ")
contador=retornar_vocales(cadena)
print("La cantidad de vocales es:",contador)

print("--------------Otra Opcion-------------------")

def cantidad_vocales_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=="a" or palabra[x]=="A":
            cant=cant+1
    return cant

palabra=input("Ingrese la palabra: ")
print("La palabra",palabra, "tiene",cantidad_vocales_a(palabra),"a")