from Model.Veterinario import Veterinario
from View.VistaVeterinario import VistaVeterinario

class ControladorVeterinario:
    def __init__(self):
        self.vista = VistaVeterinario()
        self.listaVeterinarios = []

    def cargarVeterinarios(self):
        with open("veterinarios.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, nombre, estado, legajo = linea.strip().split(",")
            self.listaVeterinarios.append(Veterinario(int(codigo), nombre, estado, legajo))

    def buscarVeterinario(self, codigo):
        for vet in self.listaVeterinarios:
            if int(vet.codigo) == int(codigo):
                return vet

    def mostrarInfo(self):
        veterinariosActivos = ["Veterinarios Activos"]
        for vet in self.listaVeterinarios:
            if vet.isActiva():
                veterinariosActivos.append(vet.getInfo())
        return veterinariosActivos

    def cambiarEstadoVeterinario(self):
        self.vista.mostrarLista(self.mostrarInfo())
        veterinario = self.vista.getDato()
        altaObaja = self.vista.altaObaja()
        objVeterinario = self.buscarVeterinario(veterinario)
        if altaObaja == "a":
            objVeterinario.darAlta()
            self.vista.mostrarDato(objVeterinario.getEstado())
        elif altaObaja == "b":
            objVeterinario.darBaja()
            self.vista.mostrarDato(objVeterinario.getEstado())
        else:
            self.vista.mensajeError()

    def iniciar(self):
        self.cargarVeterinarios()