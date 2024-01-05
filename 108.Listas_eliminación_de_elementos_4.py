"""
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y 
generar una nueva lista con dichos valores.
"""

lista=[]

for x in range(5):
    valor=int(input("Ingrese el valor: "))
    lista.append(valor)
print("Lista original")    
print(lista)
print("---------------------------------")

lista2=[]
posicion=0
while posicion<len(lista):
    if lista[posicion]>=10:
        lista2.append(lista.pop(posicion))
    else:
        posicion=posicion+1
print("Lista con elementos borrados")
print(lista)

print("---------------------------------")
print("Lista con valores iguales o mayores a 10")
print(lista2)