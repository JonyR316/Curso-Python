"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego 
de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de 
edad (mayores o iguales a 18 años)
"""


nombres=[]
edades=[]

for x in range(5):
    nombre=input("Ingrese el nombre: ")
    nombres.append(nombre)
    edad=int(input("Ingrese la edad: "))
    edades.append(edad)
print("Listados Completos")
print(nombres)
print(edades)
print("listado de personas mayores de edad")
for x in range (5):
    if edades[x]>= 18:
        print(nombres[x])