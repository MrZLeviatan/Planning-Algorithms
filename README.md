<h1 align="center">

  _Planning Algorithms_

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)


</h1>  
  
This repository contains implementations of different process planning algorithms used in operating systems. Scheduling algorithms are essential to manage the execution of processes efficiently, optimizing the use of system resources and improving user experience.

>***Este repositorio contiene implementaciones de diferentes algoritmos de planificación de procesos utilizados en sistemas operativos. Los algoritmos de planificación son esenciales para gestionar la ejecución de los procesos de manera eficiente, optimizando el uso de los recursos del sistema y mejorando la experiencia del usuario.***


<p align="center">
  
[![Algoritmo-Icono.png](https://i.postimg.cc/bwXCc4gk/Algoritmo-Icono.png)]()

</p>

---

## 📚 Table of Contents / Tabla de Contenidos

1. [Features](#-features--características) / [Características](#-features--características)
2. [Tools](#️-tools--herramientas) / [Herramientas](#️-tools--herramientas)
3. [Algorithms Included](#-algorithms-included--algoritmos-incluidos) / [Algoritmos Incluidos](#-algorithms-included--algoritmos-incluidos)
4. [System Requirements](#-System-Requirements--Requisitos-Sistema) / [Requisitos Sistema](#-System-Requirements--Requisitos-Sistema)
5. [Instructions for use](#️-instructions-for-use--intruccion-de-uso) / [Intruccion de Uso](#️-instructions-for-use--intruccion-de-uso)
6. [License](#-license--licencia) / [Licencia](#-license--licencia)
7. [Authors](#-authors--autores) / [Autores](#-authors--autores)
8. [Gratitude](#gratitude--agredecimientos) / [Agredecimientos](#gratitude--agredecimientos)
9. [Contactanos](#-contactanos--contact-us) / [Contact Us](#-contactanos--contact-us)


---



## 🌟 Features / Características

- Clear and Simple Implementations: Each algorithm has been implemented in Python with easy-to-understand code.
- Detailed Explanations: Each algorithm is accompanied by an explanation detailing its operation, advantages, and disadvantages.
- Modular and Extensible: The repository is easy to extend by adding new algorithms or improving current implementations.
>- Implementaciones Claras y Simples: Cada algoritmo ha sido implementado en Python con un código fácil de entender.
>- Explicaciones Detalladas: Junto a cada algoritmo se incluye una explicación que detalla su funcionamiento, ventajas y desventajas.
>- Modular y Extensible: El repositorio es fácil de extender añadiendo nuevos algoritmos o mejorando las implementaciones actuales.

---

## 🛠️ Tools / Herramientas

- <H3> Backend:</H3>

    - [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
 
- <H3>  IDEs/ Editors: </H3>

    - [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)


---

## 📖 Algorithms Included / Algoritmos Incluidos

### [FCFS (First Come First Serve)](/FCFS/)
The FCFS algorithm serves processes in the order in which they arrive to the system, without interruptions. It is easy to implement, but can lead to high waiting times in some cases.
>***El algoritmo FCFS atiende los procesos en el orden en que llegan al sistema, sin interrupciones. Es fácil de implementar, pero puede llevar a tiempos de espera elevados en algunos casos.***

### [SJF (Shortest Job First)](/SJF/)
SJF prioritizes the shortest processes. This algorithm seeks to minimize the average waiting time, but requires knowing in advance the duration of each process.
>***SJF prioriza los procesos más cortos. Este algoritmo busca minimizar el tiempo de espera promedio, pero requiere conocer de antemano la duración de cada proceso.***

### [SRTF (Shortest Remaining Time First)](/SRTF/)
The SRTF algorithm is a preemptive version of SJF. In this scheme, the process with the shortest remaining execution time always has priority. If a new process with a shorter duration arrives in the system, it will interrupt the running process.
>***El algoritmo SRTF es una versión preventiva de SJF. En este esquema, el proceso con el menor tiempo de ejecución restante siempre tiene prioridad. Si un nuevo proceso con una duración más corta llega al sistema, interrumpe el proceso en ejecución.***

### [Priority](/Priority/)
In priority planning, each process is assigned a priority value. Processes with higher priority are executed before those with lower priority. This algorithm can be preemptive or non-preemptive.
>***En la planificación por prioridades, cada proceso tiene un valor de prioridad asignado. Los procesos con prioridad más alta son ejecutados antes que los de menor prioridad. Este algoritmo puede ser preventivo o no preventivo.***

### [HRN (Highest Response Ratio Next)](/HRN/)
HRN is an improvement of the SJF algorithm to avoid penalizing processes that arrive later. A response ratio is calculated that takes into account both waiting time and execution time, favoring processes that have waited longer.
>***HRN es una mejora del algoritmo SJF para evitar la penalización de procesos que llegan más tarde. Se calcula una relación de respuesta que tiene en cuenta tanto el tiempo de espera como el tiempo de ejecución, favoreciendo a los procesos que han esperado más.***

### [RR (Round Robin)](/RR/)
The Round Robin algorithm distributes CPU time among all processes equally, using time slices (quantum). It is a preventive approach that ensures that no process hogs the CPU.
>***El algoritmo Round Robin distribuye el tiempo del CPU entre todos los procesos de manera equitativa, usando intervalos de tiempo (quantum). Es un enfoque preventivo que asegura que ningún proceso acapare el CPU.***

### [FMQ (Planificación Multinivel)](/FMQ/)
Multi-level planning (FMQ) organizes processes into different queues based on their priority or type. Each queue can have its own scheduling algorithm, allowing for more flexible management of processes.
>***La planificación multinivel (FMQ) organiza los procesos en diferentes colas según su prioridad o tipo. Cada cola puede tener su propio algoritmo de planificación, permitiendo una gestión más flexible de los procesos.***

---

## 🧩 System Requirements / Requisitos Sistema
To run the scheduling algorithms included in this repository, make sure you have the following:

- Python 3.x installed on your system.
- Git to clone the repository.
- An IDE or code editor (such as VS Code, PyCharm, or IntelliJ IDEA) to edit and run the scripts.
> Para ejecutar los algoritmos de planificación incluidos en este repositorio, asegúrate de tener lo siguiente:
>- Python 3.x instalado en tu sistema.
>- Git para clonar el repositorio.
>- Un IDE o editor de código (como VS Code, PyCharm o IntelliJ IDEA) para editar y ejecutar los scripts.

---

## 🛠️ Instructions for use / Intruccion de Uso

1. Clone the repository:
   >***Clonar el Reporitorio:***
   ```bash
   git clone https://github.com/MrZLeviatan/Planning-Algorithms.git
   cd Planning-Algorithms
   ```
2. Run an algorithm: Navigate to the directory of the algorithm you want to run and execute the corresponding Python file. For example, to run FCFS:
   >***Ejecutar el Algoritmos: Navega al directorio del algoritmo que deseas ejecutar y ejecuta el archivo Python correspondiente. Por ejemplo, para ejecutar FCFS:***
   ```bash
   cd fcfs
   python fcfs.py    
   ```
3. Algorithm Customization: If you want to adjust the parameters of the algorithms (such as arrival times or process execution times), you can modify the scripts directly in your     preferred code editor.
   >***Personalización de Algoritmos: Si deseas ajustar los parámetros de los algoritmos (como los tiempos de llegada o de ejecución de los procesos), puedes modificar los           scripts directamente en tu editor de código preferido.***

---

## 📜 License / Licencia
This project is licensed under the Apache-2.0 license. See the [LICENSE](/LICENSE) file for details.
>***Este proyecto está licenciado bajo la licencia Apache-2.0. Consulta el archivo [LICENSE](/LICENSE) para más detalles.***

---

## 👤 Authors / Autores 

|                                                                                                                                 Author                                                                                                                                 |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [@Nicolas C.S](https://github.com/MrZLeviatan) <br>[![Icon.jpg](https://i.postimg.cc/FsbjKxLk/Icon.jpg)](https://github.com/MrZLeviatan) <br> [![](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/MrZLeviatan) |


---

## 🤝Gratitude / Agredecimientos

"Thank you to everyone who has contributed to and supported this project, and to the open-source community for their valuable collaboration. I also want to thank the readers for taking the time to explore this repository and for their interest in learning more about
>***Gracias a todos los que han contribuido y apoyado este proyecto, y a la comunidad de código abierto por su valiosa colaboración. También agradezco a los lectores por tomarse el tiempo de explorar este repositorio y su interés en aprender más sobre los algoritmos de planificación.***

## 📫 Contactanos: / Contact Us

  - [![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/jPCTARQv) 
