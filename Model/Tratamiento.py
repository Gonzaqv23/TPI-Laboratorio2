class Tratamiento:
    def __init__(self, diagnostico, vacuna, descripcion):
        self.diagnostico = diagnostico
        self.vacuna = vacuna
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion