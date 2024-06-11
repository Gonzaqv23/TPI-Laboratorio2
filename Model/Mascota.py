class Mascota:
    def __init__(self, codigo, nombre, prop, raza, especie, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.propietario = prop
        self.raza = raza
        self.especie = especie
        self.estado = estado

    def isActiva(self):
        if self.estado == 1:
            return True
        else:
            return False

    def cambiarEstado(self):
        if self.estado == 0:
            self.estado = 1
        else:
            self.estado = 0

    def __str__(self):
        return f"{self.nombre}, Raza: {self.raza}"

    def __repr__(self):
        return f"{self.nombre}, Raza: {self.raza}"