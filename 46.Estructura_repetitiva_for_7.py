# Desarrolar un programa que solicite la carga de 10 numeros e imprima la suma de los ultimos 5
# valores ingresados.

suma=0

for x in range(10):
    valor= int(input("Ingresar el valor: "))
    if x >=5:
        suma = suma + valor
print("La suma de los ultimos 5 valores es: ") 
print(suma)