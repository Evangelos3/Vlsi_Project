import networkx as nx
import matplotlib.pyplot as plt

# Load the circuit from an IBM01 file using the parser
parser = IBM01Parser('example.nets')
circuit = parser.parse()

# Create a NetworkX graph from the circuit
G = nx.Graph()
for cell in circuit:
    G.add_node(cell)
for i in range(len(circuit)):
    for j in range(i + 1, len(circuit)):
        if circuit[i][j] == 1:
            G.add_edge(i, j, weight=0.5)

# Run the Kernighan-Lin algorithm
partition = [0] * len(circuit)
for iteration in range(10):  # run for 10 iterations
    max_gain = 0
    best_exchange = None
    for i in range(len(circuit)):
        for j in range(i + 1, len(circuit)):
            if partition[i] != partition[j]:
                gain_i = sum(G.degree(i, weight='weight')) - sum(G.degree(j, weight='weight'))
                gain_j = sum(G.degree(j, weight='weight')) - sum(G.degree(i, weight='weight'))
                total_gain = gain_i + gain_j
                if total_gain > max_gain:
                    max_gain = total_gain
                    best_exchange = (i, j)
    if best_exchange:
        partition[best_exchange[0]], partition[best_exchange[1]] = partition[best_exchange[1]], partition[best_exchange[0]]
        print(f"Iteration {iteration + 1}: Exchanged cells {best_exchange[0]} and {best_exchange[1]}")

# Visualize the partitioned graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=['blue' if partition[i] == 0 else 'green' for i in range(len(circuit))])
nx.draw_networkx_edges(G, pos, edge_color='gray')
plt.show()
