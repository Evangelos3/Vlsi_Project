import random
import networkx as nx
import matplotlib.pyplot as plt

# Load the circuit from an IBM01 file using the parser
parser = IBM01Parser('example.pl')
circuit = parser.parse()

# Create a NetworkX graph from the circuit
G = nx.Graph()
for cell in circuit:
    G.add_node(cell)
for i in range(len(circuit)):
    for j in range(i + 1, len(circuit)):
        if circuit[i][j] == 1:
            G.add_edge(i, j, weight=0.5)

# Run the Tetris legalization algorithm
def classic_tetris(placement):
    for i in range(len(placement)):
        for j in range(i + 1, len(placement)):
            if placement[i] > placement[j]:
                placement[i], placement[j] = placement[j], placement[i]
    return placement

def restricted_row_heuristic(placement, threshold=0.05):
    for i in range(len(placement)):
        for j in range(i + 1, len(placement)):
            if placement[i] > placement[j] and random.random() < threshold:
                placement[i], placement[j] = placement[j], placement[i]
    return placement

def left_right_heuristic(placement):
    for i in range(len(placement)):
        for j in range(i + 1, len(placement)):
            if placement[i] > placement[j] and placement[i] % 2 == 0:
                placement[i], placement[j] = placement[j], placement[i]
    return placement

# Run the Tetris legalization algorithms
placement = list(range(len(circuit)))
random.shuffle(placement)

print("Initial placement:")
print(placement)

placement = classic_tetris(placement)
print("Classic Tetris:")
print(placement)

placement = restricted_row_heuristic(placement)
print("Restricted Row Heuristic (5%):")
print(placement)

placement = left_right_heuristic(placement)
print("Left-Right Heuristic:")
print(placement)

# Visualize the legalized placement
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=['blue' if placement[i] < len(placement) // 2 else 'green' for i in range(len(placement))])
nx.draw_networkx_edges(G, pos, edge_color='gray')
plt.show()
