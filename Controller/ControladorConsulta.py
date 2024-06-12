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
            self.listaConsultas.append(Consulta(int(codigo), masc, vet, diag, trat, vac, fecha))

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
        self.vista.mostrarDato(consulta)

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

    def menu(self):
        while True:
            opcion = self.vista.mostrarMenu()
            if opcion == "1":
                self.menuListas()
            elif opcion == "2":
                self.hacerConsulta()
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
            elif opcion == "8":
                pass
            elif opcion == "0":
                self.vista.mensajeDespedida()
                break
            else:
                self.vista.mensajeError()

    def iniciar(self):
        self.cargarConsultas()
        self.vista.mensajeBienvenida()
        self.menu()