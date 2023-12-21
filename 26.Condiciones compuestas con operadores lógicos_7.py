# Escribir un programa que pida ingresar la cordenada de un punto en el plano, es decir dos valores
# enteros x e y (distintos de cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto 
# (1 Cuadrante si x>0  Y  y>0 ,  2 Cuadrante: x<0Y y >0, etc )

x= int(input("Ingrese el primer valor: "))
y= int(input("Ingrese el segundo valor: "))

if x > 0 and y >0:
    print("Este es el cuadrante 1")
else:
    if x < 0 and y >0:
        print("Este es el cuadrante 2")
    else:
        if x < 0 and y < 0:
            print("Este es el cuadrante 3")
        else:
            if x > 0 and y < 0:
                print("Este es el cuadrante 4")
            else:
                print("Se encuentra en algun eje")
print("Fin")