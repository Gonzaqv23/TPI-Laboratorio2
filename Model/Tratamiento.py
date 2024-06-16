class Tratamiento:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.diagnostico = ""
        self.vacuna = ""
        self.descripcion = descripcion

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.descripcion}"

    def __str__(self):
        return f"Tratamiento: {self.descripcion}"

    def __repr__(self):
        return f"Tratamiento: {self.descripcion}"