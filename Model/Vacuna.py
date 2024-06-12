class Vacuna:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def isActiva(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def __str__(self):
        return f"Vacuna: {self.nombre}"

    def __repr__(self):
        return f"Vacuna: {self.nombre}"