# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuantos tienen
# notas mayores o iguales a 7 y cuantos menores.

aprobado=0
reprobado=0

for x in range(10):
    nota=int(input("Ingresar valor: "))
    if nota >= 7:
        aprobado=aprobado+1
    else:
        reprobado=reprobado+1

print("Aprobados: ")
print(aprobado)
print("Reprobados: ")
print(reprobado)