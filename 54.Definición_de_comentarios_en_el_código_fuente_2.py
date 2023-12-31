"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la
carga al ingresar el valor -1. Dejar como comentario dentro del codigo fuente el enunciado del
problema y algun otro comentario de linea pertinente.
"""
suma=0
valor=int(input("Ingresar valor (-1 Finaliza la carga): ")) # Se carga el primer valor

while valor!=-1:
    suma= suma + valor
    valor=int(input("Ingresar valor (-1 Finaliza la carga): ")) # Se carga el segundo valor hasta el ultimo
print("La suma de los valores ingresados: ")
print(suma)