from Mascota import Mascota, Raza, Especie
from Consulta import Consulta, FichaMedica, Diagnostico, Tratamiento, Vacuna
from Persona import Propietario, Veterinario

lista_razas = []
lista_especies = []
lista_diagnosticos = []
lista_tratamientos = []
lista_vacunas = []
lista_proietarios = []
lista_veterinarios = []
lista_mascotas = []
lista_consultas = []
lista_fichasMedicas = []

def cargarRazas():
    with open("razas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, nombre, estado = linea.strip().split(",")
        lista_razas.append(Raza(int(codigo),nombre,int(estado)))

def cargarEspecies():
    with open("especies.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, descripcion = linea.strip().split(",")
        lista_especies.append(Especie(int(codigo),descripcion))

def cargarDiagnosticos():
    with open("diagnosticos.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, descripcion = linea.strip().split(",")
        lista_diagnosticos.append(Diagnostico(int(codigo),descripcion))

def cargarTratamientos():
    with open("tratamientos.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, descripcion = linea.strip().split(",")
        lista_tratamientos.append(Tratamiento(int(codigo),descripcion))

def cargarVacunas():
    with open("vacunas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, descripcion = linea.strip().split(",")
        lista_vacunas.append(Vacuna(int(codigo),descripcion))

def cargarPropietarios():
    with open("propietarios.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, nombre, telefono = linea.strip().split(",")
        lista_proietarios.append(Propietario(int(codigo),nombre,telefono))

def cargarVeterinarios():
    with open("veterinarios.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        codigo, nombre, legajo = linea.strip().split(",")
        lista_veterinarios.append(Veterinario(int(codigo),nombre,legajo))

def cargarMascotas():
    with open("mascotas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        codigo = datos[0]
        nombre = datos[1]
        prop = buscarObjeto(lista_proietarios, datos[2])
        raza = buscarObjeto(lista_razas, datos[3])
        especie = buscarObjeto(lista_especies, datos[4])
        lista_mascotas.append(Mascota(int(codigo),nombre,prop,raza,especie))

def cargarConsultas():
    with open("consultas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        codigo = datos[0]
        masc = buscarObjeto(lista_mascotas, datos[1])
        vet = buscarObjeto(lista_veterinarios, datos[2])
        diag = buscarObjeto(lista_diagnosticos, datos[3])
        trat = buscarObjeto(lista_diagnosticos, datos[4])
        vac = buscarObjeto(lista_diagnosticos, datos[5])
        lista_consultas.append(Consulta(int(codigo),masc,vet,diag,trat,vac))

def cargarFichaMedica():
    pass

def buscarObjeto(lista, objeto):
    for obj in lista:
        if obj.codigo == objeto:
            return obj

def mostrarInfo(lista):
    for item in lista:
        print(item)

def mostrarListado(lista):
    for i in lista:
        print(i)

def darDeAlta(item, lista):
    pass

def modificar(item, lista):
    pass

def darDeBaja(item, lista):
    pass

def main():
    cargarRazas()
    cargarEspecies()
    cargarDiagnosticos()
    cargarTratamientos()
    cargarVacunas()
    cargarPropietarios()
    cargarVeterinarios()
    cargarMascotas()
    cargarConsultas()
    cargarFichaMedica()
    opcion = int(input("Bienvevido. Ingrese la opcion deseada:\n"
                       "1 - Listado Mascotas Activas\n"
                       "2 - Listado Tratamientos\n"
                       "3 - Listado Diagnosticos\n"
                       "4 - Listado Vacunas\n"
                       "5 - Listado Razas\n"
                       "6 - Listado Veterinarios\n"
                       "7 - Mostrar Ficha Medica\n"
                       "8 - Consultar cantidad de Mascotas de un Cliente\n"
                       "9 - Consultar cantidad de Consultas por Mascotas\n"
                       "10 - Consultar cantidad de Tratamientos por Mascotas\n"
                       "11 - Ranking de Diagnosticos\n"
                       "12 - Cantidad de Razas por Diagnostico\n"
                       "13 - Salir\n"))
    while opcion >= 0:
        if opcion == 1:
            mostrarListado(lista_mascotas)
            opcion = 0
        if opcion == 2:
            mostrarListado(lista_tratamientos)
            opcion = 0
        if opcion == 3:
            mostrarListado(lista_diagnosticos)
            opcion = 0
        if opcion == 4:
            mostrarListado(lista_vacunas)
            opcion = 0
        if opcion == 5:
            mostrarListado(lista_razas)
            opcion = 0
        if opcion == 6:
            mostrarListado(lista_veterinarios)
            opcion = 0
        if opcion == 7:
            mostrarListado(lista_fichasMedicas)
            opcion = 0
        if opcion == 8:
            pass
            opcion = 0
        if opcion == 9:
            pass
            opcion = 0
        if opcion == 10:
            pass
            opcion = 0
        if opcion == 11:
            pass
            opcion = 0
        if opcion == 12:
            pass
            opcion = 0
        if opcion == 13:
            print("Muchas Gracias. Hasta pronto!!")
            break
        else:
            opcion = int(input("Ingrese la opcion deseada:\n"
                               "1 - Listado Mascotas Activas\n"
                               "2 - Listado Tratamientos\n"
                               "3 - Listado Diagnosticos\n"
                               "4 - Listado Vacunas\n"
                               "5 - Listado Razas\n"
                               "6 - Listado Veterinarios\n"
                               "7 - Mostrar Ficha Medica\n"
                               "8 - Consultar cantidad de Mascotas de un Cliente\n"
                               "9 - Consultar cantidad de Consultas por Mascotas\n"
                               "10 - Consultar cantidad de Tratamientos por Mascotas\n"
                               "11 - Ranking de Diagnosticos\n"
                               "12 - Cantidad de Razas por Diagnostico\n"
                               "13 - Salir\n"))




if __name__ == '__main__':
    main()
