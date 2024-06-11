class Consulta:
    def __init__(self, codigo, masc, vet, diag, trat, vac, fecha):
        self.codigo = codigo
        self.mascota = masc
        self.veterinario = vet
        self.diagnostico = diag
        self.tratamiento = trat
        self.vacuna = vac
        self.fecha = fecha

    def dar_alta_consulta(self):
        pass

    def modificar_consulta(self):
        pass

    def dar_baja_consulta(self):
        pass

    def __str__(self):
        return (f"{self.codigo} de {self.mascota}, {self.veterinario}, {self.diagnostico}\n"
                f"{self.tratamiento}, {self.vacuna}, {self.fecha}\n")

    def __repr__(self):
        return (f"{self.codigo} de {self.mascota}, {self.veterinario}, {self.diagnostico}\n"
                f"{self.tratamiento}, {self.vacuna}, {self.fecha}\n")

class FichaMedica:
    def __init__(self, codigo, consulta=None):
        self.codigo = codigo
        self.consulta = [consulta]

    def __str__(self):
        return f"{self.consulta}"

    def __repr__(self):
        return f"{self.consulta}"

    def dar_alta_ficha_meidca(self):
        pass

    def modificar_ficha_medica(self):
        pass

    def dar_baja_ficha_medica(self):
        pass

class Diagnostico:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def dar_alta_diagnostico(self):
        pass

    def modificar_diagnostico(self):
        pass

    def dar_baja_diagnostico(self):
        pass

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion

class Tratamiento:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def dar_alta_tratamiento(self):
        pass

    def modificar_tratmiento(self):
        pass

    def dar_baja_tratamiento(self):
        pass

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion

class Vacuna:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    def dar_alta_vacuna(self):
        pass

    def modificar_vacuna(self):
        pass

    def dar_baja_vacuna(self):
        pass

    def __str__(self):
        return self.descripcion

    def __repr__(self):
        return self.descripcion