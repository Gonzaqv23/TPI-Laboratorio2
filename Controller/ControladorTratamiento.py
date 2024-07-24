from Model.Tratamiento import Tratamiento
from Model.Vacuna import Vacuna
from Model.Diagnostico import Diagnostico
import random

class ControladorTratamiento:
    def __init__(self, vista):
        self.vista = vista
        self.listaTratamientos = []
        self.listaVacunas = []
        self.listaDiagnosticos = []
        self.vista.configurarBotonRegistrarDiagnostico(self.registrarNuevoDiagnostico)
        self.vista.configurarBotonRegistrarTratamiento(self.registrarNuevoTratamiento)
        self.vista.configurarBotonRegistrarVacuna(self.registrarNuevaVacuna)

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

    def registrarNuevoDiagnostico(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNuevoDiagnostico()
        estado = "1"
        diagnostico = Diagnostico(codigo, nombre, estado)
        self.listaDiagnosticos.append(diagnostico)
        self.vista.configurarComboboxDiagnostico(self.listaDiagnosticos)
        self.archivarDiagnostico(codigo, nombre, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarDiagnostico(self, codigo, nombre, estado):
        with open("diagnosticos.txt", "a") as file:
            nuevo_diagnostico = f"\n{codigo},{nombre},{estado}"
            file.write(nuevo_diagnostico)

    def registrarNuevoTratamiento(self):
        codigo = random.randint(30, 499)
        descripcion = self.vista.getNuevoTratamiento()
        estado = "1"
        tratamiento = Tratamiento(codigo, descripcion, estado)
        self.listaTratamientos.append(tratamiento)
        self.vista.configurarComboboxTratamiento(self.listaTratamientos)
        self.archivarTratamiento(codigo, descripcion, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarTratamiento(self, codigo, descripcion, estado):
        with open("tratamientos.txt", "a") as file:
            nuevo_tratamiento = f"\n{codigo},{descripcion},{estado}"
            file.write(nuevo_tratamiento)

    def registrarNuevaVacuna(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNuevaVacuna()
        estado = "1"
        vacuna = Vacuna(codigo, nombre, estado)
        self.listaVacunas.append(vacuna)
        self.vista.configurarComboboxVacuna(self.listaVacunas)
        self.archivarVacuna(codigo, nombre, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarVacuna(self, codigo, nombre, estado):
        with open("vacunas.txt", "a") as file:
            nueva_vacuna = f"\n{codigo},{nombre},{estado}"
            file.write(nueva_vacuna)


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