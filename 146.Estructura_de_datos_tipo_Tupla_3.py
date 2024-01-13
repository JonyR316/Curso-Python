"""
Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. Modificar 
la lista y luego convertir la lista en tupla.

Crear otra tupla a partir de tres variables independiente que almacenan el dia, mes, año
(empaquetamiento), luego desenpaquetar la tupla a otras tres variables independientes.
"""

print("Impriminmos la tupla")
fechatupla=(6,6,1991)
print("Imprimir la tupla")
print(fechatupla)

print("Imprimimos la lista que convertimos de la tupla")
lista=list(fechatupla)
print(lista)

print("Imprimimos fecha modificada")
lista[0]=9
lista[1]=9
lista[2]=2024
print(lista)

print("Imprimimos la tupla que convertimos de la lista")
tupla2=tuple(lista)
print(tupla2)

print("Tupa con variables independientes (empaquetado)")
dia=27
mes=12
año=1998
fechatupla3=dia,mes,año
print(fechatupla3)

print("Desempaquetado la tupla a otras tres variables independientes")
dia1,mes1,año1=fechatupla3
print(dia1,mes1,año1)