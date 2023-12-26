# Escribir un problema que lea 10 numeros enteros y luego muestre cuantos valores ingresados fueron
# multiplos de 3 y cuantos de 5. Debemos tener en cuenta que hay numeros que son multiplos de 3 y
# de 5 a la vez.

mul3=0
mul5=0

for x in range(10):
    valor=int(input("Ingresar valor: "))
    if valor %3 == 0:
        mul3=mul3+1
    if valor%5 == 0:
        mul5=mul5+1

print("Cantidad de numeros multiplo de 3 : ")
print(mul3)
print("Cantidad de numeros multiplo de 5 : ")
print(mul5)