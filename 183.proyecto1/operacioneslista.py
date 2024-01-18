def cargar():
    lista=[]
    for x in range(5):
        valor=int(input("Ingresar un numero: "))
        lista.append(valor)
    return lista

def imprimir_mayor(lista):
    mayor=lista[0]
    for x in range(1,5):
        if lista[x]>mayor:
            mayor=lista[x]
    print("El mayor valor de la lista es:",mayor)

def imprimir_suma(lista):
    suma=0
    for elemento in lista:
        suma = suma + elemento
    print("La suma es:",suma) 