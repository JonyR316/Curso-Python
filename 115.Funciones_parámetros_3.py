"""
Desarrollar un programa que me permita ingresar el lado de un cuadrado. Luego preguntar si quiere 
calcular y mostrar su perimetro o su superficie.
"""
def calcular_superficie(lado):
    superficie=lado*lado
    print("La superficie es:", superficie)

def calcular_perimetro(lado):
    area=lado*4
    print("El area es:", area)

def cargar():
    lado=int(input("Ingrese el valor del lado: "))
    respuesta=input("Desea calcular perimetro o superficie: ")
    if respuesta == "superficie":
        calcular_superficie(lado)
    if respuesta == "perimetro":
        calcular_perimetro(lado)

cargar()
