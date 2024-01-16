"""
confeccionar un programa que permita la carga de una lista de 5 enteros por teclado.
Luego en otras funciones:
1) Imprimirla en forma completa.
2) Obtener y mostrar el mayor.
3) Mostrar la suma de todos sus componentes.
Utilizar la nueva sintaxis de for vista en este concepto.
"""

def cargar():
    lista=[]
    for x in range(5):
        numero=int(input("Ingresar el valor: "))
        lista.append(numero)
    return lista

def imprimir(lista):
    print("Lista Completa")
    for elemento in lista:
        print(elemento)

def cargar_mayor(lista):
    mayor =lista[0]
    for elemento in lista:
        if elemento>mayor:
            mayor= elemento
    print("El numero mayor es:",mayor)     

def cargar_suma(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    print("La suma total de todos los valores es:",suma)

lista=cargar()
imprimir(lista)
cargar_mayor(lista)
cargar_suma(lista)