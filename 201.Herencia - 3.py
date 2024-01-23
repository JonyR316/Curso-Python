"""
Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y metodos 
comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un 
plazo de imposicion en dias y a tasa de interes. Hacer que la caja de ahorro no genera intereses. 
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase 
Plazofijo.
"""

class Cuenta:

    def __init__(self, titular, monto):
        self.titular=titular
        self.monto=monto
    
    def imprimir(self):
        print("Titular:", self.titular)
        print("Monto:", self.monto)

class CajaAhorra(Cuenta):

    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()

class PlazoFijo(Cuenta):

    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto)
        self.plazo=plazo
        self.interes=interes

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().imprimir()
        print("plazo en dias:",self.plazo)
        print("Intereses:",self.interes)
        self.ganancia()

    def ganancia(self):
        gan=self.monto*self.interes/100
        print("Monto de intereses:",gan)

cajadeahorro1=CajaAhorra("Jonathan",1600)
cajadeahorro1.imprimir()

plazofijo1=PlazoFijo("Belen" ,6000, 60, 15)
plazofijo1.imprimir()


    