
class VistaConsulta:


      def menuAltasyBajas(self):
            print("\n"
                  "1 - Diagnostico\n"
                  "2 - Mascota\n"
                  "3 - Veterinario\n"
                  "4 - Raza\n"
                  "5 - Propietario\n"
                  "6 - Tratamiento\n"
                  "7 - Vacuna\n"
                  "0 - Atras\n\n")
            opcion = input("Elija Opcion: ")
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

      def mostrarTratamientosXmascota(self, cantidad):
            print(f"\nLa Mascota seleccionada tiene {cantidad} tratamientos\n")

      def mostrarRanking(self, diagnostico, frecuencia):
            print(f"{diagnostico}, Frecuencia: {frecuencia}")