class Consulta:
    def __init__(self, codigo, masc, vet, diag, trat, vac, fecha):
        self.codigo = codigo
        self.mascota = masc
        self.veterinario = vet
        self.diagnostico = diag
        self.tratamiento = trat
        self.vacuna = vac
        self.fecha = fecha

    def getMascota(self):
        return self.mascota

    def __str__(self):
        return (f"{self.codigo} de {self.mascota}, {self.veterinario}, {self.diagnostico}\n"
                f"{self.tratamiento}, {self.vacuna}, {self.fecha}\n")

    def __repr__(self):
        return (f"{self.codigo} de {self.mascota}, {self.veterinario}, {self.diagnostico}\n"
                f"{self.tratamiento}, {self.vacuna}, {self.fecha}\n")