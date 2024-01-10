"""
Desarrollar una aplicacion que permita ingresar por teclado los nombres de 5 articulos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y los precios
3) Imprimir el nombre de el articulo con un precio mayor.
4) Ingresar por teclado un importe y luego mostrar todos los articulos con un precio menor igual al 
valor ingresado.
"""
def datos_articulos():
    nombres=[]
    precios=[]
    for x in range(5):
        nombre=input("Ingrese el nombre: ")
        nombres.append(nombre)
        precio=int(input("Ingrese el precio: "))
        precios.append(precio)
    return  [nombres, precios]

def imprimir_articulos(nombres,precios):
    print("Listado de nombres y precios")
    for x in range(len(nombres)):
        print(nombres[x], precios[x])

def mayor_precio(nombres, precios):
    mayor=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>mayor:
            mayor=precios[x]
            pos=x
    print("Articulo con mayor precio:",nombres[pos],"su precio es:",mayor)

def consulta_precio(nombres,precios):
    valor=int(input("Ingrese un importe para mostrar los ariculos con un precio similar o menor: "))
    for x in range(len(precios)):
        if precios[x]<=valor:
            print(nombres[x],precios[x])


nombres,precios=datos_articulos()
imprimir_articulos(nombres,precios)
mayor_precio(nombres, precios)
consulta_precio(nombres,precios)
 