<h1 align="center">

_Shortest Job First (SJF)_

</h1>

It is a process scheduling algorithm in operating systems that selects the process with the shortest execution time (also known as burst time) to be executed next. This approach is based on the premise that by processing the shortest jobs first, the average waiting time for all queued processes can be reduced.
>***Es un algoritmo de planificacion de procesos en sistemas operativos que selecciona el proceso con el menor tiempo de ejecucion (tambien conocido como tiempo de burst) para ser ejecutado a continuacion. Este enfoque se basa en la premisa de que, al procesar primero los trabajos mas cortos, se puede reducir el tiempo promedio de espera de todos los procesos de cola.***

---

## 🌟 Features / Características
- **Type**: Non-preemptive.
- **Execution Order**: The process with the shortest burst time is executed first.
- **Advantages**: Minimizes average waiting time and turnaround time.
- **Disadvantages**: Can cause starvation for longer processes. 

>- **Tipo**: No proventivo.
>- **Orden de Ejecucion**: El proceso con el tiempo de ejecution más corto se ejecuta primero.
>- **Ventajas**: Minimiza el tiempo de espera y el tiempo de respuesta.
>- **Desventajas**: Puede causar inanicion en procesos mas largos.

---

## 🛠️ Program Function / Funcion del Programa

This program implements the SJF algorithm to simulate process sheduling. Given a set of processes with their arrival times and burst times, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, wich is the total time a process spends in the system.
>***Este programa implementa el algoritmo SJF para simular la programación de procesos. Dado un conjunto de procesos con sus tiempos de llegada y tiempos de ráfaga, el programa calculará:***
>- Tiempo de finalización de cada proceso.
>- Tiempo de espera de cada proceso.
>- Tiempo de respuesta, que es el tiempo total que un proceso pasa en el sistema.

---

## 🛠️ Instructions for use / Intruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the SJF script, navigate to the directory where the "SJF.py" file is located and excute the following command in the terminal:
    >***To run the SJF script, navigate to the directory where the "SJF.py" file is located and excute the following command in the terminal:***

    ```bash
        python SJF.py
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

## 🧩 [Programa / Program](/SJF/SJF.py)

```python
class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id 
        self.arrival_time = arrival_time  
        self.burst_time = burst_time  
        self.completion_time = 0  
        self.waiting_time = 0  
        self.turnaround_time = 0  

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    
    n = len(processes) 
    current_time = 0  
    completed_processes = 0  

    while completed_processes < n:
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        
        if ready_queue:
            current_process = min(ready_queue, key=lambda x: x.burst_time)
            current_time += current_process.burst_time  
            current_process.completion_time = current_time 
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time  
            completed_processes += 1 
        else:
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
        Process(2, 5, 4),  
        Process(3, 2, 3),  
        Process(4, 3, 9)   
    ]
    
    scheduled_processes = sjf(processes)  
    print_schedule(scheduled_processes)  

```
 