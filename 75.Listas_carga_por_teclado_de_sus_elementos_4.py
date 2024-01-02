"""
Cargar por teclado y almacenar en una altura las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuantas personas son mas altas que el promedio y 
cuantas mas bajas
"""

lista=[]
suma=0

for x in range(5):
    altura=float(input("Ingrese la altura: "))
    lista.append(altura)
    suma= suma+altura
    promedio= suma/5
print(lista)
print("El promedio de la altura es: ")
print(promedio)
altas=0
bajas=0
for x in range(5):
    if lista[x] > promedio:
        altas=altas+1
    else:
        if lista[x] < promedio:
            bajas= bajas + 1
print("Alturas bajas:")
print(bajas)
print("Alturas altas: ")
print(altas)