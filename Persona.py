class Persona:
    def __init__(self, codigo, nombre, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado

    def dar_alta_persona(self):
        pass

    def modificar_persona(self):
        pass

    def dar_baja_persona(self):
        pass

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

class Propietario(Persona):
    def __init__(self, codigo, nombre, estado, telefono, num_mascotas):
        super().__init__(codigo, nombre, estado)
        self.telefono = telefono
        self.num_mascotas = num_mascotas

class Veterinario(Persona):
    def __init__(self, codigo, nombre, estado, legajo):
        super().__init__(codigo, nombre, estado)
        self.legajo = legajo