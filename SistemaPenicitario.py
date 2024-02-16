
from grupoGuardia import Grupo_guardia
from preso_permanente import PresoPermanente
from preso_temporal import PresoTemporal
from celda import Celda
from foso import Foso

# Crear 6 objetos de tipo Grupo_guardia
grupo1 = Grupo_guardia(3, 7, 10, True, 30)
grupo2 = Grupo_guardia(4, 5, 8, False, 30)
grupo3 = Grupo_guardia(2, 9, 12, True, 25)
grupo4 = Grupo_guardia(5, 6, 14, False, 35)
grupo5 = Grupo_guardia(1, 8, 13, True, 40)
grupo6 = Grupo_guardia(3, 4, 11, False, 15)


# Crear 3 objetos de tipo PresoPermanente
preso1 = PresoPermanente( "Macdiel", "Universitario", "Yakuza", 20, True, 7, "Excelente", "Bien")
preso2 = PresoPermanente( "Arian","Secundario", "Latinos", 15, False, 5, "Bien", "Excelente")
preso3 = PresoPermanente( "Pedro","Preuniversitario", "Blancos", 10, True, 10, "Mal", "Bien")

# Crear 3 objetos de tipo PresoTemporal
preso_temporal1 = PresoTemporal( "Miguel", "Ninguno", "Yakuza", 5, True, 3, True, 4)
preso_temporal2 = PresoTemporal( "Antonio", "Secundario", "Latinos", 3, False, 2, False, 2)
preso_temporal3 = PresoTemporal( "Pedro", "Preuniversitario", "Blancos", 7, True, 5, True, 3)

preso_foso1 = PresoPermanente( "Jose", "Sencundario", "Blancos", 15, True, 5, "Excelente", "Bien")
preso_foso2 = PresoTemporal( "Luis", "Secundario", "Latinos", 4, False, 2, True, 3)

grupo_foso1 = Grupo_guardia(2, 4, 12, True, 35)
grupo_foso2 = Grupo_guardia(5, 6, 7, False, 15)

celda1 = Celda( 1, preso1, grupo1 )
celda2 = Celda( 2, preso_temporal1, grupo2 )
celda3 = Celda( 3,  preso2, grupo3 )
celda4 = Celda( 4, preso_temporal2, grupo4 )
celda5 = Celda( 5,  preso3, grupo5 )
celda6 = Celda( 6, preso_temporal3, grupo6 )

lista_celdas = [ celda1, celda2, celda3, celda4, celda5, celda6]

pila_foso = Foso()

pila_foso.apilar( preso_foso1, grupo_foso1, 9)
pila_foso.apilar( preso_foso2, grupo_foso2, 8)

#1. Transcurrir un día

def transcurrir_dia():
   
    primera_celda = lista_celdas.pop(0)
    lista_celdas.append(primera_celda)

    pila_foso.disminuir_dia()

    foso_aux = Foso()
 
    while not pila_foso.esta_vacio():

        top_foso = pila_foso.extraer_cima_actual_foso()

        if ( top_foso.dias_restantes == 0 ):

            celda_aux = Celda( len(lista_celdas), top_foso.preso, top_foso.grupo_guardia )
            lista_celdas.append(celda_aux)

        else:

            foso_aux.apilar(top_foso.preso, top_foso.grupo_guardia, top_foso.get_dias_restantes() )


    while not foso_aux.esta_vacio():

        top_foso = foso_aux.extraer_cima_actual_foso()

        pila_foso.apilar( top_foso.preso, top_foso.grupo_guardia, top_foso.get_dias_restantes() )

    print('Dia transcurrido ')

# imprimir lista de presos

