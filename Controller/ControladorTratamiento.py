from Model.Tratamiento import Tratamiento
from View.VistaTratamiento import VistaTratamiento

class ControladorTratamiento:
    def __init__(self):
        self.vista = VistaTratamiento()
        self.listaTratamientos = []

    def cargarTratamientos(self):
        with open("tratamientos.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, descripcion = linea.strip().split(",")
            self.listaTratamientos.append(Tratamiento(int(codigo), descripcion))

    def iniciar(self):
        self.cargarTratamientos()