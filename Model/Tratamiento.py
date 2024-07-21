class Tratamiento:
    def __init__(self, codigo, descripcion, estado):
        self.codigo = codigo
        self.diagnostico = ""
        self.vacuna = ""
        self.descripcion = descripcion
        self.estado = estado

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.descripcion}"

    def getEstado(self):
        if int(self.estado) == 1:
            return f"{self.codigo} - {self.descripcion} - Estado: Habilitado"
        elif int(self.estado) == 0:
            return f"{self.codigo} - {self.descripcion} - Estado: NO habilitado"

    def __str__(self):
        return f"{self.descripcion}"

    def __repr__(self):
        return f"{self.descripcion}"