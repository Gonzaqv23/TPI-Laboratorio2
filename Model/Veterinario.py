class Veterinario:
    def __init__(self, codigo, nombre, legajo, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.legajo = legajo
        self.estado = estado

    def isActiva(self):
        if int(self.estado) == 1:
            return True
        else:
            return False

    def getInfo(self):
        return f"Codigo: {self.codigo}, {self.nombre}"

    def __str__(self):
        return f"Veterinario: {self.nombre}, Legajo: {self.legajo}"

    def __repr__(self):
        return f"Propietario: {self.nombre}, Legajo: {self.legajo}"