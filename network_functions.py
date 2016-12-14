import networkx as nx
import matplotlib.pyplot as plt


def plot_modules(modules, G):
    """ Plot the modules of a graph"""
    values = [modules[n] for n in G.nodes()]
    nx.draw(G, node_color=values)
    plt.show()


def get_graph(filename):
    """ return a graph from an edge list"""
    G = nx.Graph()
    f = open(filename)
    data = f.readlines()
    edges = []
    for line in data:
        entry = map(int, line.rstrip().split())
        if entry:
            edges.append(tuple(entry))
    G.add_edges_from(edges)
    f.close()
    return G
