class VistaConsulta:

      def mensajeBienvenida(self):
            print("\n****Bienvenido****\n")

      def mensajeDespedida(self):
            print("Muchas Gracias. Hasta pronto!!")

      def mensajeError(self):
            print("Opcion incorrecta. Intente de nuevo")

      def menuListas(self):
            print("\n"
                  "1 - Listado Mascotas Activas\n"
                  "2 - Listado Tratamientos\n"
                  "3 - Listado Diagnosticos\n"
                  "4 - Listado Vacunas\n"
                  "5 - Listado Razas\n"
                  "6 - Listado Veterinarios\n"
                  "0 - Atras\n")
            opcion = input("Elija el Listado que quiere ver: ")
            return opcion


      def mostrarMenu(self):
            print("\n"
                  "1 - Mostrar Listado\n"
                  "2 - REALIZAR CONSULTA\n"
                  "3 - Consultar cantidad de Mascotas de un Cliente\n"
                  "4 - Consultar cantidad de Consultas por Mascotas\n"
                  "5 - Consultar cantidad de Tratamientos por Mascotas\n"
                  "6 - Ranking de Diagnosticos\n"
                  "7 - Cantidad de Razas por Diagnostico\n"
                  "8 - Mostrar Ficha Medica\n"
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