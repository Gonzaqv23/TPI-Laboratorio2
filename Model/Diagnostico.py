class Diagnostico:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def getCodigo(self):
        return self.codigo

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def isActiva(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def getEstado(self):
        if int(self.estado) == 1:
            return f"{self.codigo} - {self.nombre} - Estado: Habilitado"
        elif int(self.estado) == 0:
            return f"{self.codigo} - {self.nombre} - Estado: NO habilitado"

    def __str__(self):
        return f"Diagnostico: {self.nombre}"

    def __repr__(self):
        return f"Diagnostico: {self.nombre}"