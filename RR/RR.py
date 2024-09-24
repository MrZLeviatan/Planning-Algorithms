# Función para imprimir la tabla de procesos
def print_process_table(processes, burst_times, waiting_times, turnaround_times):
    print(f"{'Proceso':<10}{'Burst Time':<12}{'Waiting Time':<15}{'Turnaround Time':<20}")
    for i in range(len(processes)):
        print(f"{processes[i]:<10}{burst_times[i]:<12}{waiting_times[i]:<15}{turnaround_times[i]:<20}")

# Función para calcular tiempos de espera y turnaround
def calculate_waiting_turnaround_times(processes, burst_times, quantum):
    n = len(processes)
    remaining_burst_times = burst_times[:]  # Copia de los tiempos de ráfaga
    waiting_times = [0] * n
    turnaround_times = [0] * n
    t = 0  # Tiempo actual

    # Mientras queden procesos con tiempo de ráfaga pendiente
    while True:
        done = True
        for i in range(n):
            if remaining_burst_times[i] > 0:  # Si el proceso aún tiene tiempo de ráfaga
                done = False
                if remaining_burst_times[i] > quantum:  # Si el proceso necesita más que el quantum
                    t += quantum
                    remaining_burst_times[i] -= quantum
                else:
                    t += remaining_burst_times[i]
                    waiting_times[i] = t - burst_times[i]
                    remaining_burst_times[i] = 0
        if done:
            break

    # Calcular tiempos de turnaround
    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

    return waiting_times, turnaround_times

# Función principal del algoritmo Round Robin
def round_robin(processes, burst_times, quantum):
    print("\nEjecución del algoritmo Round Robin")
    waiting_times, turnaround_times = calculate_waiting_turnaround_times(processes, burst_times, quantum)

    # Imprimir la tabla de resultados
    print_process_table(processes, burst_times, waiting_times, turnaround_times)

    # Calcular promedios
    avg_waiting_time = sum(waiting_times) / len(processes)
    avg_turnaround_time = sum(turnaround_times) / len(processes)
    print(f"\nTiempo promedio de espera: {avg_waiting_time:.2f}")
    print(f"Tiempo promedio de turnaround: {avg_turnaround_time:.2f}")

# Datos quemados para los procesos
processes = [1, 2, 3, 4]  # Identificadores de procesos
burst_times = [3, 5, 4, 6]  # Tiempos de ráfaga de los procesos
quantum = 4  # Cuanto de tiempo

# Ejecutar el algoritmo Round Robin
round_robin(processes, burst_times, quantum)
