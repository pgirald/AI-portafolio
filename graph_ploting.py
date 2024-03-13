import networkx as nx
import matplotlib as plt


def _graph_segments(G: nx.Graph) -> tuple[list[float | int], list[float | int]]:
    edges = G.edges
    x = [tup[0] for edge in edges for tup in edge]
    y = [tup[1] for edge in edges for tup in edge]
    return (x, y)


def _weight_labels(G: nx.Graph) -> tuple[list[int], list[int], list[str]]:
    edges = G.edges
    x = [(edge[0][0] + edge[1][0]) / 2 for edge in edges]
    y = [(edge[0][1] + edge[1][1]) / 2 for edge in edges]
    labels = [_weightof(G, edge) for edge in edges]
    labels = [str(label) for label in labels]
    return (x, y, labels)


def _nodes(G: nx.Graph) -> tuple[list[float | int], list[float | int]]:
    nodes = G.nodes
    x = [node[0] for node in nodes]
    y = [node[1] for node in nodes]
    return (x, y)


def _weightof(G: nx.Graph, edge,weight: str = "weight") -> float:
    if weight in G[edge[0]][edge[1]]:
        return G.get_edge_data(edge[0], edge[1])[weight]
    return ""


def _plot_edges(
    bounds: tuple[float | int, float | int],
    p: plt,
    lines: tuple[float | int, float | int],
    color,
):
    (x, y) = lines
    for i in range(0, len(x) - 1, 2):
        p.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color=color)
    (width, height) = bounds
    p.xlim(-1, width)
    p.ylim(-1, height)
    p.grid(True)
    p.gca().invert_yaxis()
    p.gca().xaxis.set_ticks_position("top")
    p.grid(False)


def plot_edges(
    G: nx.Graph, bounds: tuple[float | int, float | int], p: plt, color: str
):
    _plot_edges(bounds, p, _graph_segments(G), color)


def plot_weights(G: nx.Graph, p: plt):
    for x, y, label in zip(*_weight_labels(G)):
        p.text(
            x,
            y,
            label,
            verticalalignment="center",
            horizontalalignment="center",
            fontsize=6,
        )


def plot_nodes(G: nx.Graph, p: plt):
    p.scatter(*_nodes(G))


def plot_graph(G: nx.Graph, bounds: tuple[float | int, float | int], p: plt, color):
    plot_nodes(G, p)
    plot_weights(G, p)
    _plot_edges(bounds, p, _graph_segments(G), color)


def get_bounds(G: nx.Graph) -> tuple[float | int, float | int]:
    (x, y) = _nodes(G)
    return (max(x) - min(x), max(y) - min(y))
