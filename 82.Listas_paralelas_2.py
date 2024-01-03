"""
Crear y cargar dos listas con los nombres de 5 prductos en una y sus respectivos precios en otra.
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto 
ingresado.
"""
productos=[]
precios=[]

for x in range(5):
    producto=input("Ingresar el nombre del producto: ")
    productos.append(producto)
    precio=int(input("Ingrese el precio del producto: "))
    precios.append(precio)
print("Listados Completos")
print(productos)
print(precios)
print("Productos tienen un precio mayor al primer producto")
cantidad=0
for x in range(1,5):
    if precios[x] > precios[0]:
        cantidad=cantidad+1
print(cantidad)