"""
Confeccionar una funcion que reciba una serie de edades y me retorne la cantidad que son mayores o iguales 
a 18 (como minimo se envia un entero a la funcion.)
"""
def mayor_edad(edad, *edades):
    contador=0
    if edad>=18:
        contador=contador+1
    for x in range(len(edades)):
        if edades[x]>=18:
            contador=contador+1
    return contador

print("Cantidad de personas mayores a 18 años son:", mayor_edad(16,17,18,19,20,21,22,23,24,25,26))