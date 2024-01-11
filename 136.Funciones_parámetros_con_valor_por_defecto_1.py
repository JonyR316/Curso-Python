"""
Confeccionar una funcion que reciba un string como parametros y en forma opcional un segundo 
string con un caracter. La funcion debe mostrar el string subrayado con el caracter que indica el 
segundo parametro.
"""

def titulo_subrayado(titulo, caracter="*"):
    print(titulo)
    print(caracter*len(titulo))

titulo_subrayado("Sistema de administracion")
titulo_subrayado("Ingenieria en Sistemas", "_")
titulo_subrayado("Hola Mundo","-")
titulo_subrayado("Sistema Ventas","x")
