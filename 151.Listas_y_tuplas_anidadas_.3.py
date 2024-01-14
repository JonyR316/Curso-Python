"""
Almacenar en una lista 5 empleados, cada elemento es una lista con el nombre del empleado junto a sus 
ultimos tres sueldos(estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1) Carga de los nombres de empleados y sus ultimos tres sueldos.
2) Imprimir el monto total cobrado por cada empleado.
3) Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los ultimos tres 
meses.

Tener en cuenta que la estructura de datos si se carga por asignacion deberia ser similar a:

empleados = [["Juan",(2000,3000,4000)],["Ana",(5000,6000,7000)],etc.]
"""

def cargar_empleados():
    empleados=[]
    for x in range(5):
        nombre=input("Ingrese el nombre: ")
        sueldo1=int(input("Ingrese el sueldo: "))
        sueldo2=int(input("Ingrese el sueldo: "))
        sueldo3=int(input("Ingrese el sueldo: "))
        empleados.append([nombre,(sueldo1,sueldo2,sueldo3)])
    return empleados

def imprimir_empleados(empleados):
    print("Listado de Empleados y sus sueldos")
    for x in range(len(empleados)):
        print(empleados[x][0], empleados[x][1])


def monto_total(empleados):
    print("Monto ganado por cada empleado")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(empleados[x][0],total)


def ingreso_superior1000(empleados):
    print("Empleados que tuvieron un ingreso trimestral mayor a 10000")
    for x in range(5):
        total=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if total>10000:
            print(empleados[x][0],total)



empleados=cargar_empleados()
print("-------------------------------------------------")
imprimir_empleados(empleados)
print("-------------------------------------------------")
monto_total(empleados)
print("-------------------------------------------------")
ingreso_superior1000(empleados)
