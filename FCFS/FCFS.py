# Definimos una clase para los procesos
class Proceso:
    #El método __init__ es el constructor de la clase.
    def __init__(self, id, tiempo_llegada, tiempo_ejecucion):
        self.id = id # Identificador de cada procesos.
        self.tiempo_llegada = tiempo_llegada # Tiempo en el que el proceso llega al sistema.
        self.tiempo_ejecucion = tiempo_ejecucion # La duración que el proceso requiere para ejecutarse.
        self.tiempo_espera = 0
        self.tiempo_finalizacion = 0
        self.tiempo_retorno = 0

# Función para calcular los tiempos de espera, retorno y finalización
def calcular_fcfs(procesos):
    tiempo_actual = 0

    for proceso in procesos:
        # El tiempo de espera es el tiempo actual menos el tiempo de llegada
        proceso.tiempo_espera = max(0, tiempo_actual - proceso.tiempo_llegada)

        # El tiempo de finalización es el tiempo actual más el tiempo de ejecución del proceso
        proceso.tiempo_finalizacion = tiempo_actual + proceso.tiempo_ejecucion

        # El tiempo de retorno es el tiempo de finalización menos el tiempo de llegada
        proceso.tiempo_retorno = proceso.tiempo_finalizacion - proceso.tiempo_llegada

        # Actualizamos el tiempo actual
        tiempo_actual += proceso.tiempo_ejecucion

# Función para imprimir los resultados
def imprimir_resultados(procesos):
    print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Espera':<10}{'Retorno':<10}{'Finalización':<15}")
    # :<10 formatea el texto para que ocupe un espacio de 10 caracteres, alineado a la izquierda, lo que genera una tabla bien formateada.
    for proceso in procesos:
        print(f"{proceso.id:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}{proceso.tiempo_finalizacion:<15}")

# Lista de procesos (ID, Tiempo de llegada, Tiempo de ejecución)
procesos = [
    Proceso("P1", 1, 5),
    Proceso("P2", 4, 3),
    Proceso("P3", 3, 1),
    Proceso("P4", 2, 2)
]

# Ordenamos los procesos por tiempo de llegada
procesos.sort(key=lambda p: p.tiempo_llegada)

# Calculamos los tiempos para cada proceso
calcular_fcfs(procesos)

# Imprimimos los resultados
imprimir_resultados(procesos)
