class Mascota:
    def __init__(self,codigo, nombre, prop, raza, especie):
        self.codigo = codigo
        self.nombre = nombre
        self.prop = prop
        self.raza = raza
        self.especie = especie

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

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


class Especie:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion