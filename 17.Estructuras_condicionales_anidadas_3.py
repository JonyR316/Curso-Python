# Se ingresa por teclado un valor entero, mostrar un mensaje que indique 
# si el numero es positivo, negativo o nulo (es decir cero)

valor= int(input("Ingrese el valor: "))

print("Su valor es: ")

if valor == 0:
    print("nulo")
else:
    if valor > 0:
        print("Positivo")
    else:
        print("Negativo")
print("Fin")