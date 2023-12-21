# En una empresa trabajan n empleados cuyos sueldos oscilan entre 100 y 500, realizar un programa
# a que lea los sueldos que cobra cada empleado e informe cuantos empleados cobran entre 100 y 300
# y cuantos cobran mas de 300.
# Ademas el programa debera informar el importe que gasta la empresa en sueldos al personal

cont1=0
cont2=0
gastos=0
x=1
n=int(input("Ingresar el numero de empleados: "))

while x <= n:
    sueldo=int(input("Ingrese el sueldo: "))
    if sueldo <= 300:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
    gastos = gastos + sueldo
    x = x + 1
print("Sueldo menor a 300") 
print(cont1) 
print("Sueldo mayor a 300") 
print(cont2) 
print("Gasto total de la empresa") 
print(gastos) 