"""
Desarrollar una funcion que reciba una lista de string y nos retorne el que tiene mas caracteres. Si hay 
mas de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente mas bajo. 
En el bloque principainiciamos por asignacion la lista de string:
palabras=["enero","febero","marzo","abril","mayo","junio"]
"""

def mascaracteres(lista):
    pos=0
    for x in range(1,len(lista)):
        if len(lista[x])>len(lista[pos]):
            pos=x
    return lista[pos]

palabras=["enero","febero","marzo","abril","mayo","junio"]
print(palabras)
print("Palabra con mas caracteres:",mascaracteres(palabras))