from Model.Raza import Raza
import random

class ControladorRaza:
    def __init__(self, vista):
        self.vista = vista
        self.listaRazas = []
        self.vista.configurarBotonRegistrarRaza(self.registrarNuevaRaza)

    def cargarRazas(self):
        with open("razas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            codigo,nombre,estado = linea.strip().split(",")
            self.listaRazas.append(Raza(codigo, nombre, estado))

    def buscarRaza(self, codigo):
        for raza in self.listaRazas:
            if int(raza.codigo) == int(codigo):
                return raza

    def buscarRazaxNombre(self, nombre):
        for raza in self.listaRazas:
            if raza.nombre == nombre:
                return raza

    def buscarCodigoxNombre(self, nombre):
        for raza in self.listaRazas:
            if raza.nombre == nombre:
                return raza.codigo

    def registrarNuevaRaza(self):
        codigo = random.randint(30, 499)
        nombre = self.vista.getNuevaRaza()
        estado = "1"
        raza = Raza(codigo, nombre, estado)
        self.listaRazas.append(raza)
        self.vista.configurarComboRazaMascota(self.listaRazas)
        self.archivarRaza(codigo, nombre, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarRaza(self, codigo, nombre, estado):
        with open("razas.txt", "a") as file:
            nueva_raza = f"\n{codigo},{nombre},{estado}"
            file.write(nueva_raza)

    def cambiarEstadoRaza(self, raza):
        objRaza = self.buscarRazaxNombre(raza)
        objRaza.cambiarEstado()
        self.vista.limpiarListbox()
        for ra in self.listaRazas:
            self.vista.insertarEnListados(f"{ra}-{ra.getEstado()}")
        razas_habilitadas = [raz for raz in self.listaRazas if raz.isHabilitado()]
        self.vista.configurarComboRazaMascota(razas_habilitadas)
        self.cambiarEstadoArchivoRaza(raza)

    def cambiarEstadoArchivoRaza(self, raza):
        with open("razas.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == raza:
                if datos[2] == "1":
                    datos[2] = "0"
                elif datos[2] == "0":
                    datos[2] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("razas.txt", "w") as archivo:
            archivo.writelines(lineas)


    def iniciar(self):
        self.cargarRazas()