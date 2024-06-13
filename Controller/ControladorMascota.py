from Model.Mascota import Mascota
from View.VistaMascota import VistaMascota
import random

class ControladorMascota:
    def __init__(self, controladorRaza, controladorPropietario):
        self.vista = VistaMascota()
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

    def mostrarInfoPropietarios(self):
        propietarios = ["Propietarios"]
        for prop in self.controladorPropietario.listaPropietarios:
            propietarios.append(prop.getInfo())
        return propietarios

    def registrarMascotas(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNombre()
        self.vista.mostrarLista(self.mostrarInfoPropietarios())
        propietario = self.vista.getDato()
        objPropietario = self.controladorPropietario.buscarPropietario(propietario)
        self.vista.mostrarLista(self.controladorRaza.listarInfoRazas())
        raza = self.vista.getDato()
        objRaza = self.controladorRaza.buscarRaza(raza)
        estado = "1"
        mascota = Mascota(codigo, nombre, objPropietario, objRaza, estado)
        self.listaMascotas.append(mascota)
        self.vista.mostrarDato(mascota)
        self.archivarMascota(codigo, nombre, propietario, raza, estado)


    def archivarMascota(self, codigo, nombre, propietario, raza, estado):
        with open("mascotas.txt", "a") as file:
            nueva_mascota = f"\n{codigo},{nombre},{propietario},{raza},{estado}"
            file.write(nueva_mascota)

    def mascotasXpropietario(self):
        cant = 0
        self.vista.mostrarLista(self.mostrarInfoPropietarios())
        propietario = self.vista.getDato()
        objPropietario = self.controladorPropietario.buscarPropietario(propietario)
        for masc in self.listaMascotas:
            if masc.getPropietario() == objPropietario:
                cant += 1
        self.vista.mostrarMascotasXpropietario(cant)


    def consultasXmascotas(self):
        for masc in self.listaMascotas:
            self.vista.mostrarDato(masc.getCantidadConsultas())

    def tratamientosXmascotas(self):
        pass

    def listarRazas(self):
        lista = []
        for raza in self.controladorRaza.listaRazas:
            lista.append(raza)
        return lista

    def iniciar(self):
        self.cargarMascotas()