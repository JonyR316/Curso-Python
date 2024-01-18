"""
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la ultima.
3) Imprimir la lista.
"""

def cargar():
    palabras=[]
    for x in range(5):
        palabra=input("Ingrese la palabra: ")
        palabras.append(palabra)
    return palabras

def intercambiar_palabras(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux

def imprimir_palabras(palabras):
    print("Lista de Palabras")
    print(palabras)

palabras=cargar()
imprimir_palabras(palabras)
intercambiar_palabras(palabras)
imprimir_palabras(palabras)