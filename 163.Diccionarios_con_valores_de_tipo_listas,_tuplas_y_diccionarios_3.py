"""
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el numero de documento 
del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de 
materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def cargar():
    alumnos={}
    for x in range(3):
        cedula=input("Ingrese la cedula: ")
        listamaterias=[]
        continua="s"
        while continua == "s":
            materia=input("Ingrese la materia: ")
            nota=int(input("Ingrese la nota: "))
            listamaterias.append((materia,nota))
            continua=input("Quiere cargar otra materia [s/n] ?:")
        alumnos[cedula]=listamaterias
    return alumnos

def imprimir_alumnos(alumnos):
    print("Listado completo de materias")
    for cedula in alumnos:
        print("Con el numero de cedula: ",cedula)
        for materia,nota in alumnos[cedula]:
            print(materia,nota)

def consulta_alumnos(alumnos):
    cedula=(input("Ingrese la cedula ha ser consultda : "))
    if cedula in alumnos:
        for materia,nota in alumnos[cedula]:
            print(materia,nota)
    else:
        print("No existen tal alumno")


alumnos=cargar()
print("------------------------------------")
imprimir_alumnos(alumnos)
print("------------------------------------")
consulta_alumnos(alumnos)