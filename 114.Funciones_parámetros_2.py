"""
Confeccionar una funcion que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores 
hacerlo por teclado en otra funncion.
"""
def mostar_mayor(valor1,valor2,valor3):
    if valor1>valor2 and valor1 > valor3:
        print("El valor mayor es:",valor1)
    else:
        if valor2 > valor3:
           print("El valor mayor es:",valor2)
        else:
            print("El valor mayor es:",valor3)


def cargar():
    valor1=int(input("Ingresar el valor: "))
    valor2=int(input("Ingresar el valor: "))
    valor3=int(input("Ingresar el valor: "))
    mostar_mayor(valor1,valor2,valor3)

cargar()



