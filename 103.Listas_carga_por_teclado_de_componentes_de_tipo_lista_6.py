"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los numeros de dias
del mes que el empleado falto.
Imprimir los nombres de empleados y los dias que falto.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos dias. 
"""

empleados=[]
dias=[]

for k in range(3):
    nombre= input("Ingrese el nombre: ")
    empleados.append(nombre)
    cantidad=int(input("Cuantos dias falto: "))
    dias.append([])
    for x in range(cantidad):
      dia=input("Ingrese el dia que falto: ")
      dias[k].append(dia)
print("-----------------------------------------")
print("Listado de nombres de empleados y los dias que falto")
for k in range(3):
   print("Empleado", empleados[k])
   for x in range(len(dias[k])):
      print("Falto", dias[k][x])

print("-----------------------------------------")

print("Nombre del empleado y la cantidad de inasistencias")
for x in range(3):
    print(empleados[x], len(dias[x]))

menor=len(dias[0])
for x in range(1,3):
   if len(dias[x])<menor:
      menor=len(dias[x])

print("-----------------------------------------")

print("Empleados que faltaron menos dias")
for x in range(3):
   if len(dias[x])==menor:
      print(empleados[x])