from Model.Veterinario import Veterinario
import random

class ControladorVeterinario:
    def __init__(self, vista):
        self.vista = vista
        self.listaVeterinarios = []
        self.vista.configurarBotonRegistrarVeterinario(self.registrarNuevoVeterinario)

    def cargarVeterinarios(self):
        with open("veterinarios.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo, nombre, estado, legajo = linea.strip().split(",")
            self.listaVeterinarios.append(Veterinario(int(codigo), nombre, estado, legajo))

    def buscarVeterinarioxCodigo(self, codigo):
        for vet in self.listaVeterinarios:
            if int(vet.codigo) == int(codigo):
                return vet

    def buscarVeterinario(self, nombre):
        for vet in self.listaVeterinarios:
            if vet.nombre == nombre:
                return vet

    def getCodigoxNombre(self, nombre):
        for vet in self.listaVeterinarios:
            if vet.nombre == nombre:
                return vet.codigo

    def registrarNuevoVeterinario(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNuevoVeterinario()
        legajo = random.randint(11250, 18999)
        estado = "1"
        veterinario = Veterinario(codigo, nombre, legajo, estado)
        self.listaVeterinarios.append(veterinario)
        self.vista.configurarComboboxVeterinario(self.listaVeterinarios)
        self.archivarVeterinario(codigo, nombre, legajo, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarVeterinario(self, codigo, nombre, legajo, estado):
        with open("veterinarios.txt", "a") as file:
            nuevo_veterinario = f"\n{codigo},{nombre}, {legajo},{estado}"
            file.write(nuevo_veterinario)

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