"""
Definir una clase Cliente que almacene un codigo de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene todos los codigos de 
clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
"""

class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta Suspendido")
        else:
            print("Esta habilitado")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)


cliente1=Cliente(1,"Jonathan")
cliente2=Cliente(2,"Belen")
cliente3=Cliente(3,"Jefferson")
cliente4=Cliente(4,"Xavier")

cliente2.suspender()
cliente3.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)