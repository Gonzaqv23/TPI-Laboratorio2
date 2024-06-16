from Model.Consulta import Consulta
from View.VistaConsulta import VistaConsulta
from datetime import date
import random

class ControladorConsulta:
    def __init__(self, controladorMascota, controladorTratamiento, controladorVeterinario):
        self.vista = VistaConsulta()
        self.controladorMascota = controladorMascota
        self.controladorTratamiento = controladorTratamiento
        self.controladorVeterinario =controladorVeterinario
        self.listaConsultas = []

    def cargarConsultas(self):
        with open("consultas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            masc = self.controladorMascota.buscarMascota(datos[1])
            vet = self.controladorVeterinario.buscarVeterinario(datos[2])
            diag = self.controladorTratamiento.buscarDiagnostico(datos[3])
            trat = self.controladorTratamiento.buscarTratamiento(datos[4])
            vac = self.controladorTratamiento.buscarVacuna(datos[5])
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
        self.vista.mostrarLista(self.controladorMascota.mostrarInfo())
        mascota = self.vista.getDato()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        self.vista.mostrarLista(self.controladorVeterinario.mostrarInfo())
        veterinario = self.vista.getDato()
        objVeterinario = self.controladorVeterinario.buscarVeterinario(veterinario)
        self.vista.mostrarLista(self.controladorTratamiento.mostrarInfoDiagnosticos())
        disgnostico = self.vista.getDato()
        objDiagnostico = self.controladorTratamiento.buscarDiagnostico(disgnostico)
        self.vista.mostrarLista(self.controladorTratamiento.mostrarInfoTratamientos())
        tratamiento = self.vista.getDato()
        objTratamiento = self.controladorTratamiento.buscarTratamiento(tratamiento)
        self.vista.mostrarLista(self.controladorTratamiento.mostrarInfoVacunas())
        vacuna = self.vista.getDato()
        objVacuna = self.controladorTratamiento.buscarVacuna(vacuna)
        fecha = date.today()
        consulta = Consulta(codigo,objMascota,objVeterinario,objDiagnostico,objTratamiento,objVacuna,fecha)
        self.listaConsultas.append(consulta)
        objMascota.cargarFichaMedica(consulta)
        self.vista.mostrarDato(consulta)
        self.archivarConsulta(codigo,mascota,veterinario,disgnostico,tratamiento,vacuna,fecha)

    def archivarConsulta(self, codigo,mascota,veterinario,disgnostico,tratamiento,vacuna,fecha):
        with open("consultas.txt", "a") as file:
            nueva_consulta = f"\n{codigo},{mascota},{veterinario},{disgnostico},{tratamiento},{vacuna},{fecha}"
            file.write(nueva_consulta)

    def mostrarFichaMedica(self):
        self.vista.mostrarLista(self.controladorMascota.mostrarInfoTodas())
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
        self.vista.mostrarLista(self.controladorMascota.mostrarInfoTodas())
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
            self.vista.mostrarDato(objDiagnostico.estado)
        elif altaObaja == "b":
            objDiagnostico.darBaja()
            self.vista.mostrarDato(objDiagnostico.estado)
        else:
            self.vista.mensajeError()

    def darAltasYbajas(self):
        while True:
            opcion = self.vista.menuAltasyBajas()
            if opcion == "1":
                self.cambiarEstadoDiagnostico()
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                pass
            elif opcion == "0":
                break
            else:
                self.vista.mensajeError()


    def menuListas(self):
        while True:
            opcion = self.vista.menuListas()
            if opcion == "1":
                self.vista.mostrarLista(self.controladorMascota.mostrarActivas())
            elif opcion == "2":
                self.vista.mostrarLista(self.controladorTratamiento.listaTratamientos)
            elif opcion == "3":
                self.vista.mostrarLista(self.controladorTratamiento.listaDiagnosticos)
            elif opcion == "4":
                self.vista.mostrarLista(self.controladorTratamiento.listaVacunas)
            elif opcion == "5":
                self.vista.mostrarLista(self.controladorMascota.listarRazas())
            elif opcion == "6":
                self.vista.mostrarLista(self.controladorVeterinario.listaVeterinarios)
            elif opcion == "0":
                break
            else:
                self.vista.mensajeError()

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
        self.vista.mensajeBienvenida()
        self.menu()