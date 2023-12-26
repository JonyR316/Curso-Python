# Codificar un programa que lea n numeros enteros y calcule la cantidad de valores mayores o iguales a 1000
# (n se carga por teclado)
# Este tipo de problemas tambien se puede resolver empleando la estructura repetitiva for. Lo 
# primero que se hace es cargar una variante que indique la cantidad de valores a ingresar. Dicha
# variable se carga antes de entrar a la estructura repetitiva for.

cantidad=0
n=int(input("Ingresar el numero : "))

for x in range(n):
    valor=int(input("Ingrese la cantidad: "))
    if valor >= 1000:
        cantidad= cantidad+1
print("Cantidad de numeros mayores o iguales a 1000 son: ")
print(cantidad)