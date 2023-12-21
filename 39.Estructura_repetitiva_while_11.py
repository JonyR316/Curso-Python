# Desarrollar un programa que permita cargar n numeros enteros y luego nos informe cuantos valores
# fueron pares y cuantos impares.
# Emplear el operador "%" en la condicion de la estructura condicional(Este operador retorna el resto
# de la division de dos valores, por ejemplo 11%2 retorna un 1 )

pares= 0
impares= 0
x= 1
n=int(input("Ingrese la cantidad de numeros : "))

while x <= n:
    valor=int(input("Ingrese el valor: "))
    if valor%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x + 1
print("Cantidad de pares: ")
print(pares)
print("Cantidad de pares: ")
print(impares)
