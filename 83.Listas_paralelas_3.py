"""
En un curso de 4 alumnos se registraron las notas de sus examenes y se deben procesar de acuerdo a lo 
siguiente:
A) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)

B) Realizar un listado que muestre los nombres, notas y condicion de alunmo.
En la condicion, colocar "Muy Bueno" si la nota es mayor o igual a 8. 
"Bueno" si la nota esta entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.

C) Imprimir cuantos alumnos tienen la leyenda "Muy Bueno"
"""

nombres=[]
notas=[]

for x in range(4):
    nombre=input("Ingrese el nombre del alunmo: ")
    nombres.append(nombre)
    nota=int(input("Ingresar la nota: "))
    notas.append(nota)
cantidad=0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x]>=8:
        cantidad=cantidad+1
        print("Muy bueno")
    else:
        if notas[x] >=4:
            print("Bueno")
        else:
            print("Insuficiente")
print("Cantidad de alumnos con Muy bueno")
print(cantidad)
            

