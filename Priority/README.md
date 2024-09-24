<h1 align="center">

_Priority_

</h1>

The Priority Scheduling algorithm is a preemptive scheduling method used in operating systems to manage the execution of processes. In this approach, each process is assigned a priority level, with lower numbers indicating higher priority. The scheduler selects the process with the highest priority for execution, allowing more critical tasks to be completed before less critical ones.
>***El algoritmo de programación prioritaria es un método de programación preventiva que se utiliza en los sistemas operativos para gestionar la ejecución de procesos. En este enfoque, a cada proceso se le asigna un nivel de prioridad, donde los números más bajos indican una prioridad más alta. El programador selecciona el proceso con la mayor prioridad para su ejecución, lo que permite que las tareas más críticas se completen antes que las menos críticas.***

---

## 🌟 Features / Características
- **Type**: Preemptive.
- **Execution Order**: The process with the highest priority (lowest number) is executed first.
- **Advantages**: Ensures critical processes are executed promptly and minimizes the waiting time for high-priority processes.
- **Disadvantages**: Can cause starvation for lower-priority processes if higher-priority tasks continuously arrive.
>- **Tipo**: Preventivo.
>- **Orden de Ejecución**: El proceso con la prioridad más alta (número más bajo) se ejecuta primero.
>- **Ventajas**: Asegura que los procesos críticos se ejecuten rápidamente y minimiza el tiempo de espera para los procesos de alta prioridad.
>- **Desventajas**: Puede causar inanición en los procesos de baja prioridad si los de alta prioridad llegan constantemente.

---

## 🛠️ Program Function / Función del Programa
This program implements the Priority Scheduling algorithm to simulate process scheduling. Given a set of processes with their arrival times, burst times, and priority levels, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, which is the total time a process spends in the system.
- The order of execution based on priority levels.

>***Este programa implementa el algoritmo de Planificación por Prioridades para simular la programación de procesos. Dado un conjunto de procesos con sus tiempos de llegada, tiempos de ráfaga y niveles de prioridad, el programa calculará:***

>- Tiempo de finalización de cada proceso.
>- Tiempo de espera de cada proceso.
>- Tiempo de respuesta, que es el tiempo total que un proceso pasa en el sistema.
>- El orden de ejecución basado en los niveles de prioridad.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the Priority script, navigate to the directory where the "Priority.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script Prioridad, navegue hasta el directorio donde se encuentra el archivo "Priority.py" y ejecute el siguiente comando en la terminal:***

    ```bash
        python Priority.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
    Process | Arrival Time | Burst Time | Priority | Start Time | Completion Time | Waiting Time | Turnaround Time
    --------------------------------------------------------------------------------------------------------------
    P2      | 1            | 1          | 1        | 1          | 2               | 0            | 1              
    P5      | 4            | 5          | 2        | 4          | 9               | 0            | 5              
    P1      | 0            | 10         | 3        | 9          | 19              | 9            | 19             
    P3      | 2            | 2          | 4        | 19         | 21              | 17           | 19             
    P4      | 3            | 1          | 5        | 21         | 22              | 18           | 19             
    ```

---

## 🧩 [Program / Programa](/Priority/Priority.py)

    ```python
    class Process:
    def __init__(self, id, arrival_time, burst_time, priority):
      
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  
        self.priority = priority  
        self.completion_time = 0 
        self.waiting_time = 0  
        self.turnaround_time = 0  
        self.start_time = -1  

    def priority_scheduling(processes):
    
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    
    current_time = 0  
    completed_processes = 0 
    ready_queue = []  
    executed_processes = []  

    while completed_processes < len(processes):
       
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_time > 0:
                ready_queue.append(p)

        if ready_queue:
            
            ready_queue.sort(key=lambda x: x.priority)

            current_process = ready_queue[0]

            if current_process.start_time == -1:
                current_process.start_time = current_time

            current_process.remaining_time -= 1

            if current_process.remaining_time == 0:
                current_process.completion_time = current_time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
                executed_processes.append(current_process)  
                ready_queue.pop(0)

        current_time += 1

    return executed_processes  

    def print_schedule(processes):

    print("Process | Arrival Time | Burst Time | Priority | Start Time | Completion Time | Waiting Time | Turnaround Time")
    print("--------------------------------------------------------------------------------------------------------------")
    
    for p in processes:
        print(f"P{p.id}      | {p.arrival_time:<13} | {p.burst_time:<10} | {p.priority:<8} | {p.start_time:<10} | {p.completion_time:<15} | {p.waiting_time:<12} | {p.turnaround_time:<15}")

    if __name__ == "__main__":

    processes = [
        Process(1, 0, 10, 3),  
        Process(2, 1, 1, 1),  
        Process(3, 2, 2, 4),  
        Process(4, 3, 1, 5),
        Process(5, 4, 5, 2)  
    ]

    scheduled_processes = priority_scheduling(processes)
    
    print_schedule(scheduled_processes)
    ```
    
