"""
En el bloque principaldel programa definir un diccionario que almacene los nombres de paises como 
clave y como valor la cantidad de habitantes. Implementar una funcion para mostrar cada clave y valor.
"""

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

paises={"Ecuador":17000000, "Brasil":150000000, "Argentina":900000000, "Colombia":60000000, "Peru":70000000}
imprimir(paises)