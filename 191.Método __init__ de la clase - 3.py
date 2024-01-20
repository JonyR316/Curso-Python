"""
Desarrollar una clase que represente un Cuadrado y tenga los siguientes metodos: inicializar el valor 
del lado llegando como parametro al metodo __init__ (definir un atributo llamado lado), imprimir 
su perimetro y su superficie.
"""

class Cuadrado:

    def __init__(self,lado):
        self.lado=lado

    def perimetro(self):
        perimetro=self.lado*4
        print("El perimetro del cuadrado es:",perimetro)

    def superficie(self):
        superficie=self.lado*self.lado
        print("La superficie del cuadrado es:",superficie)
        

cuadrado1=Cuadrado(6)
cuadrado1.perimetro()
cuadrado1.superficie()


print("----------------Otra respuesta------------------------")

class Cuadrado:

    def __init__(self,lado):
        self.lado=lado

    def imprimir(self):
        print("Lado:",self.lado)

    def perimetro_superficie(self):
        perimetro=self.lado*4
        print("El perimetro es:",perimetro)
        superficie=self.lado*self.lado
        print("La superficie es:",superficie)

cuadrado1=Cuadrado(6)
cuadrado1.imprimir()
cuadrado1.perimetro_superficie()