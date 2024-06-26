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

    def listarInfoRazas(self):
        lista = ["Raza"]
        for raza in self.listaRazas:
            lista.append(raza.getInfo())
        return lista

    def listarRazas(self):
        lista = ["Razas"]
        for raza in self.listaRazas:
            lista.append(raza.getEstado())
        return lista


    def iniciar(self):
        self.cargarRazas()