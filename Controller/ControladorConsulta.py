from Model.Consulta import Consulta
from datetime import date
import random

class ControladorConsulta:
    def __init__(self, controladorMascota, controladorTratamiento, controladorVeterinario, vista):
        self.vista = vista
        self.controladorMascota = controladorMascota
        self.controladorTratamiento = controladorTratamiento
        self.controladorVeterinario =controladorVeterinario
        self.listaConsultas = []
        self.vista.configurarComboboxMascotas(self.controladorMascota.listaMascotas)
        self.vista.configurarComboboxVeterinario(self.controladorVeterinario.listaVeterinarios)
        self.vista.configurarComboboxDiagnostico(self.controladorTratamiento.listaDiagnosticos)
        self.vista.configurarComboboxTratamiento(self.controladorTratamiento.listaTratamientos)
        self.vista.configurarComboboxVacuna(self.controladorTratamiento.listaVacunas)
        self.vista.configurarBotonHacerConsulta(self.hacerConsulta)
        self.vista.configurarBotonListados(self.mostrarListado)

    def cargarConsultas(self):
        with open("consultas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            masc = self.controladorMascota.buscarMascotaxCodigo(datos[1])
            vet = self.controladorVeterinario.buscarVeterinarioxCodigo(datos[2])
            diag = self.controladorTratamiento.buscarDiagnosticoxCodigo(datos[3])
            trat = self.controladorTratamiento.buscarTratamientoxCodigo(datos[4])
            vac = self.controladorTratamiento.buscarVacunaxCodigo(datos[5])
            fecha = datos[6]
            consulta = Consulta(int(codigo), masc, vet, diag, trat, vac, fecha)
            self.listaConsultas.append(consulta)
            masc.cargarFichaMedica(consulta)

    def buscarObjeto(self, lista, objeto):
        for obj in lista:
            if obj.codigo == objeto:
                return obj

    def hacerConsulta(self):
        codigo = random.randint(20, 399)
        datos = self.vista.getDatosConsulta()
        mascota, veterinario, diagnostico, tratamiento, vacuna = datos.split(",")
        objMascota = self.controladorMascota.buscarMascota(mascota)
        objVeterinario = self.controladorVeterinario.buscarVeterinario(veterinario)
        objDiagnostico = self.controladorTratamiento.buscarDiagnostico(diagnostico)
        objTratamiento = self.controladorTratamiento.buscarTratamiento(tratamiento)
        objVacuna = self.controladorTratamiento.buscarVacuna(vacuna)
        fecha = date.today()
        objConsulta = Consulta(codigo, objMascota, objVeterinario, objDiagnostico, objTratamiento, objVacuna, fecha)
        self.listaConsultas.append(objConsulta)
        objMascota.cargarFichaMedica(objConsulta)
        self.vista.mostrarMensajeConsulta(objConsulta)
        codMascota = self.controladorMascota.getCodigoxNombre(mascota)
        codVeterinario = self.controladorVeterinario.getCodigoxNombre(veterinario)
        codDiagnostico = self.controladorTratamiento.getCodigoxNombreDiagnostico(diagnostico)
        codTratamiento = self.controladorTratamiento.getCodigoxNombreTratamiento(tratamiento)
        codVacuna = self.controladorTratamiento.getCodigoxNombreVacuna(vacuna)
        self.archivarConsulta(codigo, codMascota, codVeterinario, codDiagnostico, codTratamiento, codVacuna, fecha)

    def archivarConsulta(self, codigo,mascota,veterinario,disgnostico,tratamiento,vacuna,fecha):
        with open("consultas.txt", "a") as file:
            nueva_consulta = f"\n{codigo},{mascota},{veterinario},{disgnostico},{tratamiento},{vacuna},{fecha}"
            file.write(nueva_consulta)

    def mostrarFichaMedica(self):
        self.vista.mostrarLista(self.controladorMascota.mostrarInfo())
        mascota = self.vista.getDato()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        if (objMascota.mostrarFichaMedica()):
            self.vista.mostrarLista(objMascota.mostrarFichaMedica())
        else:
            self.vista.mensajeNoFichaMedica()

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
        self.vista.mostrarLista(self.controladorMascota.mostrarInfo())
        mascota = self.vista.getDato()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        for consulta in self.listaConsultas:
            if consulta.getMascota() == objMascota:
                cant += 1
        self.vista.mostrarTratamientosXmascota(cant)

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


    def darAltasYbajas(self):
        while True:
            opcion = self.vista.menuAltasyBajas()
            if opcion == "1":
                self.cambiarEstadoDiagnostico()
            elif opcion == "2":
                self.controladorMascota.cambiarEstadoMascota()
            elif opcion == "3":
                self.controladorVeterinario.cambiarEstadoVeterinario()
            elif opcion == "4":
                self.controladorMascota.cambiarEstadoRaza()
            elif opcion == "5":
                self.controladorMascota.cambiarEstadoPropietario()
            elif opcion == "6":
                self.controladorTratamiento.cambiarEstadoTratamiento()
            elif opcion == "7":
                self.controladorTratamiento.cambiarEstadoVacuna()
            elif opcion == "0":
                break
            else:
                self.vista.mensajeError()


    def mostrarListado(self):
        opcion = self.vista.getOpcion()
        if opcion == 1:
            self.vista.limpiarListbox()
            for item in self.listaConsultas:
                self.vista.insertarEnListados(item)
        elif opcion == 2:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.listaMascotas:
                self.vista.insertarEnListados(item)
        elif opcion == 3:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaDiagnosticos:
                self.vista.insertarEnListados(item)
        elif opcion == 4:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.controladorPropietario.listaPropietarios:
                self.vista.insertarEnListados(item)
        elif opcion == 5:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaTratamientos:
                self.vista.insertarEnListados(item)
        elif opcion == 6:
            self.vista.limpiarListbox()
            for item in self.controladorVeterinario.listaVeterinarios:
                self.vista.insertarEnListados(item)
        elif opcion == 7:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaVacunas:
                self.vista.insertarEnListados(item)
        elif opcion == 8:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.controladorRaza.listaRazas:
                self.vista.insertarEnListados(item)

    def menuDatos(self):
        while True:
            opcion = self.vista.mostrarMenuDatos()
            if opcion == "1":
                self.controladorMascota.mascotasXpropietario()
            elif opcion == "2":
                self.controladorMascota.consultasXmascotas()
            elif opcion == "3":
                self.tratamientosXmascota()
            elif opcion == "4":
                self.rankingDiagnosticos()
            elif opcion == "0":
                break
            else:
                self.vista.mensajeError()

    def menu(self):
        while True:
            opcion = self.vista.mostrarMenu()
            if opcion == "1":
                self.menuListas()
            elif opcion == "2":
                self.hacerConsulta()
            elif opcion == "3":
                self.mostrarFichaMedica()
            elif opcion == "4":
                self.menuDatos()
            elif opcion == "5":
                self.controladorMascota.registrarMascotas()
            elif opcion == "6":
                self.controladorMascota.agregarPropietario()
            elif opcion == "7":
                self.darAltasYbajas()
            elif opcion == "0":
                self.vista.mensajeDespedida()
                break
            else:
                self.vista.mensajeError()

    def iniciar(self):
        self.cargarConsultas()