"""
Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el metodo 
__init__, calcular su suma, resta, multiplicacion y division, cada una es un metodo, imprimir dichos 
resultados.
"""

class Operaciones:

    def __init__(self):
        self.valor1=int(input("Ingrese el primer numero: "))
        self.valor2=int(input("Ingrese el segundo numero: "))

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
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()