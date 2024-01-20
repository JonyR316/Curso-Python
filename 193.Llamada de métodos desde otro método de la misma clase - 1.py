"""
Plantear una clase Operaciones que solicite en el metodo __init__ la carga de dos enteros e 
inmediatamente muestre su suma, resta, multiplicacion y division. Hacer cada operacion en otro 
metodo de la clase Operacion y llamarlos desde el mismo metodo __init__.
"""

class Operaciones:

    def __init__(self):
        self.valor1=int(input("Ingrese el primer numero: "))
        self.valor2=int(input("Ingrese el segundo numero: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        suma=self.valor1+self.valor2
        print("La suma es:",suma)

    def resta(self):
        resta=self.valor1-self.valor2
        print("El resultado de la resta es:",resta)

    def multiplicacion(self):
        multiplicacion=self.valor1*self.valor2
        print("El resultado de la multiplicacion es:",multiplicacion)

    def division(self):
        division=self.valor1/self.valor2
        print("El resultado de la division es:",division)


operacion1=Operaciones()