def imprimir_lista_presos():

    i = 0

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numero de celda - Nombre - Nivel de escolaridad - Pandilla - Años de condena - Asesinato - Prestigio - Tipo de Preso - Relación guardia - Relación preso - Experiencia combate - Nivel de adaptación')
    tabla = [ ]

    for celda in lista_celdas:

        if isinstance( celda.get_preso(), PresoPermanente ):

            fila = [ f'{i+1}', f'{celda.get_preso().get_nombre()}', f'{celda.get_preso().get_nivel_escolaridad()}', f'{celda.get_preso().get_pandilla()}', f'{celda.get_preso().get_annos_condena()}', f'{celda.get_preso().get_asesinato()}', f'{celda.get_preso().get_prestigio()}', 'Permanente' ,f'{celda.get_preso().get_relacion_guardia()}', f'{celda.get_preso().get_relacion_resto_presos()}', '-', '-' ]

            tabla.append( fila )

        elif isinstance( celda.get_preso(), PresoTemporal):
            
            fila = [ f'{i+1}', f'{celda.get_preso().get_nombre()}', f'{celda.get_preso().get_nivel_escolaridad()}', f'{celda.get_preso().get_pandilla()}', f'{celda.get_preso().get_annos_condena()}', f'{celda.get_preso().get_asesinato()}', f'{celda.get_preso().get_prestigio()}', 'Temporal' ,'-', '-', f'{celda.get_preso().get_experiencia_combate()}', f'{celda.get_preso().get_nivel_adaptacion()}' ]

            tabla.append( fila )
        
        i = i + 1

    
    for fila in tabla:
        print("{:<17} {:<9} {:<22} {:<15} {:<13} {:<10} {:<12} {:<15} {:<20} {:<20} {:<25} {:<20}".format(*fila))

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def imprimir_presos_foso():

    pila_foso.imprimir()

# crear un guardia
def crear_grupoGuardia():

    cant_vigilantes = 0
    exp_promedio = 0
    extrictos = 0
    confiabilidad = False
    tiempo_respuesta = 0

    print('-----------------------')
    print('Crear grupo de guardia')
    print('-----------------------')

    print()

    while True:
        cant_vigilantes_str = input('Ingrese la cantidad de vigilantes (1 - 5): \n')

        cant_vigilantes = int(cant_vigilantes_str)

        if cant_vigilantes >= 1 and cant_vigilantes <= 5:
            break
        else:
            print('La cantidad de vigilantes debe de ser entre 1 y 5')

    print()
    
    while True:
        exp_promedio_str = input('Ingrese la experiencia promedio (1 - 10): \n')

        exp_promedio = int(exp_promedio_str)

        if exp_promedio >= 1 and exp_promedio <= 10:
            break
        else:
            print('La experiencia promedio debe ser entre 1 y 10')

    print()

    while True:

        extrictos_str = input('Ingrese que tan extrictos son con los presos (1-15): \n')

        extrictos = int(extrictos_str)

        if extrictos >= 1 and exp_promedio <= 15:
            break
        else:
            print('Debe ser entre 1 y 15')
    
    print()

    while True:
            
        confiabilidad_str = input('¿El grupo tiende a confiarse en horas altas? \n')

        if confiabilidad_str.lower() == 'si' or confiabilidad_str.lower() == 'sí':
            confiabilidad = True
            break
        elif confiabilidad_str.lower() == 'no':
            confiabilidad = False
            break
        else:
            print('La confiabilidad debe ser si o no')

    print()

    while True: 

        tiempo_respuesta_str = input('Ingrese el tiempo de respueta de la policía (15-45) : \n' )

        tiempo_respuesta = int(tiempo_respuesta_str)

        if tiempo_respuesta >= 15 and tiempo_respuesta <= 45:
            break
        else:
            print('El tiempo de respuesta debe ser entre 15 y 45')

    grupo_guardia = ( cant_vigilantes, exp_promedio, extrictos, confiabilidad, tiempo_respuesta )

    return grupo_guardia

