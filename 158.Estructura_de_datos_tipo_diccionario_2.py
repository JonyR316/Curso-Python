"""
Crear un diccionario que permita almacenar 5 articulos, utilizar como clave el nombre de productos
y como valor el precio del mismo.
Desarrolar ademas las funciones de:
1) Imprimir en forma completa el diccionario.
2) Imprimir solo los articulos con precio superior a 100.
"""

def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingresar el producto: ")
        valor=int(input("Ingrese el valor: "))
        productos[nombre]=valor
    return productos

def imprimir_productos(productos):
    print("Listado de todos los productos")
    for nombre in productos:
        print(nombre, productos[nombre])

def precio_superior(productos):
    print("Productos con precio superior a 100")
    for nombre in productos:
        if productos[nombre] > 100:
            print(nombre)


productos=cargar()
imprimir_productos(productos)
precio_superior(productos)