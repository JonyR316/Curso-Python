"""
Definir una funcion que cargue una lista con palabras y la retorne.
Luego otra funcion tiene que mostrar todas las palabras de la lista que tienen mas de 5 caracteres.
"""
def cargar_palabras():
    palabras=[]
    cantidad=int(input("Ingrese el numero de palabras: "))
    for x in range(cantidad):
        palabra=input("Ingrese la palabra: ")
        palabras.append(palabra)
    return palabras
    


def mascaracteres(palabras):
    print("Palabras con mas de 5 caracteres: ")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra) 

palabras=cargar_palabras()
mascaracteres(palabras)