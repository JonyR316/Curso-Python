"""
Desarrollar una aplicacion que nos permita crear un diccionario ingles/castellano. La clave es la 
palabra en ingles y el valor es la palabra en castellano.
Crearlas siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traduccion.
"""

def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        ingles=input("Ingrese la palabra en ingles: ")
        castellano=input("Ingrese la palabra en castellano: ")
        diccionario[ingles]=castellano
        continua=input("Quiere cargar otra palabra [s/n] ?: ")
    return diccionario

def imprimir_productos(diccionario):
    print("Listado de palabras de diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

def consulta_palabara(diccionario):
    palabra=input("Ingrese la palabra en ingles a consultar: ")
    if palabra in diccionario:
        print("En castellano significa",diccionario[palabra])
    else:
        print("No esta la traduccion de dicha palabra")


diccionario=cargar()
imprimir_productos(diccionario)
consulta_palabara(diccionario)