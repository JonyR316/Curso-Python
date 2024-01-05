"""
Confeccionar una funcion que le enviemos como parametro un string y nos retorne la cantidad de caracteres 
que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la funcion dos 
veces. Imprimir en el bloque principal cual de las dos palabras tiene mas caracteres.
"""

def largo(cadena):
    return len(cadena)

nombre1=input("Ingrese el primer nombre: ")
nombre2=input("Ingrese el segundo nombre: ")
largo1=largo(nombre1)
largo2=largo(nombre2)
if largo1 == largo2:
    print("Los nombres tienen la misma cantidad de caracteres")
else:
    if largo1 > largo2:
        print(nombre1,": ""tiene mas caracteres")
    else:
        print(nombre2,": ""tiene mas caracteres")