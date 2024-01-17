"""
Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista de 5 nombres.
2) Ordenar alfabeticamente la lista.
3) Imprimir la lista de nombres.
"""

def carga():
    nombres=[]
    for x in range(5):
        nombre=input("Ingrese el nombre: ")
        nombres.append(nombre)
    return nombres

def orden_alfabetico(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux= nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]= aux
        
def imprimir_lista(nombres):
    for nombre in nombres:
        print(nombre)

nombres=carga()
print("Lista antes de ordenar albaticamente")
imprimir_lista(nombres)
orden_alfabetico(nombres)
print("Lista ordenada albaticamente")
imprimir_lista(nombres)