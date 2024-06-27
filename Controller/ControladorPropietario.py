from Model.Propietario import Propietario
from View.VistaPropietario import VistaPropietario
import random


class ControladorPropietario:
    def __init__(self):
        self.vista = VistaPropietario()
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

    def registrarPropietario(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNombre()
        estado = "1"
        propietario = Propietario(codigo, nombre, estado)
        self.listaPropietarios.append(propietario)
        self.vista.mostrarDato(propietario)
        self.archivarPropietario(codigo, nombre, estado)

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