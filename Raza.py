class Raza:
    def __init__(self, codigo, nombre="", estado=1):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def __str__(self):
        if self.estado == 1:
            return f"Raza: {self.nombre} Habilitada: SI"
        else:
            return f"Raza: {self.nombre} Habilitada: NO"

    def cambiarEstado(self):
        if self.estado == 1:
            self.estado = 0
        else:
            self.estado = 1