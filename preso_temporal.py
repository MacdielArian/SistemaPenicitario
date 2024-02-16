from preso import Preso

class PresoTemporal(Preso):
    def __init__(self, nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio,
                 experiencia_combate, nivel_adaptacion):
        super().__init__(nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio)
        self.experiencia_combate = experiencia_combate
        self.nivel_adaptacion = nivel_adaptacion

    # Setters y getters para experiencia_combate
    def set_experiencia_combate(self, experiencia):
        self.experiencia_combate = experiencia

    def get_experiencia_combate(self):
        return self.experiencia_combate

    # Setters y getters para nivel_adaptacion
    def set_nivel_adaptacion(self, nivel):
        self.nivel_adaptacion = nivel

    def get_nivel_adaptacion(self):
        return self.nivel_adaptacion