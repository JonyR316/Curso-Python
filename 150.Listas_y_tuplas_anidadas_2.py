"""
Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes. 
Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar 
el nombre del pais con mayor cantidad de habitantes.
"""

def cargar_paispoblacion():
    paises=[]
    for x in range(5):
        pais=input("Ingrese el nombre del pais: ")
        cantidad=int(input("Ingrese la cantidad de habitantes: "))
        paises.append((pais,cantidad))
    return paises


def imprimir_paises(paises):
    print("Listado de paises y habitantes")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])


def mayor_habitantes(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("El pais con mayor poblacion es :",paises[pos][0],"con",paises[pos][1],"habitantes")

paises=cargar_paispoblacion()
imprimir_paises(paises)
mayor_habitantes(paises)