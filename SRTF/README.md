<h1 align="center">

_Shortest Remaining Time First (SRTF)_

</h1>

The SRTF (Shortest Remaining Time First) is a preemptive version of the SJF (Shortest Job First) algorithm. It schedules processes based on the shortest remaining execution time. When a new process arrives and has a shorter remaining time than the currently running process, the current process is preempted, and the new one starts executing.
>***SRTF (Shortest Remaining Time First) es una versión preventiva del algoritmo SJF (Shortest Job First). Programa los procesos en función del menor tiempo restante de ejecución. Cuando llega un nuevo proceso y tiene un tiempo restante más corto que el proceso que se está ejecutando actualmente, el proceso actual se interrumpe y el nuevo comienza a ejecutarse.***

---

## 🌟 Features / Características
- **Type**: Preemptive.
- **Execution Order**: The process with the shortest remaining time is executed first.
- **Advantages**: Minimizes average waiting time and turnaround time more effectively than non-preemptive   algorithms.
- **Disadvantages**: Can lead to frequent context switching and process starvation for longer tasks.

>- **Tipo**: Preventivo.
>- **Orden de Ejecucion**: El proceso con el menor tiempo restante se ejecuta primero.
>- **Ventajas**: Minimiza el tiempo de espera y el tiempo de retorno de manera más efectiva que los algoritmos no preventivos.
>- **Desventajas**: Puede provocar cambios de contexto frecuentes e inanición de procesos más largos.

---

## 🛠️ Program Function / Funcion del Programa

This program implements the SRTF algorithm to simulate process scheduling. Given a set of processes with their arrival times and burst times, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, wich is the total time a process spends in the system.
- Remaining time, continuously updated to handle preemption.
  
>***Este programa implementa el algoritmo SRTF para simular la programación de procesos. Dado un conjunto de procesos con sus tiempos de llegada y tiempos de ejecucion, el programa calculará:***
>- Tiempo de finalización de cada proceso.
>- Tiempo de espera de cada proceso.
>- Tiempo de respuesta, que es el tiempo total que un proceso pasa en el sistema.
>- Tiempo restante, actualizado continuamente para manejar la preemisión.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the SRTF script, navigate to the directory where the "SRTF.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script SRTF, navegue hasta el directorio donde se encuentra el archivo "SRTF.py" y ejecute el siguiente comando en la terminal:***

    ```bash
        python SRTF.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
        Process | Arrival Time | Burst Time | Completion Time | Waiting Time | Turnaround Time
        ---------------------------------------------------------------------------------------
        P1      |      0      |      8     |        8        |      0      |       8
        P2      |      1      |      4     |       12        |      7      |      11
        P3      |      2      |      9     |       21        |     10      |      18
    ```

---

## 🧩 [Program / Programa](/SRTF/SRTF.py)

```python
class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id  # Identificador del proceso
        self.arrival_time = arrival_time  # Tiempo de llegada del proceso
        self.burst_time = burst_time  # Tiempo de ejecución total del proceso
        self.remaining_time = burst_time  # Tiempo de ejecución restante (usado en SRTF)
        self.completion_time = 0  # Tiempo en que el proceso termina
        self.waiting_time = 0  # Tiempo que el proceso ha esperado
        self.turnaround_time = 0  # Tiempo total en el sistema

def srtf(processes):
    # Ordenar procesos por tiempo de llegada
    processes.sort(key=lambda x: x.arrival_time)
    
    n = len(processes)  # Número total de procesos
    current_time = 0  # Tiempo actual en la simulación
    completed_processes = 0  # Contador de procesos completados
    ready_queue = []  # Cola de procesos listos para ejecutar

    while completed_processes < n:
        # Añadir a la cola de listos los procesos que han llegado hasta el tiempo actual
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_time > 0:
                ready_queue.append(p)

        # Si la cola de listos no está vacía, seleccionar el proceso con menor tiempo restante
        if ready_queue:
            # Ordenar la cola de listos por tiempo restante (y luego por tiempo de llegada en caso de empate)
            ready_queue.sort(key=lambda x: x.remaining_time)
            current_process = ready_queue[0]  # Proceso con menor tiempo restante
            current_process.remaining_time -= 1  # Reducir su tiempo restante

            if current_process.remaining_time == 0:  # Si el proceso ha terminado
                current_process.completion_time = current_time + 1  # Tiempo en el que finaliza el proceso
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  # Calcular tiempo de retorno
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time  # Calcular tiempo de espera
                completed_processes += 1  # Incrementar el contador de procesos completados
                ready_queue.pop(0)  # Eliminar el proceso de la cola de listos

        # Si no hay procesos listos, avanzar el tiempo
        current_time += 1

    return processes  # Devolver la lista de procesos con sus tiempos calculados

def print_schedule(processes):
    # Imprimir encabezados de la tabla
    print("Process | Arrival Time | Burst Time | Completion Time | Waiting Time | Turnaround Time")
    print("---------------------------------------------------------------------------------------")
    # Imprimir información de cada proceso en formato tabular
    for p in processes:
        print(f"P{p.id}      | {p.arrival_time:<13} | {p.burst_time:<11} | {p.completion_time:<15} | {p.waiting_time:<12} | {p.turnaround_time:<15}")

if __name__ == "__main__":
    # Datos predefinidos para los procesos
    processes = [
        Process(1, 5, 8),  # Proceso 1: llega en 0 y tiene un tiempo de ejecución de 8
        Process(2, 1, 4),  # Proceso 2: llega en 1 y tiene un tiempo de ejecución de 4
        Process(3, 2, 9),  # Proceso 3: llega en 2 y tiene un tiempo de ejecución de 9
        Process(4, 3, 5)   # Proceso 4: llega en 3 y tiene un tiempo de ejecución de 5
    ]
    
    scheduled_processes = srtf(processes)  # Ejecutar el algoritmo SRTF
    print_schedule(scheduled_processes)  # Imprimir el programa con los tiempos calculados
    ```
    