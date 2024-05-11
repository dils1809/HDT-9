# Sistema de Rutas Mínimas para Distribución de Paquetes

## Autor
Dilary Sarahí Cruz López - 231010

## Descripción
Este proyecto implementa un sistema para calcular rutas mínimas para la distribución de paquetes entre diferentes estaciones utilizando el algoritmo de Dijkstra. El sistema está desarrollado en Python y utiliza la biblioteca NetworkX para modelar las rutas como un grafo. Los usuarios pueden ingresar el nombre de la estación de salida y el sistema mostrará las rutas más económicas a todos los destinos posibles.

## Objetivos
- **Implementar el algoritmo de Dijkstra para calcular la ruta más corta entre nodos en un grafo.**
- **Utilizar grafos para modelar las rutas de distribución de paquetes entre diferentes estaciones.**
- **Proporcionar una interfaz de usuario interactiva que permita a los usuarios seleccionar una estación de salida y visualizar las rutas más económicas.**

## Estructura del Código
- **main.py**: Contiene la función principal del programa, gestiona la interacción con el usuario y la visualización del grafo.
- **grafos.py**: Define las funciones para cargar los datos del grafo desde un archivo, calcular las rutas mínimas y dibujar el grafo.
- **rutas.txt**: Archivo de texto que contiene los datos de las rutas, incluyendo las estaciones de origen, destino y el costo asociado.

## Funcionamiento del Programa
El programa solicita al usuario que ingrese el nombre de la estación de salida. Una vez ingresado, el sistema calcula y muestra el costo de la ruta más barata a cada destino posible desde la estación especificada. La visualización del grafo ayuda a los usuarios a entender las conexiones entre las estaciones.


## Instalación y Ejecución

### Requisitos
- Python 3.8 o superior
- Bibliotecas de Python: NetworkX, Matplotlib

### Instalación de Bibliotecas
Ejecuta el siguiente comando para instalar las bibliotecas necesarias:
```bash
pip install networkx matplotlib


