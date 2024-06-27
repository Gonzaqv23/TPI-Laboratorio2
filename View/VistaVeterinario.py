class VistaVeterinario:

    def mensajeError(self):
        print("Opcion incorrecta. Intente de nuevo")

    def altaObaja(self):
        opc = input("Realizar Alta o baja (a/b): ")
        return opc

    def mostrarLista(self, lista):
        for i in lista:
            print(i)

    def mostrarDato(self, dato):
        print(dato)

    def getDato(self):
        codigo = input("\n\nSeleccione un codigo: ")
        return codigo