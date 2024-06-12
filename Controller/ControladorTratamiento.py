from Model.Tratamiento import Tratamiento
from Model.Vacuna import Vacuna
from Model.Diagnostico import Diagnostico

class ControladorTratamiento:
    def __init__(self):
        self.listaTratamientos = []
        self.listaVacunas = []
        self.listaDiagnosticos = []

    def cargarTratamientos(self):
        with open("tratamientos.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, descripcion = linea.strip().split(",")
            self.listaTratamientos.append(Tratamiento(int(codigo), descripcion))

    def cargarVacunas(self):
        with open("vacunas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, descripcion, estado = linea.strip().split(",")
            self.listaVacunas.append(Vacuna(int(codigo), descripcion, estado))

    def cargarDiagnosticos(self):
        with open("diagnosticos.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, descripcion, estado = linea.strip().split(",")
            self.listaDiagnosticos.append(Diagnostico(int(codigo), descripcion, estado))

    def buscarTratamiento(self, codigo):
        for trat in self.listaTratamientos:
            if int(trat.codigo) == int(codigo):
                return trat

    def buscarVacuna(self, codigo):
        for vac in self.listaVacunas:
            if int(vac.codigo) == int(codigo):
                return vac

    def buscarDiagnostico(self, codigo):
        for diag in self.listaDiagnosticos:
            if int(diag.codigo) == int(codigo):
                return diag

    def mostrarInfoDiagnosticos(self):
        diagnosticosActivos = ["Diagnosticos"]
        for diag in self.listaDiagnosticos:
            if diag.isActiva():
                diagnosticosActivos.append(diag.getInfo())
        return diagnosticosActivos

    def mostrarInfoTratamientos(self):
        tratamientosActivos = ["Tratamientos"]
        for trat in self.listaTratamientos:
            tratamientosActivos.append(trat.getInfo())
        return tratamientosActivos

    def mostrarInfoVacunas(self):
        vacunasActivas = ["Vacunas"]
        for vacuna in self.listaVacunas:
            if vacuna.isActiva():
                vacunasActivas.append(vacuna.getInfo())
        return vacunasActivas

    def iniciar(self):
        self.cargarTratamientos()
        self.cargarVacunas()
        self.cargarDiagnosticos()