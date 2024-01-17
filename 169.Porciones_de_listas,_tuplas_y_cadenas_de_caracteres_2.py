"""
Confeccionar una funcion que le enviemos un numero de mes como parametro y nos retorne una tupla 
con todos los nombres de meses que faltan hasta fin de año (utilizar el concepto de porciones)
"""

def meses_faltantes(numeromeses):
    meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre",
           "Noviembre","Diciembre")
    return meses[numeromeses:]

numeromeses=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(numeromeses)
print("Nombres de meses que faltan hasta fin de año")
print(mesesfalta)