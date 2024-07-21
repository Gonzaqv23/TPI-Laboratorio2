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
        self.listbox_listados = tk.Listbox(self.tab2, width=75, height=25)
        self.listbox_listados.pack(pady=20)
        self.opcion = tk.IntVar()
        self.radio1 = ttk.Radiobutton(self.tab2, text="Consultas", value=1, variable=self.opcion)
        self.radio1.place(x=180, y=440)
        self.radio2 = ttk.Radiobutton(self.tab2, text="Mascotas", value=2, variable=self.opcion)
        self.radio2.place(x=280, y=440)
        self.radio3 = ttk.Radiobutton(self.tab2, text="Diagnosticos", value=3, variable=self.opcion)
        self.radio3.place(x=380, y=440)
        self.radio4 = ttk.Radiobutton(self.tab2, text="Propietarios", value=4, variable=self.opcion)
        self.radio4.place(x=180, y=480)
        self.radio5 = ttk.Radiobutton(self.tab2, text="Tratamientos", value=5, variable=self.opcion)
        self.radio5.place(x=280, y=480)
        self.radio6 = ttk.Radiobutton(self.tab2, text="Veterinarios", value=6, variable=self.opcion)
        self.radio6.place(x=380, y=480)
        self.radio7 = ttk.Radiobutton(self.tab2, text="Vacunas", value=7, variable=self.opcion)
        self.radio7.place(x=180, y=520)
        self.radio8 = ttk.Radiobutton(self.tab2, text="Razas", value=8, variable=self.opcion)
        self.radio8.place(x=280, y=520)

        self.boton_listar = tk.Button(self.tab2, text="Listar", font=("Arial", 10))
        self.boton_listar.place(x=300, y=580)



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

    def configurarBotonHacerConsulta(self, command):
        self.boton_hacer_consulta.config(command=command)

    def getDatosConsulta(self):
        mascota = self.combobox_mascota.get()
        veterinario = self.combobox_veterinario.get()
        diagnostico = self.combobox_diagnostico.get()
        tratamiento = self.combobox_tratamiento.get()
        vacuna = self.combobox_vacuna.get()
        consulta = f"{mascota},{veterinario},{diagnostico},{tratamiento},{vacuna}"
        return consulta

    def mostrarMensajeConsulta(self, consulta):
        self.mensajeInfoConsulta = tk.messagebox.showinfo("Consulta Registrada Correctamente", consulta)

    def getOpcion(self):
        opcion = self.opcion.get()
        return opcion

    def insertarEnListados(self, elemento):
        self.listbox_listados.insert(tk.END, elemento)

    def configurarBotonListados(self, command):
        self.boton_listar.config(command=command)

    def limpiarListbox(self):
        self.listbox_listados.delete(0, tk.END)