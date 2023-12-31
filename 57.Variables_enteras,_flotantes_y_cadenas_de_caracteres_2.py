"""
Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabeticamente o si
son iguales
"""

nombre1= input("Ingrese nombre: ")
nombre2= input("Ingrese nombre: ")

if nombre1 == nombre2:
    print("Ingreso dos nombres iguales")
else:
    if nombre1 > nombre2:
        print("Es Mayor Alfabeticamente")
        print(nombre1)
    else:
        print("Es Menor Alfabeticamente")
        print(nombre2)