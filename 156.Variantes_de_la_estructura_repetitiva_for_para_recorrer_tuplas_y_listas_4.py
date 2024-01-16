"""
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla
con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

def cargar_productos():
    productos=[]
    for x in range(5):
        producto=input("Ingrese el producto: ")
        precio=int(input("Ingrese el precio: "))
        productos.append((producto,precio))
    return productos

def imprimir_productos(productos):
    print("Lista completa de productos y precios")
    for producto,precio in productos:
        print(producto,precio)

def precio_intermedio(productos):
    print("Productos con precio entre 10 y 15")
    for producto,precio in productos:
        if precio >=10 and precio <=15:
            print(producto,precio)


productos=cargar_productos()
imprimir_productos(productos)
precio_intermedio(productos)