class Consulta:
    def __init__(self, codigo, masc, vet, diag, trat, vac):
        self.codigo = codigo
        self.mascota = masc
        self.veterinario = vet
        self.diagnostico = diag
        self.tratamiento = trat
        self.vacuna = vac

    def __str__(self):
        return f"{self.codigo} de {self.mascota}"

    def __repr__(self):
        return f"{self.codigo} de {self.mascota}"

class FichaMedica:
    def __init__(self, codigo, consulta=None):
        self.codigo = codigo
        self.consulta = [consulta]

    def __str__(self):
        return f"{self.consulta}"

    def __repr__(self):
        return f"{self.consulta}"

class Diagnostico:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion

class Tratamiento:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion

class Vacuna:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion