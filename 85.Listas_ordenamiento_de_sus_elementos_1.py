"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor de la lista a la 
ultima posicion. 
"""
sueldos=[]

for x in range(5):
    valor=int(input("Ingresar el valor del sueldo: "))
    sueldos.append(valor)
print("Lista de Sueldos Original")
print(sueldos)
for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
print("Lista tiene el ultimo elemento ordenado")
print(sueldos)
