"""
Confeccionar una funcion que reciba una cadena de caracteres y nos devuelva los tres primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por pantalla 
los primeros tres caracteres de cada mes.
"""
def primeros_3caracteres(cadena):
    return cadena[:3]


meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre",
           "Noviembre","Diciembre")

for mes in meses:
    print(primeros_3caracteres(mes))