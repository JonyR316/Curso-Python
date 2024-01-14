"""
Confeccionar un programa con las siguientes funciones:

1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores.

2) Una funcion que reciba como parametro dos tuplas con los nombres y sueldos de empleados y muestre 
el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la funcion de carga y segidamente llamar a la 
funcion que muestre el nombre de empleado con sueldo mayor.
"""

def cargar_empleado():
    nombre=input("Ingrese el nombre: ")  
    sueldo=int(input("Ingrese el sueldo : "))
    return  [nombre, sueldo]

def mayor_sueldo(empleado1, empleado2):
        if empleado1[1]>empleado2[1]:
            print(empleado1[0], "Tiene el mayor sueldo")
        else:
            print(empleado2[0], "Tiene el mayor sueldo") 

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)