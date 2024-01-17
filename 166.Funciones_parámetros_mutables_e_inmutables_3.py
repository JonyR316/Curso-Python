"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor 
su numero telefonico:
1) Carga de contactos y su numero telefonico.
2) Premitir modificar el numero telefonico. Se ingresa el nombre del contacto para su busqueda.
3) Imprimir la lista completa de contactos con sus numeros telefonicos.
"""

def carga():
    contactos={}
    continua="s"
    while continua == "s":
        contacto=input("Ingrese el nombre del contacto: ")
        telefono=int(input("Ingrese el numero de telefono: "))
        contactos[contacto]=telefono
        continua=input("Desea ingresar un nuevo contacto [s/n] ?: ")
    return contactos

def modificar_telefono(contactos):
    contacto=(input("Ingrese el contacto a ser modificado: "))
    if contacto in contactos:
        telefono=int(input("Ingrese el nuevo nuemero de telefono:"))
        contactos[contacto]=telefono
    else:
        print("No existe este contacto")
       
def imprimir_contactos(contactos):
    print("Listado de todos los contactos")
    for contacto in contactos:
        print(contacto, contactos[contacto])

contactos=carga()
imprimir_contactos(contactos)
modificar_telefono(contactos)
imprimir_contactos(contactos)