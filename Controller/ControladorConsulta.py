from Model.Consulta import Consulta
from View.VistaConsulta import VistaConsulta

class ControladorConsulta:
    def __init__(self, controladorMascota, controladorTratamiento, controladorVeterinario):
        self.vista = VistaConsulta()
        self.controladorMascota = controladorMascota
        self.controladorTratamiento = controladorTratamiento
        self.controladorVeterinario =controladorVeterinario
        self.listaConsultas = []

    # def cargarConsultas(self):
    #     with open("consultas.txt") as file:
    #         lineas = file.readlines()
    #     for linea in lineas:
    #         datos = linea.strip().split(",")
    #         codigo = datos[0]
    #         masc = buscarObjeto(lista_mascotas, datos[1])
    #         vet = buscarObjeto(lista_veterinarios, datos[2])
    #         diag = buscarObjeto(lista_diagnosticos, datos[3])
    #         trat = buscarObjeto(lista_diagnosticos, datos[4])
    #         vac = buscarObjeto(lista_diagnosticos, datos[5])
    #         self.listaConsultas.append(Consulta(int(codigo), masc, vet, diag, trat, vac))

    def buscarObjeto(self, lista, objeto):
        for obj in lista:
            if obj.codigo == objeto:
                return obj

    def menu(self):
        while True:
            opcion = self.vista.mostrarMenu()
            if opcion == "1":
                pass
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
            elif opcion == "0":
                self.vista.mensajeDespedida()
                break
            else:
                self.vista.mensajeError()

    def iniciar(self):
        self.vista.mensajeBienvenida()
        self.menu()