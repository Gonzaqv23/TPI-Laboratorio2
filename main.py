import tkinter as tk

from Controller.ControladorConsulta import ControladorConsulta
from Controller.ControladorMascota import ControladorMascota
from Controller.ControladorTratamiento import ControladorTratamiento
from Controller.ControladorVeterinario import ControladorVeterinario
from Controller.ControladorRaza import ControladorRaza
from Controller.ControladorPropietario import ControladorPropietario
from View.Vista import Vista

def main():
    root = tk.Tk()
    vista = Vista(root)
    controladorPropietario = ControladorPropietario(vista)
    controladorPropietario.iniciar()
    controladorRaza = ControladorRaza(vista)
    controladorRaza.iniciar()
    controladorMascota = ControladorMascota(controladorRaza, controladorPropietario, vista)
    controladorMascota.iniciar()
    controladorTratamiento = ControladorTratamiento(vista)
    controladorTratamiento.iniciar()
    controladorVeterinario = ControladorVeterinario(vista)
    controladorVeterinario.iniciar()
    controladorConsulta = ControladorConsulta(controladorMascota, controladorTratamiento, controladorVeterinario, vista)
    controladorConsulta.iniciar()
    root.mainloop()


if __name__ == '__main__':
    main()
