"""
Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades 
la carga por teclado y su impresion.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus metodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agrege un atributo 
sueldo y muestre si debe pagar impuestos(sueldo superior a 3000)
Tambien en el bloque principal del programa crear un objeto de la clase Empleado.
"""

class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=int(input("Ingrese el sueldo: "))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(self.nombre,"Debe pagar impuestos")
        else:
            print(self.nombre,"No debe pagar impuestos")

empleado1=Empleado()
empleado1.imprimir()
empleado1.pagar_impuestos()