class Process:
    def __init__(self, id, arrival_time, burst_time, priority):
        # Inicializa un proceso con ID, tiempo de llegada, tiempo de ráfaga y prioridad
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time  # Tiempo restante para completar el proceso
        self.priority = priority  # Prioridad del proceso (menor número = mayor prioridad)
        self.completion_time = 0  # Tiempo de finalización del proceso
        self.waiting_time = 0  # Tiempo de espera del proceso
        self.turnaround_time = 0  # Tiempo total que pasa el proceso en el sistema
        self.start_time = -1  # Momento en que el proceso comienza a ejecutarse

def priority_scheduling(processes):
    # Función que implementa el algoritmo de planificación por prioridad (preemptivo)
    
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    
    current_time = 0  # Tiempo actual en la simulación
    completed_processes = 0  # Contador de procesos completados
    ready_queue = []  # Cola de procesos listos para ejecutar
    executed_processes = []  # Almacena los procesos que ya fueron ejecutados

    while completed_processes < len(processes):
        # Añadir a la cola de listos los procesos que han llegado
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue and p.remaining_time > 0:
                ready_queue.append(p)

        if ready_queue:
            # Ordenar la cola de listos por prioridad (menor número = mayor prioridad)
            ready_queue.sort(key=lambda x: x.priority)

            # Seleccionar el proceso con mayor prioridad
            current_process = ready_queue[0]

            # Registrar el momento en que el proceso comienza a ejecutarse
            if current_process.start_time == -1:
                current_process.start_time = current_time

            # Ejecutar el proceso por 1 unidad de tiempo
            current_process.remaining_time -= 1

            # Si el proceso termina su ejecución
            if current_process.remaining_time == 0:
                current_process.completion_time = current_time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed_processes += 1
                executed_processes.append(current_process)  # Agregar a la lista de ejecutados
                ready_queue.pop(0)

        # Avanzar en el tiempo
        current_time += 1

    return executed_processes  # Devolver los procesos ejecutados en orden

def print_schedule(processes):
    # Imprimir la tabla con los detalles de la planificación de procesos
    print("Process | Arrival Time | Burst Time | Priority | Start Time | Completion Time | Waiting Time | Turnaround Time")
    print("--------------------------------------------------------------------------------------------------------------")
    
    for p in processes:
        print(f"P{p.id}      | {p.arrival_time:<13} | {p.burst_time:<10} | {p.priority:<8} | {p.start_time:<10} | {p.completion_time:<15} | {p.waiting_time:<12} | {p.turnaround_time:<15}")

if __name__ == "__main__":
    # Definir un conjunto de procesos con datos quemados (predefinidos)
    processes = [
        Process(1, 0, 10, 3),  # Proceso 1: llegada en tiempo 0, ráfaga de 10, prioridad 3
        Process(2, 1, 1, 1),   # Proceso 2: llegada en tiempo 1, ráfaga de 1, prioridad 1
        Process(3, 2, 2, 4),   # Proceso 3: llegada en tiempo 2, ráfaga de 2, prioridad 4
        Process(4, 3, 1, 5),   # Proceso 4: llegada en tiempo 3, ráfaga de 1, prioridad 5
        Process(5, 4, 5, 2)    # Proceso 5: llegada en tiempo 4, ráfaga de 5, prioridad 2
    ]

    # Ejecutar el algoritmo de planificación por prioridad
    scheduled_processes = priority_scheduling(processes)
    
    # Imprimir el resultado de la planificación en el orden de ejecución
    print_schedule(scheduled_processes)




