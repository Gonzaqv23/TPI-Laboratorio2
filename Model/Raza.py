class Raza:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def darAlta(self):
        self.estado = 1

    def darBaja(self):
        self.estado = 0

    def __str__(self):
        return f"Raza: {self.nombre}"

    def __repr__(self):
        return f"Raza: {self.nombre}"