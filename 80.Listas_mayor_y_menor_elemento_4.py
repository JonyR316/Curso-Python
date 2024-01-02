"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la 
lista (es decir si dicho valor se encuentra en 2 o mas posiciones en la lista).
"""

lista=[]

for x in range(5):
    valor=int(input("Ingrese el valor: "))
    lista.append(valor)
mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
       mayor= lista[x]
print("Lista de todos los valores:")
print(lista)
print("Valor mayor: ")
print(mayor)
contador=0
for x in range(5):
    if lista[x]==mayor:
        contador = contador + 1
if contador>1:
    print("El valor mayor se encuntra repetido en la lista")
