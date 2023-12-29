""" Realizar un programa que lea los lados de n triangulos, e informar:
A) De cada uno de ellos, que tipo de triangulo es: equilatero(tres lados), Isosceles(dos lados iguales)
o escaleno(ningun lado igual)
B) Cantidad de triangulos de cada tipo. """

n=int(input("Ingrese el numero de triangulos: "))
cantidad1=0
cantidad2=0
cantidad3=0

for x in range(n):
    lado1=int(input("Ingresar el valor del lado: "))
    lado2=int(input("Ingresar el valor del lado: "))
    lado3=int(input("Ingresar el valor del lado: "))
    if lado1 == lado2 and lado1 == lado3:
        print("Triangulo Equilatero")
        cantidad1= cantidad1 + 1
    else:
        if lado2 == lado1 or lado2 == lado3 or lado1 == lado3:
            print("Triangulo Isosceles")
            cantidad2= cantidad2 + 1
        else:
            print("Triangulo Escaleno")
            cantidad3 = cantidad3 + 1

print("Cantidad de Equilatero")
print(cantidad1)
print("Cantidad de Isosceles")
print(cantidad2)
print("Cantidad de Escaleno")
print(cantidad3)



""" ---------------------------------------"""

for x in range(n):
    lado1=int(input("Ingresar el valor del lado: "))
    lado2=int(input("Ingresar el valor del lado: "))
    lado3=int(input("Ingresar el valor del lado: "))
    print("El tipo de trianulo es: ")
    if lado1 == lado2 and lado1 == lado3:
        print("Triangulo Equilatero")
        cantidad1= cantidad1 + 1
    else:
        if lado2 == lado1 or lado2 == lado3 or lado1 == lado3:
            print("Triangulo Isosceles")
            cantidad2= cantidad2 + 1
        else:
            if lado1!=lado2 and lado1 !=lado3 and lado2!=lado3:
                print("Triangulo Escaleno")
                cantidad3 = cantidad3 + 1
print("La Cantidad de triangulos son: ")
print("Triangulo Equilatero")
print(cantidad1)
print("Triangulo Isosceles")
print(cantidad2)
print("Triangulo Escaleno")
print(cantidad3)