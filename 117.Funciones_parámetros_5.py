"""
Confeccionar una funcion que reciba tres enteros y los muestre ordenados de menor a mayor. En otra 
funcion solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer funcion definida.
"""

def cargar_enteros(valor1,valor2, valor3):
    if valor1<valor2 and valor2<valor3:
        if valor2<valor3:
            print(valor1,valor2,valor3)
        else:
            print(valor1,valor3,valor2)
    else:
        if valor2<valor3:
            if valor1<valor3:
                print(valor2,valor1,valor3)
            else:
                print(valor2,valor3,valor1)
        else:
            if valor1<valor2:
                print(valor3,valor1,valor2)
            else:
                print(valor3,valor2,valor1)

def cargar():
    valor1=int(input("Ingresar el valor: "))
    valor2=int(input("Ingresar el valor: "))
    valor3=int(input("Ingresar el valor: "))
    cargar_enteros(valor1,valor2,valor3)

cargar()