"""
Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una 
cantidad par de elementos)
3) Imprimir una lista.
"""

def cargar_enteros():
    enteros=[]
    for x in range(10):
        valor=int(input("Ingrese un valor: "))
        enteros.append(valor)
    return enteros

def retornar_mitad(enteros):
    mitad=len(enteros)//2
    return enteros[:mitad]

def imprimir(enteros):
    print("Lista de enteros")
    print(enteros)

enteros= cargar_enteros()
enteros2=retornar_mitad(enteros)
imprimir(enteros)
imprimir(enteros2)