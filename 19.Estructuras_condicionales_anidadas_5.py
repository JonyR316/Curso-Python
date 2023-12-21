# Un postulante a un empleo realiza un test de capacitacion, se obtuvo la siguiente informacion:
# cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contesto correctamente.
# Se pide confeccionar un programa que ingrese los dos datos por teclado e informe 
# el nivel del mismo segun el porcentaje de respuestas correctas que ha obtenido, sabiendo que:

# Nivel maximo: Porcentaje >= 90%
# Nivel medio: Porcentaje >= 75% y < 90%
# Nivel regular: Porcentaje >= 50% y < 75%
# Nivel maximo: Porcentaje < 50%

total_preguntas= int(input("Numero total de preguntas: "))
total_correctas= int(input("Total Correctas: "))

porcentaje= total_correctas*100/total_preguntas


if porcentaje >= 90:
    print("Nivel Maximo")
else:
    if porcentaje >= 75:
        print("Nivel Medio")
    else:
        if porcentaje >= 50:
            print("Nivel Regular")
        else:
            print("Fuera de nivel")
print("Fin")