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

    def buscarTratamiento(self, codigo):
        for trat in self.listaTratamientos:
            if int(trat.codigo) == int(codigo):
                return trat

    def iniciar(self):
        self.cargarTratamientos()