# Se ingresa por teclado tres numeros, si al menos uno de los valores ingresados es menor a 10,
#imprimir en pantalla "Alguno de los numero es menor a 10"

valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))
valor3= int(input("Ingrese el tercer valor: "))



if valor1 < 10 or valor2 <10 or valor3 < 10:
    print("Alguno de los numero es menor a 10")
else:
    print("Todos los numero son mayores a 10")
