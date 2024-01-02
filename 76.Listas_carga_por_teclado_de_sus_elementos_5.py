"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 
4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados 
agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

mañanasueldos=[]
print("Mañana")
for x in range(4):
    valor=int(input("Ingrese el valor del sueldo: "))
    mañanasueldos.append(valor)
tardesueldos=[]
print("Tarde")
for x in range(4):
    valor=int(input("Ingrese el valor del sueldo: "))
    tardesueldos.append(valor)
print("Los sueldos de la mañana son: ")
print(mañanasueldos)
print("Los sueldos de la tarde son: ")
print(tardesueldos)


