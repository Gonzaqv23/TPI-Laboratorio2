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
        self.vista.configurarComboboxFicha(self.controladorMascota.listaMascotas)
        self.vista.configurarBotonGenerar(self.generarFicha)
        self.vista.configurarBotonImprimir(self.imprimirFicha)
        self.vista.configurarComboPropietarioMascota(self.controladorMascota.controladorPropietario.listaPropietarios)
        self.vista.configurarComboRazaMascota(self.controladorMascota.controladorRaza.listaRazas)

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

    def generarFicha(self):
        fecha = date.today()
        self.vista.limpiarListaFicha()
        mascota = self.vista.getMascotaFicha()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        if (objMascota.mostrarFichaMedica()):
            titulo = f"****FICHA MEDICA**** Fecha: {fecha}"
            self.vista.setListaFicha(titulo)
            for item in objMascota.mostrarFichaMedica():
                self.vista.setListaFicha(item)
        else:
            self.vista.mostrarMensajeNoFicha()

    def imprimirFicha(self):
        self.vista.mostrarMensajeImprimir()

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

    def iniciar(self):
        self.cargarConsultas()