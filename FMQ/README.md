<h1 align="center">

_Planificación Multinivel (FMQ)_

</h1>

The FMQ (Fair Minimum Queue) scheduling algorithm is a non-preemptive scheduling algorithm that organizes processes based on their burst time. This algorithm prioritizes processes with shorter burst times and separates them into high and low priority categories.

>***El algoritmo FMQ (Cola Mínima Justa) es un algoritmo de planificación no preventivo que organiza los procesos según su tiempo de ráfaga. Este algoritmo prioriza los procesos con tiempos de ráfaga más cortos y los separa en categorías de alta y baja prioridad.***

---

## 🌟 Features / Características
- **Type**: Non-preemptive.
- **Execution Order**: Processes are divided into high and low priority based on their burst times.
- **Advantages**: Efficient for processes with shorter burst times, minimizes average waiting time.
- **Disadvantages**: May lead to starvation for longer processes.

> - **Tipo**: No preventivo.
> - **Orden de Ejecución**: Los procesos se dividen en alta y baja prioridad según sus tiempos de ráfaga.
> - **Ventajas**: Eficiente para procesos con tiempos de ráfaga más cortos, minimiza el tiempo de espera promedio.
> - **Desventajas**: Puede provocar inanición en procesos más largos.

---

## 🛠️ Program Function / Función del Programa

This program implements the FMQ algorithm to simulate process scheduling. Given a set of processes with their burst times, the program will calculate:

- Waiting time for each process.
- Turnaround time for each process.
  
> ***Este programa implementa el algoritmo FMQ para simular la programación de procesos. Dado un conjunto de procesos con sus tiempos de ráfaga, el programa calculará:***
> - Tiempo de espera de cada proceso.
> - Tiempo de retorno de cada proceso.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the FMQ script, navigate to the directory where the "FMQ.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script FMQ, navegue hasta el directorio donde se encuentra el archivo "FMQ.py" y ejecute el siguiente comando en la terminal:***

    ```bash
        python FMQ.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
        Resultado de la programación FMQ - Alta Prioridad:
        Proceso   Tiempo de Espera    Tiempo de Retorno
        P1        0                   10
        P4        10                  15
        P6        15                  27
    ```

    ```bash
        Resultado de la programación FMQ - Baja Prioridad:
        Proceso   Tiempo de Espera    Tiempo de Retorno
        P2        0                   20
        P3        20                  50
        P5        50                  75
    ```

---

## 🧩 [Program / Programa](/FMQ/FMQ.py)

```python
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

procesos = [
    Proceso("P1", 10),
    Proceso("P2", 20),
    Proceso("P3", 30),
    Proceso("P4", 5),
    Proceso("P5", 7),
    Proceso("P6", 12)
]

alta_prioridad = [p for p in procesos if p.tiempo_burst < 15]
baja_prioridad = [p for p in procesos if p.tiempo_burst >= 15]

calcular_tiempos(alta_prioridad)
imprimir_tabla(alta_prioridad, "Alta")

calcular_tiempos(baja_prioridad)
imprimir_tabla(baja_prioridad, "Baja")
```