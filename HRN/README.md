<h1 align="center">

_Highest Response Ratio Next (HRN)_

</h1>


The HRN (Highest Response Ratio Next) algorithm is a non-preemptive process scheduling algorithm that selects the next process to execute based on the response ratio.This ratio is calculated for each process as:

            Response Ratio = Waiting Time + Burst Time / Burst Time

>***El algoritmo HRN (Highest Response Ratio Next) es un algoritmo de planificacion de procesos no preventivo que selecciona el siguiente proceso a ejecutar basandose en el ratio de respuesta. Este ratio se calcula para cada proceso como:***

>***        Ratio de Respuesta = Tiempo Espera + Tiempo Rafaga/Tiempo Rafaga       ***

---

## 🌟 Features / Características
- **Type**: Non-preemptive.
- **Execution Order**: The process with the highest response ratio is executed first.
- **Advantages**: Reduce starvation and prioritizes processes that have been waiting.
- **Disadvantages**: Still prone to inefficiencies in certain process loads.

>- **Tipo**: No preventivo.
>- **Orden de Ejecucion**: El proceso con el mayor ratio de respuesta se ejecuta primero.
>- **Ventajas**: Reduce la inanicion y prioriza los procesos que han estado esperando mas tiempo.
>- **Desventajas**: Todavia puede tener ineficiencias en ciertas cargas de procesos.

---


## 🛠️ Program Function / Funcion del Programa
This program implements the HRN algorithm to simulate process sheduling. Given a set of processes with their arrival and burst times, the program will calculate:

- Completion time for each process.
- Waiting time for each process.
- Turnaround time, which is the total time a process spends in the system.
- The order of execution based on the response ration.

>***Este programa implementa el algoritmo HRN para simular la planificacion de procesos. Dado un conjunto de procesos con sus tiempos de llegada y tiempos de rafaga, el programa calculara:***
>- Tiempo de finalizacion de cada proceso.
>- Tiempo de espera de cada proceso.
>- Tiempo de respuesta, que es el tiempo total que un proceso pasa en el sistema.
>- El orden de ejecucion basado en el ratio de respuesta.

---

## 🛠️ Instructions for use / Instruccion de Uso

1. **Run the program**: First, ensure you have python installed on your system.
    >**Ejecute el programa**: primero, asegúrese de tener Python instalado en su sistema.    
    
    To run the HRN script, navigate to the directory where the "HRN.py" file is located and excute the following command in the terminal:
    >***Para ejecutar el script HRN, navegue hasta el directorio donde se encuentra el archivo "HRN.py" y ejecute el siguiente comando en la terminal:***

    ```bash
        python HRN.py
    ```
2. The program will generate a table similar to the following:
    >***El programa generará una tabla similar a la siguiente:***

    ```bash
    | ID  | Llegada | Ejecución | Finalización | Espera | Respuesta |
    |-----|---------|-----------|--------------|--------|-----------|
    | 1   | 0       | 8         | 8            | 0      | 8         |
    | 2   | 1       | 4         | 12           | 7      | 11        |
    | 3   | 2       | 9         | 21           | 10     | 19        |
    | 4   | 3       | 5         | 26           | 18     | 23        |
    ```

---

## 🧩 [Program / Programa](/SJF/SJF.py)

```python
class Proceso:
    def __init__(self, id, tiempo_llegada, tiempo_ejecucion):
        self.id = id                        
        self.tiempo_llegada = tiempo_llegada  
        self.tiempo_ejecucion = tiempo_ejecucion  
        self.tiempo_espera = 0              
        self.tiempo_respuesta = 0           
        self.tiempo_finalizacion = 0        
        self.ratio_respuesta = 0            


def calcular_ratio_respuesta(proceso, tiempo_actual):

    tiempo_espera = tiempo_actual - proceso.tiempo_llegada
    ratio_respuesta = (tiempo_espera + proceso.tiempo_ejecucion) / proceso.tiempo_ejecucion
    return ratio_respuesta


def planificacion_hrn(procesos):
    tiempo = 0  
    procesos_completados = []  

    while procesos:
     
        procesos_disponibles = [p for p in procesos if p.tiempo_llegada <= tiempo]
        
        if not procesos_disponibles:
            tiempo += 1
            continue

        for p in procesos_disponibles:
            p.ratio_respuesta = calcular_ratio_respuesta(p, tiempo)

        proceso_siguiente = max(procesos_disponibles, key=lambda p: p.ratio_respuesta)

        tiempo += proceso_siguiente.tiempo_ejecucion
        proceso_siguiente.tiempo_finalizacion = tiempo

        proceso_siguiente.tiempo_respuesta = proceso_siguiente.tiempo_finalizacion - proceso_siguiente.tiempo_llegada
        proceso_siguiente.tiempo_espera = proceso_siguiente.tiempo_respuesta - proceso_siguiente.tiempo_ejecucion

        procesos_completados.append(proceso_siguiente)

        procesos.remove(proceso_siguiente)

    print("\n{:<10} {:<10} {:<15} {:<15} {:<10} {:<10}".format("ID", "Llegada", "Ejecución", "Finalización", "Espera", "Respuesta"))
    for p in procesos_completados:
        print("{:<10} {:<10} {:<15} {:<15} {:<10} {:<10}".format(p.id, p.tiempo_llegada, p.tiempo_ejecucion, p.tiempo_finalizacion, p.tiempo_espera, p.tiempo_respuesta))


procesos = [
    Proceso(1, 0, 8), 
    Proceso(2, 1, 10),  
    Proceso(3, 2, 2),  
    Proceso(4, 3, 4)   
]

planificacion_hrn(procesos)
```