"""
Confeccionar un programa que genere un numero aleatorio entre 1 y 10 y no se muestre.
El operador debe tratar de adivinar el numero ingresado.
Cada vez que ingrese un numero mostrar un mensaje "Gano" si es igual al generado o "El numero 
aleatorio es mayor" o "El numero aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesito.
"""
import random

print("Intenta adivinar el numero que pienso entre 1 y 10")
aleatorio=random.randint(1,10)

intentos=0
elegido=-1
while elegido!= aleatorio:
    elegido=int(input("Que numero elige? : "))
    if aleatorio>elegido:
        print("Piensa en un numero mayor")
    else:
        if aleatorio<elegido:
            print("Piensa en un numero menor ")
    intentos=intentos+1
print("Ganaste en",intentos,"intentos")