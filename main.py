from Mascota import Raza

lista_razas = []

def cargarRazas():
    with open("razas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        nombre, estado = linea.strip().split(",")
        lista_razas.append(Raza(nombre,int(estado)))
def mostrarRazas():
    for raza in lista_razas:
        print(raza)

def mostrarMenuListado():
    opcion = int(input("Elija el listado que quiere ver: \n"
                       "1 - Mascotas Activas\n"
                       "2 - Tratamiento\n"
                       "3 - Diagnosticos\n"
                       "4 - Vacunas\n"
                       "5 - Razas\n"
                       "6 - Veterinarios\n"))
    return opcion

def mostrarListado(opcion):
    pass

def main():
    #cargarRazas()
    #mostrarRazas()
    opcion = int(input("Bienvevido. Ingrese la opcion deseada:\n"
                       "1 - Ver Listado Especifico\n"
                       "2 - Mostrar Ficha Medica\n"
                       "3 - Consultar cantidad de Mascotas de un Cliente\n"
                       "4 - Consultar cantidad de Consultas por Mascotas\n"
                       "5 - Consultar cantidad de Tratamientos por Mascotas\n"
                       "6 - Ranking de Diagnosticos\n"
                       "7 - Cantidad de Razas por Diagnostico\n"
                       "8 - Salir\n"))
    while opcion > 0:
        if opcion == 1:
            mostrarMenuListado()
            break
        if opcion == 2:
            pass
            break
        if opcion == 3:
            pass
            break
        if opcion == 4:
            pass
            break
        if opcion == 5:
            pass
            break
        if opcion == 6:
            pass
            break
        if opcion == 7:
            pass
            break
        if opcion == 8:
            print("Muchas Gracias. Hasta Pronto!!")
            break
        else:
            print("Ingrese opcion correcta")
            opcion = int(input("Bienvevido. Ingrese la opcion deseada:\n"
                               "1 - Ver Listado Especifico\n"
                               "2 - Mostrar Ficha Medica\n"
                               "3 - Consultar cantidad de Mascotas de un Cliente\n"
                               "4 - Consultar cantidad de Consultas por Mascotas\n"
                               "5 - Consultar cantidad de Tratamientos por Mascotas\n"
                               "6 - Ranking de Diagnosticos\n"
                               "7 - Cantidad de Razas por Diagnostico\n"
                               "8 - Salir\n"))




if __name__ == '__main__':
    main()
