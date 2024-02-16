from preso import Preso

class PresoPermanente(Preso):
    def __init__(self, nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio,
                 relacion_guardia, relacion_resto_presos):
        super().__init__( nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio)
        self.relacion_guardia = relacion_guardia
        self.relacion_resto_presos = relacion_resto_presos

    # Setters y getters para relacion_guardia
    def set_relacion_guardia(self, relacion):
        self.relacion_guardia = relacion

    def get_relacion_guardia(self):
        return self.relacion_guardia

    # Setters y getters para relacion_resto_presos
    def set_relacion_resto_presos(self, relacion):
        self.relacion_resto_presos = relacion

    def get_relacion_resto_presos(self):
        return self.relacion_resto_presos
