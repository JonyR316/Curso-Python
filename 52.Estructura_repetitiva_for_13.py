"""Se cuenta con la siguiente informacion:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
A) Obtener el promedio de las edades de cada turno (tres promedios)
B) Imprimir dichos promedios (promedio de cada turno)
C) Mostrar por pantalla un mensaje que indique cual de los tres tiene un promedio de edades mayor."""

mañana=0
tarde=0
noche=0

for m in range(5):
    valor=int(input("Ingrese la edad: "))
    mañana=mañana+valor
promedio1= mañana /5
print("El promedio de la mañana es: ")
print(promedio1)
for t in range(6):
    valor=int(input("Ingrese la edad: "))
    tarde=tarde+valor
promedio2= tarde/6
print("El promedio de la tarde es: ")
print(promedio2)
for n in range(11):
    valor=int(input("Ingrese la edad: "))
    noche=noche + valor
promedio3= noche /11
print("El promedio de la noche es: ")
print(promedio3)
if promedio1 > promedio2 and promedio1 >promedio3:
    print("El promedio de edad mayor es la mañana con: ")
    print(promedio1)
else:
    if promedio2 > promedio3:
        print("El promedio de edad mayor es la tarde con: ")
        print(promedio2)
    else:
        print("El promedio de edad mayor es la noche con: ")
        print(promedio3)