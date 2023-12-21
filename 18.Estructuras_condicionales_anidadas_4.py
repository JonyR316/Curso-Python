# Confeccionar un programa que me permita cargar un numero entero positivo de hasta tres cifras
# y muestre un mensaje indicando si tiene 1, 2, o 3 tres cifras.
# Mostrar un mensaje de error si el numero de cifars en mayor.

valor= int(input("Ingrese un numero entero positivo entre 1 y 999: "))

if valor < 10:
    print("El valor tiene una cifra")
else:
    if valor < 100:
        print("El valor tiene dos cifras")
    else:
        if valor < 1000:
            print("El valor tiene tres cifras")
        else:
            print("Error")
print("Fin")