"""
Crear un diccionario en Python que defina como clave el numero de documento de una persona y 
como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su numero de documento.
"""

def cargar():
    diccionario={}
    for x in range(4):
        cedula=int(input("Ingrese el numero de cedula: "))
        nombre=input("Ingrese el nombre: ")
        diccionario[cedula]=nombre
    return diccionario

def imprimir_productos(diccionario):
    print("Listado de personas con sus cedulas")
    for cedula in diccionario:
        print(cedula, diccionario[cedula])

def consulta_nombre(diccionario):
    numero=int(input("Ingrese el numero a ser consultado : "))
    if numero in diccionario:
        print("El nombre de la persona es",diccionario[numero])
    else:
        print("No esta la persona de dicho numero")


diccionario=cargar()
imprimir_productos(diccionario)
consulta_nombre(diccionario)
