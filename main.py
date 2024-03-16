import networkx as nx
import matplotlib.pyplot as plt
import maze as mz
import graph_ploting as gp

height = 60
width = 100
weight_bounds = (20, 50)
generator = lambda G: nx.minimum_spanning_tree(G, algorithm="boruvka")
agent = nx.dijkstra_path
maze = mz.Maze(width, height, weight_bounds)
start = maze.nodes[0][0]
goal = maze.nodes[-1][-1]

maze.setGenerator(generator)
maze.setAgent(agent)
problem = maze.generate()
solution = maze.solve(start, goal)

plt.figure()
#gp.plot_graph(problem, (maze.width, maze.height), plt, color="blue")
mz.plot_maze(maze, plt, color="green")
plt.scatter([start[0], goal[0]], [start[1], goal[1]], color="red")
gp.plot_edges(solution, (maze.width, maze.height), plt, color="blue")
plt.show()
