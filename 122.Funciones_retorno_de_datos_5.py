"""
Elaborar una funcion que nos retorne el perimetro de un cuadrado pasando como parametros el valor 
de un lado.
"""
def retornar_perimetro(lado):
    perimetro= lado*4
    return perimetro

lado=int(input("Ingrese el valor del lado: "))
perimetro=retornar_perimetro(lado)
print("El perimetro del cuadrado es:",perimetro)