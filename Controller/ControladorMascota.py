from Model.Mascota import Mascota

class ControladorMascota:
    def __init__(self, controladorRaza, controladorPropietario):
        self.controladorRaza = controladorRaza
        self.controladorPropietario = controladorPropietario
        self.listaMascotas = []

    def cargarMascotas(self):
        with open("mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            nombre = datos[1]
            propietario = self.controladorPropietario.buscarPropietario(datos[2])
            raza = self.controladorRaza.buscarRaza(datos[3])
            estado = datos[4]
            self.listaMascotas.append(Mascota(int(codigo), nombre, propietario, raza,int(estado)))

    def buscarMascota(self, codigo):
        for masc in self.listaMascotas:
            if int(masc.codigo) == int(codigo):
                return masc

    def mostrarActivas(self):
        mascotasActivas = []
        for masc in self.listaMascotas:
            if masc.isActiva():
                mascotasActivas.append(masc)
        return mascotasActivas

    def mostrarInfo(self):
        mascotasActivas = ["Mascotas"]
        for masc in self.listaMascotas:
            if masc.isActiva():
                mascotasActivas.append(masc.getInfo())
        return mascotasActivas

    def mostrarInfoTodas(self):
        mascotas = ["Mascotas"]
        for masc in self.listaMascotas:
            mascotas.append(masc.getInfo())
        return mascotas


    def listarRazas(self):
        lista = []
        for raza in self.controladorRaza.listaRazas:
            lista.append(raza)
        return lista

    def iniciar(self):
        self.cargarMascotas()