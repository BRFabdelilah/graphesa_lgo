import matplotlib.pyplot as plt
import networkx as nx

# Création du graphe orienté
G = nx.DiGraph()

# Ajout des sommets au graphe
G.add_nodes_from(range(1, 10))  # Nous avons 9 sommets

# Ajout des arêtes au graphe
edges = [(1, 2), (1, 6), (2, 3), (4, 2), (2, 5),(5, 6),
         (3, 4), (3, 5), (4, 8), (4, 9), (6, 7), (7, 1)] 
G.add_edges_from(edges)

# Détection du cycle dans le graphe
cycles = list(nx.simple_cycles(G))

# Trier les cycles en fonction de leur longueur (nombre de sommets)
cycles.sort(key=lambda x: len(x), reverse=True)

# Affichage du graphe
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, arrowsize=20)

# Définition des couleurs pour chaque cycle
cycle_colors = ['red', 'green', 'blue', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'pink']

# Affichage de chaque cycle avec une couleur différente
for i, cycle_nodes in enumerate(cycles):
    print(cycle_nodes)
    cycle_edges = [(cycle_nodes[i], cycle_nodes[i + 1]) for i in range(len(cycle_nodes) - 1)]
    cycle_edges.append((cycle_nodes[-1], cycle_nodes[0]))
    nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color=cycle_colors[i % len(cycle_colors)], width=2, arrowsize=20)

plt.show()
