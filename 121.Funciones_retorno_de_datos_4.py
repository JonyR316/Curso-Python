"""
Elaborar una funcion que reciba tres enteros y nos retorne el valor promedio de los mismos.
"""

def calcular_promedio(valor1,valor2,valor3):
    promedio= (valor1+valor2+valor3) / 3
    return promedio

valor1=int(input("Ingrese el valor: "))
valor2=int(input("Ingrese el valor: "))
valor3=int(input("Ingrese el valor: "))
promedio=calcular_promedio(valor1,valor2,valor3)
print("El promedio es:",promedio)