from View.VistaMascota import VistaMascota
from Model.Mascota import Mascota

class ControladorMascota:
    def __init__(self):
        self.vista = VistaMascota()
        self.listaMascotas = []

    def cargarMascotas(self):
        with open("mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            nombre = datos[1]
            propietario = datos[2]
            raza = datos[3]
            especie = datos[4]
            estado = datos[5]
            self.listaMascotas.append(Mascota(int(codigo), nombre, propietario, raza, especie,int(estado)))

    def iniciar(self):
        self.cargarMascotas()