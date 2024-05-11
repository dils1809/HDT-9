import networkx as nx
import matplotlib.pyplot as plt

def cargar(ruta):
    """Carga un grafo desde un archivo de texto con las rutas."""
    G = nx.Graph()
    with open(ruta, 'r', encoding='utf-8') as file:
        for line in file:
            partes = line.strip().split(',')
            origen = partes[0].strip().strip('"').title()
            destino = partes[1].strip().strip('"').title()
            costo = int(partes[2].strip())
            G.add_edge(origen, destino, weight=costo)
            G.add_edge(destino, origen, weight=costo)
    return G

def ruta(G, origen):
    """Aplica Dijkstra para encontrar las distancias más cortas desde un origen."""
    return nx.single_source_dijkstra_path_length(G, origen, weight='weight')

def mostrar(G):
    """Dibuja el grafo usando matplotlib."""
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=7)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    plt.show()

def main():
    """Función principal del programa."""
    archivo = 'rutas.txt'
    G = cargar(archivo)
    print("Nodos cargados en el grafo:", G.nodes)
    mostrar(G)

    while True:
        inicio = input("Ingrese el nombre de la estación de salida (deje en blanco para salir): ").strip().title()
        if inicio == "":
            break
        if inicio in G:
            dists = ruta(G, inicio)
            print(f"Costo de ruta más barata desde {inicio}: ")
            for dest, costo in dists.items():
                print(f"{dest}: {costo}")
        else:
            print("Estación no encontrada.")

if __name__ == "__main__":
    main()
