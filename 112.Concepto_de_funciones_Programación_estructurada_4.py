"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque
principal del programa llamar a 2 veces a dicha funcion (sin utilizar una estructura repetitiva)
"""

def numero_menor():
    valor1=int(input("Ingrese el valor: "))
    valor2=int(input("Ingrese el valor: "))
    valor3=int(input("Ingrese el valor: "))
    if valor1<valor2 and valor1<valor3:
        print("El numero menor es:",valor1)
    else:
        if valor2<valor3:
            print("El numero menor es:",valor2)
        else:
            print("El numero menor es:",valor3)

numero_menor()
numero_menor()