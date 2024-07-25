from Model.Consulta import Consulta
from datetime import date
import random

class ControladorConsulta:
    def __init__(self, controladorMascota, controladorTratamiento, controladorVeterinario, vista):
        self.vista = vista
        self.controladorMascota = controladorMascota
        self.controladorTratamiento = controladorTratamiento
        self.controladorVeterinario =controladorVeterinario
        self.listaConsultas = []
        self.iniciarConfiguraciones()

    def iniciarConfiguraciones(self):
        mascotas_habilitadas = [masc for masc in self.controladorMascota.listaMascotas if masc.isHabilitado]
        self.vista.configurarComboboxMascotas(mascotas_habilitadas)
        veterinarios_habilitados = [vet for vet in self.controladorVeterinario.listaVeterinarios if vet.isHabilitado()]
        self.vista.configurarComboboxVeterinario(veterinarios_habilitados)
        diag_habilitados = [diag for diag in self.controladorTratamiento.listaDiagnosticos if diag.isHabilitado()]
        self.vista.configurarComboboxDiagnostico(diag_habilitados)
        trat_habilitados = [trat for trat in self.controladorTratamiento.listaTratamientos if trat.isHabilitado()]
        self.vista.configurarComboboxTratamiento(trat_habilitados)
        vac_habilitadas = [vac for vac in self.controladorTratamiento.listaVacunas if vac.isHabilitado()]
        self.vista.configurarComboboxVacuna(vac_habilitadas)
        self.vista.configurarComboboxFicha(self.controladorMascota.listaMascotas)
        lista_prop = self.controladorMascota.controladorPropietario.listaPropietarios
        prop_habilitados = [prop for prop in lista_prop if prop.isHabilitado()]
        self.vista.configurarComboPropietarioMascota(prop_habilitados)
        lista_razas = self.controladorMascota.controladorRaza.listaRazas
        razas_habilitadas = [raza for raza in lista_razas if raza.isHabilitado()]
        self.vista.configurarComboRazaMascota(razas_habilitadas)
        self.vista.configurarBotonHacerConsulta(self.hacerConsulta)
        self.vista.configurarBotonListados(self.mostrarListado)
        self.vista.configurarBotonGenerar(self.generarFicha)
        self.vista.configurarBotonImprimir(self.imprimirFicha)

    def cargarConsultas(self):
        with open("consultas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            codigo = datos[0]
            masc = self.controladorMascota.buscarMascotaxCodigo(datos[1])
            vet = self.controladorVeterinario.buscarVeterinarioxCodigo(datos[2])
            diag = self.controladorTratamiento.buscarDiagnosticoxCodigo(datos[3])
            trat = self.controladorTratamiento.buscarTratamientoxCodigo(datos[4])
            vac = self.controladorTratamiento.buscarVacunaxCodigo(datos[5])
            fecha = datos[6]
            consulta = Consulta(int(codigo), masc, vet, diag, trat, vac, fecha)
            self.listaConsultas.append(consulta)
            masc.cargarFichaMedica(consulta)

    def buscarObjeto(self, lista, objeto):
        for obj in lista:
            if obj.codigo == objeto:
                return obj

    def hacerConsulta(self):
        codigo = random.randint(20, 399)
        datos = self.vista.getDatosConsulta()
        mascota, veterinario, diagnostico, tratamiento, vacuna = datos.split(",")
        objMascota = self.controladorMascota.buscarMascota(mascota)
        objVeterinario = self.controladorVeterinario.buscarVeterinario(veterinario)
        objDiagnostico = self.controladorTratamiento.buscarDiagnostico(diagnostico)
        objTratamiento = self.controladorTratamiento.buscarTratamiento(tratamiento)
        objVacuna = self.controladorTratamiento.buscarVacuna(vacuna)
        fecha = date.today()
        objConsulta = Consulta(codigo, objMascota, objVeterinario, objDiagnostico, objTratamiento, objVacuna, fecha)
        self.listaConsultas.append(objConsulta)
        objMascota.cargarFichaMedica(objConsulta)
        self.vista.mostrarMensajeConsulta(objConsulta)
        codMascota = self.controladorMascota.getCodigoxNombre(mascota)
        codVeterinario = self.controladorVeterinario.getCodigoxNombre(veterinario)
        codDiagnostico = self.controladorTratamiento.getCodigoxNombreDiagnostico(diagnostico)
        codTratamiento = self.controladorTratamiento.getCodigoxNombreTratamiento(tratamiento)
        codVacuna = self.controladorTratamiento.getCodigoxNombreVacuna(vacuna)
        self.archivarConsulta(codigo, codMascota, codVeterinario, codDiagnostico, codTratamiento, codVacuna, fecha)

    def archivarConsulta(self, codigo,mascota,veterinario,disgnostico,tratamiento,vacuna,fecha):
        with open("consultas.txt", "a") as file:
            nueva_consulta = f"\n{codigo},{mascota},{veterinario},{disgnostico},{tratamiento},{vacuna},{fecha}"
            file.write(nueva_consulta)

    def generarFicha(self):
        fecha = date.today()
        self.vista.limpiarListaFicha()
        mascota = self.vista.getMascotaFicha()
        objMascota = self.controladorMascota.buscarMascota(mascota)
        if (objMascota.mostrarFichaMedica()):
            titulo = f"****FICHA MEDICA**** Fecha: {fecha}"
            self.vista.setListaFicha(titulo)
            for item in objMascota.mostrarFichaMedica():
                self.vista.setListaFicha(item)
        else:
            self.vista.mostrarMensajeNoFicha()

    def imprimirFicha(self):
        self.vista.mostrarMensajeImprimir()

    def rankingDiagnosticos(self):
        conteo_diagnosticos = {}
        for consulta in self.listaConsultas:
            codigo_diagnostico = consulta.diagnostico.getCodigo()
            conteo_diagnosticos[codigo_diagnostico] = conteo_diagnosticos.get(codigo_diagnostico, 0) + 1
        diagnosticos_ordenados = sorted(conteo_diagnosticos.items(), key=lambda x: x[1], reverse=True)
        for codigo, frecuencia in diagnosticos_ordenados:
            self.vista.configurarLabelRanking(self.controladorTratamiento.buscarDiagnosticoxCodigo(codigo), frecuencia)

    def extraerItem(self):
        dato = self.vista.getElementoLista().split("-")
        item = dato[0]
        return item

    def cambiarEstadoMascota(self):
        mascota = self.extraerItem()
        self.controladorMascota.cambiarEstadoMascota(mascota)

    def cambiarEstadoDiagnostico(self):
        diagnostico = self.extraerItem()
        self.controladorTratamiento.cambiarEstadoDiagnostico(diagnostico)

    def cambiarEstadoPropietario(self):
        propietario = self.extraerItem()
        self.controladorMascota.controladorPropietario.cambiarEstadoPropietario(propietario)

    def cambiarEstadoRaza(self):
        raza = self.extraerItem()
        self.controladorMascota.controladorRaza.cambiarEstadoRaza(raza)

    def cambiarEstadoTratamiento(self):
        tratamiento = self.extraerItem()
        self.controladorTratamiento.cambiarEstadoTratamiento(tratamiento)

    def cambiarEstadoVeterinario(self):
        veterinario = self.extraerItem()
        self.controladorVeterinario.cambiarEstadoVeterinario(veterinario)

    def cambiarEstadoVacuna(self):
        vacuna = self.extraerItem()
        self.controladorTratamiento.cambiarEstadoVacuna(vacuna)

    def mostrarListado(self):
        opcion = self.vista.getOpcion()
        if opcion == 1:
            self.vista.limpiarListbox()
            for item in self.listaConsultas:
                self.vista.insertarEnListados(item)
        elif opcion == 2:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.listaMascotas:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
            self.vista.configurarBotonCambiarEstado(self.cambiarEstadoMascota)
        elif opcion == 3:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaDiagnosticos:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
            self.vista.configurarBotonCambiarEstado(self.cambiarEstadoDiagnostico)
        elif opcion == 4:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.controladorPropietario.listaPropietarios:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
            self.vista.configurarBotonCambiarEstado(self.cambiarEstadoPropietario)
        elif opcion == 5:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaTratamientos:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
                self.vista.configurarBotonCambiarEstado(self.cambiarEstadoTratamiento)
        elif opcion == 6:
            self.vista.limpiarListbox()
            for item in self.controladorVeterinario.listaVeterinarios:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
                self.vista.configurarBotonCambiarEstado(self.cambiarEstadoVeterinario)
        elif opcion == 7:
            self.vista.limpiarListbox()
            for item in self.controladorTratamiento.listaVacunas:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
                self.vista.configurarBotonCambiarEstado(self.cambiarEstadoVacuna)
        elif opcion == 8:
            self.vista.limpiarListbox()
            for item in self.controladorMascota.controladorRaza.listaRazas:
                self.vista.insertarEnListados(f"{item}-{item.getEstado()}")
            self.vista.configurarBotonCambiarEstado(self.cambiarEstadoRaza)

    def iniciar(self):
        self.cargarConsultas()
        self.rankingDiagnosticos()