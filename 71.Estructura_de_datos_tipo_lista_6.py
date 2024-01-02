"""
Definir una lista que almacene por asignacion los nombres de 5 personas. Contar cunatos de esos nombres
tienen 5 o mas caracteres.
"""

lista=["Jonathan", "Belen", "Emma", "Jefferson", "Xavier"]

contador=0
x=0

while x <len(lista):
    if len(lista[x])>=5:
        contador= contador+1
    x=x+1
print("Listado completo de nombres: ")
print(lista)
print("Nombres que contienen 5 o mas caracteres son")
print(contador)