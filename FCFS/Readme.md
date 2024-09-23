<h1 align="center">

_First Come First Server (FCFS)_

</h1>

is a simple, non-preemptive scheduling algorithm where processes are executed in the order they arrive. No priority is given to any process, meaning the first to arrive is the first to be executed without interruption.
>*** Es un algoritmo de programación simple y no preemptivo en el que los procesos se ejecutan en el orden en que llegan. No se le da prioridad a ningún proceso, lo que significa que el primero en llegar es el primero en ejecutarse sin interrupción.

## 🌟 Features / Características
- Type : Non-preemptive.
- Execution Order: The process that arrives first is executed first.
- Advantages: Simple to implement.
- Disadvantages: Can cause long wait times for shorter processes if a longer one arrives first (convoy effect).

>- Tipo: No proventivo.
>- Orden de Ejecucion: El proceso que llega primero es el que se ejecuta primero.
>- Ventajas: Sencillo de implementar.
>- Desventajas: Puede causar tiempos de espera largos para procesos cortos si uno mas largo llega antes (efecto convoy).


## 🛠️ Program Function / Funcion del Programa
This program implements the FCFS algorithm to simulate process scheduling. Given a set of processes with their arrival times and execution times, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, which is the total time a process spends in the system.
>***Este programa implementa el algoritmo FCFS para simular la planificacion de procesos. Dado un conjunto de procesos con sus tiempos de llegada y tiempos de ejecucion, el programa calculara:
>- Tiempo de finalizacion de cada proceso.
>- Tiempo de espera para cada proceso.
>- Tiempo de retorno (o turnaround time), que es el tiempo total que un proceso pasa en el sistema.

