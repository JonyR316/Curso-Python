"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado 
de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. Llamar 
desde el bloque del programa principal a ambas funciones.
"""

def cuadrado():
    valor1=int(input("Ingrese el valor: "))
    cuadrado= valor1*valor1
    print("El cuadrado del valor es:",cuadrado)

def carga_suma():
    valor1=int(input("Ingrese el valor: "))
    valor2=int(input("Ingrese el valor: "))
    suma= valor1+valor2
    print("El resulatado de la suma es:",suma)


cuadrado()
carga_suma()