"""
Solicitar por teclado la cantidad de mepleados que tiene la empresa. Crear y cargar una lista con
todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenados de menor a mayor.
"""
n=int(input("Ingrese la cantidad de empleados: "))
sueldos=[]

for x in range(n):
    sueldo=int(input("Ingresar el valor del sueldo: "))
    sueldos.append(sueldo)
for x in range(n-1):
    for x in range(n-1):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
print("Lista de sueldos ordenados de menor a mayor")
print(sueldos)