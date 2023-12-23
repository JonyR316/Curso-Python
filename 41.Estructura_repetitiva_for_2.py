# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma
# de los valores ingresados y su promedio. Este problema ya lo desarrollamos 
# Lo resolvemos empleando la estructura for para repetir la carga de los diezvalore por teclado

suma=0
for x in range(10):
    valor=int(input("Ingrese un valor: "))
    suma= suma + valor
print("La suma de los 10 valores es: ")
print(suma)
promedio=suma/10
print("El promedio es: ")
print(promedio)