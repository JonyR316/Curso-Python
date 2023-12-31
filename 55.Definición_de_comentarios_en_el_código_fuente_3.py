"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma.
Definir varias lineas de comentarios indicando el nombre del programa, el programador y la fecha de la 
ultima modificacion. Utilizar el caracter # para los comentarios.
"""

# Programa: Carga de 10 numeros reales
# Programador: Jonathan Rodriguez
# Fecha de la ultima modificacion: 31/12/2023

suma=0

for x in range(10):
    valor= float(input("Ingresar el valor: "))
    suma = suma + valor
print("Valor final de la suma: ")
print(suma)