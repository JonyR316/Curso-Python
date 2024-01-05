"""
Confeccionar una aplicacionque muestre una presentacion en pantalla del prorama.
Solicite la carga de dos valores y nos muestre la suma.
Mostrar finalmente un mensaje de despedida del programa. 
"""

def mostar_mensaje(mensaje):
    print("------------------------------------")
    print(mensaje)
    print("------------------------------------")

def cargar_suma():
    valor1=int(input("Ingresar el valor: "))
    valor2=int(input("Ingresar el valor: "))
    suma=valor1+valor2
    print("La suma de los valores es:",suma)

mostar_mensaje("Ingrese los valores a sumar")
cargar_suma()
mostar_mensaje("Gracias por utilizar este programa a finalizado")