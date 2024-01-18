"""
Cargar una cadena por teclado luego:
1) Imprimir los 2 primeros caracteres
2) Imprimir los 2 ultimos.
3) Imprimir todos menos el primero y el ultimo cararcter.
"""

cadena=input("Ingrese una cadena de caracteres: ")
print("Primeros dos de caractres") 
print(cadena[:2])
print("Ultimos dos caracteres")
print(cadena[len(cadena)-2:])
print("Todos menos el primero y el ultimo cararcter")
print(cadena[1:len(cadena)-1])

