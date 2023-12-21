# Realizar un programa que permita cargar dos listas de 15 valores cada una.
# Informar con un mensaje cual de las dos listas tiene un valor acumlado mayor (mensajes "Lista 1 mayor", 
# "Lista 2 mayor", "Listas iguales")
# Tener en cuenta que puede haber dos o mas estructuras repetitivas en un algoritmo.

suma1= 0
suma2= 0
x=1

print("Ingrese los valores de la Primera Lista")
while x <= 15:
    valor= int(input("Ingrese el valor: "))
    suma1= suma1 + valor
    x = x + 1
print("El valor total es: ")
print(suma1)
x=1   
print("Ingrese los valores de la Segunda Lista")
while x <= 15:
    valor= int(input("Ingrese el valor: "))
    suma2= suma2 + valor
    x = x + 1
print("El valor total es: ")
print(suma2)
if suma1>suma2:
    print("Lista 1 Mayor")
else:
    if suma2 > suma1:
        print("Lista 2 Mayor")
    else:
        print("Listas iguales")