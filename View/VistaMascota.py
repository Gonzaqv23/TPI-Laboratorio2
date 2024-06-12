class VistaMascota:

    def getNombre(self):
        nombre = input("\nIngrese el Nombre de la Mascota: ")
        return nombre

    def mostrarDato(self, dato):
        print(dato)

    def getDato(self):
        dato = input("\nIngrese Codigo: ")
        return dato

    def mostrarLista(self, lista):
        for i in lista:
            print(i)