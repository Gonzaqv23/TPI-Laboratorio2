class Mascota:
    def __init__(self, codigo, nombre, prop, raza, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.propietario = prop
        self.raza = raza
        self.estado = estado
        self.fichaMedica = []

    def isHabilitado(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def cargarFichaMedica(self, consulta):
        self.fichaMedica.append(consulta)

    def mostrarFichaMedica(self):
        return self.fichaMedica

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def getPropietario(self):
        return self.propietario

    def getCantidadConsultas(self):
        if len(self.fichaMedica) > 1:
            return f"{self.nombre}: {len(self.fichaMedica)} consultas"
        elif len(self.fichaMedica) == 1:
            return f"{self.nombre}: {len(self.fichaMedica)} consulta"
        else:
            return f"{self.nombre} aun no tiene consultas"

    def getEstado(self):
        if int(self.estado) == 0:
            return f"-------Estado: Inhabilitado"
        elif int(self.estado) == 1:
            return f"-------Estado: Habilitado"

    def cambiarEstado(self):
        if int(self.estado) == 0:
            self.estado = 1
        elif int(self.estado) == 1:
            self.estado = 0

    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"{self.nombre}"