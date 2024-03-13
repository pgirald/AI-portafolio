import networkx as nx
import matplotlib.pyplot as plt
import maze as mz
import graph_ploting as gp

height = 50
width = 50
weight_bounds = (20, 50)
generator = nx.minimum_spanning_tree
agent = nx.dijkstra_path
maze = mz.Maze(width, height, weight_bounds)
start = maze.nodes[20][0]
goal = maze.nodes[0][-1]

# nx.draw(G, with_labels=True, font_weight='bold')
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold'
# plt.show()
maze.setGenerator(generator)
maze.setAgent(agent)
problem = maze.generate()
solution = maze.solve(start, goal)

plt.figure()
mz.plot_maze(maze, plt, color="green")
plt.scatter([start[0], goal[0]], [start[1], goal[1]], color="red")
gp.plot_edges(solution, (maze.width, maze.height), plt, color="blue")
plt.show()
