"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave sera 
su numero de legajo y en su valor almacenar una lista con el nombre, profesion y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su numero de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesion de "analista de sisitemas".
"""
def carga():
    empleados={}
    continua="s"
    while continua == "s":
        legajo=input("Ingrese el numero de legajo: ")
        nombre=input("Ingrese el nombre: ")
        profesion=input("Ingrese la profesion: ")
        sueldo=int(input("Ingrese el sueldo: "))
        empleados[legajo]=[nombre,profesion,sueldo]
        continua=input("Desea ingresar un nuevo empleado [s/n] ?: ")
    return empleados

def imprimir_empleados(empleados):
    print("Lista completa de empleados")
    for legajo in empleados:
        print(legajo,empleados[legajo])

def modificar_telefono(empleados):
    legajo=(input("Ingrese el numero del legajo del empleado a modificar el sueldo: "))
    if legajo in empleados:
        sueldo=int(input("Ingrese el nuevo sueldo: "))
        empleados[legajo][2]=sueldo
    else:
        print("No existe este empleado")

def profesion(empleados):
    print("Listado de empleados con titulo de Analista de Sistemas")
    for legajo in empleados:
        if empleados[legajo][1]== "Analista de Sistemas":
            print(legajo,empleados[legajo][0],empleados[legajo][2])

empleados=carga()
imprimir_empleados(empleados)
modificar_telefono(empleados)
imprimir_empleados(empleados)
profesion(empleados)