# crear un preso
def crear_preso():

    preso_opcion = ''
    nombre = ''
    nivel_escolaridad = ''
    pandilla = ''
    annos_condena = 0
    asesinato = ''
    prestigio = ''
    relacion_guardia = ''
    relacion_presos = ''
    exp_combate = False
    nivel_adaptacion = 0

    print('-----------------')
    print('Crear prisionero')
    print('-----------------')

    while True:

        print('Elige el preso \n ' + '1. Preso Temporal' + '\n 2. Preso Permanente')
        preso_opcion = input()

        if preso_opcion == '1':
            break
        elif preso_opcion == '2':
            break
        else:
            print('Debes elegir entre 1 y 2')

    print()

    nombre = input('¿Cuál es el nombre del prisionero? \n')

    print()
    
    while True:

        print('Elige el nivel de escolaridad \n ' + '1. Ninguno' + '\n 2. Secundario' + '\n 3. Preuniversitario' + '\n 4.Universitario')
        nivel_escolaridad_str = input()

        if nivel_escolaridad_str == '1':
            nivel_escolaridad = 'Ninguno'
            break
        elif nivel_escolaridad_str == '2':
            nivel_escolaridad = 'Secundario'
            break
        elif nivel_escolaridad_str == '3':
            nivel_escolaridad = 'Preuniversitario'
            break
        elif nivel_escolaridad_str == '4':
            nivel_escolaridad = 'Universitario'
            break
        else:
            print('El nivel de escolaridad es incorrecto')

    print()

    while True:

        print('Elige a que pandilla pertenece \n ' + '1. Yakuza' + '\n 2. Latinos' + '\n 3. Blancos' + '\n 4. Afros')
        pandilla_str = input()

        if pandilla_str == '1':
            pandilla = 'Yakuza'
            break
        elif pandilla_str == '2':
            pandilla = 'Latinos'
            break
        elif pandilla_str == '3':
            pandilla = 'Blancos'
            break
        elif pandilla_str == '4':
            pandilla = 'Afros'
            break
        else:
            print('La pandilla es incorrecta')

    annos_condena_str = input('¿Cuántos años de condena tiene: ? \n')

    annos_condena = int(annos_condena_str)

    print()
    
    while True:
            
        asesinatos_str = input('¿El preso cometió asesinatos o no ? \n')

        if asesinatos_str.lower() == 'si' or asesinatos_str.lower() == 'sí':
            asesinato = True
            break
        elif asesinatos_str.lower() == 'no':
            asesinato = False
            break
        else:
            print('La respuesta debe ser si o no')

    print()

    while True:

        prestigio_str = input('Ingrese el prestigio del preso (1-15): \n')

        prestigio = int(prestigio_str)

        if prestigio >= 1 and prestigio <= 15:
            break
        else:
            print('El prestigio debe ser entre 1 y 15')

    if preso_opcion == '1':

        print()

        exp_combate_str = input('¿El preso tiene experiencia en combate? \n')

        if exp_combate_str.lower() == 'si' or exp_combate_str.lower() == 'sí':
            exp_combate = True
        else:
            exp_combate = False

        while True:

            print()

            nivel_adaptacion_str = input('Que nivel de adaptacion tiene este preso: (1-15) \n')

            nivel_adaptacion = int(nivel_adaptacion_str)

            if nivel_adaptacion >= 1 or nivel_adaptacion <= 5:
                break
            else:
                print('El nivel de adaptacion debe ser un número entre 1 y 5')

        preso_temporal = PresoTemporal( nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio, exp_combate, nivel_adaptacion  )

        return preso_temporal

    else:

        while True:

            print()

            print('Eliga como es la relación con los guardias \n' + ' 1.Excelente' + '\n 2.Buena' + '\n 3.Mal')
            relacion_guardia_str = input()

            if relacion_guardia_str == '1':
                relacion_guardia = 'Excelente'
                break
            elif relacion_guardia_str == '2':
                relacion_guardia = 'Buena'
                break
            elif relacion_guardia_str == '3':
                relacion_guardia = 'Mal'
                break
            else:
                print('La relación debe ser entre 1 y 3')

        while True:

            print()

            print('Eliga como es la relación con los demás preso \n ' + ' 1. Excelente' + '\n 2.Buena' + '\n 3.Mal')

            relacion_presos_str = input()

            if relacion_presos_str == '1':
                relacion_presos = 'Excelente'
                break
            elif relacion_presos_str == '2':
                relacion_presos = 'Buena'
                break
            elif relacion_presos_str == '3':
                relacion_presos = 'Mal'
                break
            else:
                print('La relación debe ser entre 1 y 3')

        preso_permanente = PresoPermanente( nombre, nivel_escolaridad, pandilla, annos_condena, asesinato, prestigio, relacion_guardia, relacion_presos)

        return preso_permanente


def crear_celda():

    grupo_guardia = crear_grupoGuardia()
    preso = crear_preso()

    print( 'Esta es la nueva celda que queremos crear', len( lista_celdas ) , preso, grupo_guardia )

    celda = Celda( len(lista_celdas) + 1, preso, grupo_guardia )

    lista_celdas.append(celda)

