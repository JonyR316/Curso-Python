"""
Mostrar la tabla de multiplicar del 5 empleando primero el while y segundo de nuevo 
empleando el for. (definir un comentario previo a cada algoritmo y un comentario de bloque al 
principio del programa)
"""

print("Tabla de multiplicar del 5")
# Algoritmopara mostrar la tabla de multiplicar del 5 con el while

x=5
while x <=50:
    print(x)
    x = x +5

print("Tabla de multiplicar del 5")
# Algoritmopara mostrar la tabla de multiplicar del 5 con el for

for x in range(5, 51, 5):
    print(x)