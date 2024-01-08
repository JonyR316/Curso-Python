"""
Confeccionar una funcion que cargue por teclado una lista de 5 enteros y la retorne. Una segunda 
funcion debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal 
del programa llamar a ambas funciones.
"""

def cargar_enteros():
    lista=[]
    for x in range(5):
        valor=int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista

def imprimir_mayores10(lista):
    print("Elementos de lista mayores a 10")
    for x in range(len(lista)):
        if lista[x]>10:
            print(lista[x])



lista2=cargar_enteros()
imprimir_mayores10(lista2)