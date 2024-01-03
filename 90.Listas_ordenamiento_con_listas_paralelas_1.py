"""
Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas.
Luego ordenar las notas de mayor a menor.Imprimir las notas y los nombres de los alumnos.
"""

nombres=[]
notas=[]

for x in range(5):
    nombre=input("Ingrese el nombre: ")
    nombres.append(nombre)
    nota=int(input("Ingrese el valor de la nota: "))
    notas.append(nota)
for x in range(4):
    for x in range(4):
        if notas[x]<notas[x+1]:
            aux1=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux1
            aux2=nombres[x]
            nombres[x]=nombres[x+1]
            nombres[x+1]=aux2
print("Lista de notas y los nombres de los alumnos")
for x in range(5):
    print(nombres[x], notas[x])