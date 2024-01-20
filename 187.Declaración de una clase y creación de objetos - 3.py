"""
Confeccionar una clase que permita cargar el nombre y la edad de una persona. Mostrar los datos 
cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    def inicializar(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

    def mostrar_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")


persona1=Persona()
persona1.inicializar("Jonathan", 32)
persona1.imprimir()
persona1.mostrar_edad()

persona2=Persona()
persona2.inicializar("Belen", 14)
persona2.imprimir()
persona2.mostrar_edad()
