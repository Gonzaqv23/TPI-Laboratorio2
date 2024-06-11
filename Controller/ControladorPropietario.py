from Model.Propietario import Propietario


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

    def iniciar(self):
        self.cargarPropietarios()