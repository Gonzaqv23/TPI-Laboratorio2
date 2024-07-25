from Model.Mascota import Mascota
import random

class ControladorMascota:
    def __init__(self, controladorRaza, controladorPropietario, vista):

        self.controladorRaza = controladorRaza
        self.controladorPropietario = controladorPropietario
        self.vista = vista
        self.listaMascotas = []
        self.vista.configurarBotonRegistrarMascota(self.registrarNuevaMascota)

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

    def buscarMascota(self, nombre):
        for masc in self.listaMascotas:
            if masc.nombre == nombre:
                return masc

    def buscarMascotaxCodigo(self, codigo):
        for masc in self.listaMascotas:
            if int(masc.codigo) == int(codigo):
                return masc

    def getCodigoxNombre(self, nombre):
        for masc in self.listaMascotas:
            if masc.nombre == nombre:
                return masc.codigo


    def registrarNuevaMascota(self):
        codigo = random.randint(30, 499)
        nombre, propietario, raza = self.vista.getNuevaMascota().split(",")
        objPropietario = self.controladorPropietario.buscarPropietarioxNombre(propietario)
        objRaza = self.controladorRaza.buscarRazaxNombre(raza)
        estado = "1"
        mascota = Mascota(codigo, nombre, objPropietario, objRaza, estado)
        self.listaMascotas.append(mascota)
        self.vista.configurarComboboxFicha(self.listaMascotas)
        self.vista.configurarComboboxMascotas(self.listaMascotas)
        cod_propietario = self.controladorPropietario.buscarCodigoxNombre(propietario)
        cod_raza = self.controladorRaza.buscarCodigoxNombre(raza)
        self.archivarMascota(codigo, nombre, cod_propietario, cod_raza, estado)
        self.vista.mostrarMensajeRegistroExitoso()

    def archivarMascota(self, codigo, nombre, propietario, raza, estado):
        with open("mascotas.txt", "a") as file:
            nueva_mascota = f"\n{codigo},{nombre},{propietario},{raza},{estado}"
            file.write(nueva_mascota)

    def cambiarEstadoMascota(self, mascota):
        objMascota = self.buscarMascota(mascota)
        objMascota.cambiarEstado()
        self.vista.limpiarListbox()
        for masc in self.listaMascotas:
            self.vista.insertarEnListados(f"{masc}-{masc.getEstado()}")
        mascotas_habilitadas = [mascot for mascot in self.listaMascotas if mascot.isHabilitado()]
        self.vista.configurarComboboxMascotas(mascotas_habilitadas)
        self.cambiarEstadoArchivoMascotas(mascota)

    def cambiarEstadoArchivoMascotas(self, mascota):
        with open("mascotas.txt") as file:
            lineas = file.readlines()
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[1] == mascota:
                if datos[4] == "1":
                    datos[4] = "0"
                elif datos[4] == "0":
                    datos[4] = "1"
                lineas[i] = ",".join(datos) + "\n"
        with open("mascotas.txt", "w") as archivo:
            archivo.writelines(lineas)


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

    def iniciar(self):
        self.cargarMascotas()