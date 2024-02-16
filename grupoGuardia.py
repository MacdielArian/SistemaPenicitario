
class Grupo_guardia:

    def __init__(self, cant_vigilantes, exp_promedio, extrictos, confiabilidad, tiempo_respuesta):

        self.cant_vigilantes = cant_vigilantes
        self.exp_promedio = exp_promedio
        self.extrictos = extrictos
        self.confiabilidad = confiabilidad
        self.tiempo_respuesta = tiempo_respuesta

     # Setter para cant_vigilantes
    def set_cant_vigilantes(self, cant):
        self.cant_vigilantes = cant

    # Getter para cant_vigilantes
    def get_cant_vigilantes(self):
        return self.cant_vigilantes

    # Setter para exp_promedio
    def set_exp_promedio(self, exp):
        self.exp_promedio = exp

    # Getter para exp_promedio
    def get_exp_promedio(self):
        return self.exp_promedio

    # Setter para extrictos
    def set_extrictos(self, extrictos):
        self.extrictos = extrictos

    # Getter para extrictos
    def get_extrictos(self):
        return self.extrictos

    # Setter para confiabilidad
    def set_confiabilidad(self, confiabilidad):
        self.confiabilidad = confiabilidad

    # Getter para confiabilidad
    def get_confiabilidad(self):
        return self.confiabilidad

    # Setter para tiempo_respuesta
    def set_tiempo_respuesta(self, tiempo):
        self.tiempo_respuesta = tiempo

    # Getter para tiempo_respuesta
    def get_tiempo_respuesta(self):
        return self.tiempo_respuesta