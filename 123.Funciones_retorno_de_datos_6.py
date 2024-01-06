"""
Confeccionar una funcion que calcule la superficie de un rectangulo y la retorne, la funcion recibe
como parametros los valores de dos de sus lados:

En el bloque principal del programa cargar los lados de dos de rectangulos y luego mostrar cual de los 
dos tiene una superficie mayor.contador=contador+1
"""

def retornar_superficie(lado1,lado2):
    superficie = lado1 * lado2
    return superficie
        
print("Primer Rectangulo")  
lado1=int(input("Ingresar el valor del lado: "))
lado2=int(input("Ingresar el valor del lado: "))
print("segundo Rectangulo")  
lado3=int(input("Ingresar el valor del lado: "))
lado4=int(input("Ingresar el valor del lado: "))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los rectangulos son iguales")
else:
    if retornar_superficie(lado1,lado2) > retornar_superficie(lado3,lado4):
        print("la superficie del primer rectangulo es mayor midiendo:",retornar_superficie(lado1,lado2))
    else:
        print("la superficie del segundo rectangulo es mayor midiendo:",retornar_superficie(lado3,lado4))