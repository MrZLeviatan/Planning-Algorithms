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
        self.id = id 
        self.arrival_time = arrival_time 
        self.burst_time = burst_time 
        self.remaining_time = burst_time  
        self.completion_time = 0 
        self.waiting_time = 0  
        self.turnaround_time = 0 

def srtf(processes):
    processes.sort(key=lambda x: x.arrival_time)
    n = len(processes)  
    current_time = 0 
    completed_processes = 0  
    ready_queue = [] 

    while completed_processes < n:
        
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_time > 0:
                ready_queue.append(p)

        if ready_queue:
            ready_queue.sort(key=lambda x: x.remaining_time)
            current_process = ready_queue[0] 
            current_process.remaining_time -= 1 

            if current_process.remaining_time == 0: 
                current_process.completion_time = current_time + 1 
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time 
                completed_processes += 1  
                ready_queue.pop(0) 

        current_time += 1

    return processes 

def print_schedule(processes):
    print("Process | Arrival Time | Burst Time | Completion Time | Waiting Time | Turnaround Time")
    print("---------------------------------------------------------------------------------------")
    for p in processes:
        print(f"P{p.id}      | {p.arrival_time:<13} | {p.burst_time:<11} | {p.completion_time:<15} | {p.waiting_time:<12} | {p.turnaround_time:<15}")

if __name__ == "__main__":
    processes = [
        Process(1, 5, 8),  
        Process(2, 1, 4),  
        Process(3, 2, 9),  
        Process(4, 3, 5)   
    ]
    
    scheduled_processes = srtf(processes)  
    print_schedule(scheduled_processes)
```
    
