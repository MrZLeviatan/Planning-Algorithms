<h1 align="center">

_First Come First Server (FCFS)_

</h1>

It is a simple, non-preemptive scheduling algorithm where processes are executed in the order they arrive. No priority is given to any process, meaning the first to arrive is the first to be executed without interruption.
>***Es un algoritmo de programación simple y no preventivo en el que los procesos se ejecutan en el orden en que llegan. No se le da prioridad a ningún proceso, lo que significa que el primero en llegar es el primero en ejecutarse sin interrupción.***

---

## 🌟 Features / Características
- **Type** : Non-preemptive.
- **Execution Order**: The process that arrives first is executed first.
- **Advantages**: Simple to implement.
- **Disadvantages**: Can cause long wait times for shorter processes if a longer one arrives first (convoy effect).

>- **Tipo**: No preventivo.
>- **Orden de Ejecucion**: El proceso que llega primero es el que se ejecuta primero.
>- **Ventajas**: Sencillo de implementar.
>- **Desventajas**: Puede causar tiempos de espera largos para procesos cortos si uno mas largo llega antes (efecto convoy).

---

## 🛠️ Program Function / Funcion del Programa
This program implements the FCFS algorithm to simulate process scheduling. Given a set of processes with their arrival times and execution times, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, which is the total time a process spends in the system.
>***Este programa implementa el algoritmo FCFS para simular la planificacion de procesos. Dado un conjunto de procesos con sus tiempos de llegada y tiempos de ejecucion, el programa calculara:***
>- Tiempo de finalizacion de cada proceso.
>- Tiempo de espera para cada proceso.
>- Tiempo de retorno (o turnaround time), que es el tiempo total que un proceso pasa en el sistema.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the FCFS script, navigate to the directory where the "FCFS.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script FCFS, navegue hasta el directorio donde se encuentra el archivo "FCFS.py" y ejecute el siguiente        comando en la terminal:***

    ```bash
        python FCFS.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
   Process | Arrival Time | Execution Time | Completion Time | Waiting Time | Turnaround Time
    ------------------------------------------------------------------------------------------
    P1      |      0      |       4        |        4        |      0      |       4
    P2      |      1      |       3        |        7        |      3      |       6
    P3      |      2      |       2        |        9        |      5      |       7
    ```
---

## 🧩 [Program / Programa](/FCFS/FCFS.py)

```python
class Proceso:
    #El método __init__ es el constructor de la clase.
    def __init__(self, id, tiempo_llegada, tiempo_ejecucion):
        self.id = id # Identificador de cada procesos.
        self.tiempo_llegada = tiempo_llegada # Tiempo en el que el proceso llega al sistema.
        self.tiempo_ejecucion = tiempo_ejecucion # La duración que el proceso requiere para ejecutarse.
        self.tiempo_espera = 0
        self.tiempo_finalizacion = 0
        self.tiempo_retorno = 0

def calcular_fcfs(procesos):
    tiempo_actual = 0

    for proceso in procesos:
        proceso.tiempo_espera = max(0, tiempo_actual - proceso.tiempo_llegada)

        proceso.tiempo_finalizacion = tiempo_actual + proceso.tiempo_ejecucion

        proceso.tiempo_retorno = proceso.tiempo_finalizacion - proceso.tiempo_llegada

        tiempo_actual += proceso.tiempo_ejecucion

def imprimir_resultados(procesos):
    print(f"{'Proceso':<10}{'Llegada':<10}{'Ejecución':<10}{'Espera':<10}{'Retorno':<10}{'Finalización':<15}")
    for proceso in procesos:
        print(f"{proceso.id:<10}{proceso.tiempo_llegada:<10}{proceso.tiempo_ejecucion:<10}{proceso.tiempo_espera:<10}{proceso.tiempo_retorno:<10}{proceso.tiempo_finalizacion:<15}")

procesos = [
    Proceso("P1", 1, 5),
    Proceso("P2", 4, 3),
    Proceso("P3", 3, 1),
    Proceso("P4", 2, 2)
]

procesos.sort(key=lambda p: p.tiempo_llegada)

calcular_fcfs(procesos)

imprimir_resultados(procesos)
```
    
