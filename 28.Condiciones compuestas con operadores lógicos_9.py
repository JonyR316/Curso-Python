# Escribir un programa en el cual : dada una lista de tres valores numericos distintos se calcule
# e informe su rango de variacion ( debe mostrar el mayor y el menor de ellos )

valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))
valor3= int(input("Ingrese el tercer valor: "))

if valor1 <  valor2 and valor1 < valor3:
    print("Este es el numero menor: ")
    print(valor1)
else:
    if valor2 < valor3:
        print("Este es el numero menor: ")
        print(valor2)
    else:
        print("Este es el numero menor: ")
        print(valor3)
if valor1 >  valor2 and valor1 > valor3:
    print("Este es el numero mayor: ")
    print(valor1)
else:
    if valor2 > valor3:
        print("Este es el numero mayor: ")
        print(valor2)
    else:
        print("Este es el numero mayor: ")
        print(valor3)
print("Fin")