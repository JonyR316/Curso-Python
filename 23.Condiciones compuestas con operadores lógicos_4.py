# Se ingresan por teclado tres numeros, si todos los valores ingresados son menores a 10,
#imprimir en pantalla el mensaje "Todos los numeros son menores a diez"

valor1= int(input("Ingrese el primer valor: "))
valor2= int(input("Ingrese el segundo valor: "))
valor3= int(input("Ingrese el tercer valor: "))

if valor1 < 10 and valor2 < 10 and valor3 < 10:
    print("Todos los numeros son menores a diez")
    print(valor1,valor2,valor3)
else:
    print("Todos los numeros son mayores a diez")
    print(valor1,valor2,valor3)
print("Fin")