from Model.Propietario import Propietario
import random


class ControladorPropietario:
    def __init__(self, vista):
        self.vista = vista
        self.listaPropietarios = []
        self.vista.configurarBotonRegistrarPropietario(self.registrarPropietario)

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
        nombre = self.vista.getNuevoPropietario()
        estado = "1"
        propietario = Propietario(codigo, nombre, estado)
        self.listaPropietarios.append(propietario)
        self.vista.configurarComboPropietarioMascota(self.listaPropietarios)
        self.archivarPropietario(codigo, nombre, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarPropietario(self, codigo, nombre, estado):
        with open("propietarios.txt", "a") as file:
            nuevo_propietario = f"\n{codigo},{nombre},{estado}"
            file.write(nuevo_propietario)

    def cambiarEstadoPropietario(self, propietario):
        objPropietario = self.buscarPropietarioxNombre(propietario)
        objPropietario.cambiarEstado()
        self.vista.limpiarListbox()
        for prop in self.listaPropietarios:
            self.vista.insertarEnListados(f"{prop}-{prop.getEstado()}")
        prop_habilitados = [prop for prop in self.listaPropietarios if prop.isHabilitado()]
        self.vista.configurarComboPropietarioMascota(prop_habilitados)
        self.cambiarEstadoArchivoPropietario(propietario)

    def cambiarEstadoArchivoPropietario(self, propietario):
        with open("propietarios.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == propietario:
                if datos[2] == "1":
                    datos[2] = "0"
                elif datos[2] == "0":
                    datos[2] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("propietarios.txt", "w") as archivo:
            archivo.writelines(lineas)


    def iniciar(self):
        self.cargarPropietarios()