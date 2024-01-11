"""
Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma 
en la misma linea.
"""
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingresar el valor entero: "))
        lista.append(valor)
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x],end=",")

lista=cargar()
imprimir(lista)

print("------------------------------------")

print("uno","dos","tres", sep="*")

print("------------------------------------")

print("uno","dos","tres", sep="*", end="*")
print("cuatro","cinco", sep="*")