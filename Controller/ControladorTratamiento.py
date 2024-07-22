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

    def cambiarEstadoDiagnostico(self):
        self.vista.mostrarLista(self.controladorTratamiento.mostrarInfoDiagnosticos())
        disgnostico = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objDiagnostico = self.controladorTratamiento.buscarDiagnostico(disgnostico)
        if altaObaja == "a":
            objDiagnostico.darAlta()
            self.vista.mostrarDato(objDiagnostico.getEstado())
        elif altaObaja == "b":
            objDiagnostico.darBaja()
            self.vista.mostrarDato(objDiagnostico.getEstado())
        else:
            self.vista.mensajeError()

    def rankingDiagnosticos(self):
        conteo_diagnosticos = {}
        for consulta in self.listaConsultas:
            codigo_diagnostico = consulta.diagnostico.getCodigo()
            conteo_diagnosticos[codigo_diagnostico] = conteo_diagnosticos.get(codigo_diagnostico, 0) + 1
        diagnosticos_ordenados = sorted(conteo_diagnosticos.items(), key=lambda x: x[1], reverse=True)
        for codigo, frecuencia in diagnosticos_ordenados:
            self.vista.mostrarRanking(self.controladorTratamiento.buscarDiagnostico(codigo),frecuencia)

    def tratamientosXmascota(self):
        cant = 0
        mascota = self.vista.getDato()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        for consulta in self.listaConsultas:
            if consulta.getMascota() == objMascota:
                cant += 1
        self.vista.mostrarTratamientosXmascota(cant)

    def iniciar(self):
        self.cargarTratamientos()
        self.cargarVacunas()
        self.cargarDiagnosticos()