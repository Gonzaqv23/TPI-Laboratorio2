class Veterinario:
    def __init__(self, codigo, nombre, estado, legajo):
        self.codigo = codigo
        self.nombre = nombre
        self.estado = estado
        self.legajo = legajo

    def __str__(self):
        return f"Veterinario: {self.nombre}, Legajo: {self.legajo}"

    def __repr__(self):
        return f"Propietario: {self.nombre}, Legajo: {self.legajo}"