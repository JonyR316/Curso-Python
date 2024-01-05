def presentacion():
    print("Programa que permite cargar por teclado dos valores")
    print("Efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("---------------------------------------------------")

def carga_suma():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    suma=valor1+valor2
    print("La suma de los valores es:",suma)

def finalizacion():
    print("---------------------------------------------------")
    print("Gracias por utilizar este programa")

# Bloque principal de nuestreo programa
presentacion()
carga_suma()
finalizacion()