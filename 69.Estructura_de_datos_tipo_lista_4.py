"""
Definir por asignacion una lista con 8 elementos enteros. Contar cuantos dichos valores almacenan un valor
superior a 100
"""

lista=[100, 200, 300, 400, 500, 3, 6, 9]
contador=0
x=0

while x < len(lista):
    if lista[x]>= 100:
        contador= contador +1 
    x= x+1
print("La lista contiene los siguientes valores: ")
print(lista)
print("Valores mayores a 100 son: ")
print(contador)