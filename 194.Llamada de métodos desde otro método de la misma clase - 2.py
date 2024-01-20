"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menu de 
opciones que permita:
1) Cargar alumnos.
2) Listar alumnos.
3) Mostrar alumnos con notas mayores o iguales a 7.
4) Finalizar programa.
"""

class Alumnos:
    
    def __init__(self):
        self.nombres=[]
        self.notas=[]

    def menu(self):
        opcion=0
        while opcion != 4:
            print("1.- Carga de alumnos")
            print("2.- Listar alumnos")
            print("3.- Mostrar alumnos con notas mayores o iguales a 7")
            print("4.- Finalizar programa")
            opcion=int(input("Ingrese su opcion:"))
            if opcion == 1:
                self.cargar()
            else:
                if opcion == 2:
                    self.listar()
                else:
                    if opcion == 3:
                        self.notas_altas()
                    
    def cargar(self):
        for x in range(5):
            nombre=input("Ingrese el nombre: ")
            self.nombres.append(nombre)
            nota=int(input("Ingrese la nota: ")) 
            self.notas.append(nota)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def listar(self):
        print("Listado Completo de Alumnos")
        for x in range(5):
            print(self.nombres[x], self.notas[x])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def notas_altas(self):
        print("Listado de Alumnos con notas iguales o superiores a 7")
        for x in range(5):
            if self.notas[x] >= 7:
                print(self.nombres[x], self.notas[x])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

alumnos1=Alumnos()
alumnos1.menu()