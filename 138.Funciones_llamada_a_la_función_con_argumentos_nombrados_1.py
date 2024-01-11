"""
Confeccionar una funcion que llegue como primer parametro el nombre del empleado, como segundo parametro 
el costo por hora y finalmente la cantidad de horas trabjadas.
Llamar a dicha funcion empleando la caracteristica de Python de argumentos nombrados.
"""

def calcular_sueldo(nombre, costohora, cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre, "trabajo",cantidadhoras,"y cobra un sueldo de:",sueldo)


calcular_sueldo("Jonathan",10,100)
calcular_sueldo(cantidadhoras=60,nombre="Belen",costohora=60)

print("-----------------------------------------------")

for x in range(10):
    if x==9:
        print(x)
    else:
        print(x, end="-")
print("Fin del programa")