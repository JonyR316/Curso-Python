"""
Desarrollar un programa que cree una lista de 50 elemnetos. El primer elemento es una lista con un 
elemento entero, el segundo es una lista de dos elementos etc.
la lista deberia tener esta estructura y asignarle a esos valores a medida que se crean los elementos
"""

lista=[]
cant=1
for k in range(50):
    lista.append([])
    valor=1
    for x in range(cant):
        lista[k].append(valor)
        valor=valor+1
    cant=cant+1
print(lista)