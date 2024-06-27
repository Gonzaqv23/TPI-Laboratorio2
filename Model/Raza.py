class Raza:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def isActiva(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def getEstado(self):
        if int(self.estado) == 1:
            return f"{self.codigo} - {self.nombre} - Estado: Habilitado"
        elif int(self.estado) == 0:
            return f"{self.codigo} - {self.nombre} - Estado: NO habilitado"

    def __str__(self):
        return f"Raza: {self.nombre}"

    def __repr__(self):
        return f"Raza: {self.nombre}"