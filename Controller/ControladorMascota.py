from View.VistaMascota import VistaMascota

class ControladorMascota:
    def __init__(self):
        self.vista = VistaMascota()

    # def cargarMascotas():
    #     with open("mascotas.txt") as file:
    #         lineas = file.readlines()
    #     for linea in lineas:
    #         datos = linea.strip().split(",")
    #         codigo = datos[0]
    #         nombre = datos[1]
    #         prop = buscarObjeto(lista_proietarios, datos[2])
    #         raza = buscarObjeto(lista_razas, datos[3])
    #         especie = buscarObjeto(lista_especies, datos[4])
    #         lista_mascotas.append(Mascota(int(codigo), nombre, prop, raza, especie))

    # def cargarPropietarios():
    #     with open("propietarios.txt") as file:
    #         lineas = file.readlines()
    #     for linea in lineas:
    #         codigo, nombre, telefono = linea.strip().split(",")
    #         lista_proietarios.append(Propietario(int(codigo), nombre, telefono))

    # def cargarEspecies():
    #     with open("especies.txt") as file:
    #         lineas = file.readlines()
    #     for linea in lineas:
    #         codigo, descripcion = linea.strip().split(",")
    #         lista_especies.append(Especie(int(codigo), descripcion))

    # def cargarRazas():
    #     with open("razas.txt") as file:
    #         lineas = file.readlines()
    #     for linea in lineas:
    #         codigo, nombre, estado = linea.strip().split(",")
    #         lista_razas.append(Raza(int(codigo), nombre, int(estado)))

    def iniciar(self):
        pass