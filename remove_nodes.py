import networkx as nx
import json
import sys

G = nx.read_graphml('graphs/notes.graphml')
targets = sys.argv[1:]
matches = [n for n in G.nodes if any(t in n.lower() for t in targets)]
G.remove_nodes_from(matches)

nx.write_graphml(G, 'graphs/notes.graphml')

with open('graphs/notes.json', 'w') as f:
	json.dump(nx.cytoscape_data(G), f)
