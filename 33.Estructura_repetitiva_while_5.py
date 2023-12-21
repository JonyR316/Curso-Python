# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuantos 
# tienen notas mayores o iguales a 7 y cuantos menores.

x=1
altas=0
bajas=0

while x <= 10:
    nota=int(input("Ingrese la nota: "))
    if nota >= 7:
        altas = altas + 1
    else:
        bajas = bajas + 1
    x = x + 1
print("Numero total de notas altas")
print(altas)
print("Numero total de notas bajas")
print(bajas)