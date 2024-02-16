
from preso_permanente import PresoPermanente
from preso_temporal import PresoTemporal

class Nodo:

    def __init__(self, preso, grupo_guardia, dias_restantes):
        self.preso = preso
        self.grupo_guardia = grupo_guardia
        self.dias_restantes = dias_restantes
        self.siguiente = None

    # Setter para modificar la cantidad de días restantes
    def set_dias_restantes(self, dias):
        self.dias_restantes = dias

    # Getter para obtener la cantidad de días restantes
    def get_dias_restantes(self):
        return self.dias_restantes

class Foso:

    def __init__(self):
        self.cima = None  # Inicializamos la pila vacía

    def apilar(self, preso, grupo_guardia, dias_restantes):
        nuevo_nodo = Nodo(preso, grupo_guardia, dias_restantes )
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            print("El foso está vacío")
        else:
            valor_removido = self.cima
            self.cima = self.cima.siguiente
            print(f"Elemento desapilado: {valor_removido}")

    def disminuir_dia(self):

        if self.cima is None:
            print("El foso está vacío")
        else:
            actual = self.cima

            while actual:

                actual.set_dias_restantes( actual.get_dias_restantes() - 1)
                actual = actual.siguiente


    def extraer_cima_actual_foso(self):
        
        actual_foso = None

        if self.cima is None:
            print('El foso está vacío')
        else:
            actual_foso = self.cima
            self.cima = self.cima.siguiente

        return actual_foso
    
    def esta_vacio(self):

        return self.cima is None


    
    def presos_con_max_dias(self):
        if self.cima is None:
            print("El foso está vacío")
            return []

        max_dias = self.cima.dias_restantes
        presos_max_dias = [self.cima.preso]
        actual = self.cima.siguiente

        while actual:
            if actual.dias_restantes > max_dias:
                max_dias = actual.dias_restantes
                presos_max_dias = [actual.preso]
            elif actual.dias_restantes == max_dias:
                presos_max_dias.append(actual.preso)
            actual = actual.siguiente

        return presos_max_dias
        

    def imprimir(self):
        actual = self.cima

        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Numero de celda - Restantes - Nombre - Nivel de escolaridad - Pandilla - Años de condena - Asesinato - Prestigio - Tipo de Preso - Relación guardia - Relación preso - Experiencia combate - adaptación')
        tabla = [ ]

        i = 0

        while actual:

            if isinstance( actual.preso, PresoPermanente ):

                fila = [ f'{i+1}', f'{actual.dias_restantes}' ,f'{actual.preso.get_nombre()}', f'{actual.preso.get_nivel_escolaridad()}', f'{actual.preso.get_pandilla()}', f'{actual.preso.get_annos_condena()}', f'{actual.preso.get_asesinato()}', f'{actual.preso.get_prestigio()}', 'Permanente' ,f'{actual.preso.get_relacion_guardia()}', f'{actual.preso.get_relacion_resto_presos()}', '-', '-' ]

                tabla.append( fila )

            elif isinstance( actual.preso, PresoTemporal):
            
                fila = [ f'{i+1}', f'{actual.dias_restantes}' ,f'{actual.preso.get_nombre()}', f'{actual.preso.get_nivel_escolaridad()}', f'{actual.preso.get_pandilla()}', f'{actual.preso.get_annos_condena()}', f'{actual.preso.get_asesinato()}', f'{actual.preso.get_prestigio()}', 'Temporal' ,'-', '-', f'{actual.preso.get_experiencia_combate()}', f'{actual.preso.get_nivel_adaptacion()}' ]

                tabla.append( fila )
            
            actual = actual.siguiente
        
            i = i + 1

    
        for fila in tabla:
            print("{:<17} {:<12} {:<15} {:<15} {:<15} {:<13} {:<10} {:<12} {:<15} {:<20} {:<20} {:<18} {:<18}".format(*fila))

        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')



   

