class Consulta:
    def __init__(self, cod, masc, vet, diag, trat, vac):
        self.codigo = cod
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
    def __init__(self, cod, masc):
        self.codigo = cod
        self.mascota = masc

    def __str__(self):
        return f"Ficha Medica de {self.mascota}"

    def __repr__(self):
        return f"Ficha Medica de {self.mascota}"