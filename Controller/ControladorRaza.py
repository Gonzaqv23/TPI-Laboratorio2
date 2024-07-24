from Model.Raza import Raza
import random

class ControladorRaza:
    def __init__(self, vista):
        self.vista = vista
        self.listaRazas = []
        self.vista.configurarBotonRegistrarRaza(self.registrarNuevaRaza)

    def cargarRazas(self):
        with open("razas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo,nombre,estado = linea.strip().split(",")
            self.listaRazas.append(Raza(codigo, nombre, estado))

    def buscarRaza(self, codigo):
        for raza in self.listaRazas:
            if int(raza.codigo) == int(codigo):
                return raza

    def buscarRazaxNombre(self, nombre):
        for raza in self.listaRazas:
            if raza.codigo == nombre:
                return raza

    def buscarCodigoxNombre(self, nombre):
        for raza in self.listaRazas:
            if raza.nombre == nombre:
                return raza.codigo

    def registrarNuevaRaza(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNuevaRaza()
        estado = "1"
        raza = Raza(codigo, nombre, estado)
        self.listaRazas.append(raza)
        self.vista.configurarComboRazaMascota(self.listaRazas)
        self.archivarRaza(codigo, nombre, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarRaza(self, codigo, nombre, estado):
        with open("razas.txt", "a") as file:
            nueva_raza = f"\n{codigo},{nombre},{estado}"
            file.write(nueva_raza)

    def cambiarEstadoRaza(self):
        self.vista.mostrarLista(self.controladorRaza.listarInfoRazas())
        raza = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objRaza = self.controladorRaza.buscarRaza(raza)
        if altaObaja == "a":
            objRaza.darAlta()
            self.vista.mostrarDato(objRaza.getEstado())
        elif altaObaja == "b":
            objRaza.darBaja()
            self.vista.mostrarDato(objRaza.getEstado())
        else:
            self.vista.mensajeError()


    def iniciar(self):
        self.cargarRazas()