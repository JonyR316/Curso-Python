# Se carga una fecha (dia, mes, año). Mostrar un mensaje si corresponde al primer trimestre del año
# (enero, febrero, marzo) Cargar por teclado el valor numerico del dia, mes, año.
# Ejemplo: dia:10 mes:2 año:2023

dia= int(input("Ingrese el dia: "))
mes= int(input("Ingrese el mes: "))
año= int(input("Ingrese el año: "))

print("La fecha ingresada es: ")

if mes == 1 or mes == 2 or mes == 3:
    print('Dia:',dia, 'Mes:',mes, 'Año:',año)
    print("Comprende al primer trimestre")
else:
    print("La fecha no pertenece al primer trimestres")