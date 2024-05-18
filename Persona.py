class Persona:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

class Propietario(Persona):
    def __init__(self, codigo, nombre, telefono):
        super().__init__(codigo, nombre)
        self.telefono = telefono

class Veterinario(Persona):
    def __init__(self, codigo, nombre, legajo):
        super().__init__(codigo, nombre)
        self.legajo = legajo