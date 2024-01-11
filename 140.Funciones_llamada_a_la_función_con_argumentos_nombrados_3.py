"""
Elaborar una funcion que muestre la tabla de multiplicar del valor que le enviemos como parametro. 
Definir un segundo parametro llamado termino que por defecto almacene el valor 10. Se deben 
mostrar tantos terminos de la tabla de multiplicar como lo indica el segundo parametro.
Llamar a la funcion desde el bloque principal de nuestro programa con argumentos nombrados.
"""

def tabla(numero, terminos=10):
    for x in range(terminos):
        valor=x * numero
        print(valor,",",sep="",end="")
    print()


print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)