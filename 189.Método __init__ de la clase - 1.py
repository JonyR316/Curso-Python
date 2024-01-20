"""
Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo. 
En el metodo __init__ cargar los atributos por teclado y luego en otro metodo imprimir sus datos y 
por ultimo uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)
"""

class Empleado:

    def __init__(self):
        self.nombre=input("Ingresar el nombre: ")
        self.sueldo=int(input("Ingrese el sueldo: "))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def mensaje(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

empleado1=Empleado()
empleado1.imprimir()
empleado1.mensaje()