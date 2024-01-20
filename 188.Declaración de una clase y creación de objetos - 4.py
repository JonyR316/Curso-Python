"""
Desarrollar un programa que cargue los lados de un triangulo por teclado e implemente los 
siguientes motodos: Inicializar los atributos, imprimir el valor del lado mayor y otro metodo que 
muestre si es equilatero o no. El nombre de la clase llamarla Triangulo.
"""

class Triangulo:

    def inicializar(self):
        self.lado1=int(input("Ingrese el primer lado: "))
        self.lado2=int(input("Ingrese el segundo lado: "))
        self.lado3=int(input("Ingrese el tercer lado: "))

    def imprimir(self):
        print("Lado 1: ",self.lado1)
        print("Lado 2: ",self.lado2)
        print("Lado 3: ",self.lado3)

    def lado_mayor(self):
        print("Lado mayor:")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)
    
    def triangulo_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Equilatero")
        else:
            print("No es equilatero")


triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.triangulo_equilatero()


print("--------------Otra solucion-----------------------------")

class Triangulo:

    def inicializar(self):
        self.lado1=int(input("Ingrese el primer lado: "))
        self.lado2=int(input("Ingrese el segundo lado: "))
        self.lado3=int(input("Ingrese el tercer lado: "))

    def imprimir(self):
        print("Lado 1: ",self.lado1)
        print("Lado 2: ",self.lado2)
        print("Lado 3: ",self.lado3)
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Equilatero")
        else:
            if self.lado1 == self.lado2 and self.lado1 != self.lado3 or self.lado2 == self.lado3 and self.lado2 != self.lado1:
                print("Isosceles")
            else:
                if self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
                    print("Escaleno")

triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.tipo_triangulo()