class Tratamiento:
    def __init__(self, codigo, descripcion, estado):
        self.codigo = codigo
        self.diagnostico = ""
        self.vacuna = ""
        self.descripcion = descripcion
        self.estado = estado

    def isHabilitado(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.descripcion}"

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
        return f"{self.descripcion}"

    def __repr__(self):
        return f"{self.descripcion}"