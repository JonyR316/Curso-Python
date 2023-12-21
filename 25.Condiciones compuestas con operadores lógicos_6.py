# Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el
#segundo y a este resultado se lo multiplica por el tercero

valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))
valor3= int(input("Ingrese el tercer valor: "))



if valor1 == valor2 and valor1 == valor3:
    suma=(valor1+valor2)
    print("la suma es: ")
    print(suma)
    resultado= (valor1+valor2)*valor3
    print("El resultado es: ")
    print(resultado)
else:
    print("Todos los valores no son iguales")