def tiempo_fuga( preso ):

    tiempo_fuga_prisionero = 0

    if isinstance( preso, PresoPermanente):
        
        if preso.get_nivel_escolaridad == 'Universidad' and preso.get_relacion_guardia == 'Excelente':
            tiempo_fuga_prisionero = 15
        elif preso.get_nivel_escolaridad == 'Universidad' and preso.get_relacion_guardia == "Buena":
            tiempo_fuga_prisionero = 20
        else:
            tiempo_fuga_prisionero = 35

    elif isinstance (preso, PresoTemporal):
        
        if preso.get_nivel_adaptacion == 5:
            tiempo_fuga_prisionero = 30
        else:
            tiempo_fuga_prisionero = 40

    return tiempo_fuga_prisionero
    
def fuga( pos ):

    preso_primera_celda = lista_celdas[ pos ].get_preso()
    grupo_guardia_primera_celda = lista_celdas[ pos ].get_grupo_guardia()

    tiempo_fuga_preso = tiempo_fuga( preso_primera_celda )

   
    if tiempo_fuga_preso < grupo_guardia_primera_celda.get_tiempo_respuesta():

        return 0

    else:

        return preso_primera_celda

#2. Fuga individual
        
def fuga_individual():

    valor = fuga( 0 )

    if valor == 0:
        lista_celdas.pop(0) 
        print('El recluso se logro escapar')
    else:

        lista_celdas[0].get_preso().set_annos_condena( lista_celdas[0].get_preso().get_annos_condena() + 1 )

        pila_foso.apilar( lista_celdas[0].get_preso(), lista_celdas[0].get_grupo_guardia(), 10 )
        lista_celdas.pop(0)

        print('El recluso fue capturado, llevado al foso y se le aumento un año en su condena')

def fuga_en_grupo( cant_presos ):

    lista_presos_fuga_grupo = []
    lista_presos_mismo_prestigio = []
    listas_pos = []
    pos_mayor_prestigio = 0

    for i in range(cant_presos):

        valor = fuga( i )

        if not valor == 0:
            lista_presos_fuga_grupo.append(lista_celdas[i].get_preso())

    if len(lista_presos_fuga_grupo) >=1 and len(lista_presos_fuga_grupo) <= cant_presos:

        maximo_prestigio = lista_presos_fuga_grupo[0].get_prestigio()

        for i in range( len ( lista_presos_fuga_grupo) ):

            if maximo_prestigio < lista_presos_fuga_grupo[i].get_prestigio():
                maximo_prestigio = lista_presos_fuga_grupo[i].get_prestigio()
                pos_mayor_prestigio = i

        
        for i in range( len ( lista_presos_fuga_grupo )):
           
            if maximo_prestigio == lista_presos_fuga_grupo[i].get_prestigio():
                lista_presos_mismo_prestigio.append( lista_presos_fuga_grupo[i] )
                listas_pos.append(i)

        if len(lista_presos_mismo_prestigio) == 1:
           
            # Sumar un ano de condena a cada integrante:
                    
            for i in range ( cant_presos ):

                lista_celdas[i].get_preso().set_annos_condena( lista_celdas[i].get_preso().get_annos_condena() + 1 )

            pila_foso.apilar( lista_celdas[pos_mayor_prestigio].get_preso(), lista_celdas[i].get_grupo_guardia(), 10)

            lista_celdas.pop(pos_mayor_prestigio)

            print('Intento de fuga grupal fallido y su lider llevado al foso')

        else:

            mayor_tiempo_fuga_individual = ( tiempo_fuga(lista_presos_mismo_prestigio[0]) + (cant_presos - 1) )

            for i in range( len(lista_presos_mismo_prestigio) ):

                if mayor_tiempo_fuga_individual < ( tiempo_fuga(lista_presos_mismo_prestigio[i]) + (cant_presos - 1) ):
                    mayor_tiempo_fuga_individual = tiempo_fuga(lista_presos_mismo_prestigio[i]) + (cant_presos - 1)
                    pos_mayor_prestigio = listas_pos[i]

            # Sumar un ano de condena a cada integrante:
                    
            for i in range ( cant_presos ):

                lista_celdas[i].get_preso().set_annos_condena( lista_celdas[i].get_preso().get_annos_condena() + 1 )

            pila_foso.apilar(lista_celdas[pos_mayor_prestigio].get_preso(), lista_celdas[pos_mayor_prestigio].get_grupo_guardia(), 10  )

            lista_celdas.pop(pos_mayor_prestigio)

            print('Intento de fuga grupal fallido y su lider llevado al foso')

    else: 
        print('Intengo de fuga por grupo exitosa')


