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
