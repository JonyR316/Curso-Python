"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista. 
"""

def cargar():
    lista=[]
    continua="s"
    while continua == "s":
        valor=int(input("Ingrese el valor: "))
        lista.append(valor)
        continua=input("Desea ingresar otro valor [s/n] ?: ")
    return lista

def fijar_cero(lista):
    for x in range(len(lista)):
        if lista[x]<10:
            lista[x]=0


lista=cargar()
print(lista)
fijar_cero(lista)
print(lista)