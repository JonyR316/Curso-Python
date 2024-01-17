"""
Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. Permitir almacenar 
distintas actividades para la misma fecha (se ingresa la hora y la actividad)
Implementar las siguientes funciones:
1) Carga de datos en la agenda.
2) Listado completo de la agenda.
3) Consulta de una fecha.
"""

def cargar():
    agenda={}
    continua="s"
    while continua=="s":
        fecha=input("Ingrese la fecha con formato dd/mm/aaaa: ")
        continua2="s"
        lista=[]
        while continua2 == "s":
            hora=input("Ingrese la hora con formato hh/mm: ")
            actividad=input("Ingrese la actividad: ")
            lista.append((hora,actividad))
            continua2=input("Quiere cargar otra actividad para la misma fecha [s/n] ?: ")
        agenda[fecha]=lista
        continua=input("Quiere cargar otra fecha [s/n] ?: ")
    return agenda
    

def imprimir_agenda(agenda):
    print("Listado completo de la agenda")
    for fecha in agenda:
        print("Para la fecha",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)


def consulta_fecha(agenda):
    fecha=(input("Ingrese la fecha a ser consultada : "))
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No existen actividades en dicha fecha")

agenda=cargar()
print("---------------------------")
imprimir_agenda(agenda)
print("---------------------------")
consulta_fecha(agenda)