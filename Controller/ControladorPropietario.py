from Model.Propietario import Propietario
import random


class ControladorPropietario:
    def __init__(self):
        self.listaPropietarios = []

    def cargarPropietarios(self):
        with open("propietarios.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, nombre, estado = linea.strip().split(",")
            self.listaPropietarios.append(Propietario(codigo, nombre, estado))

    def buscarPropietario(self, codigo):
        for prop in self.listaPropietarios:
            if int(prop.codigo) == int(codigo):
                return prop

    def buscarPropietarioxNombre(self, nombre):
        for prop in self.listaPropietarios:
            if prop.nombre == nombre:
                return prop

    def buscarCodigoxNombre(self, nombre):
        for prop in self.listaPropietarios:
            if prop.nombre == nombre:
                return prop.codigo

    def registrarPropietario(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNombre()
        estado = "1"
        propietario = Propietario(codigo, nombre, estado)
        self.listaPropietarios.append(propietario)
        self.vista.mostrarDato(propietario)
        self.archivarPropietario(codigo, nombre, estado)

    def cambiarEstadoPropietario(self):
        self.vista.mostrarLista(self.controladorPropietario.listarPropietarios())
        propietario = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objPropietario = self.controladorPropietario.buscarPropietario(propietario)
        if altaObaja == "a":
            objPropietario.darAlta()
            self.vista.mostrarDato(objPropietario.getEstado())
        elif altaObaja == "b":
            objPropietario.darBaja()
            self.vista.mostrarDato(objPropietario.getEstado())
        else:
            self.vista.mensajeError()

    def archivarPropietario(self, codigo, nombre, estado):
        with open("propietarios.txt", "a") as file:
            nuevo_propietario = f"\n{codigo},{nombre},{estado}"
            file.write(nuevo_propietario)

    def listarPropietarios(self):
        lista = []
        for prop in self.listaPropietarios:
            lista.append(prop.getEstado())
        return lista

    def iniciar(self):
        self.cargarPropietarios()