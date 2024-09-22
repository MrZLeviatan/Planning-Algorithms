<h1 align="center">

  _Planning Algorithms_

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


</h1>  
  
This repository contains implementations of different process planning algorithms used in operating systems. Scheduling algorithms are essential to manage the execution of processes efficiently, optimizing the use of system resources and improving user experience.

>***Este repositorio contiene implementaciones de diferentes algoritmos de planificación de procesos utilizados en sistemas operativos. Los algoritmos de planificación son esenciales para gestionar la ejecución de los procesos de manera eficiente, optimizando el uso de los recursos del sistema y mejorando la experiencia del usuario.***


<p align="center">
  
[![Algoritmo-Icono.png](https://i.postimg.cc/bwXCc4gk/Algoritmo-Icono.png)](https://postimg.cc/xcRyLxW1)

</p>

---

## 📚 Table of Contents / Tabla de Contenidos

1. [Features](#-features--características) / [Características](#-features--características)
2. [Tools](#-tools--herramientas) / [Herramientas](#-tools--herramientas)
11. [Contribution](#contribution) / [Contribución](#contribución)
12. [License](#license) / [Licencia](#licencia)
13. [Contact](#contact) / [Contacto](#contacto)


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

    - ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 
- <H3>  IDEs/ Editors: </H3>

    - ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


---

## Algorithms Included / Algoritmos Incluidos

### [FCFS (First Come First Serve]()
The FCFS algorithm serves processes in the order in which they arrive to the system, without interruptions. It is easy to implement, but can lead to high waiting times in some cases.
>***El algoritmo FCFS atiende los procesos en el orden en que llegan al sistema, sin interrupciones. Es fácil de implementar, pero puede llevar a tiempos de espera elevados en algunos casos.***

### [SJF (Shortest Job First)]()
SJF prioritizes the shortest processes. This algorithm seeks to minimize the average waiting time, but requires knowing in advance the duration of each process.
>***SJF prioriza los procesos más cortos. Este algoritmo busca minimizar el tiempo de espera promedio, pero requiere conocer de antemano la duración de cada proceso.***


### [Round Robin]
El algoritmo Round Robin distribuye el tiempo del CPU entre todos los procesos de manera equitativa, usando intervalos de tiempo (quantum). Es un enfoque preventivo que asegura que ningún proceso acapare el CPU.

Ver implementación

Planificación por Prioridad
En la planificación por prioridad, los procesos son ejecutados de acuerdo a su prioridad asignada. Este algoritmo puede ser tanto preventivo como no preventivo.

Ver implementación

Planificación Multinivel
La planificación multinivel clasifica los procesos en diferentes colas según su prioridad o tipo, permitiendo un manejo más flexible de diferentes clases de procesos.

Ver implementación




