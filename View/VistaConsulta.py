class VistaConsulta:

      def mensajeBienvenida(self):
            print("\n****Bienvenido****\n")

      def mensajeDespedida(self):
            print("Muchas Gracias. Hasta pronto!!")

      def mensajeError(self):
            print("Opcion incorrecta. Intente de nuevo")

      def mostrarMenu(self):
            print("1 - Listado Mascotas Activas\n"
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
                  "0 - Salir\n\n")
            opcion = input("Elija opcion deseada: ")
            return opcion

      def mostrarLista(self, lista):
            for i in lista:
                  print(i)