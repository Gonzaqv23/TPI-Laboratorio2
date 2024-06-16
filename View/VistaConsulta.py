class VistaConsulta:

      def mensajeBienvenida(self):
            print("\n****Bienvenido****\n")

      def mensajeDespedida(self):
            print("Muchas Gracias. Hasta pronto!!")

      def mensajeError(self):
            print("Opcion incorrecta. Intente de nuevo")

      def menuAltasyBajas(self):
            print("\n"
                  "1 - Diagnostico\n"
                  "2 - Mascota\n"
                  "3 - Propietario\n"
                  "4 - Raza\n"
                  "5 - Tratamiento\n"
                  "6 - Vacuna\n"
                  "7 - Veterinario\n"
                  "0 - Atras\n\n")
            opcion = input("Elija Opcion: ")
            return opcion

      def menuListas(self):
            print("\n"
                  "1 - Listado Mascotas Activas\n"
                  "2 - Listado Tratamientos\n"
                  "3 - Listado Diagnosticos\n"
                  "4 - Listado Vacunas\n"
                  "5 - Listado Razas\n"
                  "6 - Listado Veterinarios\n"
                  "0 - Atras\n\n")
            opcion = input("Elija el Listado que quiere ver: ")
            return opcion

      def mostrarMenuDatos(self):
            print("\n"
                  "1 - Consultar cantidad de Mascotas de un Propietario\n"
                  "2 - Consultar cantidad de Consultas por Mascota\n"
                  "3 - Consultar cantidad de Tratamientos por Mascota\n"
                  "4 - Ranking de Diagnosticos\n"
                  "0 - Atras\n\n")
            opcion = input("Elija opcion deseada: ")
            return opcion

      def mostrarMenu(self):
            print("\n"
                  "1 - Mostrar Listado\n"
                  "2 - REALIZAR CONSULTA\n"
                  "3 - Mostrar Ficha Medica\n"
                  "4 - Mostrar Informacion\n"
                  "5 - Registrar Mascota\n"
                  "6 - Registrar Propietario\n"
                  "7 - Altas/Bajas\n"
                  "0 - Salir\n\n")
            opcion = input("Elija opcion deseada: ")
            return opcion

      def getDato(self):
            codigo = input("\n\nSeleccione un codigo: ")
            return codigo

      def mostrarLista(self, lista):
            for i in lista:
                  print(i)

      def mostrarDato(self, dato):
            print(dato)

      def mensajeNoFichaMedica(self):
            print("\nNo Tiene Ficha Medica Aun\n")

      def mostrarTratamientosXmascota(self, cantidad):
            print(f"\nLa Mascota seleccionada tiene {cantidad} tratamientos\n")

      def mostrarRanking(self, diagnostico, frecuencia):
            print(f"{diagnostico}, Frecuencia: {frecuencia}")