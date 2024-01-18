"""
Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con numeros enteros comprendidos entre 0 y 1000.
Mostrar la lista por pantalla.
Luego mezclar los elementos de la lista y volver a mostrarlo.
"""
import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print("Lista de numeros aleatorios")
    print(lista)

def mezclar(lista):
    random.shuffle(lista)


lista=cargar()
imprimir(lista)
mezclar(lista)
imprimir(lista)
