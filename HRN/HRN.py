# Definir una clase para almacenar los detalles de cada proceso
class Proceso:
    def __init__(self, id, tiempo_llegada, tiempo_ejecucion):
        self.id = id                        # ID del proceso
        self.tiempo_llegada = tiempo_llegada  # Tiempo de llegada del proceso
        self.tiempo_ejecucion = tiempo_ejecucion  # Tiempo de ejecución (ráfaga) del proceso
        self.tiempo_espera = 0              # Tiempo de espera inicializado en 0
        self.tiempo_respuesta = 0           # Tiempo de respuesta inicializado en 0
        self.tiempo_finalizacion = 0        # Tiempo de finalización inicializado en 0
        self.ratio_respuesta = 0            # Ratio de respuesta inicializado en 0


# Función para calcular el ratio de respuesta
def calcular_ratio_respuesta(proceso, tiempo_actual):
    # El tiempo de espera es la diferencia entre el tiempo actual y el tiempo de llegada
    tiempo_espera = tiempo_actual - proceso.tiempo_llegada
    # El ratio de respuesta se calcula como (tiempo de espera + tiempo de ráfaga) / tiempo de ráfaga
    ratio_respuesta = (tiempo_espera + proceso.tiempo_ejecucion) / proceso.tiempo_ejecucion
    return ratio_respuesta


# Función que implementa el algoritmo HRN de planificación
def planificacion_hrn(procesos):
    tiempo = 0  # Inicializar el tiempo actual del sistema a 0
    procesos_completados = []  # Lista para almacenar los procesos completados

    # Mientras queden procesos por ejecutar
    while procesos:
        # Filtrar los procesos que han llegado hasta el tiempo actual
        procesos_disponibles = [p for p in procesos if p.tiempo_llegada <= tiempo]
        
        # Si no hay procesos disponibles, avanzar el tiempo
        if not procesos_disponibles:
            tiempo += 1
            continue

        # Calcular el ratio de respuesta para cada proceso disponible
        for p in procesos_disponibles:
            p.ratio_respuesta = calcular_ratio_respuesta(p, tiempo)

        # Seleccionar el proceso con el mayor ratio de respuesta
        proceso_siguiente = max(procesos_disponibles, key=lambda p: p.ratio_respuesta)

        # Actualizar el tiempo al momento en que el proceso finaliza
        tiempo += proceso_siguiente.tiempo_ejecucion
        proceso_siguiente.tiempo_finalizacion = tiempo

        # Calcular el tiempo de respuesta y el tiempo de espera
        proceso_siguiente.tiempo_respuesta = proceso_siguiente.tiempo_finalizacion - proceso_siguiente.tiempo_llegada
        proceso_siguiente.tiempo_espera = proceso_siguiente.tiempo_respuesta - proceso_siguiente.tiempo_ejecucion

        # Añadir el proceso completado a la lista
        procesos_completados.append(proceso_siguiente)
        # Eliminar el proceso de la lista de pendientes
        procesos.remove(proceso_siguiente)

    # Imprimir los resultados en forma de tabla
    print("\n{:<10} {:<10} {:<15} {:<15} {:<10} {:<10}".format("ID", "Llegada", "Ejecución", "Finalización", "Espera", "Respuesta"))
    for p in procesos_completados:
        print("{:<10} {:<10} {:<15} {:<15} {:<10} {:<10}".format(p.id, p.tiempo_llegada, p.tiempo_ejecucion, p.tiempo_finalizacion, p.tiempo_espera, p.tiempo_respuesta))


# Procesos con datos quemados
procesos = [
    Proceso(1, 0, 8),  # Proceso 1 llega en t=0 y tiene una ráfaga de 8 unidades de tiempo
    Proceso(2, 1, 10),  # Proceso 2 llega en t=1 y tiene una ráfaga de 4 unidades de tiempo
    Proceso(3, 2, 2),  # Proceso 3 llega en t=2 y tiene una ráfaga de 9 unidades de tiempo
    Proceso(4, 3, 4)   # Proceso 4 llega en t=3 y tiene una ráfaga de 5 unidades de tiempo
]

# Ejecutar la planificación HRN
planificacion_hrn(procesos)
