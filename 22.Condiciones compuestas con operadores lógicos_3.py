# Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha
# corresponde a Navidad

dia= int(input("Ingrese el dia: "))
mes= int(input("Ingrese el mes: "))
año= int(input("Ingrese el año: "))

if dia == 25 and mes == 12:
    print('Dia:',dia, 'Mes:',mes, 'Año:',año)
    print("Es Navidad")
else:
    print("La fecha ingresada es: ")
    print('Dia:',dia, 'Mes:',mes, 'Año:',año)