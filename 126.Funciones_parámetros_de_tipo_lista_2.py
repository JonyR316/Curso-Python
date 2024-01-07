"""
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implemewntar
una funcion que imprima el mayor y el menor valor de la lista.
"""

def mayormenor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    print("El numero mayor es:",mayor)
    print("El numero menor es:",menor)

lista=[]
for x in range(5):
    valor=int(input("Ingrese el valor: "))
    lista.append(valor)
mayormenor(lista)


print("---------------Otar Solucion----------------")
def cargar_mayor(lista):
    mayor =lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor= lista[x]
    return mayor        

def cargar_menor(lista):
    menor =lista[0]
    for x in range(1,len(lista)):
        if lista[x]<menor:
            menor= lista[x]
    return menor



lista=[]
for x in range(5):
    valor=int(input("ingrese el valor: "))
    lista.append(valor)

print("El numero mayor es:",cargar_mayor(lista))

print("El numero menor es:",cargar_menor(lista))