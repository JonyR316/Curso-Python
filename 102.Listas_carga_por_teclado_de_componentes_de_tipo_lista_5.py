"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como daoto las
temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del pais y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuados para el almacenamiento de los datos en memoria.
A) Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
B) Imprimir los nombres de los paises y las temperaturas medias mensuales de las misma.
C) Calcular la temperatura media trimestral de cada pais.
D) Imprimir los nombres de los paises y las temperaturas medias trimestral.
E) Imprimir el nombre del pais con la temperatura media trimestral mayor. 
"""
paises=[]
temperaturas=[]
promediotemparturas=[]

for x in range(4):
    pais=input("Ingrese el nombre del pais: ")
    paises.append(pais)
    temperatura1=int(input("Ingrese la primer temperatura: "))
    temperatura2=int(input("Ingrese la segunda temperatura: "))
    temperatura3=int(input("Ingrese la tercer temperatura: "))
    temperaturas.append([temperatura1, temperatura2, temperatura3])

print("Paises y sus temperaturas")
for x in range(4):
    print(paises[x], temperaturas[x][0], temperaturas[x][1], temperaturas[x][2])

print("Temperatura trimestral de cada pais")
for x in range(4):
    total= (temperaturas[x][0]+ temperaturas[x][1]+ temperaturas[x][2]) / 3
    promediotemparturas.append(total)
for x in range(4):
    print(paises[x],promediotemparturas[x])


temmayor=0
mayor=promediotemparturas[0];
for x in range(1,4):
    if promediotemparturas[x]>mayor:
        mayor=promediotemparturas[x]
        temmayor=x
print("Pais con la temperatura media trimestral mayor")
print(paises[temmayor])
print("Con una temperatura de: ", mayor)