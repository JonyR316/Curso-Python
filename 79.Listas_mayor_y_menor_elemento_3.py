"""
Ingresar por teclado los nombres de 5 personas y almacenados en una lista. Mostrar el nombre de persona
menor en orden alfabetico.
"""

lista=[]

for x in range(5):
    valor=input("Ingrese el nombre: ")
    lista.append(valor)
menor=lista[0]
for x in range(1,5):
    if lista[x]< menor:
        menor = lista[x]
print("Lista de nombres completa")
print(lista)
print("El nombre de persona menor en orden alfabetico es: ")
print(menor)