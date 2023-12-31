"""
Realizar la carga de enteros por teclado. Preguntar despues que el valor si desea cargar otro
valor debiendo el operador ingresar la cadena "si" o "no" por teclado.
Mostrar la suma de los valores ingresados 
"""

suma=0
opcion="si"

while opcion == "si":
    valor=int(input("Ingrese el valor: "))
    suma= suma + valor
    opcion= input("Desea ingresar otro valor? si/no: ")
print("La suma de los valores ingresados es: ")
print(suma)