# Se ingresa por teclado un numero positivo de uno o dos digitos (1...99) nostrar un mensaje indicando
# si el numero tiene uno o dos digitos.
# (Tener en cuenta que condicion debe cumplirse para tener dos digitos  un numero entero)

valor= int(input("Ingrese un valor de 1 a 99: "))

if valor > 9:
    print("El numero entero tiene dos digitos")
else:
    print("El numero entero tiene un digito")

#-------------------------------------------#

if valor >= 10:
    print("El numero entero tiene dos digitos")
else:
    print("El numero entero tiene un digito")