class Vacuna:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def isHabilitado(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

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