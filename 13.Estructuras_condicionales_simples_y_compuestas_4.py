# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar
# un mensaje "Aprobado"

not1= int(input("Ingrese la primera nota: "))
not2= int(input("Ingrese la segunda nota: "))
not3= int(input("Ingrese la tercer nota: "))

promedio= (not1+not2+not3)/3
print("El promedio es:")
print(promedio)

if promedio >= 7:
    print("Aprobado")
else:
    print("Reprobado")
print("Fin")