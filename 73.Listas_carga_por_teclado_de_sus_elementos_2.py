"""
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros 
al ingresar el cero. Mostrar finalmente el tamaño de la lista y el contenido de la lista.
"""

lista=[]
valor=int(input("Ingresar un valor (Digite 0 si desea finalizar): "))

while valor != 0:
    lista.append(valor)
    valor=int(input("Ingresar un valor (Digite 0 si desea finalizar): "))
print("Tamaño de la lista:")
print(len(lista))
print("Contenido de la lista: ")
print(lista)
