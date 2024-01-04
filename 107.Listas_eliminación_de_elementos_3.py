"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos 
de cada empleado.
Ingresar por teclado cuando inicia el programa a la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre).
"""
empleados=[]
sueldos=[]
cantidad=int(input("Cuantos empleados tiene la empresa: "))
for x in range(cantidad):
    nombre=input("Nombre del empleado: ")
    empleados.append(nombre)
    sueldo=int(input("Ingrese el sueldo: "))
    sueldos.append(sueldo)
print("-----------------------------------------")
print("Lista completa de empleados con sueldo")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])
print("-----------------------------------------")
posicion=0
while posicion<len(sueldos):
    if sueldos[posicion]>1000:
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion=posicion+1

print("Listado de sueldos menores a 1000")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])