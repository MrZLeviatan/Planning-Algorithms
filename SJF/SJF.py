class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id  # Identificador del proceso
        self.arrival_time = arrival_time  # Tiempo de llegada del proceso
        self.burst_time = burst_time  # Tiempo de ejecución del proceso
        self.completion_time = 0  # Tiempo en que el proceso termina
        self.waiting_time = 0  # Tiempo que el proceso ha esperado
        self.turnaround_time = 0  # Tiempo total en el sistema

def sjf(processes):
    # Ordenar procesos por tiempo de llegada y, en caso de empate, por tiempo de ejecución
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    
    n = len(processes)  # Número total de procesos
    current_time = 0  # Tiempo actual en la simulación
    completed_processes = 0  # Contador de procesos completados

    # Mientras haya procesos por completar
    while completed_processes < n:
        # Filtrar los procesos que han llegado hasta el tiempo actual
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        
        if ready_queue:
            # Seleccionar el proceso con el tiempo de ejecución más corto de los listos
            current_process = min(ready_queue, key=lambda x: x.burst_time)
            current_time += current_process.burst_time  # Incrementar el tiempo actual por el tiempo de ejecución del proceso
            current_process.completion_time = current_time  # Establecer el tiempo de finalización del proceso
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time  # Calcular tiempo de retorno
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time  # Calcular tiempo de espera
            completed_processes += 1  # Incrementar el contador de procesos completados
        else:
            current_time += 1  # Si no hay procesos listos, avanzar el tiempo

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
        Process(2, 5, 4),  # Proceso 2: llega en 1 y tiene un tiempo de ejecución de 4
        Process(3, 2, 3),  # Proceso 3: llega en 2 y tiene un tiempo de ejecución de 9
        Process(4, 3, 9)   # Proceso 4: llega en 3 y tiene un tiempo de ejecución de 5
    ]
    
    scheduled_processes = sjf(processes)  # Ejecutar el algoritmo SJF
    print_schedule(scheduled_processes)  # Imprimir el programa con los tiempos calculados
