<h1 align="center">

_Round Robin (RR)_

</h1>

The Round Robin (RR) algorithm is a process scheduling method in operating systems that assigns each process a fixed time slice, known as a "time quantum". If a process does not complete within its quantum, it is preempted and placed at the end of the process queue, allowing the next process to execute. This cycle continues until all processes are completed.
>***El algoritmo Round Robin (RR) es un metodo de planificacion de procesos en sistemas operativos que asigna a cada proceso un tiempo fijo, conocido como "time quantum" durante el cual puede ejecutarse. Si un proceso no finaliza dentro del quantum, se interrumpe y se coloca al final de la cola de procesos, permitiendo que el siguiente proceso en la cola se ejecute. Este ciclo continua hasta que todos los procesos han sido completados.***

---

## 🌟 Features / Características
- **Type**: Preemptive.
- **Execution Order**: Processes are executed in a cyclic order with a fixed time quantum.
- **Advantages**: Ensures fairness by giving each process equal time slots. Reduces starvation.
- **Disadvantages**: May cause high context switching overhead with too small time quantums.

>- **Tipo**: Preventivo.
>- **Orden de Ejecucion**: Los procesos se ejecutan en orden ciclico con un quantum de tiempo fijo.
>- **Ventajas**: Garantiza equidad al dar a cada proceso una cantidad de tiempo igual. Reduce la inanicion.
>- **Desventajas**: Puede causar sobrecarga de cambio de contexto con quantums muy menores.

---

## 🛠️ Program Function / Funcion del Programa

This program implements the Round Robin (RR) algorithm for process scheduling. Given a set of processes with their burst times and a fixed quantum, the program calculates:

- Waiting time for each process.
- Turnaround time for each process.

>***Este programa implementa el algoritmo Round Robin (RR) para la planificacion de procesos. Dado un conjunto de procesos con sus tiempos de rafaga y un quantum de tiempo fijo, el programa calculara:***

>- Tiempo de espera de cada proceso.
>- Tiempo de espera de cada proceso.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the RR script, navigate to the directory where the "RR.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script RR, navegue hasta el directorio donde se encuentra el archivo "RR.py" y ejecute el siguiente comando en la terminal:***

    ```bash
        python RR.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
    | Proceso | Burst Time | Waiting Time | Turnaround Time|
    |---------|------------|--------------|----------------|
    | 1       | 10         | 13           | 23             |
    | 2       | 5          | 10           | 15             |
    | 3       | 8          | 14           | 22             |
    | 4       | 6          | 12           | 18             |
    ```

---

## 🧩 [Program / Programa](/RR/RR.py)

```python

def print_process_table(processes, burst_times, waiting_times, turnaround_times):
    print(f"{'Proceso':<10}{'Burst Time':<12}{'Waiting Time':<15}{'Turnaround Time':<20}")
    for i in range(len(processes)):
        print(f"{processes[i]:<10}{burst_times[i]:<12}{waiting_times[i]:<15}{turnaround_times[i]:<20}")

def calculate_waiting_turnaround_times(processes, burst_times, quantum):
    n = len(processes)
    remaining_burst_times = burst_times[:] 
    waiting_times = [0] * n
    turnaround_times = [0] * n
    t = 0  

    while True:
        done = True
        for i in range(n):
            if remaining_burst_times[i] > 0:  
                done = False
                if remaining_burst_times[i] > quantum: 
                    t += quantum
                    remaining_burst_times[i] -= quantum
                else:
                    t += remaining_burst_times[i]
                    waiting_times[i] = t - burst_times[i]
                    remaining_burst_times[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

    return waiting_times, turnaround_times

def round_robin(processes, burst_times, quantum):
    print("\nEjecución del algoritmo Round Robin")
    waiting_times, turnaround_times = calculate_waiting_turnaround_times(processes, burst_times, quantum)

    print_process_table(processes, burst_times, waiting_times, turnaround_times)

    avg_waiting_time = sum(waiting_times) / len(processes)
    avg_turnaround_time = sum(turnaround_times) / len(processes)
    print(f"\nTiempo promedio de espera: {avg_waiting_time:.2f}")
    print(f"Tiempo promedio de turnaround: {avg_turnaround_time:.2f}")

processes = [1, 2, 3, 4]  
burst_times = [3, 5, 4, 6]  
quantum = 4  

round_robin(processes, burst_times, quantum)
```
