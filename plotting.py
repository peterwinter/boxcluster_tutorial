import matplotlib.pyplot as plt


def add_cuts(ax, cuts, N):
    if cuts[-1] != N:
        cuts.append(N)
    print(len(cuts))
    c_last = 0
    for c in cuts:
        color = 'k'
        ax.plot([c, c], [c, c_last], color)
        ax.plot([c, c_last], [c, c], color)
        ax.plot([c, c_last], [c_last, c_last], color)
        ax.plot([c_last, c_last], [c, c_last], color)
        c_last = c


def mplot(a, title=None, boxes=None):
    cmap = 'spectral'
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pcolor(a, vmin=0.1, vmax=0.8, cmap=cmap)
    N = len(a)
    if boxes is not None:
        add_cuts(ax, cuts=boxes.copy(), N=N)
    ax.set_xlim([0, N])
    ax.set_ylim([0, N])
    if title is not None:
        ax.set_title(title, size=20)
    plt.show()


def mplot2(a, title=None, boxes=None, cmap='spectral'):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pcolor(a, cmap=cmap)
    N = len(a)
    if boxes is not None:
        add_cuts(ax, cuts=boxes.copy(), N=N)
    ax.set_xlim([0, N])
    ax.set_ylim([0, N])
    if title is not None:
        ax.set_title(title, size=20)
    plt.show()


def plot_modules(modules, G):
    """ Plot the modules of a graph"""
    import networkx as nx
    values = [modules[n] for n in G.nodes()]
    nx.draw(G, node_color=values)
    plt.show()


def get_graph(filename):
    """ return a graph from an edgelist """
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
