class VistaMascota:

    def getNombre(self):
        nombre = input("\nIngrese el Nombre de la Mascota: ")
        return nombre

    def mostrarDato(self, dato):
        print(dato)

    def getDato(self):
        dato = input("\nIngrese Codigo: ")
        return dato

    def mensajeError(self):
        print("Opcion incorrecta. Intente de nuevo")

    def altaObaja(self):
        opc = input("Realizar Alta o baja (a/b): ")
        return opc

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def mostrarMascotasXpropietario(self, cantidad):
        print(f"\nEl Propietario seleccionado posee {cantidad} mascotas\n")