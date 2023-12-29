# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medidad de la
# base y la altura de un triangulo. El programa debera informar:
# De cada triangulo la medida de su base, su altura y su superficie (la superficie se calcula con el 
# producto de la base por la altura sobre 2).
# La cantidad de triangulos cuya es mayor a 12.

n=int(input("Ingrese el numero de pares:"))
cantidad=0

for x in range(n):
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
    superficie= (base * altura)/2
    print("La superficie es: ")
    print(superficie)
    if superficie > 12:
        cantidad= cantidad+1
print("La cantidad de triangulos con la supercie mayor a 12: ")
print(cantidad)
