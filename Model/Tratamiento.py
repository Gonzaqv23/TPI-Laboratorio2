class Tratamiento:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.diagnostico = ""
        self.vacuna = ""
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion