import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion Veterinaria")
        self.root.geometry("680x680+350+50")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        self.fondo = tk.PhotoImage(file="Veterinaria.png")
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)
        self.tab3 = tk.Frame(self.notebook)
        self.tab4 = tk.Frame(self.notebook)
        self.tab5 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Consultas")
        self.notebook.add(self.tab2, text="Listados")
        self.notebook.add(self.tab3, text="Ficha Medica")
        self.notebook.add(self.tab4, text="Registrar")
        self.notebook.add(self.tab5, text="Informacion")

        # TAB 1: Realizar Consulta
        self.fondo1 = tk.Label(self.tab1, image=self.fondo)
        self.fondo1.place(x=0, y=0, relwidth=1, relheight=1)
        self.imagen = tk.PhotoImage(file="perro.png")
        self.label_imagen = tk.Label(self.tab1, image=self.imagen)
        self.label_imagen.pack(pady=15)
        self.label_mascota = tk.Label(self.tab1, text="Seleccione Mascota:")
        self.label_mascota.pack(pady=10)
        self.combobox_mascota = ttk.Combobox(self.tab1, width=50)
        self.combobox_mascota.pack()
        self.label_veterinario = tk.Label(self.tab1, text="Veterinario:")
        self.label_veterinario.pack(pady=10)
        self.combobox_veterinario = ttk.Combobox(self.tab1, width=40)
        self.combobox_veterinario.pack()
        self.label_diagnostico = tk.Label(self.tab1, text="Diagnostico:")
        self.label_diagnostico.pack(pady=10)
        self.combobox_diagnostico = ttk.Combobox(self.tab1, width=40)
        self.combobox_diagnostico.pack()
        self.label_tratamiento = tk.Label(self.tab1, text="Tratamiento:")
        self.label_tratamiento.pack(pady=10)
        self.combobox_tratamiento = ttk.Combobox(self.tab1, width=40)
        self.combobox_tratamiento.pack()
        self.label_vacuna = tk.Label(self.tab1, text="Vacuna:")
        self.label_vacuna.pack(pady=10)
        self.combobox_vacuna = ttk.Combobox(self.tab1, width=40)
        self.combobox_vacuna.pack()

        self.boton_hacer_consulta = tk.Button(self.tab1, text="Hacer Consulta")
        self.boton_hacer_consulta.pack(pady=35)

        # TAB 2: Mostrar listados
        self.fondo2 = tk.Label(self.tab2, image=self.fondo)
        self.fondo2.place(x=0, y=0, relwidth=1, relheight=1)
        self.listbox_listados = tk.Listbox(self.tab2, width=75, height=25)
        self.listbox_listados.pack(pady=20)
        self.label_cambiar_estado = tk.Label(self.tab2, text="Para cambiar estado seleccione Item "
                                                             "y luego presione boton 'Cambiar Estado'")
        self.label_cambiar_estado.pack()
        self.opcion = tk.IntVar()
        self.radio1 = ttk.Radiobutton(self.tab2, text="Consultas", value=1, variable=self.opcion)
        self.radio1.place(x=180, y=480)
        self.radio2 = ttk.Radiobutton(self.tab2, text="Mascotas", value=2, variable=self.opcion)
        self.radio2.place(x=280, y=480)
        self.radio3 = ttk.Radiobutton(self.tab2, text="Diagnosticos", value=3, variable=self.opcion)
        self.radio3.place(x=380, y=480)
        self.radio4 = ttk.Radiobutton(self.tab2, text="Propietarios", value=4, variable=self.opcion)
        self.radio4.place(x=180, y=520)
        self.radio5 = ttk.Radiobutton(self.tab2, text="Tratamientos", value=5, variable=self.opcion)
        self.radio5.place(x=280, y=520)
        self.radio6 = ttk.Radiobutton(self.tab2, text="Veterinarios", value=6, variable=self.opcion)
        self.radio6.place(x=380, y=520)
        self.radio7 = ttk.Radiobutton(self.tab2, text="Vacunas", value=7, variable=self.opcion)
        self.radio7.place(x=180, y=560)
        self.radio8 = ttk.Radiobutton(self.tab2, text="Razas", value=8, variable=self.opcion)
        self.radio8.place(x=280, y=560)

        self.boton_listar = tk.Button(self.tab2, text="Listar", font=("Arial", 11, "bold"))
        self.boton_listar.place(x=210, y=600)
        self.boton_cambiar_estado = tk.Button(self.tab2, text="Cambiar Estado", font=("Arial", 11, "bold"))
        self.boton_cambiar_estado.place(x=340, y=600)

        # TAB 3: Generar Ficha Medica

        self.fondo3 = tk.Label(self.tab3, image=self.fondo)
        self.fondo3.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_generar_ficha = tk.Label(self.tab3, text="Generar Ficha Medica:", font=("Aerial", 11))
        self.label_generar_ficha.pack(pady=15)
        self.lista_ficha = tk.Listbox(self.tab3, width=90, height=25)
        self.lista_ficha.pack(pady=10)
        self.label_ficha_masc = tk.Label(self.tab3, text="Elegir Mascota:")
        self.label_ficha_masc.pack(pady=15)
        self.combobox_ficha_masc = ttk.Combobox(self.tab3, width=40)
        self.combobox_ficha_masc.pack()
        self.boton_generar_ficha = tk.Button(self.tab3, text="Generar", font=("Aerial", 12))
        self.boton_generar_ficha.place(x=220, y=580)
        self.boton_imprimir_ficha = tk.Button(self.tab3, text="Imprimir", font=("Aerial", 12))
        self.boton_imprimir_ficha.place(x=380, y=580)

        #TAB 4: Registros

        self.fondo4 = tk.Label(self.tab4, image=self.fondo)
        self.fondo4.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_registrar_mascota = tk.Label(self.tab4, text="Registrar Nueva Mascota", font=("Aerial", 11, "bold"))
        self.label_registrar_mascota.place(x=60, y=10)
        self.label_nombre_nueva_mascota = tk.Label(self.tab4, text="Nombre:")
        self.label_nombre_nueva_mascota.place(x=60, y=50)
        self.nuevo_nombre_masc = tk.StringVar()
        self.entrada_nombre_mascota = tk.Entry(self.tab4, textvariable=self.nuevo_nombre_masc)
        self.entrada_nombre_mascota.place(x=150, y=50)
        self.label_propietaio_mascota = tk.Label(self.tab4, text="Propietario:")
        self.label_propietaio_mascota.place(x=320, y=50)
        self.combo_propietario_mascota = ttk.Combobox(self.tab4, width=18)
        self.combo_propietario_mascota.place(x=410, y=50)
        self.label_raza_mascota = tk.Label(self.tab4, text="Raza:")
        self.label_raza_mascota.place(x=70, y=100)
        self.combo_raza_mascota = ttk.Combobox(self.tab4)
        self.combo_raza_mascota.place(x=145, y=100)
        self.boton_registrar_mascota = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_mascota.place(x=415, y=100)


        self.label_registrar_propietario = tk.Label(self.tab4, text="Registrar Nuevo Propietario", font=("Aerial", 11, "bold"))
        self.label_registrar_propietario.place(x=60, y=170)
        self.nombre_propietario = tk.StringVar()
        self.entrada_nombre_propietario = tk.Entry(self.tab4, textvariable=self.nombre_propietario)
        self.entrada_nombre_propietario.place(x=75, y=220)
        self.boton_registrar_propietario = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_propietario.place(x=105, y=250)

        self.label_registrar_diagnostico = tk.Label(self.tab4, text="Registrar Nuevo Diagnostico", font=("Aerial", 11, "bold"))
        self.label_registrar_diagnostico.place(x=370, y=170)
        self.nombre_diagnostico = tk.StringVar()
        self.entrada_nombre_diagnostico = tk.Entry(self.tab4, textvariable=self.nombre_diagnostico)
        self.entrada_nombre_diagnostico.place(x=385, y=220)
        self.boton_registrar_diagnostico = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_diagnostico.place(x=415, y=250)

        self.label_registrar_raza = tk.Label(self.tab4, text="Registrar Nueva Raza", font=("Aerial", 11, "bold"))
        self.label_registrar_raza.place(x=60, y=320)
        self.nombre_raza = tk.StringVar()
        self.entrada_nombre_raza = tk.Entry(self.tab4, textvariable=self.nombre_raza)
        self.entrada_nombre_raza.place(x=75, y=385)
        self.boton_registrar_raza = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_raza.place(x=105, y=415)

        self.label_registrar_tratamiento = tk.Label(self.tab4, text="Registrar Nuevo Tratamiento", font=("Aerial", 11, "bold"))
        self.label_registrar_tratamiento.place(x=370, y=320)
        self.nombre_tratamiento = tk.StringVar()
        self.entrada_nombre_tratamiento = tk.Entry(self.tab4, textvariable=self.nombre_tratamiento)
        self.entrada_nombre_tratamiento.place(x=385, y=385)
        self.boton_registrar_tratamiento = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_tratamiento.place(x=415, y=415)

        self.label_registrar_vacuna = tk.Label(self.tab4, text="Registrar Nueva Vacuna", font=("Aerial", 11, "bold"))
        self.label_registrar_vacuna.place(x=60, y=490)
        self.nombre_vacuna = tk.StringVar()
        self.entrada_nombre_vacuna = tk.Entry(self.tab4, textvariable=self.nombre_vacuna)
        self.entrada_nombre_vacuna.place(x=75, y=545)
        self.boton_registrar_vacuna = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_vacuna.place(x=105, y=580)

        self.label_registrar_veterinario = tk.Label(self.tab4, text="Registrar Nuevo Veterinario",
                                                    font=("Aerial", 11, "bold"))
        self.label_registrar_veterinario.place(x=370, y=490)
        self.nombre_veterinario = tk.StringVar()
        self.entrada_nombre_veterinario = tk.Entry(self.tab4, textvariable=self.nombre_veterinario)
        self.entrada_nombre_veterinario.place(x=385, y=545)
        self.boton_registrar_veterinario = tk.Button(self.tab4, text="Registrar")
        self.boton_registrar_veterinario.place(x=415, y=580)

        #TAB 5: Informacion

        self.fondo5 = tk.Label(self.tab5, image=self.fondo)
        self.fondo5.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_nombre_ranking = tk.Label(self.tab5, text="Ranking de Diagnosticos:",
                                             font=("Aerial", 12, "bold"))
        self.label_nombre_ranking.pack(pady=15)
        self.lista_ranking = tk.Listbox(self.tab5, width=35, height=6)
        self.lista_ranking.pack()
        self.label_titulo_consXmasc = tk.Label(self.tab5, text="Cantidad de Consultas por Mascota:",
                                            font=("Aerial", 12, "bold"))
        self.label_titulo_consXmasc.pack(pady=15)
        self.lista_consultas_x_mascotas = tk.Listbox(self.tab5, width=40, height=25)
        self.lista_consultas_x_mascotas.pack()

    def setElementoListaRanking(self, diagnostico, frecuencia):
        texto = f"{diagnostico} - Frecuencia: {frecuencia}"
        self.lista_ranking.insert(tk.END, texto)

    def setElementoListaConsultasxMascotas(self, dato):
        self.lista_consultas_x_mascotas.insert(tk.END, dato)

    def getElementoLista(self):
        item_seleccionado = self.listbox_listados.get(self.listbox_listados.curselection())
        return item_seleccionado

    def configurarComboboxMascotas(self, lista):
        self.combobox_mascota["values"] = lista

    def configurarComboboxVeterinario(self, lista):
        self.combobox_veterinario["values"] = lista

    def configurarComboboxDiagnostico(self, lista):
        self.combobox_diagnostico["values"] = lista

    def configurarComboboxTratamiento(self, lista):
        self.combobox_tratamiento["values"] = lista

    def configurarComboboxVacuna(self, lista):
        self.combobox_vacuna["values"] = lista

    def configurarComboboxFicha(self, lista):
        self.combobox_ficha_masc["values"] = lista

    def configurarComboPropietarioMascota(self, lista):
        self.combo_propietario_mascota["values"] = lista

    def configurarComboRazaMascota(self, lista):
        self.combo_raza_mascota["values"] = lista

    def configurarBotonCambiarEstado(self, command):
        self.boton_cambiar_estado.config(command=command)

    def configurarBotonHacerConsulta(self, command):
        self.boton_hacer_consulta.config(command=command)

    def configurarBotonGenerar(self, command):
        self.boton_generar_ficha.config(command=command)

    def configurarBotonImprimir(self, command):
        self.boton_imprimir_ficha.config(command=command)

    def configurarBotonRegistrarMascota(self, command):
        self.boton_registrar_mascota.config(command=command)

    def configurarBotonRegistrarPropietario(self, command):
        self.boton_registrar_propietario.config(command=command)

    def configurarBotonRegistrarDiagnostico(self, command):
        self.boton_registrar_diagnostico.config(command=command)

    def configurarBotonRegistrarRaza(self, command):
        self.boton_registrar_raza.config(command=command)

    def configurarBotonRegistrarTratamiento(self, command):
        self.boton_registrar_tratamiento.config(command=command)

    def configurarBotonRegistrarVacuna(self, command):
        self.boton_registrar_vacuna.config(command=command)

    def configurarBotonRegistrarVeterinario(self, command):
        self.boton_registrar_veterinario.config(command=command)

    def getNuevoVeterinario(self):
        nuevo_veterinario = self.entrada_nombre_veterinario.get()
        return nuevo_veterinario

    def getNuevaVacuna(self):
        nueva_vacuna = self.entrada_nombre_vacuna.get()
        return nueva_vacuna

    def getNuevoPropietario(self):
        nuevo_propietario = self.entrada_nombre_propietario.get()
        return nuevo_propietario

    def getNuevoDiagnostico(self):
        nuevo_diagnostico = self.entrada_nombre_diagnostico.get()
        return nuevo_diagnostico

    def getNuevaRaza(self):
        nueva_raza = self.entrada_nombre_raza.get()
        return nueva_raza

    def getNuevoTratamiento(self):
        nueva_tratamiento = self.entrada_nombre_tratamiento.get()
        return nueva_tratamiento

    def getDatosConsulta(self):
        mascota = self.combobox_mascota.get()
        veterinario = self.combobox_veterinario.get()
        diagnostico = self.combobox_diagnostico.get()
        tratamiento = self.combobox_tratamiento.get()
        vacuna = self.combobox_vacuna.get()
        consulta = f"{mascota},{veterinario},{diagnostico},{tratamiento},{vacuna}"
        return consulta

    def getMascotaFicha(self):
        mascota = self.combobox_ficha_masc.get()
        return mascota

    def getNuevaMascota(self):
        nombre = self.entrada_nombre_mascota.get()
        propietario = self.combo_propietario_mascota.get()
        raza = self.combo_raza_mascota.get()
        nueva_mascota = f"{nombre},{propietario},{raza}"
        return nueva_mascota


    def setListaFicha(self, elemento):
        self.lista_ficha.insert(tk.END, elemento)

    def mostrarMensajeNoFicha(self):
        self.lista_ficha.delete(0, tk.END)
        mensaje = "Mascota Sin Consultas"
        self.lista_ficha.insert(tk.END,mensaje)

    def limpiarListaFicha(self):
        self.lista_ficha.delete(0, tk.END)

    def mostrarMensajeConsulta(self, consulta):
        self.mensajeInfoConsulta = tk.messagebox.showinfo("Consulta Registrada Correctamente", consulta)

    def mostrarMensajeImprimir(self):
        self.mensaje_imprimir = tk.messagebox.showinfo("Imprimir Ficha Medica", "La Ficha Medica\n"
                                                                                "se envio a la cola de Impresion")

    def mostrarMensajeRegistroExitoso(self):
        self.mensaje_registro_exitoso = tk.messagebox.showinfo("Nuevo Registro", "Registro "
                                                                                 "realizado Exitosamente")

    def getOpcion(self):
        opcion = self.opcion.get()
        return opcion

    def insertarEnListados(self, elemento):
        self.listbox_listados.insert(tk.END, elemento)

    def configurarBotonListados(self, command):
        self.boton_listar.config(command=command)

    def limpiarListbox(self):
        self.listbox_listados.delete(0, tk.END)