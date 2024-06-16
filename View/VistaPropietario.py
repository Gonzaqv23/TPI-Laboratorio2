class VistaPropietario:

    def getNombre(self):
        nombre = input("\nIngrese el Nombre del Propietario: ")
        return nombre

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def mostrarDato(self, dato):
        print(dato)