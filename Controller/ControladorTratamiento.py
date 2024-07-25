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

    def cambiarEstadoTratamiento(self, tratamiento):
        objTratamiento = self.buscarTratamiento(tratamiento)
        objTratamiento.cambiarEstado()
        self.vista.limpiarListbox()
        for trat in self.listaTratamientos:
            self.vista.insertarEnListados(f"{trat}-{trat.getEstado()}")
        tratamiento_habilitados = [tratam for tratam in self.listaTratamientos if tratam.isHabilitado()]
        self.vista.configurarComboboxTratamiento(tratamiento_habilitados)
        self.cambiarEstadoArchivoTratamiento(tratamiento)

    def cambiarEstadoArchivoTratamiento(self, tratamiento):
        with open("tratamientos.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == tratamiento:
                if datos[2] == "1":
                    datos[2] = "0"
                elif datos[2] == "0":
                    datos[2] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("tratamientos.txt", "w") as archivo:
            archivo.writelines(lineas)

    def registrarNuevoTratamiento(self):
        codigo = random.randint(30, 499)
        descripcion = self.vista.getNuevoTratamiento()
        estado = "1"
        tratamiento = Tratamiento(codigo, descripcion, estado)
        self.listaTratamientos.append(tratamiento)
        trat_habilitados = [trat for trat in self.listaTratamientos if trat.isHabilitado()]
        self.vista.configurarComboboxTratamiento(trat_habilitados)
        self.archivarTratamiento(codigo, descripcion, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarTratamiento(self, codigo, descripcion, estado):
        with open("tratamientos.txt", "a") as file:
            nuevo_tratamiento = f"\n{codigo},{descripcion},{estado}"
            file.write(nuevo_tratamiento)

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


    def cambiarEstadoDiagnostico(self, diagnostico):
        objDiagnostico = self.buscarDiagnostico(diagnostico)
        objDiagnostico.cambiarEstado()
        self.vista.limpiarListbox()
        for diag in self.listaDiagnosticos:
            self.vista.insertarEnListados(f"{diag}-{diag.getEstado()}")
        diag_habilitados = [diag for diag in self.listaDiagnosticos if diag.isHabilitado()]
        self.vista.configurarComboboxDiagnostico(diag_habilitados)
        self.cambiarEstadoArchivoDiagnostico(diagnostico)

    def cambiarEstadoArchivoDiagnostico(self, diagnostico):
        with open("diagnosticos.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == diagnostico:
                if datos[2] == "1":
                    datos[2] = "0"
                elif datos[2] == "0":
                    datos[2] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("diagnosticos.txt", "w") as archivo:
            archivo.writelines(lineas)

    def cambiarEstadoVacuna(self, vacuna):
        objVacuna = self.buscarVacuna(vacuna)
        objVacuna.cambiarEstado()
        self.vista.limpiarListbox()
        for vac in self.listaVacunas:
            self.vista.insertarEnListados(f"{vac}-{vac.getEstado()}")
        vacunas_habilitadas = [vacu for vacu in self.listaVacunas if vacu.isHabilitado()]
        self.vista.configurarComboboxVacuna(vacunas_habilitadas)
        self.cambiarEstadoArchivoVacuna(vacuna)

    def cambiarEstadoArchivoVacuna(self, vacuna):
        with open("vacunas.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == vacuna:
                if datos[2] == "1":
                    datos[2] = "0"
                elif datos[2] == "0":
                    datos[2] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("vacunas.txt", "w") as archivo:
            archivo.writelines(lineas)

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