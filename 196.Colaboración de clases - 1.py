"""
Un banco tiene 3 clientes que pueden hacer depositos y extracciones. Tambien el banco requiere 
que al final del dia calcule la cantidad de dinero que hay depositado.

Lo primero que hacemos es identificar la clases.

Podemos identificar la clase Cliente y la clase Banco.

Luego debemos definir los atributos y los metodos de cada clase:
"""

class Cliente:

    def __init__(self, nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self, monto):
        self.monto=self.monto+monto
    
    def extraer(self, monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto
    
    def  imprimir(self):
        print(self.nombre,"tiene depsitado la suma de:",self.monto)


class Banco:

    def __init__(self):
        self.cliente1=Cliente("Jonathan")
        self.cliente2=Cliente("Belen")
        self.cliente3=Cliente("Jefferson")

    def operar(self):
        self.cliente1.depositar(66)
        self.cliente2.depositar(99)
        self.cliente3.depositar(33)
        self.cliente3.extraer(3)
        self.cliente2.extraer(9)
        self.cliente1.extraer(6)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("Total de dinero en el banco:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


banco1=Banco()
banco1.operar()
banco1.depositos_totales()