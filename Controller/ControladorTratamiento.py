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
            codigo, descripcion, estado = linea.strip().split(",")
            self.listaTratamientos.append(Tratamiento(int(codigo), descripcion, estado))

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

    def buscarTratamientoxCodigo(self, codigo):
        for trat in self.listaTratamientos:
            if int(trat.codigo) == int(codigo):
                return trat

    def buscarDiagnosticoxCodigo(self, codigo):
        for diag in self.listaDiagnosticos:
            if int(diag.codigo) == int(codigo):
                return diag

    def buscarVacunaxCodigo(self, codigo):
        for vac in self.listaVacunas:
            if int(vac.codigo) == int(codigo):
                return vac

    def buscarTratamiento(self, nombre):
        for trat in self.listaTratamientos:
            if trat.descripcion == nombre:
                return trat

    def buscarVacuna(self, nombre):
        for vac in self.listaVacunas:
            if vac.nombre == nombre:
                return vac

    def buscarDiagnostico(self, nombre):
        for diag in self.listaDiagnosticos:
            if diag.nombre == nombre:
                return diag

    def getCodigoxNombreTratamiento(self, nombre):
        for trat in self.listaTratamientos:
            if trat.descripcion == nombre:
                return trat.codigo

    def getCodigoxNombreDiagnostico(self, nombre):
        for diag in self.listaDiagnosticos:
            if diag.nombre == nombre:
                return diag.codigo

    def getCodigoxNombreVacuna(self, nombre):
        for vac in self.listaVacunas:
            if vac.nombre == nombre:
                return vac.codigo

    def mostrarInfoDiagnosticos(self):
        diagnosticos = ["Diagnosticos"]
        for diag in self.listaDiagnosticos:
            diagnosticos.append(diag.getEstado())
        return diagnosticos

    def mostrarInfoTratamientos(self):
        tratamientos = ["Tratamientos"]
        for trat in self.listaTratamientos:
            tratamientos.append(trat.getEstado())
        return tratamientos

    def mostrarInfoVacunas(self):
        vacunas = ["Vacunas"]
        for vacuna in self.listaVacunas:
            vacunas.append(vacuna.getEstado())
        return vacunas

    def cambiarEstadoTratamiento(self):
        self.vista.mostrarLista(self.mostrarInfoTratamientos())
        tratamiento = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objTratamiento = self.buscarTratamiento(tratamiento)
        if altaObaja == "a":
            objTratamiento.darAlta()
            self.vista.mostrarDato(objTratamiento.getEstado())
        elif altaObaja == "b":
            objTratamiento.darBaja()
            self.vista.mostrarDato(objTratamiento.getEstado())
        else:
            self.vista.mensajeError()

    def cambiarEstadoVacuna(self):
        self.vista.mostrarLista(self.mostrarInfoVacunas())
        vacuna = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objVacuna = self.buscarVacuna(vacuna)
        if altaObaja == "a":
            objVacuna.darAlta()
            self.vista.mostrarDato(objVacuna.getEstado())
        elif altaObaja == "b":
            objVacuna.darBaja()
            self.vista.mostrarDato(objVacuna.getEstado())
        else:
            self.vista.mensajeError()

    def iniciar(self):
        self.cargarTratamientos()
        self.cargarVacunas()
        self.cargarDiagnosticos()