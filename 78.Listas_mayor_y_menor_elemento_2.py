"""
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor
valor de la lista y la posicion donde se encuentra. 
"""

lista=[]

for x in range(5):
    valor= int(input("Ingrese el valor: "))
    lista.append(valor)
menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]< menor:
        menor=lista[x]
        posicion=x
print("lista de valores")
print(lista)
print("El valor menor es:")
print(menor)
print("Su posicion es: ")
print(posicion)