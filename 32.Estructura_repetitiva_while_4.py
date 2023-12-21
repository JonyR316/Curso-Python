# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego
# ingresar la longitud de cada perfil; sabiendo que la pieza cuya longitud este comprendida en el rango
# de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote

x=1
cantidad=0
n=int(input("Ingrese la cantidad de piezas: "))

while x <= n:
    largo=float(input("Ingresar el largo de la pieza: "))
    if largo>=1.20 and largo<=1.30:
        cantidad = cantidad + 1
    x= x+1
print("Cantidad de piezas aptas: ")
print(cantidad)