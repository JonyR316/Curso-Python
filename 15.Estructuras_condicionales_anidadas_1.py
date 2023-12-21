# Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio
# e imprima alguno de estos mensajes:
# Si el promedio es >= 7 mostrar "Aprobado".
# Si el promedio es >= 4 y < 7 mostrar "Regular".
# Si el promedio es < 4 mostrar "Reprobado".

nota1= int(input("Ingrese la primera nota: "))
nota2= int(input("Ingrese la segunda nota: "))
nota3= int(input("Ingrese la tercer nota: "))

promedio= (nota1+nota2+nota3)/3
print("Su promedio es: ")
print(promedio)

if promedio >=7:
    print("Aprobado")
else:
    if promedio >=4:
        print("Regular")
    else:
        print("Reprobado")
print("Fin")
