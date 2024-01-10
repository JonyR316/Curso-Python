"""
En uan empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresion de todos los sueldos.
3) Cuantos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que estan por debajo del promedio.
"""


def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        sueldo=int(input("Ingrese el sueldo: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])

def mayor_sueldo(sueldos):
    contador=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            contador=contador+1
    print("Personas con sueldo superior a $4000:", contador)

def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio=suma//10
    return promedio

def menorque_promedio(sueldos):
    pro=promedio(sueldos)
    print("Promedio de sueldos de los empleados:",pro)
    print("Sueldos inferiores a el promedio:")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])


sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
mayor_sueldo(sueldos)
menorque_promedio(sueldos)
