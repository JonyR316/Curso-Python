"""
Confeccionar una funcion que le enviemos como parametros dos enteros y nos retorne el mayor.
"""
def mostar_mayor(valor1,valor2):
    if valor1>valor2:
        mayor=valor1
    else:
        mayor=valor2
    return mayor



valor1=int(input("Ingresar el valor: "))
valor2=int(input("Ingresar el valor: "))
print(mostar_mayor(valor1,valor2))

print("------------Otra Solucion----------")

def valor_mayor(valor1,valor2):
    if valor1>valor2:
        return valor1
    else:
        return valor2

valor1=int(input("Ingresar el valor: "))
valor2=int(input("Ingresar el valor: "))
x=valor_mayor(valor1,valor2)
print(x)