import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random as rn
import graph_ploting as gp
from typing import Callable


class Maze:
    _nodes: np.ndarray
    _G: nx.Graph
    _width: int
    _height: int
    _bounds: tuple[int, int]
    _maze: nx.Graph

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def nodes(self):
        return self._nodes

    def __init__(self, width: int, height: int, bounds: tuple[int, int]):
        self._width = width
        self._height = height
        self._bounds = bounds
        self._G = nx.Graph()
        self._nodes: np.ndarray = np.empty((height, width), dtype=object)

        for i in range(height):
            for j in range(width):
                self._nodes[i][j] = (j, i)
        
        self._nodes.flags.writeable = False

        self._G.add_nodes_from(self._nodes.flatten().tolist())

        for i in range(height):
            for j in range(width - 1):
                self._G.add_edge(
                    self._nodes[i][j],
                    self._nodes[i][j + 1],
                    weight=rn.randrange(bounds[0], bounds[1] + 1),
                )

        for i in range(height - 1):
            for j in range(width):
                self._G.add_edge(
                    self._nodes[i][j],
                    self._nodes[i + 1][j],
                    weight=rn.randrange(bounds[0], bounds[1] + 1),
                )

    def generate(self, generator: Callable[[nx.Graph], nx.Graph]) -> nx.Graph:
        self._maze = generator(self._G)
        return self._maze


def _maze_segments(maze: Maze) -> tuple[list[int], list[int]]:
    x = []
    y = []
    nodes = maze._nodes
    for i in range(maze._height):
        for j in range(maze._width - 1):
            if not maze._maze.has_edge(nodes[i][j], nodes[i][j + 1]):
                center = (nodes[i][j][0] + nodes[i][j + 1][0]) / 2
                x.extend([center, center])
                y.extend([nodes[i][j][1] + 0.5, nodes[i][j][1] - 0.5])
    for i in range(maze._height - 1):
        for j in range(maze._width):
            if not maze._maze.has_edge(nodes[i][j], nodes[i + 1][j]):
                middle = (nodes[i][j][1] + nodes[i + 1][j][1]) / 2
                y.extend([middle, middle])
                x.extend([nodes[i][j][0] + 0.5, nodes[i][j][0] - 0.5])
    top_left = (nodes[0][0][0] - 0.5, nodes[0][0][1] - 0.5)
    top_right = (nodes[0][-1][0] + 0.5, nodes[0][-1][1] - 0.5)
    bottom_left = (
        nodes[-1][0][0] - 0.5,
        nodes[-1][0][1] + 0.5,
    )
    bottom_right = (
        nodes[maze._width - 1][maze._height - 1][0] + 0.5,
        nodes[maze._width - 1][maze._height - 1][1] + 0.5,
    )

    x.extend(
        [
            top_left[0],
            top_right[0],
            top_right[0],
            bottom_right[0],
            bottom_right[0],
            bottom_left[0],
            bottom_left[0],
            top_left[0],
        ]
    )
    y.extend(
        [
            top_left[1],
            top_right[1],
            top_right[1],
            bottom_right[1],
            bottom_right[1],
            bottom_left[1],
            bottom_left[1],
            top_left[1],
        ]
    )

    return (x, y)


def plot_maze_grid(maze: Maze, p: plt, color: str):
    gp.plot_graph(maze._G, (maze._width, maze._height), p, color)


def plot_maze(maze: Maze, p: plt, color):
    gp._plot_edges((maze._width, maze._height), p, _maze_segments(maze), color)
