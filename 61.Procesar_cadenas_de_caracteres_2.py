"""
Ingresar un mail por teclado.Verificar si el string ingresado contiene solo un caracter "@".
"""

correo= input("Ingresar un email :")
cantidad=0
x=0

while x <len(correo):
    if correo[x]=="@":
        cantidad=cantidad+1
    x= x+1
if cantidad==1:
    print("Contiene un caracter @ el correo ingresado")
else:
    print("No contiene un caracter @ en el correo ingresado")