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
    nueva_raza = Raza("Pastor Aleman", 1)




if __name__ == '__main__':
    main()
