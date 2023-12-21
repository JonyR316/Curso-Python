# De un operario se conoce su sueldo y los años de antiguedad. Se pide confeccionar un programa que
# lea los datos de entrada  e informe:
# a) Si el sueldo es infeior a 500 y su antiguedad es igual o superior a 10 años, otorgarle un aumento
# del 20% mostrar el sueldo a pagar
# b) Si el sueldo es inferior a 500 pero su antiguedad es menor a 10 años, otorgarle un aumento de 5%
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios


sueldo = int(input("Ingrese su salario: "))
años_antiguedad = int(input("Ingrese la cantidad de años: "))

if sueldo < 500 and años_antiguedad >= 10:
    aumento= sueldo * 0.20
    print("Le corresponde el 20% de aumento el cual es: ")
    print(aumento)
    sueldo_pagar= sueldo + aumento
    print("Su sueldo total es: ")
    print(sueldo_pagar)
else:
    if sueldo < 500 and años_antiguedad < 10:
        aumento= sueldo * 0.05
        print("Le corresponde el 5% de aumento el cual es: ")
        print(aumento)
        sueldo_pagar= sueldo + aumento
        print("Su sueldo total es: ")
        print(sueldo_pagar)
    else:
        if sueldo >= 500:
            print("Su sueldo total es: ")
            print(sueldo)
print("Fin")