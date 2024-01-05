"""
Confeccionar una funcion que le enviamos como parametro el valor del lado de un cuadrado y nos 
retorne su superficie.
"""

def calcular_superficie(lado):
    superficie=lado*lado
    return superficie

lado=int(input("Ingrese el valor entero: "))
superficie =calcular_superficie(lado)
print("La superficie es:",superficie)

print("----------- Otra Soucion----------")
lado=int(input("Ingrese el valor entero: "))
print("La superficie es:",calcular_superficie(lado))

print("----------- Otra Soucion----------")
# En el caso que pida imprimir mensaje que sea igual a 100
lado=int(input("Ingrese el valor entero: "))
if calcular_superficie(lado)==100:
    print("Es igual a 100")
else:
    print("La superficie no es 100")

