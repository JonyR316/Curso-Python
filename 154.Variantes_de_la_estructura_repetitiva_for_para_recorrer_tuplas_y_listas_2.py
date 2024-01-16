"""
Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones.
1) Carga de empleados.
2) Impresion de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000.

Si se cargara por teclado seria algo similar a:

empleados = [("juan",2300)("pedro",1200), etc.....]
"""

def cargar_empleados():
    empleados=[]
    for x in range(5):
        empleado=input("Ingrese el nombre: ")
        sueldo=int(input("Ingrese el sueldo: "))
        empleados.append((empleado,sueldo))
    return empleados

def imprimir(empleados):
    print("Lista Completa")
    for empleado,sueldo in empleados:
        print(empleado,sueldo)

def sueldo_mayor(empleados):
    empleado=empleados[0]
    for elemento in empleados:
        if elemento[1]>empleado[1]:
            empleado= elemento
    print("El empleado con mayor sueldo es :",empleados[0][0],"con",empleados[0][1],"dolares")

def mayor_sueldo(empleados):
    contador=0
    for empleado in empleados:
        if empleado[1]<1000:
            contador=contador+1
    print("Personas con sueldo inferior a $1000:", contador)

empleados=cargar_empleados()
imprimir(empleados)
sueldo_mayor(empleados)
mayor_sueldo(empleados)