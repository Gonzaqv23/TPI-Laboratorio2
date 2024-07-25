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

    def cambiarEstadoVeterinario(self, veterinario):
        objVeterinario = self.buscarVeterinario(veterinario)
        objVeterinario.cambiarEstado()
        self.vista.limpiarListbox()
        for vet in self.listaVeterinarios:
            self.vista.insertarEnListados(f"{vet}-{vet.getEstado()}")
        veterinarios_habilitados = [veter for veter in self.listaVeterinarios if veter.isHabilitado()]
        self.vista.configurarComboboxVeterinario(veterinarios_habilitados)
        self.cambiarEstadoArchivoVeterinario(veterinario)

    def cambiarEstadoArchivoVeterinario(self, veterinario):
        with open("veterinarios.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == veterinario:
                if datos[3] == "1":
                    datos[3] = "0"
                elif datos[3] == "0":
                    datos[3] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("veterinarios.txt", "w") as archivo:
            archivo.writelines(lineas)

    def iniciar(self):
        self.cargarVeterinarios()