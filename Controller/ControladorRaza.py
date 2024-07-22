from Model.Raza import Raza

class ControladorRaza:
    def __init__(self):
        self.listaRazas = []

    def cargarRazas(self):
        with open("razas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo,nombre,estado = linea.strip().split(",")
            self.listaRazas.append(Raza(codigo,nombre,estado))

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