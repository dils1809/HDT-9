import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo_desde_archivo(ruta_archivo):
    """Crea y devuelve un grafo basado en un archivo de texto con las rutas."""
    G = nx.Graph()
    with open(ruta_archivo, 'r') as file:
        for line in file:
            partes = line.strip().split(',')
            origen = partes[0].strip('"').strip()
            destino = partes[1].strip('"').strip()
            costo = int(partes[2].strip())
            G.add_edge(origen, destino, weight=costo)
            G.add_edge(destino, origen, weight=costo)  # Asegurar simetría
    return G

def dijkstra_desde_origen(G, origen):
    """Utiliza el algoritmo de Dijkstra para encontrar la ruta más corta desde un origen."""
    return nx.single_source_dijkstra_path_length(G, origen, weight='weight')

def dibujar_grafo(G):
    """Dibuja el grafo con matplotlib."""
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=15)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def main():
    """Función principal que ejecuta el programa."""
    archivo_rutas = 'rutas.txt'
    G = crear_grafo_desde_archivo(archivo_rutas)
    dibujar_grafo(G)

    while True:
        origen = input("Ingrese el nombre de la estación de salida (deje en blanco para salir): ")
        if origen == "":
            break
        if origen in G:
            distancias = dijkstra_desde_origen(G, origen)
            print("Costo de ruta más barata desde {}: ".format(origen))
            for destino, costo in distancias.items():
                print(f"{destino}: {costo}")
        else:
            print("Estación no encontrada.")

if __name__ == "__main__":
    main()
