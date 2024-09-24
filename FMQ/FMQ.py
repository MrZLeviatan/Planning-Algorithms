class Proceso:
    def __init__(self, nombre, tiempo_burst):
        self.nombre = nombre
        self.tiempo_burst = tiempo_burst
        self.tiempo_espera = 0
        self.tiempo_retorno = 0

def calcular_tiempos(procesos):
    tiempo_total = 0
    for p in procesos:
        p.tiempo_espera = tiempo_total
        tiempo_total += p.tiempo_burst
        p.tiempo_retorno = p.tiempo_espera + p.tiempo_burst

def imprimir_tabla(procesos, prioridad):
    print(f"\nResultado de la programación FMQ - {prioridad} Prioridad:")
    print("Proceso   Tiempo de Espera    Tiempo de Retorno")
    for p in procesos:
        print(f"{p.nombre}        {p.tiempo_espera}                   {p.tiempo_retorno}")

# Datos de entrada
procesos = [
    Proceso("P1", 10),
    Proceso("P2", 20),
    Proceso("P3", 30),
    Proceso("P4", 5),
    Proceso("P5", 7),
    Proceso("P6", 12)
]

# Separar procesos en alta y baja prioridad
alta_prioridad = [p for p in procesos if p.tiempo_burst < 15]
baja_prioridad = [p for p in procesos if p.tiempo_burst >= 15]

# Calcular tiempos para alta prioridad
calcular_tiempos(alta_prioridad)
imprimir_tabla(alta_prioridad, "Alta")

# Calcular tiempos para baja prioridad
calcular_tiempos(baja_prioridad)
imprimir_tabla(baja_prioridad, "Baja")
