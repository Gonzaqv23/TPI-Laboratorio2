from Raza import Raza

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

def main():
    cargarRazas()
    mostrarRazas()
    opcion = int(input("Bienvevido. Ingrese la opcion deseada:\n"
                       "1 - Listado Mascotas Activas\n"
                       "2 - Listado Tratamientos\n"
                       "3 - Listado Diagnosticos\n"
                       "4 - Listado Vacunas\n"
                       "5 - Listado Razas\n"
                       "6 - Listado Veterinarios\n"
                       "7 - Listado Clientes\n"
                       "8 - Mostrar Ficha Medica\n"
                       "9 - Consultar cantidad de Mascotas de un Cliente\n"
                       "10 - "))




if __name__ == '__main__':
    main()
