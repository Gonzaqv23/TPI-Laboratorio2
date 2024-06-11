from View.VistaMascota import VistaMascota
from Model.Mascota import Mascota

class ControladorMascota:
    def __init__(self, controladorRaza, controladorPropietario):
        self.vista = VistaMascota()
        self.controladorRaza = controladorRaza
        self.controladorPropietario = controladorPropietario
        self.listaMascotas = []

    def cargarMascotas(self):
        with open("mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            nombre = datos[1]
            propietario = self.controladorPropietario.buscarPropietario(datos[2])
            raza = self.controladorRaza.buscarRaza(datos[3])
            estado = datos[4]
            self.listaMascotas.append(Mascota(int(codigo), nombre, propietario, raza,int(estado)))

    def buscarMascota(self, codigo):
        for masc in self.listaMascotas:
            if int(masc.codigo) == int(codigo):
                return masc

    def mostrarActivas(self):
        mascotasActivas = []
        for masc in self.listaMascotas:
            if masc.isActiva():
                mascotasActivas.append(masc)
        return mascotasActivas

    def iniciar(self):
        self.cargarMascotas()