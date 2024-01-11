"""
Confeccionar una funcion que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de 
dichos valores. Debe tener tres parametros por defecto.
"""

def sumar(v1,v2,v3=0,v4=0,v5=0):
    suma=v1+v2+v3+v4+v5
    return suma

print("La suma de 6 + 5 =", sumar(6,5))
print("La suma de 6 + 5 + 4 =", sumar(6,5,4))
print("La suma de 6 + 5 + 4 + 3 =", sumar(6,5,4,3))
print("La suma de 6 + 5 + 4 + 3 + 2 =", sumar(6,5,4,3,2))