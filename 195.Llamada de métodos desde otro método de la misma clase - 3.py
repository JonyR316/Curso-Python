"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la 
persona, telefono y mail.
Debe mostrar un menu con las siguientes opciones:
1) Carga de un contacto en la agenda.
2) Listado Completo de la agenda.
3) Consulta ingresando el nombre de la persona.
4) Modificacion de su telefono y email.
5) Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.contactos={}

    def menu(self):
        opcion=0
        while opcion != 5:
            print("1.- Carga de contacto")
            print("2.- Listado Completo de la agenda")
            print("3.- Consulta de Contacto")
            print("4.- Editar Contacto")
            print("5.- Finalizar programa")
            opcion=int(input("Ingrese su opcion: "))
            if opcion == 1:
                self.cargar()
            else:
                if opcion == 2:
                    self.listar()
                else:
                    if opcion == 3:
                        self.consulta_contacto()
                    else:
                        if opcion == 4:
                         self.editar_contacto()

    def cargar(self):
        continua="s"
        while continua=="s":
            self.nombre=input("Ingrese el nombre: ")
            self.telefono=int(input("Ingrese el numero de telefono: "))
            self.email=input("Ingrese el Email: ")
            self.contactos[self.nombre]=self.telefono,self.email
            continua=input("Quiere cargar otro contacto [s/n] ?: ")
        return self.contactos
    
    def listar(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Listado de todos los Contactos")
        for self.nombre in self.contactos:
            print(self.nombre, self.contactos[self.nombre][0],self.contactos[self.nombre][1])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def consulta_contacto(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        self.nombre=input("Ingrese el nombre de la persona a ser consultado : ")
        if self.nombre in self.contactos:
            print(self.nombre,"su telefono es:",self.contactos[self.nombre][0],"y su email es:",self.contactos[self.nombre][1])
        else:
            print("No existe el contacto")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    def editar_contacto(self):
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        self.nombre=(input("Ingrese el nombre del contacto a ser modificado: "))
        if self.nombre in self.contactos:
            self.telefono=int(input("Ingrese el nuevo nuemero de telefono: "))
            self.email=input("Ingrese el nuevo Email: ")
            self.contactos[self.nombre]=(self.telefono,self.email)
        else:
            print("No existe este contacto")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        
contacto1=Agenda()
contacto1.menu()