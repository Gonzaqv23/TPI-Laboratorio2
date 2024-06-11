from Model.Consulta import Consulta
from View.VistaConsulta import VistaConsulta

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
            diag = datos[3]
            trat = self.controladorTratamiento.buscarTratamiento(datos[4])
            vac = datos[5]
            fecha = datos[6]
            self.listaConsultas.append(Consulta(int(codigo), masc, vet, diag, trat, vac, fecha))

    def buscarObjeto(self, lista, objeto):
        for obj in lista:
            if obj.codigo == objeto:
                return obj

    def listarDiagnosticos(self):
        listaDiagnosticos = []
        with open("diagnosticos.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            listaDiagnosticos.append(datos[1])
        return listaDiagnosticos

    def listarVacunas(self):
        listaVacunas = []
        with open("vacunas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            listaVacunas.append(datos[1])
        return listaVacunas

    def listarRazas(self):
        listaRazas = []
        with open("razas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            listaRazas.append(datos[1])
        return listaRazas

    def gestionarConsultas(self):
        pass


    def menu(self):
        while True:
            opcion = self.vista.mostrarMenu()
            if opcion == "1":
                self.vista.mostrarLista(self.controladorMascota.mostrarActivas())
            elif opcion == "2":
                self.vista.mostrarLista(self.controladorTratamiento.listaTratamientos)
            elif opcion == "3":
                self.vista.mostrarLista(self.listarDiagnosticos())
            elif opcion == "4":
                self.vista.mostrarLista(self.listarVacunas())
            elif opcion == "5":
                self.vista.mostrarLista(self.listarRazas())
            elif opcion == "6":
                self.vista.mostrarLista(self.controladorVeterinario.listaVeterinarios)
            elif opcion == "7":
                self.vista.mostrarLista(self.listaConsultas) #ficha Medica
            elif opcion == "8":
                pass
            elif opcion == "9":
                pass
            elif opcion == "10":
                pass
            elif opcion == "11":
                pass
            elif opcion == "12":
                pass
            elif opcion == "13":
                self.gestionarConsultas()
            elif opcion == "0":
                self.vista.mensajeDespedida()
                break
            else:
                self.vista.mensajeError()

    def iniciar(self):
        self.cargarConsultas()
        self.vista.mensajeBienvenida()
        self.menu()