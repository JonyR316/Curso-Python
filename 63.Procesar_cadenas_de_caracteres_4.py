"""
Cargar una oracion por teclado. Mostrar luego cuantos en blanco se ingresaron. Tener en cuenta que un
espacio en blanco es igual a " ", en cambio una cadena vacia es "".
"""
oracion= input("Ingrese la oracion: ")
cantidad=0
x=0

while x < len(oracion):
    if oracion[x] == " ":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de espacios en blan que contiene es: ")
print(cantidad)