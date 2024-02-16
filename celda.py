
class Celda:
    
    def __init__(self, numeroCelda, preso, grupo_guardia):
        self.numeroCelda = numeroCelda
        self.preso = preso 
        self.grupo_guardia = grupo_guardia  
    
    # Setter para la propiedad 'presos'
    def set_preso(self, nuevos_preso):
        self.preso = nuevos_preso

    # Getter para la propiedad 'presos'
    def get_preso(self):
        return self.preso

    # Setter para la propiedad 'grupo_guardia'
    def set_grupo_guardia(self, nuevo_grupo):
        self.grupo_guardia = nuevo_grupo

    # Getter para la propiedad 'grupo_guardia'
    def get_grupo_guardia(self):
        return self.grupo_guardia

    