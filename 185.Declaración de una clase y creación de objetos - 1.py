"""
Implementaremos una clase llamada Persona que tendra como atributo(variable) su nombre y dos metodos 
(funciones), uno de dichos metodos inicializara el atributo nombre y el siguiente metodo 
mostrara en la pantalla el contenido del mismo.

Definir dos objetos de la clase Persona.
"""

class Persona:

    def inicializar(self, nom):
        self.nombre=nom
    
    def imprimir(self):
        print("Nombre:",self.nombre)


persona1=Persona()
persona1.inicializar("Jonathan")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Belen")
persona2.imprimir()