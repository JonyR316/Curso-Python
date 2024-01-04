"""
Se tiene que cargar la siguiente informacion:
- Nombres de 3 empleados
- Ingresos en concepto de sueldo, cobrado por cada empleado, en los ultimos 3 meses
Confeccionar el programa para:

A) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
B) Generar una lista que contenga el ingreso acumulado en sueldos en los ultimos 3 meses para cada empleado.
C) Mostrar por pantalla el total pagado en sueldos a cada empleado en los ultimos 3 meses.
D) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado.
"""

empleados=[]
sueldos=[]
sueldostotal=[]
for x in range(3):
    empleado=input("Ingrese el nombre del empleado: ")
    empleados.append(empleado)
    sueldo1=int(input("Ingrese la sueldo 1: "))
    sueldo2=int(input("Ingrese la sueldo 2: "))
    sueldo3=int(input("Ingrese la sueldo 3: "))
    sueldos.append([sueldo1,sueldo2,sueldo3])

print("Empleados y sus 3 sueldos")
for x in range(3):
    print(empleados[x], sueldos[x][0], sueldos[x][1], sueldos[x][2])

print("Sueldos total de cada empleado")
for x in range(3):
    total= sueldos[x][0]+ sueldos[x][1]+ sueldos[x][2]
    sueldostotal.append(total)
for x in range(3):
    print(empleados[x],sueldostotal[x])
    



posmayor=0
mayor=sueldostotal[0];
for x in range(1,3):
    if sueldostotal[x]>mayor:
        mayor=sueldostotal[x]
        posmayor=x
print("Empleado con mayor valor acumulado")
print(empleados[posmayor])
print("Con un ingreso", mayor)