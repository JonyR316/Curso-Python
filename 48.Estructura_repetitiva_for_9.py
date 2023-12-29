# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar
# del mismo (Los primeros 12 terminos)
# Ejemplo: Si ingreso 3 debera aparecer en pantalla los valores 3, 6, 9, hasta el 36.


valor=int(input("Ingrese el numero de la tabla: "))

for x in range(1,13):
    tabla= valor * x
    print(tabla)
