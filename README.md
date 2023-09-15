# Quantum-Computing-Hack-2023

## Descripción del Problema
Una empresa de reparto se enfrenta al desafío de optimizar las rutas de su flota de camiones para minimizar el tiempo y los costos de entrega de paquetes a clientes ubicados en diferentes lugares. El objetivo de este proyecto es encontrar la longitud total de viaje más corta para todos los camiones, lo que a su vez minimizará el costo total en términos de tiempo. Para lograrlo, se utilizan métodos de optimización combinatoria.


### Cálculo de Distancias Euclidianas (Numpy y Matplotlib)
En la primera parte del proyecto, se aborda el cálculo de distancias euclidianas entre ubicaciones en el plano cartesiano. El código incluye las siguientes etapas:

1. Definición de dos cuadrados en el plano cartesiano con coordenadas (0, 0) y (1, 1).
2. Cálculo de la distancia entre los cuadrados utilizando la función `np.linalg.norm()`, que calcula la norma euclidiana de un vector (en este caso, la diferencia entre las coordenadas de los cuadrados).
3. Representación gráfica de los cuadrados utilizando la biblioteca Matplotlib.
4. Impresión de la distancia entre los cuadrados en la consola.

### Cálculo de Distancias Cuánticas (Qiskit y Numpy)
En la segunda parte del proyecto, se exploran las distancias cuánticas entre puntos en el plano cartesiano. El proceso implica los siguientes pasos:

1. Definición de tres puntos diferentes en el plano cartesiano.
2. Cálculo de la distancia euclidiana entre cada uno de estos puntos y un punto de destino específico.
3. Creación de un circuito cuántico utilizando Qiskit para calcular la distancia entre cada punto y el punto de destino.
4. Ejecución del circuito cuántico en un simulador cuántico para obtener resultados.
5. Cálculo de la probabilidad de cada resultado y determinación de la distancia más corta.
6. Creación de una gráfica que ilustra los puntos y la distancia más corta calculada.

### Optimización de Rutas con NetworkX (Python)
En la tercera parte del proyecto, se aborda la optimización de rutas utilizando la biblioteca NetworkX. El proceso implica lo siguiente:

1. Creación de un grafo que representa ubicaciones y conexiones entre ellas.
2. Definición de un punto de inicio y un punto de destino.
3. Cálculo del camino más corto entre el punto de inicio y el punto de destino utilizando NetworkX.
4. Dibujo de un gráfico que muestra el grafo y el camino más corto en rojo.
5. Cálculo de la distancia total del camino más corto en función de los pesos de las aristas del grafo.

## Objetivos
El objetivo principal de este proyecto es abordar el desafío de optimizar las rutas de entrega de paquetes de una empresa de reparto. Se busca minimizar el tiempo total de viaje y, por lo tanto, reducir los costos operativos. Algunos de los puntos clave son:

- Encontrar la longitud total de viaje más corta para todos los camiones.
- Utilizar métodos de optimización combinatoria para abordar el problema.
- Considerar diferentes ubicaciones y escalas de entrega (interurbano, dentro de una ciudad, última milla).
- Determinar la cantidad óptima de camiones en la flota.
- Diseñar planes para atender a la mayor cantidad de ubicaciones en el menor tiempo posible y con el menor número de camiones.

## Contribuciones y Futuro
Este proyecto puede ampliarse y mejorarse de diversas formas:

- Implementar algoritmos de optimización cuántica para resolver problemas más complejos de asignación de rutas.
- Integrar datos reales de ubicaciones y distancias para aplicaciones prácticas.
- Explorar estrategias de optimización en tiempo real para la planificación dinámica de rutas.
- Desarrollar una interfaz de usuario para que las empresas de reparto puedan utilizar esta solución.

## Requisitos
El proyecto utiliza las siguientes bibliotecas y herramientas:

- Numpy
- Matplotlib
- Qiskit
- NetworkX
- Python 3.x

Asegúrate de tener estas bibliotecas instaladas para ejecutar el código correctamente.

## Ejecución
Puedes ejecutar los diferentes componentes del proyecto siguiendo las instrucciones detalladas en los archivos Jupyter proporcionados.

¡Esperamos que este proyecto sea de utilidad y fomente la exploración de soluciones innovadoras para problemas de logística y optimización de rutas!

---
