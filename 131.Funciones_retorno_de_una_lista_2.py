"""
Confeccionar una funcion que cargue por teclado una lista de 5 enteros y la retorne. Una segunda
funcion debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque 
principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.
"""

def cargar_enteros():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista

def mayormenor(lista):
    mayor=lista[0]
    menor=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>mayor:
            mayor=lista[x]
        else:
            if lista[x]<menor:
                menor=lista[x]
    return [menor, mayor]

lista2=cargar_enteros()
rango=mayormenor(lista2)
print("El menor elemento en la lista es:", rango[0])
print("El mayor elemento en la lista es:", rango[1])
