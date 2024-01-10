"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una gardar los valores positivos y en otra los negativos 
3) Imprimir las dos listas generadas.
"""

def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingresar el valor: "))
        lista.append(valor)
    return lista

def generar_lista(lista):
    listanegativa=[]
    listapositiva=[]
    for x in range(len(lista)):
        if lista[x]<0:
            listanegativa.append(lista[x])
        else:
            if lista[x]>0:
                listapositiva.append(lista[x])
    return [listanegativa,listapositiva]

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])

lista=cargar()
listanegativa,listapositiva=generar_lista(lista)
print("Lista con los valores negativos")
imprimir(listanegativa)
print("Lista con los valores positivos")
imprimir(listapositiva)