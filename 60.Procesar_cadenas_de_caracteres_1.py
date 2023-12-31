"""
Solicitar la carga del nombre de una persona en minusculas. Mostrarun mensaje si comienza con
vocal dicho nombre
"""

nombre= input("Ingrese un nombre: ")

if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print(nombre)
    print("Tu nombre empieza con vocal")
else:
    print("Tu nombre no empieza en vocal")