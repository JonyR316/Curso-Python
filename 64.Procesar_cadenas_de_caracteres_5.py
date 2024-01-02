"""
Ingresar una oracion que pueden tener letras tanto en mayusculas como minusculas. Contar la cantidad
de vocales.
Crear un segundo string con toda la oracion en minusculas para que sea mas facil disponer la condicion que
verifica que es una vocal.
"""

oracion=input("Ingresar la oracion: ")
oracionmin=oracion.lower()
cantidad=0
x=0

while x <len(oracionmin):
    if oracionmin[x]== "a" or oracionmin[x]== "e" or oracionmin[x]== "i" or oracionmin[x]== "o" or oracionmin[x]== "u":
        cantidad= cantidad+1
    x=x+1
print("La cantidad de vocales es: ")
print(cantidad)