def nivel_peligrosidad( preso ):

    nivel_peligrosidad = 1

    if isinstance( preso, PresoPermanente):

        if preso.get_relacion_resto_presos() == 'Excelente':
            nivel_peligrosidad = 5 + nivel_peligrosidad + preso.get_prestigio()
        elif preso.get_relacion_resto_presos() == 'Buena':
            nivel_peligrosidad = 3 + nivel_peligrosidad + preso.get_prestigio()
        elif preso.get_relacion_resto_presos() == 'Mala':
            nivel_peligrosidad =  ( nivel_peligrosidad + preso.get_prestigio() ) - 1
        else:
             nivel_peligrosidad = nivel_peligrosidad + preso.get_prestigio()

    elif isinstance( preso, PresoTemporal):
            
        if preso.get_experiencia_combate() == True:
            nivel_peligrosidad = nivel_peligrosidad + preso.get_nivel_adaptacion() + preso.get_nivel_adaptacion() + 3
        else:
            nivel_peligrosidad = nivel_peligrosidad + preso.get_nivel_adaptacion() + preso.get_nivel_adaptacion()

    return nivel_peligrosidad


def pelea_entre_reclusos( pos1, pos2 ):

    preso1 = lista_celdas[pos1 - 1].get_preso()
    preso2 = lista_celdas[pos2 - 1].get_preso()
    nivel_peligrosidad_preso1 = 0
    nivel_peligrosidad_preso2 = 0

    if preso1.get_pandilla() == preso2.get_pandilla():
        print('Etos reclusos no pueden pelear')
    else:
        nivel_peligrosidad_preso1 = nivel_peligrosidad( preso1 )
        nivel_peligrosidad_preso2 = nivel_peligrosidad( preso2 )

        if nivel_peligrosidad_preso1 > nivel_peligrosidad_preso2:
           
           lista_celdas[ pos1 - 1 ].get_preso().set_annos_condena(  lista_celdas[ pos1 - 1 ].get_preso().get_annos_condena() + 3 )

           pila_foso.apilar( lista_celdas[pos1 - 1].get_preso(), lista_celdas[ pos1 - 1].get_grupo_guardia(), 10 )

           lista_celdas.pop( pos1 - 1 )
           lista_celdas.pop( pos2 - 1 )

           print(f'En esta pelea ganó el preso 1: {lista_celdas[ pos1 - 1].get_preso().get_nombre()}')

        else:

           lista_celdas[ pos2 - 1 ].get_preso().set_annos_condena(  lista_celdas[ pos2 - 1 ].get_preso().get_annos_condena() + 3 )

           pila_foso.apilar( lista_celdas[pos2 - 1].get_preso(), lista_celdas[ pos2 - 1].get_grupo_guardia(), 10)

           lista_celdas.pop( pos2 - 1 )
           lista_celdas.pop( pos1 - 1 )

           print(f'En esta pelea ganó el preso 2: {lista_celdas[ pos2 - 1].get_preso().get_nombre()}')


def listado_reclusos_ordenados_anno_condena():

    lista_celdas_ordenadas = sorted( lista_celdas, key = lambda celda: celda.get_preso().get_annos_condena(), reverse = True )

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numero de celda - Nombre - Nivel de escolaridad - Pandilla - Años de condena - Asesinato - Prestigio - Tipo de Preso - Relación guardia - Relación preso - Experiencia combate - Nivel de adaptación')
    tabla = [ ]

    i = 0

    for celda in lista_celdas_ordenadas:

        if isinstance( celda.get_preso(), PresoPermanente ):

            fila = [ f'{i+1}', f'{celda.get_preso().get_nombre()}', f'{celda.get_preso().get_nivel_escolaridad()}', f'{celda.get_preso().get_pandilla()}', f'{celda.get_preso().get_annos_condena()}', f'{celda.get_preso().get_asesinato()}', f'{celda.get_preso().get_prestigio()}', 'Permanente' ,f'{celda.get_preso().get_relacion_guardia()}', f'{celda.get_preso().get_relacion_resto_presos()}', '-', '-' ]

            tabla.append( fila )

        elif isinstance( celda.get_preso(), PresoTemporal):
            
            fila = [ f'{i+1}', f'{celda.get_preso().get_nombre()}', f'{celda.get_preso().get_nivel_escolaridad()}', f'{celda.get_preso().get_pandilla()}', f'{celda.get_preso().get_annos_condena()}', f'{celda.get_preso().get_asesinato()}', f'{celda.get_preso().get_prestigio()}', 'Temporal' ,'-', '-', f'{celda.get_preso().get_experiencia_combate()}', f'{celda.get_preso().get_nivel_adaptacion()}' ]

            tabla.append( fila )
        
        i = i + 1

    
    for fila in tabla:
        print("{:<17} {:<9} {:<22} {:<15} {:<13} {:<10} {:<12} {:<15} {:<20} {:<20} {:<25} {:<20}".format(*fila))

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
       

