"""
Confeccionar una aplicacion que solicite la carga de dos valores enteros y muestres la suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una linea separadora despues de cada vez que cargamos dos valores y su suma.
"""

def carga_suma():
    valor1=int(input("Ingrese el valor: "))
    valor2=int(input("Ingrese el valor: "))
    suma= valor1+valor2
    print("El resulatado de la suma es:",suma)

def separacion():
    print("------------------------------------")


for x in range(5):
    carga_suma()
    separacion()

