"""
Confeccionar un programa que permita cargar un codigo de producto como clave en un diccionario.
Guardar para dicha clave una tupla con el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero.
"""

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo: "))
        descripcion=input("Ingrese la descripcion: ")
        precio=float(input("Ingrese el precio: "))
        stock=int(input("Ingrese el stock del producto: "))
        productos[codigo]=descripcion,precio,stock
        continua=input("Quiere cargar otro producto [s/n] ?: ")
    return productos

def imprimir(productos):
    print("Listado de palabras de diccionario")
    for codigo in productos:
        print(codigo, productos[codigo])

def consulta_nombre(productos):
    cod=int(input("Ingrese el codigo a ser consultado : "))
    if cod in productos:
        print("El producto es:",productos[cod])
    else:
        print("No existe el producto")

def valor_cero(productos):
    print("Productos con stock cero")
    for codigo in productos:
        if productos[codigo][2] == 0:
            print(codigo, productos[codigo][0], productos[codigo][1])


productos=cargar()
imprimir(productos)
consulta_nombre(productos)
valor_cero(productos)
