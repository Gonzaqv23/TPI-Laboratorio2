from Controller.ControladorConsulta import ControladorConsulta
from Controller.ControladorMascota import ControladorMascota
from Controller.ControladorTratamiento import ControladorTratamiento
from Controller.ControladorVeterinario import ControladorVeterinario

def main():

    controladorMascota = ControladorMascota()
    controladorMascota.iniciar()
    controladorTratamiento = ControladorTratamiento()
    controladorTratamiento.iniciar()
    controladorVeterinario = ControladorVeterinario()
    controladorVeterinario.iniciar()
    controladorConsulta = ControladorConsulta(controladorMascota,controladorTratamiento,controladorVeterinario)
    controladorConsulta.iniciar()


if __name__ == '__main__':
    main()
