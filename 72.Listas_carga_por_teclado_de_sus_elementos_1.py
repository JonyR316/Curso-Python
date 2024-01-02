"""
Definir una lista y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista.
Imprimir la lista generada.
"""
lista=[]

for x in range(5):
    valor=int(input("Ingresar un valor: "))
    lista.append(valor)
print(lista)
print("Elementos en lista: ")
print(len(lista))