# Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar 
#(se ingresa un valor entero en el precio del producto y la cantidad)

precio=int(input("Ingese el precio del producto: "))
cantidad=int(input("Ingresar la cantidad de unidades: "))

total= precio*cantidad
print("se debe pagar: ")
print(total)