def reclusos_mas_tiempo_foso():

    lista_presos_max_dias = pila_foso.presos_con_max_dias()

    i = len( lista_presos_max_dias )

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Numero de celda - Nombre - Nivel de escolaridad - Pandilla - Años de condena - Asesinato - Prestigio - Tipo de Preso - Relación guardia - Relación preso - Experiencia combate - Nivel de adaptación')
    tabla = [ ]

    for preso in lista_presos_max_dias:

        if isinstance( preso, PresoPermanente ):

            fila = [ f'{i}', f'{preso.get_nombre()}', f'{preso.get_nivel_escolaridad()}', f'{preso.get_pandilla()}', f'{preso.get_annos_condena()}', f'{preso.get_asesinato()}', f'{preso.get_prestigio()}', 'Permanente' ,f'{preso.get_relacion_guardia()}', f'{preso.get_relacion_resto_presos()}', '-', '-' ]

            tabla.append( fila )

        elif isinstance( preso, PresoTemporal):
            
            fila = [ f'{i}', f'{preso.get_nombre()}', f'{preso.get_nivel_escolaridad()}', f'{preso.get_pandilla()}', f'{preso.get_annos_condena()}', f'{preso.get_asesinato()}', f'{preso.get_prestigio()}', 'Temporal' ,'-', '-', f'{preso.get_experiencia_combate()}', f'{preso.get_nivel_adaptacion()}' ]

            tabla.append( fila )
        
        i = i - 1

    
    for fila in tabla:
        print("{:<17} {:<9} {:<22} {:<15} {:<13} {:<10} {:<12} {:<15} {:<20} {:<20} {:<25} {:<20}".format(*fila))

    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def menu():

    while True:

        print()
        print('---------------------------------------')
        print('Eliga una opcion: ')
        print('1. Crear celda')
        print('2. Transcurrir un día')
        print('3. Fuga de un preso')
        print('4. Fuga de un grupo de presos')
        print('5. Pelea entre varios reclusos')
        print('6. Listado con reclusos por annos de condena')
        print('7. Lista de reclusos con mas tiempo en el foso')
        print('8. Listas de presos')
        print('9. Imprimir presos del foso ')
        print('10. Salir')
        print('---------------------------------------')
        opcion = input()

        print()

        if opcion == '1':         

            crear_celda()

        elif opcion == '2':

            
            transcurrir_dia()
           

        elif opcion == '3':

            fuga_individual()

        elif opcion == '4':

            cant_presos_str = input('Eliga la cantidad de presos a fugarse en grupo: \n')
            cant_presos = int(cant_presos_str)

            if cant_presos <= len( lista_celdas ):

                fuga_en_grupo( cant_presos )

            else:

                print('La cantidad de presos no puede exceder a la cantidad de celdas \n')
            
        elif opcion == '5':

            while True:

                pos_primer_recluso_str = input('Eliga la posicion del primer recluso \n')
                pos_segundo_recluso_str = input('Eliga la posicion del segundo recluso \n')

                pos_primer_recluso = int( pos_primer_recluso_str )
                pos_segundo_recluso = int( pos_segundo_recluso_str )

                if pos_primer_recluso <= len( lista_celdas ) and pos_segundo_recluso <= len( lista_celdas ):
                  
                    pelea_entre_reclusos( pos_primer_recluso, pos_segundo_recluso )
                    break
               
                else:
                    print('Escriba posiciones correctas')

        elif opcion == '6':

            listado_reclusos_ordenados_anno_condena()

        elif opcion == '7':

            reclusos_mas_tiempo_foso()

        elif opcion == '8':

            imprimir_lista_presos()

        elif opcion == '9':

            imprimir_presos_foso()

        elif opcion == '10':
            break

    

menu()     










    



