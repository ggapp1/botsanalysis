import networkx as nx






G = nx.Graph()


G.add_node(1)
G.add_nodes_from([2, 3, 4, 5, 6])
G.add_edge(1,2)

print G.edges, G.nodes