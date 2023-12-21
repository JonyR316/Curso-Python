# Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.

horas_trabajadas= int(input("Ingrese el numero de horas: "))
valor_hora= int(input("Ingrese el valor por hora: "))


sueldo = horas_trabajadas* valor_hora
print("El sueldo mensual es: ")
print(sueldo)


#--------------------------------------#

#Calcular el sueldo mensual de un operario conociendo la cantidad de horas diarias trabajadas y el valor por hora.

horas_trabajadas= int(input("Ingrese el numero de horas: "))
valor_hora= int(input("Ingrese el valor por hora: "))

horas_trabajadas= horas_trabajadas*20
print("horas trabajadas en un mes son: ")
print(horas_trabajadas)
sueldo= horas_trabajadas*valor_hora
print("El sueldo mensual es: ")
print(sueldo)