"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando
subindeces negativos.
"""
palabra=input("Ingrese una palabra: ")
indice=-1
for x in range(len(palabra)):
    print(palabra[indice],end="")
    indice=indice-1