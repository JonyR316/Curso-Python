# Se cargan por teclado tres numeros distintos. Mostar por pantalla el mayor de ellos

num1= int(input("Ingresar el primer numero: "))
num2= int(input("Ingresar el segundo numero: "))
num3= int(input("Ingresar el tercer numero: "))

print("El numero mayor es: ")

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
print("fin")


#-----------------------------#

if num1 > num2 and num3:
        print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
print("fin")


#-----------------------------#

print("El numero mayor es: ")

if num1 > num2 and num3:
        print(num1)
else:
    if num2 > num3 and num1:
        print(num2)
    else:
        print(num3)
print("fin")