"""Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuantos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar."""

contador1=0
contador2=0
contador3=0
contador4=0

n=int(input("Ingresar puntos a procesar: "))

for f in range(n):
    x=int(input("Ingresar la coordenada X: "))
    y=int(input("Ingresar la coordenada Y: "))
    if x > 0 and y >0:
        print("Este es el cuadrante 1")
        contador1=contador1+1
    else:
        if x < 0 and y >0:
            print("Este es el cuadrante 2")
            contador2=contador2+1
        else:
            if x < 0 and y < 0:
                print("Este es el cuadrante 3")
                contador3=contador3+1
            else:
                if x > 0 and y < 0:
                    print("Este es el cuadrante 4")
                    contador4=contador4+1

print("Cantidad de Cuadeantes 1")
print(contador1)
print("Cantidad de Cuadeantes 2")
print(contador2)
print("Cantidad de Cuadeantes 3")
print(contador3)
print("Cantidad de Cuadeantes 4")
print(contador4)