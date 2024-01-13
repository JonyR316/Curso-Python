"""
Desarrollar una funcion que solicite la carga del dia, mes, y año y almacene dichos datos en una tupla 
que luego debe retornar. la segunda funcion a implementar debe recibir una tupla con la fecha y mostrarla 
por pantalla.
"""

def cargar_fecha():
    dia=int(input("Ingrese el dia: "))
    mes=int(input("Ingese el mes: "))
    año=int(input("Ingese el año: "))
    return (dia, mes,año)

def imprimir(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")
    

fecha=cargar_fecha()
imprimir(fecha)

lista=list(fecha) # La funcion "list" convierte una tupla en lista
lista[0]=2 # modifico la fecha
print(lista)

tupla2=tuple(lista) # de lista a Tupla, con la funcion "tuple"
print(tupla2)