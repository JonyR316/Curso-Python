"""
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antiguedad en el club (en años). 
En el metodo _init_ de la clase Socio pedir la carga por teclado del nombre y su antiguedad. 
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antiguedad en el club.
"""

class Socio:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.antiguedad=int(input("Ingrese los años de aniguedad: "))

    def imprimir(self):
        print(self.nombre,"tiene una antiguedad de:",self.antiguedad)

    def retornar_antiguedad(self):
        return self.antiguedad
    
class Club:

    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()

    def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if self.socio1.retornar_antiguedad() > self.socio2.retornar_antiguedad() and self.socio1.retornar_antiguedad() > self.socio3.retornar_antiguedad():
            self.socio1.imprimir()
        else:
            if self.socio2.retornar_antiguedad() > self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()

club1=Club()
club1.mayor_antiguedad()