"""
Realizar la carga de dos nombres de personas distintas. Mostrar por pantalla luego ordenados en orden 
alfabetica.
"""

nombre1=input("Ingrese el nombre: ")
nombre2=input("Ingrese el nombre: ")

print("Lista en Orden Alfabetico")
if nombre1 < nombre2:
        print(nombre1)
        print(nombre2)
else:
    print(nombre2)
    print(nombre1)