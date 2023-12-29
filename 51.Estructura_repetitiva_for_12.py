"""Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
A) La cantidad de valores ingresados negativos.
B) La cantidad de valores ingresados positivos.
C) La cantidad de multiplos de 15.
D) El valor acumulado de los numeros ingresados que son pares."""


contador1=0
contador2=0
contador3=0
contador4=0


for x in range(10):
    valor=int(input("Ingrese el valor: "))
    if valor >= 0:
        contador1= contador1 + 1
    else:
        if valor < 0:
            contador2= contador2 + 1
    if valor % 15 == 0:
        contador3= contador3+1
    if valor % 2 ==0:
        contador4 = contador4 + valor
print("La cantidad de valores ingresados positivos")
print(contador1)
print("La cantidad de valores ingresados negativos") 
print(contador2)
print("La cantidad de multiplos de 15")
print(contador3)
print("El valor acumulado de los numeros ingresados que son pares")
print(contador4)